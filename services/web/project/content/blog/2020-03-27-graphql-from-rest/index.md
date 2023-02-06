---
title: "Building a GraphQL Schema (with data from a REST API)"
date: 2020-03-27
published: true
---

I decided to build out a dashboard to track information related to the Codiv-19 panic using GraphQL and React. I used the 
NovelCOVID API (github.com/NovelCOVID/API) as my datasource. I've been using Apollo to build
both ends of the app with thier Client and Server packages. Apollo provides a set of hooks
and components that take care of most of the data handling and prodive a nice platform for 
connecting a react client to a GraphQL backend. 