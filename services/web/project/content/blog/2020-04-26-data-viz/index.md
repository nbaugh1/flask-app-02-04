---
title: "Data Visualization"
date: 2020-04-26
published: true
---

I did a lot of work this week with diffrenet methods of data visualzation. The main and most powerful tool for data viz in JavaScript is D3. With great power comes an enormous learning curve and since building these charts and graphs from scratch isn't my main focus, I decided to explore some popular React data viz libraries. There are a handful of popluar libraries and I've experimented with a couple. The first is Recharts, which is very minimalist and easy to use and was what I had the easiest time working with. The next is Nivo, which seems to have a much wider range and more visually appealing library of components. Nivo's doc site is beautiful, interactive and powerful, however in my opinion it is a bit lacking in basic implimentation explinations. Now that I've gotten a better grasp of working with Recharts, I might take another hack at Nivo. 

In order to play with these data viz tools, I build a quick creat-react-app playground to basically plug in components and mess around with what the library has to offer. I quickly realized I wanted to do a bit more than feed in sets of dummy data and decided to build in some data fetching functionality. I try to stay current with best practices so I try to use Hooks as often as possible. My main stumbling block was making sure that my data was being passed in right shape. 