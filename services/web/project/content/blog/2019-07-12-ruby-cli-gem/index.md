---
title: "Project 1: Ruby CLI Gem"
date: 2019-07-12
published: true
---
For our first end of portfolio project we have been assigned to create a Ruby CLI Data Gem. 
I wanted the subject matter of my project to be somewhat original and to be something that I find interesting and useful. Being the political junkie that I am, I immediately thought of the huge field of Democratic candidates running for president in the 2020 election. I decided it would be useful to write an app that presents the user with information about the individual candidate’s campaigns.

Since this project requires that we scrape data from a web page, I set out to find a web page that displays this information in a condensed and concise format. It didn’t take me too long to land on Ballotpedia.org as my data source. This page provided an easy to navigate list of candidates, each hyperlinked to a seperate profile page with relavent details about the candidate’s campaign.

From here I had to decide what information I wanted to show the user and how to scrape it from the web pages. Based on the information provided on the profile pages I decided that a quote from the candidate explaining why they are running, a more detailed summary of their campaign platform and experience, and a handful of recent news blurbs about the candidate would be appropriate.

First I set out to build my Scraper Class and methods. I decided I needed one to first build my Candidate instances. I decided that I should iterate through the list of candidates and build instances of a Candidate object with a name and a profile URL slug (to be used by a second method to scrape their profile page). I did so by using Nokogiri and Open-URI with the following code:

BASE_URL = "https://ballotpedia.org"
    
    
    def self.name_list_page
        Nokogiri::HTML(open("#{BASE_URL}/Democratic_presidential_nomination,_2020"))
    end

    def self.scrape_names_and_profile_pages
        name_list_page.css("div.mobile-columns ul li b a").each do |candidate|
            Dems2020::Candidate.new(candidate.text, candidate.attribute('href').value)
        end
    end
At the outset of building the project I stored this data in an array of hashes, because I felt that my biggest first obstacle would be figuring out which CSS selectors I would need to use and how to iterate through them to properly scrape and store them. Later on I refactored my code use Objects for this instead. To scrape the data from the individual profile pages I used this method:

def self.add_campaign_info
        Dems2020::Candidate.all.each do |candidate|
            candidate_info_page = Nokogiri::HTML(open("#{BASE_URL}#{candidate.info_page_url}"))
            candidate.quote = candidate_info_page.css("td")[3].text
            candidate.summary = candidate_info_page.css("p")[9..11].text
            candidate.news1 = candidate_info_page.css("li.panel ul")[0].text
            candidate.news2 = candidate_info_page.css("li.panel ul")[1].text
            candidate.news3 = candidate_info_page.css("li.panel ul")[2].text
        end
    end
Here I iterate through an array containing all of my Candidate instances and add a short quote, a campaign summary and 3 recent news headlines. One item on my TODO list is to try and refactor this code in such a way that the data is written to each candidate instance by a Candidate class method rather than by the scraper itself. Also I think that the news headlines can be stored in a better way such as in an array or maybe as objects themselves. Another TODO item.

The code for my Candidate class object is pretty short currently. It contains an initialize method, a method called find_by_index which is used by the CLI object to find a particular Candidate instance within the array of all candidates based on the user selection, and a method called all to access that array.

class Dems2020::Candidate
    attr_accessor :name, :info_page_url, :quote, :summary, :news1, :news2, :news3

    @@all = []

    def initialize (name = nil, info_page_url = nil, quote = nil, summary = nil, news1 = nil, news2 = nil, news3 = nil)
        @@all << self
        @name = name
        @info_page_url = info_page_url
        @quote = quote
        @summary = summary
        @news1 = news1
        @news2 = news2
        @news3 = news3
    end

    def self.all
        @@all
    end

    def self.find_by_index(input_number)
        Dems2020::Candidate.all[input_number - 1]
    end
end

