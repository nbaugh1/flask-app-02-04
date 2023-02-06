---
title: "Building a Site with GatsbyJS and Sanity.io CMS - Part 2"
published: true
cover: ./cover.jpeg
date: 2020-02-16
---

This series of posts about building a webiste using Sanity.io's headless CMS and GatsbyJS is essentially a walkthrough of this tutorial video by Jason Lengstorf (link to website): https://youtu.be/SLGkyodumKI.

Firstly we'll need to install Sanity if that hasnt already been done. Do this by running `npm install -g @sanity/cli`. After installing the Sanity CLI we are ready to launch Sanity and initialize a new project. 

For my project, I created a directory called /sanity-gatsby-project/ and cd'd into it. This directory will contain my studio directory and my site directoy (where we will build our Gatsby webpage). To bootstrap a new Sanity stuido, in your terminal run the command `sanity init`. This will launch the Sanity CLI which will give a series of prompts to help with setting up your project. 

The Sanity CLI greets you as so: 

"You're setting up a new project!
We'll make sure you have an account with Sanity.io. Then we'll
install an open-source JS content editor that connects to
the real-time hosted API on Sanity.io. Hang on.

Press ctrl + C at any time to quit." 

If you don't already have a Sanity account, your browser will launch and you will be prompted to create one, I chose to create one with my Google account. 

After your account is setup you can select a past project to work on or create a new one. We will be creating a new one for this walkthrough so use the arrow keys to pick 'Create new projcet'.

After this you will be asked to name your project. This is how your project will be named in the Sanity studio app, not necessarily the local directory name. I called mine 'sanity-gatsby-project-studio'. 

The next step will configure your databate settings. You are given a choice between a public or a private dataset, and you will need to name your dataset. For the purpose of this walkthrough we'll set our dataset to public (I haven't used a private dataset yet), and we will give it the default name of "production". Sanity makes it easy by offering to use this default setup and offers a Y/N option here. Selecting no leads to to prompts for your custom choices. 

Next we will set a project output path. This will create the local directory where Sanity be built locally. I set the output path for this project to '/sanity-gatsby-project/studio'.

We will then be given a choice of a few pre-defined schemas that will provide us with a basic project template, or a clean project with no predifined schmea or sample data at all. We will be using the 'blog' project tempalate. This will provide us with some basic objects already set up for us to work with and use as a template for creating our own objects needed for our project. Use the arrow keys to make your selection for the menu prompt.

From here, cd into your studio directory (sanity-gatsby-project-studio) and in your terminal run the command `sanity start` to launch the studio. In your browser, navigate to https://localhost:3333 to access it. 
