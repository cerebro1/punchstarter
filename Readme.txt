1) Install pip (If you have python 2.7.9 or later, you already have pip and can skip this step)
From a terminal enter:
sudo apt-get install python-pip
or
sudo yum install python-pip

2) install virtualenv
From a terminal enter:
sudo pip install virtualenv

3) Inside project folder create virtualenv
From a terminal enter:
virtualenv venv

4) Activate virtual env
From a terminal enter:
. ../venv/bin/activate

5) Install Flask
sudo pip install Flask

6) For ORM use SQLAlchemy
From a terminal enter:
pip install Flask-SQLAlchemy
pip install Flask-Migrate

7)To initialize database use db as instance
From a terminal enter:
python manage.py db init
python manage.py db migrate

8) For image uploading:
From a terminal enter:
pip install cloudinary
visit http://www.cloudinary.com
 -Signup for free
 -Login
 -Go to dashboard
 -Note down cloud_name, API_key, API_ secret
 -Edit the file admin.sh and set the value of environment variables
 -Run $source admin.sh

9)$python manage.py runserver
