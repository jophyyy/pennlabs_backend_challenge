# Penn Labs Backend Challenge

## Documentation

Fill out this section as you complete the challenge!

## Installation

1. Click the green "use this template" button to make your own copy of this repository, and clone it. Make sure to create a **private repository**.
2. Change directory into the cloned repository.
3. Install `pipx`
   - `brew install pipx` (macOS)
   - See instructions here https://github.com/pypa/pipx for other operating systems
4. Install `poetry`
   - `pipx install poetry`
5. Install packages using `poetry install --no-root`.

installation done!

## File Structure

- `app.py`: Main file. Has configuration and setup at the top. Add your [URL routes](https://flask.palletsprojects.com/en/1.1.x/quickstart/#routing) to this file!
- `models.py`: Model definitions for SQLAlchemy database models. Check out documentation on [declaring models](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/) as well as the [SQLAlchemy quickstart](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#quickstart) for guidance
- `bootstrap.py`: Code for creating and populating your local database. You will be adding code in this file to load the provided `clubs.json` file into a database.

initial ideas

all the data for my database is in clubs.json. to organize it and sort through it, i need to load clubs.json into an sqldatabase. from there, i'll use flask backend to communicate with rest apis so that the actual application can read clubs.json and do what the app needs to do (sort it, filter it i think? for penn users?)

sqlalchemy will be the transitioner from sqldatabase to flask backend. then i'll use postman later on to test case my application as like an actual user to see what penn students would actually see. hci? so, i'm thinking clubs.json --> sql database --> sqlalchemy --> flask --> rest api --> postman (to test) --> app

part 1: clubs.json. how do i represent it into sqldatabase and sort it? each club has code, name, description, and tags. maybe i'll use that as tabs in my sql. columns should be code, name, description and then rows for each club. etc, tags? there's multiple for each club, some overlap. so how should i like sort it in sql. can't just simply be one column there's multiple. can't just directly input it into sql, won't it like make it just one string. that won't work cause each tag is different and what if i want to sort by single tags. one column for every tag? maybe. would make it easier to search like if we wanted to find if a club is technology or pre-professional. like where technology = true would be simple. but how do we usually update columns for future tags? we'd have to update every club seperately. 



## Developing

0. Determine how to model the data contained within `clubs.json` and then complete `bootstrap.py`
1. Activate the Poetry shell with `poetry shell`.
2. Run `python3 bootstrap.py` to create the database and populate it.
3. Use `flask run` to run the project.
4. Follow the instructions [here](https://www.notion.so/pennlabs/Backend-Challenge-862656cb8b7048db95aaa4e2935b77e5).
5. Document your work in this `README.md` file.

## Submitting

Follow the instructions on the Technical Challenge page for submission.

## Installing Additional Packages

Use any tools you think are relevant to the challenge! To install additional packages
run `poetry add <package_name>` within the directory. Make sure to document your additions.
