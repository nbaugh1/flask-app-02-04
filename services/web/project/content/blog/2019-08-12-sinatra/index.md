---
title: "Project 2: Sinatra CRUD MVC"
date: 2019-08-12
published: true
---
For my Sinatra module portfolio project I decided to make an app to build a fantasy football team roster. The requirements for this project are as follows:

Build an MVC Sinatra application.
Use ActiveRecord with Sinatra.
Use multiple models.
Use at least one has_many relationship on a User model and one belongs_to relationship on another model.
Must have user accounts – users must be able to sign up, sign in, and sign out.
Validate uniqueness of user login attribute (username or email).
Once logged in, a user must have the ability to create, read, update and destroy the resource that belongs_to user.
Ensure that users can edit and delete only their own resources – not resources created by other users.
Validate user input so bad data cannot be persisted to the database.
BONUS: Display validation failures to user with error messages. (This is an optional feature, challenge yourself and give it a shot!
To make this an MVC app I had to follow the Model View Controller convention for building Ruby web apps. For this module we learned how to use Sinatra and ActiveRecord to do just that. I used Corneal to build the basic scaffolding of my app and MaterializeCSS for the layout and styling.

To get started I used Corneal to set up all of the basic file structure for the app. Corneal builds all of your basic models, controllers, views and configuration files and organizes them into their proper folders and structure.

ActiveRecord was used to build and maintain the database and associations required for this app. For this app I created User, Team, Players and a League (for a yet to be added feature) classes. ActiveRecord takes care of storing the information needed to create instances of these classes as well as allows them to associate with other through has many and belongs to. A User has many teams and a team belongs to a User etc.

This app features the ability for a user to sign up with a username and password, create a Fantasy Football Team with a name and a roster size, add players from a list of active NFL players to that team, drop players from their roster, create more than one team, view a fantasy team’s roster, a player profile page, edit a fantasy team’s name and roster size, delete a team, and log out.

I still have a lot of this I want to do with this app since it is something I might find myself using in the up coming months for fantasy football season. I would like to do a lot of work on the layout and styling of the app since it is still pretty haphazard. Being pressed for time as per usual, I had to make sure to have the app meet the requirements of the assignment rather than spend too much time making it look nice. I’m planning on adding a much more detailed player profile page with data scraped from FantasySharks.com and more detailed team pages with data scraped from my actual fantasy football league homepage. I also plan on adding the ability to add teams to a league.

github: https://github.com/nbaugh1/FFL_APP