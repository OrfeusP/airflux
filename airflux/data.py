from datetime import datetime, timedelta
from pytz import timezone
PLANES = [
    {
        'registration': 'FL-00:0001',
        'equipment': 'BOEING 734',
        'base': 'TXL',
        'current_station': 'TXL'
    },
    {
        'registration': 'FL-00:0002',
        'equipment': 'AIRBUS A321',
        'base': 'MUC',
        'current_station': 'MUC'
    },
    {
        'registration': 'FL-00:0003',
        'equipment': 'BOEING 747-400:00',
        'base': 'LHR',
        'current_station': 'LHR'

    },
    {
        'registration': 'FL-00:0004',
        'equipment': 'AIRBUS A321',
        'base': 'HAM',
        'current_station': 'HAM'

    },
]
FLIGHTS = [
    # TXL
    {
        'origin': ('TXL', timezone('Europe/Berlin')),
        'destination': ('MUN', timezone('Europe/Berlin')),
        'departure': datetime.strptime(
            '2018-04-13T10:00:00', '%Y-%m-%dT%H:%M:%S'
        ),
        'flight_time': timedelta(hours=1)
    },
    {
        'origin': ('TXL', timezone('Europe/Berlin')),
        'destination': ('MUN', timezone('Europe/Berlin')),
        'departure': datetime.strptime(
            '2018-04-13T15:00:00', '%Y-%m-%dT%H:%M:%S'
        ),
        'flight_time': timedelta(hours=1)
    },
    {
        'origin': ('TXL', timezone('Europe/Berlin')),
        'destination': ('MUN', timezone('Europe/Berlin')),
        'departure': datetime.strptime(
            '2018-04-13T16:00:00', '%Y-%m-%dT%H:%M:%S'
        ),
        'flight_time': timedelta(hours=1)
    },
    {
        'origin': ('TXL', timezone('Europe/Berlin')),
        'destination': ('MUN', timezone('Europe/Berlin')),
        'departure': datetime.strptime(
            '2018-04-13T18:00:00', '%Y-%m-%dT%H:%M:%S'
        ),
        'flight_time': timedelta(hours=1)
    },
    {
        'origin': ('TXL', timezone('Europe/Berlin')),
        'destination': ('HAM', timezone('Europe/Berlin')),
        'departure': datetime.strptime(
            '2018-04-13T21:00:00', '%Y-%m-%dT%H:%M:%S'
        ),
        'flight_time': timedelta(minutes=40)
    },

    # MUC
    {
        'origin': ('MUC', timezone('Europe/Berlin')),
        'destination': ('LHR', timezone('Europe/London')),
        'departure': datetime.strptime(
            '2018-04-13T10:00:00', '%Y-%m-%dT%H:%M:%S'
        ),
        'flight_time': timedelta(hours=2)
    },
    {
        'origin': ('MUN', timezone('Europe/Berlin')),
        'destination': ('TXL', timezone('Europe/London')),
        'departure': datetime.strptime(
            '2018-04-13T13:00:00', '%Y-%m-%dT%H:%M:%S'
        ),
        'flight_time': timedelta(hours=1)
    },
    {
        'origin': ('MUN', timezone('Europe/Berlin')),
        'destination': ('TXL', timezone('Europe/Berlin')),
        'departure': datetime.strptime(
            '2018-04-13T15:00:00', '%Y-%m-%dT%H:%M:%S'
        ),
        'flight_time': timedelta(hours=1)
    },
    {
        'origin': ('MUN', timezone('Europe/Berlin')),
        'destination': ('LHR', timezone('Europe/London')),
        'departure': datetime.strptime(
            '2018-04-13T15:30:00', '%Y-%m-%dT%H:%M:%S'
        ),
        'flight_time': timedelta(hours=2)
    },
    {
        'origin': ('MUN', timezone('Europe/Berlin')),
        'destination': ('HAM', timezone('Europe/Berlin')),
        'departure': datetime.strptime(
            '2018-04-13T17:30:00', '%Y-%m-%dT%H:%M:%S'
        ),
        'flight_time': timedelta(hours=1)
    },
    {
        'origin': ('MUN', timezone('Europe/Berlin')),
        'destination': ('LHR', timezone('Europe/London')),
        'departure': datetime.strptime(
            '2018-04-13T18:00:00', '%Y-%m-%dT%H:%M:%S'
        ),
        'flight_time': timedelta(minutes=30, hours=2)
    },
    {
        'origin': ('MUN', timezone('Europe/Berlin')),
        'destination': ('LHR', timezone('Europe/London')),
        'departure': datetime.strptime(
            '2018-04-13T20:00:00', '%Y-%m-%dT%H:%M:%S'
        ),
        'flight_time': timedelta(hours=2)
    },
    {
        'origin': ('MUN', timezone('Europe/Berlin')),
        'destination': ('TXL', timezone('Europe/Berlin')),
        'departure': datetime.strptime(
            '2018-04-13T22:00:00', '%Y-%m-%dT%H:%M:%S'
        ),
        'flight_time': timedelta(hours=1)
    },

    # LHR

    {
        'origin': ('LHR', timezone('Europe/London')),
        'destination': ('HAM', timezone('Europe/Berlin')),
        'departure': datetime.strptime(
            '2018-04-13T9:00:00', '%Y-%m-%dT%H:%M:%S'
        ),
        'flight_time': timedelta(hours=2, minutes=30)
    },
    {
        'origin': ('LHR', timezone('Europe/London')),
        'destination': ('TXL', timezone('Europe/Berlin')),
        'departure': datetime.strptime(
            '2018-04-13T12:00:00', '%Y-%m-%dT%H:%M:%S'
        ),
        'flight_time': timedelta(hours=2)
    },
    {
        'origin': ('LHR', timezone('Europe/London')),
        'destination': ('TXL', timezone('Europe/Berlin')),
        'departure': datetime.strptime(
            '2018-04-13T17:00:00', '%Y-%m-%dT%H:%M:%S'
        ),
        'flight_time': timedelta(hours=2)
    },
    {
        'origin': ('LHR', timezone('Europe/London')),
        'destination': ('MUN', timezone('Europe/Berlin')),
        'departure': datetime.strptime(
            '2018-04-13T20:30:00', '%Y-%m-%dT%H:%M:%S'
        ),
        'flight_time': timedelta(hours=2)
    },
    # HAM

    {
        'origin': ('HAM', timezone('Europe/Berlin')),
        'destination': ('MUN', timezone('Europe/Berlin')),
        'departure': datetime.strptime(
            '2018-04-13T10:00:00', '%Y-%m-%dT%H:%M:%S'
        ),
        'flight_time': timedelta(hours=1)
    },
    {
        'origin': ('HAM', timezone('Europe/Berlin')),
        'destination': ('MUN', timezone('Europe/Berlin')),
        'departure': datetime.strptime(
            '2018-04-13T13:00:00', '%Y-%m-%dT%H:%M:%S'
        ),
        'flight_time': timedelta(hours=1)
    },
    {
        'origin': ('HAM', timezone('Europe/Berlin')),
        'destination': ('MUN', timezone('Europe/Berlin')),
        'departure': datetime.strptime(
            '2018-04-13T20:00:00', '%Y-%m-%dT%H:%M:%S'
        ),
        'flight_time': timedelta(hours=1)
    },

]
