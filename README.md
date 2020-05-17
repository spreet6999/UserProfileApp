# UserProfileApp

A web application to upload and list documents for users.

Preview:

Following is Some Images which shows the functionality of the app:

## Homepage:

![Homepage](https://raw.githubusercontent.com/spreet6999/UserProfileApp/master/radme_images/Homepage.png)

## SignUp page:

![SignUp](https://raw.githubusercontent.com/spreet6999/UserProfileApp/master/radme_images/SignUp1.png)
![SignUp](https://raw.githubusercontent.com/spreet6999/UserProfileApp/master/radme_images/SignUp2.png)

## Login page:

![Login](https://raw.githubusercontent.com/spreet6999/UserProfileApp/master/radme_images/Login.png)

## Profile page:

![Profile](https://raw.githubusercontent.com/spreet6999/UserProfileApp/master/radme_images/ProfilePage1.png)
![Profile](https://raw.githubusercontent.com/spreet6999/UserProfileApp/master/radme_images/ProfilePage2.png)

## Instructions to clone this project:

### Install python, virtualenv.
### Make a python virtual environment:
jump in the desired folder and then run "virtualenv ."

### Clone UserProfileApp in this folder:
make sure you have git installed "git clone <repo_link>"

### Install all the dependencies from requirements.txt:
"pip install -r requirements.txt" django 2.2+ version dependent

### Delete the existing Database files and files inside _pycache_.

### Make all the migrations:
"python manage.py makemigrations
 python manage.py migrate"
 
### Now run the server:
"python manage.py runserver"
