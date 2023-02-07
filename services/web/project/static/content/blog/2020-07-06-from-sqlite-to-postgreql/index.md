---
title: "Changing Your Rails Database to PostgreSQL from Sqlite3"
date: 2020-07-06
published: false
---

Just about everytime I build a new Rails app I forget to use Postgres
as my default database. The simple and straight forward way to start working with Postgres is to use the flag on your initial Rails build command `rails new project-name --database=postgresql`. Without the `--database=postgresql`, Rails will build your new app with Sqlite3 as the default databse.

First thing to do is change your Gemfile. Change the lines
`# Use sqlite3 as the database for Active Record gem 'sqlite3'`

to

`# Use postgres as the database for Active Record gem 'pg'`

Run `$bundle install` after this to install the added gem.

Next `/config/database.yaml` needs to be changed. If you stared out with Sqlite3 the contents should look like this

``

# SQLite. Versions 3.8.0 and up are supported.

# gem install sqlite3

#

# Ensure the SQLite 3 gem is defined in your Gemfile

# gem 'sqlite3'

#

default: &default
adapter: sqlite3
pool: <%= ENV.fetch("RAILS_MAX_THREADS") { 5 } %>
timeout: 5000

development:
<<: \*default
database: db/development.sqlite3

# Warning: The database defined as "test" will be erased and

# re-generated from your development database when you run "rake".

# Do not set this db to the same as development or production.

test:
<<: \*default
database: db/test.sqlite3

production:
<<: \*default
database: db/production.sqlite3
`

This should be changed to
`

# PostgreSQL. Versions 8.2 and up are supported.

#

# Install the pg driver:

# gem install pg

# On OS X with Homebrew:

# gem install pg -- --with-pg-config=/usr/local/bin/pg_config

# On OS X with MacPorts:

# gem install pg -- --with-pg-config=/opt/local/lib/postgresql84/bin/pg_config

# On Windows:

# gem install pg

# Choose the win32 build.

# Install PostgreSQL and put its /bin directory on your path.

#

# Configure Using Gemfile

# gem 'pg'

#

development:
adapter: postgresql
encoding: unicode
database: YOUR_APP_NAME_development
pool: 5
username: NAME
password:
timeout: 5000

# Connect on a TCP socket. Omitted by default since the client uses a

# domain socket that doesn't need configuration. Windows does not have

# domain sockets, so uncomment these lines.

#host: localhost

# The TCP port the server listens on. Defaults to 5432.

# If your server runs on a different port number, change accordingly.

#port: 5432

# Schema search path. The server defaults to \$user,public

#schema_search_path: myapp,sharedapp,public

# Minimum log levels, in increasing order:

# debug5, debug4, debug3, debug2, debug1,

# log, notice, warning, error, fatal, and panic

# Defaults to warning.

#min_messages: notice

# Warning: The database defined as "test" will be erased and

# re-generated from your development database when you run "rake".

# Do not set this db to the same as development or production.

test:
adapter: postgresql
encoding: unicode
database: YOUR_APP_NAME_test
pool: 5
username: NAME
password:
timeout: 5000

`
