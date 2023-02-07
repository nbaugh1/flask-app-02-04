---
title: "Customizing Bash"
published: true
cover: ./cover.jpeg
date: 2020-02-01
---

Now that I've been coding alomst daily for the better part of a year I figured it was time to set up some aliases to make using the termial a bit more efficent. No matter how may times I type it, I well never spell gatsby correctly first time (my fingers think its gastby and I can't convince them otherwise). This along with the usual git commands are prime examples of repetiative commands that can be simplified with an `alias`. 
An `alias` is esseitially a custom made keyboard shortcut that refers to some command that you can enter into your terminal shell of choice (I'm using bash currently). The process is pretty simple and strightforward altough I ran into a bit of a hitch along the way which. The problem was that my user account on this laptop apparenty didn't have "superuser" right which prevented me from editing system files. This was a problem because in order to save my aliases I needed to edit the ~/.bash_profile file. This may have been a bit of overkill just to edit one file, but I decided to go the route of learning how to sign into my MacBook as the `root` user. (walkthrough: https://support.apple.com/en-us/HT204012) Root access is basically `godmode` in terms of access to your computer so proceed at your own risk.
Creating an alias is simple. The format is `alias ALIASNAME="TERMINAL COMMAND"`. For example one of mine would be `alias gatup="yarn add gatsby-cli"` which allows me to run the command `yarn add gatsby-cli` by typing `gatup` (this updates gatsby-cli to the most current version). 
After you save changes to your bash_profile, the shell needs to reload the file. This is done by typing `source ~/.bash_profile`