---
title: "Setting up a VM Development Enviroment With Vagrant"
published: true
cover: ./cover.jpeg
date: "2020-02-23"
---

Recently I've been working on a project requiring me to work within a virtual environment. Working within a VM environment allows a developer to work with a clean
slate OS and be sure that they are working in exactly the same setup as thier teammates. A VM is essentially a computer running within another computer. For this project I decided to use Vagrant 
and VirtualBox. 
The setup process for Vagrant is quite simple. First. just install the package for your particular OS. Next create a new directory `mkdir new-vagrant`. Cd into that directory `cd new-vagrant`. 
Once inside of this new directory run `vagrant init hashicorp/bionic64` the hashicorp/bionic64 tag specifies a predefined virtrual machine setup. Running this command will create a Vagrantfile in the directory.
Running `vagrant up` will boot up your new VM. From here you can connect to your new VM with `vagrant ssh` which will land you at a terminal prompt for your new machine running Ubuntu.
One of the great features of Vagrant is provisioning which allows you to sync files and folders from your local machine to your VM. To do this you specify a specific directroy within your new-vagrant directory
to be provisioned. This directory will mirror whatever you put in it and appear as /vagrant on your virtual machine. ß