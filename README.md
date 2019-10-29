
# NWatch
[![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](http://opensource.org/licenses/MIT)   
#### Author
> Victor Waichigo K.

## Description
NWatch is a web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.

## Screenshots


## Setup Instructions:
### Requirements

##### 1. Clone the repository
Clone the the repository by running 

   ```bash
   git clone https://github.com/kamauvick/NWatch.git
   ```
 or download a zip file of the project from github
 

Navigate to the project directory
```bash
cd NWatch
```

##### 2. Create a virtual environment
 Install `Virtualenv` 

   ```prettier
   pip install virtualenv
   ```

To create a virtual environment named `virtual`, run

   ```prettier
   virtualenv virtual
   ```
To activate the virtual environment we just created, run

   ```bash
   source virtual/bin/activate
   ```

##### 3. Create a database
You'll need to create a new postgress database, Type the following command to access postgress
   ```bash
    $ psql
   ```
   Then run the following query to create a new database named ```watch``` 
   ```prettier
   # create database watch
   ```


#####  4.Install dependencies
To install the requirements from `requirements.txt` file,

   ```prettier
   pip install -r requirements.txt
   ```

#####  5.Create Database migrations
Making migrations on postgres using django

```prettier
python3 manage.py makemigrations watch
```

 
then run the command below;

 ```bash
 python3 manage.py migrate
 ```

##### 6.Run the app
To run the application on your development machine, 

    python3 manage.py runserver

### Running Tests
>To run tests;

    python3 manage.py test



## GraphQL Api

> Getting data from the API 

## Technologies Used
* Django
* Python
* Html
* Css
* Javascript
* Bootstrap
* GraphQL


## User stories
>As a user of the application I should be able to:

- [X] Sign in with the application to start using.
- [X] Set up a profile about me and a general location and my neighborhood name.
- [X] Find a list of different businesses in my neighborhood.
- [X] Find Contact Information for the health department and Police authorities near my neighborhood.
- [X] Create Posts that will be visible to everyone in my neighborhood.
- [X] Change My neighborhood when I decide to move out.
- [X] Only view details of a single neighborhood


## Bugs
There are no know bugs at the moment

## License
[![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](http://opensource.org/licenses/MIT)
>MIT license &copy;  2019 Victor
 
## Collaboration Information
* Clone the repository
* Make changes and write tests
* Push changes to github
* Create a pull request

## Contacts
Reach me on:
>Email:  waichigovick@gmail.com

>Twitter:  [@kamau_vick](https://twitter.com/kamau_vick)

