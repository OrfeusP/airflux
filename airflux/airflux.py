import argparse
from pprint import pprint
import pymongo
from bson.codec_options import CodecOptions
import pytz
import data

HOST = 'mongodb'
PORT = 27017

TIMEZONES = {
    'MUN': pytz.timezone('Europe/Berlin'),
    'HAM': pytz.timezone('Europe/Berlin'),
    'TXL': pytz.timezone('Europe/Berlin'),
    'LHR': pytz.timezone('Europe/London'),
}


class AirFluxConnection:
    def __init__(self, host, port, db):
        self._host = host
        self._port = port
        self._db = db

    def __enter__(self):
        conn_uri = 'mongodb://{host}:{port}/{db}'
        airflux_conn = pymongo.MongoClient(
            conn_uri.format(host=self._host, port=self._port, db=self._db)
        )
        self.conn = airflux_conn
        self.conn.db = self._db
        return self.conn

    def __exit__(self, *args, **kwargs):
        self.conn.close()


class Airflux:
    def __init__(self, conn):

        self._conn = conn
        self._db = conn.db
        self._flights = data.FLIGHTS.copy()
        self._planes = data.PLANES.copy()
        self._codec_options = CodecOptions(tz_aware=True)

        self._flight_collection = self._conn[self._db]['flight']
        self._plane_collection = self._conn[self._conn.db]['plane']
        self._flight_plan_collection = self._conn[self._conn.db]['flight_plan']

    def init_db(self):
        # drop existing collection in the database

        self._flight_collection.drop()
        self._plane_collection.drop()
        self._flight_plan_collection.drop()

        # insert data into mongo
        self._plane_collection.insert_many(self._planes)
        self._flight_collection.insert_many(
            list(map(self._preprocess_flights, self._flights))
        )

        self._flight_plan_collection.insert_many(
            list(
                map(
                    self._set_flight_plan,
                    list(
                        self._conn[self._db].get_collection(
                            'flight', codec_options=self._codec_options
                        ).find({}, {'_id': False}).sort('departure')
                    )
                )
            )
        )

    @staticmethod
    def _preprocess_flights(fl):
        origin, origin_tz = fl['origin']
        dest, dest_tz = fl['destination']
        fl['arrival'] = fl['departure'] + fl['flight_time']
        return {
            'origin': origin,
            'destination': dest,
            'departure': fl['departure'],
            'arrival': fl['arrival']

        }

    def _set_flight_plan(self, f):

        plane_4_flight = self._plane_collection.find_one(
            {'current_station': f['origin']}
        )

        if plane_4_flight is None:
            raise Exception(
                'No plane to flight {}'.format(f)
            )

        f['departure'] = f['departure'].astimezone(
            TIMEZONES.get(f['origin'])
        ).strftime('%Y-%m-%dT%H:%M:%S%z')
        f['arrival'] = f['arrival'].astimezone(
            TIMEZONES.get(f['destination'])
        ).strftime('%Y-%m-%dT%H:%M:%S%z')

        plane_4_flight['current_station'] = f['destination']
        self._plane_collection.update(
            {'_id': plane_4_flight['_id']},
            {"$set": plane_4_flight},
            False
        )
        plane_4_flight.pop('current_station', None)
        plane_4_flight.pop('_id', None)

        return {**f, **plane_4_flight}

    def flight_plan(self, airport=None):

        """
        Queries the `flight_plan` collection and retrieves the flights

        :param airport: airport to use for filtering
        :return: list of Flight objects
        """

        air_filter = {}
        if airport:
            air_filter = {'origin': airport}

        return list(
            self._conn[self._db].get_collection('flight_plan').find(
                air_filter,
                {
                    'origin': True,
                    'destination': True,
                    'arrival': True,
                    'departure': True,
                    'equipment': True,
                    '_id': False
                }
            )
        )

    def operations_plan(self, registration):
        """
        Queries the `flight_plan` collection and
        retrieves the operation objects

        :param registration: aircraft registration
        :return: list of OperatingInstruction objects
        """
        return list(
            self._conn[self._db].get_collection('flight_plan').find(
                {
                    'registration': registration
                },
                {
                    'origin': True,
                    'destination': True,
                    'departure': True,
                    '_id': False
                }
            )
        )


def parse_args():
    parser = argparse.ArgumentParser(description='Air Flux Airlines')
    parser.add_argument(
        'cmd',
        choices=['init-db', 'flight-plan', 'operations-plan'],
        help='Select action'
    )

    group_flight_plan = parser.add_argument_group('flight-plan')
    group_flight_plan.add_argument(
        '--airport', help='select departing airport'
    )
    group_operations = parser.add_argument_group('operations-plan')
    group_operations.add_argument(
        '--registration', help='select aircraft registration'
    )

    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    with AirFluxConnection(host=HOST, port=PORT, db='test') as airflux_db:
        airflux_obj = Airflux(airflux_db)
        if args.cmd == 'init-db':
            print('Initializing db...')
            airflux_obj.init_db()
        elif args.cmd == 'flight-plan':
            pprint(
                airflux_obj.flight_plan(args.airport), indent=4
            )
        elif args.cmd == 'operations-plan':
            if args.registration is None:
                print('registration number is required')
            pprint(
                airflux_obj.operations_plan(args.registration), indent=4
            )


if __name__ == '__main__':
    main()
