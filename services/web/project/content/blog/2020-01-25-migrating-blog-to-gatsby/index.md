---
title: "Migrating Blog to Gatsby Site"
published: true
cover: ./cover.jpeg
date: 2020-01-25
---

During the process of building my personal website I decided that I wanted to display my blog posts as well. Having already started this blog and hosting it on WordPress, I figured the easy way to go about it would be to use the WordPress plugin to pull the data from this site and display it on my Gatsby site. This would be sort of a round about way of setting up a headless CMS. In order to uncomplicate the amount of workspaces that I deal with, and to organize my content into one domain, I changed course and decided to simply add the gatsby-theme-blog to my personal page, and migrate my posts from this site to my personal page.

I manually added the blog theme to my site by running npm install --save gatsby-theme-blog. After that, as with most gatsby plugins, a but of configuration is required. The plugin needs to be added to the gatsby-config.js file. This is where the blog plugin settings for your blog path, content directory, assets and such can be set.

From here, adding content to your blog is as easy as dropping a markdown file into your content/posts directory. After a bit of trial and error I realized that in order for your site to be to properly query your posts, you need at least one post with a title and date as well as some content body. The next step in this process for me is to hopefully just a bunch of copy and pasting to get my content from this site to my gatsby site.