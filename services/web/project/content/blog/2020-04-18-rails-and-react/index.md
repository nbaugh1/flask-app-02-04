---
title: "Various ways to use React with Rails"
date: 2020-04-18
published: true
---

I've spent the last few days reading about the various ways to use Ruby on Rails and React together to
to build a web application. During my bootcamp I learn how to use Rails in a couple of different ways to
build apps, first in a standard Rails only MVC style and then coupled with React using Rails as a backend
API. I'd become curious if anyone has since developed a more integrated way to work with Rails and React
together, rather than basically having 2 seperate apps working together. I found 2 other solutions which
enable the use of React components with .erb files, allowing you to render JavaScrpit and React components
directly in your Rails view files.
Initially, I was drawn to the idea of working more heavily with Rails as my development tool rather than
leaning on React. There are at least 2 people gems which are used to achive this functionality, `react-rails`
and `react_on_rails`. Both of these gems use Babel to convert the jsx into erb, they differ in the ways that
the views are eventaully rendered. The problem, however, is that I personally find this reduction in
seperation of concerns to be less desireable. I kept finding myself trying to recreate the flow that
`create-react-app` sets up out of the box. While I'm still not exactly sure which way is more performant,
the Rails API method seems to be the most modular and scalable.

-Rails API
-React on Rails
-react-rails
