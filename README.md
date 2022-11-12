# ToDo List Manager
This app is an basic ToDo list manager where user can manage and view their todo list.   

## Assumptions:
1. Since Django Rest Framework is to be used, assuming that REST APIs needs to created for todo list crud operations.
2. Frontend will be using REST APIs to communicate with backend.
3. Since todo list is user specific, app should have ability to register, login and logout.
4. App will be setup to run in local mode. (not Production)
5. For Simplicity, used sqllite3 as a data store.

## Future Considerations
   - Setup App for Production 
        - env and production configs
        - servers for api and web 
        - docker and docker compose setup 
   - Add more Unit Test Cases for ToDo list update, delete , detail , Logout APIs.
   - Unit tests for frontend
   - Beter Package Management for API
   - Using Postgres as a data store

## Prerequisites
    - Docker (Installed)
    - There should not be any app running on port 4200.
      (This can be changed in port binding of docker compose yaml file.)

## STEPS TO RUN (LOCALLY)
1. After cloning/downloading the project, create a `.local.env` file in root directory by copying contents from `.env.dist` file.
    > Note: Since this is setup for only local as of now, you can keep values in it as it is.

2. Run the below command from root directory 
    ```
    docker-compose up
    ```
    > NOTE: The command will take some time to build images and get ready to serve.

    > NOTE: Please wait for web api to get started. (Takes some time to build). Wait for message to 

3. Access the app using browser at 'http://localhost:4200'

## API Documentation
   For API documentation, view https://documenter.getpostman.com/view/22925969/2s8YerNCui

## Tech stack
1. Python -  https://www.python.org/
1. Django Rest Framework - https://www.django-rest-framework.org/
2. sqlite3 (database)- https://docs.python.org/3/library/sqlite3.html
3. django-rest-knox (For Token Authentication) -  https://james1345.github.io/django-rest-knox/ 
4. Angular v14 https://angular.io/docs

## Testing.
Test Cases were added for Backend for Register, Login and few for ToDo.
 > NOTE: Some test cases for ToDo and Logout were skipped due to time limit.

    Run tests
    ```
    docker-compose run api python manage.py test
    ```