Lastly I needed to build a CLI object. This is where I present the user with a list of candidates, ask them to make a selection, and then show the the information about the selected candidate. There were a lot of different ways that I thought about doing this in different formats and with various levels of interactivity, but because I’m working on a tight schedule since I also work full-time, I decided the best way would be the most simple and straight-forward way would be to show all of the information after the user makes a selection. I plan on doing plenty of refactoring later but I’m currently satisfied with having the app just meet the requirement of going one level deep.

Initially I wrote one giant block of code that formatted and displayed the information in the way that I wanted. I’ve sense broken it up into methods in order to make DRY. This is still a work in progress. Things on my TODO list include making sure that the user input is valid and presenting them with a message telling them to try again. Currently the app errors out if the input is a number outside of the possible range of options, and also does not deal with non-integer inputs correctly. This is the code for my CLI class (still needs to work):

class Dems2020::Cli

    @@selected_candidate = nil

    def self.list_candidates
        Dems2020::Candidate.all.each_with_index do |candidate, index|
            puts "#{index + 1}. #{candidate.name}"
            
        end
    end
    
    def self.start
        system 'clear'
        puts ""
        puts ""
        puts "2020 DEMOCRATIC CANDIDATES FOR PRESIDENT"
        puts ""
        puts "========================================"
        Dems2020::Cli.list_candidates
        puts "========================================"
        puts ""
        puts "Please enter the number of the candidate which you like to learn more about: "
        get_candidate
        print_candidate_info
        list_or_exit
    end

    def self.get_candidate
        input_number = gets.to_i 
        @@selected_candidate = Dems2020::Candidate.find_by_index(input_number)
    end

    def self.list_or_exit
        puts ""
        puts "================================================================"
        puts ""
        puts "To return to the candidate list enter 'list'"
        puts "To exit enter 'exit'"
        input = gets.strip
        if input == 'list'
            start
        elsif input == 'exit'
            puts "Thanks! Goodbye"
        else
            puts "Sorry, I didn't understand that"
            list_or_exit
        end
    end

    def self.print_candidate_info
        system 'clear'
        puts ""
        puts ""
        puts "You have chosen to learn more about -#{@@selected_candidate.name}-"
        puts "================================================================"
        puts ""
        puts "#{@@selected_candidate.name}'s reason for running for president in 2020:"
        puts ""
        puts "'#{@@selected_candidate.quote}' -#{@@selected_candidate.name}"
        puts ""
        puts "================================================================"
        puts ""
        puts "Summary of #{@@selected_candidate.name}'s campaign platform and experience:"
        puts ""
        puts @@selected_candidate.summary
        puts ""
        puts "================================================================"
        puts ""
        puts "Recent news about #{@@selected_candidate.name}:"
        puts ""
        puts @@selected_candidate.news1
        puts ""
        puts @@selected_candidate.news2
        puts ""
        puts @@selected_candidate.news3
    end
end

There are also still a couple of things I’d like to do like removing citation markers form the text and also removing a couple of bugs due to inconsistent formatting on the web pages, as well as making everything a bit prettier in the CLI, but right now this is what the app looks like when run:



Warren 2020!
One downside to this project is that it will seem less and less useful as time goes on and people drop out of the race, but for now it works for my assignment. The code should also be easily refactored to be applied to other elections, as long as ballotpedia doesn’t change things up too much.

UPDATE 7/13/19: I went ahead and moved some methods out of my sScraper class and into the Candidate class. Now all that the Scraper class does is scrape data rather than scrape data AND build candidate objects. I also refactored a bit and now rather than building all of the Candidate objects and adding their information upon running the app, only the basic Candidate objects with names and URLs are built and put into an array. The extra candidate info is scraped and added to the object instance after the user selects which candidate they’d like to read about. This has greatly decreased the amount of time it takes for the app to load since it only has to scrape data from one page upon running, rather than 24 separate pages.

github >> https://github.com/nbaugh1/candidates-app