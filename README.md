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

part 2: making users

what info does penn clubs need from users? prob undergrad, year, interests, major. and then, looking at the routes, i'll eventually need user info like their favoriting of clubs. so, i'll use username as a primary key, i'll also add columns like name, email, year. add favorite_clubs as well. there can be multiple favorite clubs, so i'll have to use the same logic i used for the club/tag relationship with multiple tables. 

push 5: added user model, created user josh and saved him to the database.

there's error with Club and Tags tables. it seems like sqlalchemy doesn't know how they're connected, might need foreign keys. testing by removing db.relationship line. okay fixed it. removing db.relationship fixed it because db.relationship tried to force a direct relationship rather than going through the middleman of Club_Tags. now, however, there are problems with my user model code. oh, i put the user creation code in the wrong file. put the user creation code into bootstrap.py. 

push 6: fixed Club and Tag relationship, put user creation code in right place.

great, user creation is working. now have to load clubs.json.

the load_data function should hypothetically just open clubs.json, turn it into python, and then output it. i think i'll import the python function json to read the json from opening the file. imported json, read the file, testing to see if it actually worked with print statement. pushing.

ok the data is definitely read. it's not a very clean print though. i'll have to format it. i think looping through data for individual clubs and then calling their parts? maybe make a club object as well, to store each datapoint.

push 8: looped through data while storing each individual's club's datapoint in a club object. 

i need to handle tags now. this is more complicated, with the matching tables. i'll use a for loop for tags because there can be multiple. testing with a for loop that loops through club["tags"] and a print statement to see if it actually will loop. 

i don't want to create a new tag for the same instances, like i don't need 3 "undergrad" tags. it's redudant. therefore, i think i need to add a query filter that'll help me determine whether each tag checked already exists in a database. that way, i can reuse existing tags and determine if i need to create a new one. 

push 9: looped through tags, used query filter to check for existing tags to reduce redudancy.

now, i have to incorporate Club_Tags to tell the database which particular club has which tag, or the relationship. so, i'll create a Club_Tags object that can hold club code and tag_id. i added db.session.commit to actually commit to the database. i'll also use flush() when creating a new tag to flush it (or like send temperary changes to database) so that tag_id is available for the ClubTags relationship.

push 10: added flush(), commit(), and ClubTag relationship.

testing bootstrap, it runs fine. but adding a print for clubs, tags, and clubtag relationships to see if it actually works, it outputs 5,3,3. which is wrong, because there should be 7 tags and 12 relationships. so, i have to debug.

ok, i found the problem, it was indentation. my for loop for tags in clubs was outside of the for loop for clubs in data. pushing! now, bootstrap.py correctly outputs 5,7,12, meaning all of clubs.json is being correctly loaded onto the database! all of part 1 complete!

part 2: apis. so our client side should send a get request to the api to return all the clubs and details. from there, our flask request needs to receive that, query it, turn it back into json, and return the json to the client. then we can use postman to test it. first, i'll add a route that simply queries the database to see if flask accepts it. ok, it runs but there's an internal error. i think it's because my route doesn't return anything. 

i'm trying to fix the 500 internal error. i'm not sure what's wrong right now. it seems that my current flask app isn't registered with sqlalchemy? 

it seems that app.py was creating db and importing models while models.py was importing db from app.py. models.py executed app.py a second time because app.py was running directly in terminal, so there were two app.pys. then, i think that two sqlalchemy instances were created, leading to the error of not registering with sqlalchemy.  i think the fix is to not let models call app.py. 

push 11: fixed circular dependency with db and app by moving db to models.py

ok, now, i have to convert my custom Club class into json. i can't just do jsonify because it's a custom class so flask will just give me an error. i'd be simpler if the Club class just became a python dictionary. the code, name, and description are already on the object, but how do we incorporate the tags?

i think for the tabs, i'll loop through each club and query clubtags using club's code to find its tag_id. from there, i'll query the tags table with the tag_id to get the string names for each tag. now that i have tags sorted out, i just appended it all onto a clubs_data dictionary to return. since jsonify can read python dicts, i'll just use jsonify to send the json array to the client. using flask, it works.

push 12: converted custom Club class into dictionaries through looping and querying to get json response for get request.

ok, that's the get route done. i think i'll do search clubs next because it's also querying clubs. i think we can simply send a get request to get the data, but we need to filter it first using query? and how efficient can we make it? if we use python, we'd have to query everything, which takes a while when scaled up. it might be faster to use sql to filter the database natively. like, before any data is sent to python we can like filter the database using sql because transfering the data then filtering is extra steps. 

i think i'll add sql database filtering by replacing the .queryall already in app.py. i'll get the search string from the url using flask's request args. we need to know check if there's a search term present in the link, and if not then just send it all (cause nothing specific is searched). then, i'll use sqlalchemy to filter the database. would it matter if there's different cases? i'll use the ilike filter, it makes the search case-sensitive. i'll also use sql's % thing to check if anywhere in the name there's the search term so where it appears doesn't matter.

push 13: created the search clubs route using sql database filtering.

for the next route, i think i'll do the one that shows the number of clubs for each tag. our get request already return clubtag relationships, etc. i'll start by sending a get request to get the tag data, then i'll sort through clubtags. since clubtags is organized by tag_id, i can simply just check how many rows in clubtags have the same tag_id. that's pretty simple, honestly. we can even use the built in count function in sqlalchemy. append the data into a dictionary, and then jsonify to send it back to the browser. works!

push 14: created number of clubs for each tag route using get requests, dictionaries, and .count()

i'll work on getting user profile route next. what would be included in a user profile that could be public/private? like username and name are public, but things like email, password (or its hash), pennkey, etc should be private. i'll first update my user class in models.py to include name and email. 

to search through all the users, i'll query all users by checking the username. i'll use the <> flask wildcard so i don't have to create a new route for each username. it'll just be an argument where flask dynamically searches by username variable. also, an if statement to test if the username actually exists, and if not, then an error of 404 status is returned. private info, like the email, isn't returned. it's kept private.

push 15: created the get user profile route with 404 handling and privacy protection using <> wildcards and queries.

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
