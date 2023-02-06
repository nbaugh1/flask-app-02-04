---
title: "Casing Conventions for Different Languages"
date: 2020-05-09
published: true
---

I often forget the various different ways that I'm supposed to case the names of methods, variables, functions etc. I was working on a Rails API today and had to look up how to name the attributes for the models I was scaffolding. I knew off hand that models themselves needed to be `Capitalizes and PascalCased`. I couldn't remember off-hand how to name my attributes though. When working with Ruby, the answer is `snake_cased`.

I've been working with JavaScript as well a lot lately. Similar to Ruby, classes in JavaScript are `PascalCased` however `camelCasing` is used instead of `snake_casing`.

These are only conventions, which means it won't necessarily break your code if you don't follow them. HOWEVER as we know, Ruby on Rails is very particular about it's conventions, its pretty much built around them (Convention over Configuration). This means that Rails will expect things to be named following these specific conventions.