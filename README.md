# Django Project(Blog Application)

During Summer 2023, I created a blog application using Django.

## To download and use this project in your local machine. Follow the below steps

- Clone the Project
  - If the SSH is not set in your local machine and github you can go with the option 1 otherwise option 2.
    - Option 1
      ```
      https://github.com/AlashShrestha/Djangopy.git
      ```
      
      - Option 2
      ```
      git@github.com:AlashShrestha/Djangopy.git
      ```
## Setup the Environment
  - Go to the folder
  
    ```
    cd Djangopy
    ```
- Create virtual environment
  - You can create the virtualenv with [virtualenv](https://pypi.org/project/virtualenv/) library.
  - You can also skip this part and follow the next step.
- Installing the libraries
  ```
  pip install -r requirements.txt
  ```
- Setting Up environment variables
  - In the root project create the .env file
  - Open the project with VS 
  ```
  code Djangopy
  ```
- To run this project, you will need to add the following environment variables to your .env 

  `SECRET_KEY`
  
  `DATABASE`
  
  `EMAIL_HOST_USER`
  
  `EMAIL_HOST_PASSWORD`
  
  `EMAIL_PORT`
  
  `DEFAULT_FROM_EMAIL`
  
## Run Project
  - Migrate the database
    ```
    python manage.py migrate
    ```
- Runserver
    ```
    python manage.py runserver
    ```
## Features

- User Management System
- Dynamic Email Sending
- CRUD operation for blog
- Cross platform

## Want to collaborate?
You can add new feature, push to the new branch and send the pull request.
