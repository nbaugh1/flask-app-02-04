---
title: "React From Scratch Without create-react-app"
date: "2020-09-10"
featured: images/featured.jpg
published: true
---

One of the best things about working with React is the ease of launching
a new application thanks to Facebook's `create-react-app`. `create-react-app`
builds everything you need for a modern React web application out of the box
with a single terminal command. As great as this tool is, there are a couple
small drawbacks I've encountered so far. The first is that I usually spend a
bit of time removing boilerplate code and arraging things to my liking, and
the second, more substaintial issue is that while `create-react-app` is great
for stepping right in to start using React, I wanted to zoom in and understand
what is happening at a lower level.

While I will definitely continue to use `create-react-app` as my main React tool,
I decided to learn to build a React app from the ground up with the added bonus
of being published to `npm` and downloadable via `npx @nbaugh1/scratch-react <APP NAME>`.
I referenced a number of articles to learn how to do this to see if there is any
variation in the process, but it looked to be pretty straight forward. The
main source that I used was the article (https://blog.usejournal.com/creating-a-react-app-from-scratch-f3c693b84658)
linked from the offical React docs. I won't cover every line of code written since its
all in the linked artice, this will be more of a high level overview of what's happening.

Creating this app first requires creating the template `index.html` file
that will be used to render the webpage of the application. The first important
thing particular to our React application is a `<div>` with an `id` equal to `root`,
which we will later use to tell React where to insert elements into the DOM.
`<div id="root"></div>` is how this line looks. The second important thing about our
`index.html` file is a tag pointing to the location of all of our sweet JavaScript.
We'll add a `script` tag pointing to `bundle.js` which is what we'll name the file
to be output by Webpack - `<script src="../dist/bundle.js"></script>`.

Since we're working with React, which means using JSX, and writing ES6 JavaScript, we
need to use Babel to transiple our JavaScript down to a browser compatable version. To
do this, we need to create a `.babelrc` file where we will configure the needed babel plugins.
The plugins needed for this project are `preset-env` for the ES6 and `preset-react` for our
React code.

Next we need to setup the all important Webpack. We'll do this in a file placed in our root
directory called `webpack.config.js`. This will be a node.js file which exports a JavaScript
object containing all of our requiered configuation settings. A lot of important things happen
based on the settings in this object. Its where we'll define our `entry` to the app (`index.js`),
the mode in which we will be working (development), the rules that will define which files
are compiled by webpack, the details of where the output file should be located and what it is
named, the settings for our localhost development server, and finally enabling HotModuleReplacement
to see live changes to our app without manual reloading.

Within the `rules` we configure for webpack, we set it to use babel to load all of our `.js`
and `.jsx` files (excluding `node_modules`) via the presets we set up in our `.babelrc` file.
We setup our `bundle.js` file's output path by defining a `publicPath` and a `filename`. We
also setup our development server to serve content from that the output file, a publicPath and
port from which it will be accessable (localhost:3000 usually).

Finally, we need to use React to tell our app exactly where to render what we've built. To do
this we use the `ReactDOM.render()` function provided by React. Into this function we pass our
App component and the HTML element to apend it to `document.getElementById("root")`. From this
we get the familiar line of `ReactDOM.render(<App />, document.getElementById("root"));` in
our index.js file. We then use our App.js component to then start building our our applicaiton.
Lastly, we need to export our App.js component as a `hot` module using `react-hot-loader`, `export default hot(module)(App);`

And thats about it. We use React to write our independent declaritave component based UI, using
JSX and ES6 JavaScript. We then use webpack to bundle all of the javascript modules included
in our app, using babel to transiple our code in to browser compatable script, and then provide
the output bundle to be delivered by our development server.

For a more detailed walkthrough, please see: https://blog.usejournal.com/creating-a-react-app-from-scratch-f3c693b84658

Source code for this project here: https://github.com/nbaugh1/scratch-react
