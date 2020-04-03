## Instagram
A clone of the Instagram app.

## Requirements
Clone the the repository by running

```
git clone https://github.com/monicaoyugi/Instagram
or download a zip file of the project from github then unzip.
```

Navigate to your project directory

## Create a virtual environment
Install Virtualenv

```
pip install virtual venv
```

To create a virtual environment named virtual, run

```
virtualenv virtual
```
To activate the virtual environment we just created,
run

```
source virtual/bin/activate
```

## Create a database
You'll need to create a new postgress database, Type the following command to access postgress

 $ psql

 Then run the following query to create a new database named  instagram

```
create database instagram
```

## Database diagram
https://dbdiagram.io/d/5e54c2c6ef8c251a0618867f

## Install dependencies
To install the requirements from requirements.txt file,

```
pip install -r requirements.txt
```

## Create Database migrations
Making migrations on postgres using django
run

```
python3 manage.py makemigrations  gram
```
then run the command below;

```
python3 manage.py migrate
```
## Run the app
To run the application on your development machine,

```
python3 manage.py runserver
```
## Running Tests
To run tests

```
python3 manage.py test
```

## Technologies Used
- Django
- Python
- Html
- Css
- Javascript
- Bootstrap

## User stories

As a user of the application I should be able to:

- Sign in to the application to start using.
- Upload my pictures to the application.
- See my profile with all my pictures.
- Follow other users and see their pictures on my timeline.
- Like a picture and leave a comment on it.

## Codebeat
[![codebeat badge](https://codebeat.co/badges/dc002ecf-b46e-4aef-a444-6202e6f747db)](https://codebeat.co/projects/github-com-monicaoyugi-instagram-master)



## LICENSE
[LICENSE](license)

__Copyright (c) {2020} Monica Oyugi.__
