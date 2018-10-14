# Air Flux Application 
Airflux  application matches aircrafts to flights given an existing timetable 

## To Run 
 * To create the docker container of the application execute:
 ``` bash
 docker-compose build --no-cache 
 ````

 * To run the application run:
    * `doker-compose up mongodb` to start the mongo container
    *  `docker-compose run airflux -h` to get the help information
    *  `docker-compose run airflux init-db` to initialize the database    
    *  `docker-compose run airflux flight-plan [--airport AIRPORT NAME]` to 
    get the all the flights (or filtered based on the `AIRPORT_NAME`)  
    *  `docker-compose run airflux operations-plan --registration 
    AIRCRAFT_REGISTRATION` to  get the all the flights of the specific 
    aircraft  