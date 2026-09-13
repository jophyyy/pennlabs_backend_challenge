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

part 1: clubs.json. how do i represent it into sqldatabase and sort it? each club has code, name, description, and tags. maybe i'll use that as tabs in my sql. columns should be code, name, description and then rows for each club. etc, tags? there's multiple for each club, some overlap. so how should i like sort it in sql. can't just simply be one column there's multiple. can't just directly input it into sql, won't it like make it just one string. that won't work cause each tag is different and what if i want to sort by single tags. one column for every tag? maybe. would make it easier to search like if we wanted to find if a club is technology or pre-professional. like where technology = true would be simple. but how do we usually update columns for future tags? we'd have to update every club seperately. so prob not that. especially since like some tags might not appear a lot. 

i also have to consider converting sql database back into python and then code will turn into json for flask to read. so sql has to be simple and organized and match everything. what if instead of using the actual strings as columns and seperators we do like matching for tags? like we give each tag a number like "tag_id" that matches undergrad with 1, tech with 2, etc. that way, the only column we need is kinda just tag_id, right? and then we can use a seperate table for all the tags that will be easy to add to. that way, we don't have to update each club with new columns for every tag. we can just add the tag to the seperate table and then add it to the club directly. like in the sql, we can have club and then tag_id. so its kinda like a relationship between two databases, making it easier to convert seeminglessly? maybe? like i'd be searching for numbers rather than strings. each club will be connected to diff tags. i have to test it out. 

so how to actually structure database? club table's key should be code, unique easily defines each club and it's simpler / shorter than name. unique too, like how some clubs can be similar in name (taekwondo clubs for example). or we could simplify it with like just "id" and give each club a number. what would be the benefit? i'm not sure. 

tag's table key should just be tag_id and then name. so each tag_id is matched with a name so it's easy to convert back to json. i'm thinking json should include full names so it's easier to read but sql holds ids so it's stable to refer to.

so how do i fit tag_id inside the club table? if each club has multiple tags, and there's only one row for each club. i don't think i should have multiple rows for each club's different tag. what if i created a different table. so the club table would have like "club_tags" simply as a number, let's say 1. then, in clubs_tags table, we have the club's code match with each tag_id. so, when reading from club_tags, we can just pull tag data for say locust clubs using the club's code. i don't think there's a good way to just put this into the club table. what if we just seperate it? like club name and stuff will come from the club table and then we get the club tags just from the clubs_tags table. so sqlalchemy calls data from both to convert to python then later code converts it into json. simpler than trying to squeeze it all into one table. multiple relationship tables? might work. 

ok, now to put all these ideas into model.py. 

first push: created club table for using sqlalchemy("db"). made columns as i said before, code as the key, clubs, description, and tag_id. 

second push: fixed tags_id in club table and added secondary table for tags as mentioned in initial thoughts for table relationships 

i think i need to use foreign keys for clubs_tags. it'll help with pairing specific club and tag together for code reference.

third push: added third table for clubtags, used foreign keys for better and more specific matching

ran the test on bootstrap.py, error. error is basically at sqlalchemy import, it might be too old since there's a compability issue with python 3.14. it didn't even get to the application code. ima just update sqlalchemy, it seems that this project was supposed to be for python 3.9 and thus that's why the sqlalchemy is a little outdated. updated, code runs. but there's some errors in my code. mistyped True as "true". first simple error, there's more.

reran it with fixed True, sqlalchemy is complaining about something. oh, i gave club tags table two columns but sqlalchemy can't read it because the database doesn't have a primary key. what should be it? club_code or the tag_id? because primary key helps us locate a single, specific row, and club_code and tag_id appear multiple times. so i don't think it can be either. it'd probably have to be a combination of the two somehow. what if both are the primary key? can we even do that? yes, apparently, both columns can combine into one primary key. let's see if that fixes it. 

ok yay, bootstrap.py runs! pushing 4th edition!



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
