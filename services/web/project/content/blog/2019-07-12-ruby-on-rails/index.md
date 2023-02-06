---
title: "Project 3: Ruby on Rails"
date: 2019-09-16
published: true
---
The task for our third module project in the Flatiron bootcamp is creating an app using Ruby on Rails. Rails is a framework that used the Model View Controller design pattern to assist in building applications using Ruby via various gems, helpers, ActiveRecord, and magic. The requirements for the project include various ActiveRecord associations, data validations, user signup, login, and onmiauth login from a thrid party.

My plan for my project is to create an app which a person can use to log their dining experiences at different restaurants. Essentially my app can be described as a combination of Twitter and Yelp. The inspiration behind this idea is inability to ever remember all of the various places my partner and I have eaten at during our time living here in NYC. My initial strategy for this project is to start simple and small, meet the project requirements as quickly as possible, keep and clean and uniform site design (I decided to use the Bootstrap CSS layout for this project) throughout development, and use any extra time for the in the week adding extra features.

My first steps in building the app are to create the models, build the database, controllers and some initial views. Rails makes this a pretty simple process with its various rails generate commands that take care of the dirty work of creating your models, controllers, migrations and other various parts of your app.

Setting up object associations in Rails is a breeze. has_many and belongs_to relationships are established simply by adding lines like the following to your models:

class User < ApplicationRecord
  has_many :visits
  has_many :restaurants, through: :visits
The has_many and has_many through ActiveRecord methods handle the SQL dirty work of assigning foreign keys and associating objects through a join table ( :visits ).

My next steps are to stub out Controllers (along with CRUD Actions) and Views for some of the basic functions of the app. Following that, adding sign up and routine login features. This is something that was much easier the second time around. Plenty of lessons were learned while adding user authorization and authentication to my Sinatra app, so this time around combined with Rails helpers like form_for, I had this part up and running pretty seamlessly. OAuth is a different matter.

I decided to use Google OAuth, rather than Facebook, because for some reason I though it might be “fun” to try out a service that we hadn’t covered in our study groups.


Well, not really. The dumb part was thinking that the process would be much different depending on the provider and that I wouldn’t really be able to rely on the lessons from my study groups. Well I was wrong. As it turns out the process is almost exactly the same. Something that I’m sure my instructor would have told me if I hadn’t waited until the end of the week to work on this part of the the project, after office hours had ended. That is dumb. Oh well, I got it working regardless and again learned a lot of things in the process. I can’t wait to start to explore what’s possible using tools like Google’s and Yelp’s APIs when I have time to go more in depth. Like my last project, I plan on continuing to develop it after I submit it for review. Hopefully it gets more extra-cirrcular attention than my Sinatra project did. ( I expanded on that one a fair amount after I submitted it, but eventually my regular curriculum took over all of my time again. It seemed kind of distracting going back to Sinatra while learning Rails.)

Getting OAuth working is one of my favorite accomplishments so far throughout my bootcamp experience. It was a bit of a painstaking process the first time around which I hope will become much easier with experience, the result is a very handy feature that everyone who uses apps understands. So far, without much reflection, my top moments so far have been -Getting Sign in with Google to work, -Connecting to and using an external API for the first time, and -Successfully scraping data with my CLI gem.

Next on up on my app is getting all of my models and database tables associated correctly. My User class already has a lot of work done due to login work, I decided to get my Visits resources stubbed out next because they’d be relatively simple. My Visit class is also acting as a JOIN table between my User class and my Restaurant class. By using has_many :through in my models, and adding a user_id and a restaurant_id column to the Visits table, I am able to call methods: user.restaurants and restaurants.users, as well as user.visits and restaurant.visits.

After setting up my Visits class I moved on to connecting to the Yelp API to help build my Restaurant objects. I wanted to use an API in this situation because it seemed like an easy way to have handle the data I would need to use for this object. This feature is in a very basic form but what how it works is: a user enters the name of a restaurant, that name is used to query the Yelp API Business Search, and the top result’s data is used to build a Restaurant object (using the name, display address, and id for now). There are many flaws and many ways for this feature to be improved, however this is a Minimum Viable Product situation.

Last on my plate before I feel like this project is ready to be reviewed setting up my views to display various things like user.restaurants, resturants.users, etc. By that point I’ll feel like its good enough to submit, but still has mountains of work left to do. I need to add better validations, trim down my routes, refactor my views, add more error displays, just to name a few things. Finally, I plan on figuring how to get this thing up on Heroku and see what happens with that.

Github: https://github.com/nbaugh1/wdye