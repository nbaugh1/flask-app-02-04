---
title: "Rails User Auth"
date: 2020-01-30
published: true
---

I've spent the past week or so refreshing myself on/learning how to impliment user authentication in a Rails/React application.
I'm working on a project where I want to install Oauth with a third party API. This is something I've done before an have a pretty good
understanding of how to do. The part I don't have any experience with, however, is using token authentication to extend the user
auth system to the client side. I understand what needs to happen (passing a token from the server to the client which the client sends
back to the server to confirm its identity) and how to get it done (either sessions or cookies), but there are a lot of options for
configuration and tools to get this done.
I wanted to use ActiveAdmin in this particular app, which is a Ruby Gem which gives you a user interface for dealing with your database,
and one of the dependencies of ActiveAdmin is Devise, a popular authentication Ruby Gem. To this point, I've only ever really used bcrypt
as an outside library for dealing with authentication, but I've heard of Devise a lot and after a bit of googling, it seems to be a very
popular solution. I've used other tools like Auth0 in other applications, and have definately been pleased with the outcome, but I want to
keep the number of dependencies to a minimum. With that in mind I decided to spend most of my time getting familiar with devise, since I've
already got it installed due to ActiveAdmin. Turns out, devise it so popular because it is extremely useful.
When creating models with devise, out of the box you're provided with a number of preconfigured methods and routes. One of the most important
if which is `before_action :authenticate_user!` (added to your application_controller). This method checks the current_user and makes sure that
it is currently authenticated, and if not, redirects to the login page.
Devise provides you with tools for User (or whatever model) creation, sign-in and out methods, tracking, password recovery, omniauth, timeouts,
locking and more.
