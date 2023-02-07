---
title: "Gatsby Plugins and GraphQL"
published: true
cover: ./cover.jpeg
date: 2020-01-18
---

One of the main features of Gatsby (a static site generator based on React) are Plugins. “Gatsby plugins are Node.js packages that implement Gatsby APIs. For larger, more complex sites, plugins let you modularize your site customizations into site-specific plugins” [from Gatsby Docs]. The Gatsby community has created a huge number of Plugins which are available to be installed (an index can be found on the Gatsby site). Using plugins enables a developer to add functionality to a site without having to reinvent to the wheel when building web sites.

I decided to take a hack a using the gatsby-source-wordpress plugin to grab posts from this blog and add a feed to my personal webpage. The first step in using a plugin is to install it via your preferred CDN (npm install gatsby-source-wordpress or yarn add gatsby-source-wordpress). Next, as with all Gatsby plugins, some code needs to be added to gastby-config.js needs to be added to configure the plugin. The plugin docs show and explain the code required to connect the plugin to your wordpress source.

One of the great things about Gatsby is its use of GraphQL and the GraphiQL IDE which you are able to access by navigating to localhost:8000/__graphql in your browser (assuming you have a development server running). The GraphiQL IDE makes handling your data unbelievably easy. You can simply click a menu of query options on the left, see the shape of the data object in the middle, the result of the query in another panel, and the code required to build a component that makes that query in another panel.

This recent discovery how nice it is to use GraphQL and the GraphiQL IDE has me excited to start using it in future projects. I think thing of more than a couple of times when being able to manipulate and browse through my data that these tools enable would’ve saved me a lot of pain and allowed me to be more creative with what I could build.