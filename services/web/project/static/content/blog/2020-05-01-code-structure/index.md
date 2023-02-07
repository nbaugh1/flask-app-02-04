---
title: "Code Structure"
date: 2020-05-01
featured: images/featured.jpg
published: true
---

One of the nice things about with Ruby on Rails as a newbie is that the "convention over configuration" philosophy means that when working on a project, there are standard ways of organizing your code. The conventions of Rails mean that certian files should be in specific places along with specified naming conventions as well. Because of these conventions, quickly builing a project with Rails is easy to do however, for better or for worse, your are (or are supposed to be) restraied to these conventions.

When working with a library such as React, however, things are quite a bit different. React simply provides the developer with a very powerful tool and lets you decide how to set it up for your self. There are tools such as Create React App which will set up a boilerplate setup for an app, but that mainly sets up and configures tools that are not part of React itself, to make a working web app. Where Rails follows the MVC design architecture, expecting Models Views and Controllers to be linked in specific ways, it is up to the developer how to organize the Components and Layouts of thier React app, and to guide the flow of data to make thier app function.

I came across this tweet: https://twitter.com/JoshWComeau/status/1255533537463341057 by @JoshWComeau showing his system for structuring his code. I follow a very similar pattern with posts on this blog. Each post is an index.mdx file which is inside of its own directory named the same as the title of the post (ex `content/posts/2020-05-01-code-structure/index.mdx`). Doing this apparently makes importing components much more efficient.
