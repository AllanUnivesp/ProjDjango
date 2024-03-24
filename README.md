`git clone https://github.com/ConradoAlmeida/ProjDjango.git`


Once you've cloned the repository, navigate into the repository.

Create a virtual environment and activate it using the following commands:
`python3 -m venv venv`
> fazer com pipenv
`source venv/bin/activate`
Once you've activated your virtual environment install your python packages by running:
`pip install -r requirements.txt`
Now let's migrate our django project:
`python manage.py migrate`
If there are no hitches here you should now be able to open your server by running:
`python manage.py runserver`
Quick and painless. If there are any issues or problems, leave a comment below!
