# Oz Bootstrap #

Oz provides a means of creating the scaffolding for an application via
`oz init`. However, this default scaffolding is very unopinionated and only
provides a basic structure.

Oz bootstrap is a very opinionated scaffolding for oz-based applications. It
provides you with:

* A basic package structure
* Scripts for working in a virtualenv-based setup
* HTML5-based templates
* Coffeescript
* SASS
* Bootstrap
* jquery
* modernizr

## Initial Setup ##

First install SASS and coffeescript. Then:

    git clone https://github.com/dailymuse/oz-bootstrap.git
    cd oz-bootstrap
    virtualenv --no-site-packages .
    ./scripts/update-dependencies

## Running The Server ##

Just run `./scripts/server`

## Adding Dependencies ##

Update your `requirements.txt`, then run `./scripts/update-dependencies`

## Running Other Oz Actions ##

Oz bootstrap provides a convenience function for running oz actions within
virtualenv + a custom environmental profile. To run an oz action, use
`./scripts/using-profile`. The first argument is the environmental profile to
use (specified in the `env` directory.) Environmental profiles specify
environment variables that can be used in `config.py`.

e.g. to run the server without the server script:
`./scripts/using-profile dev server`. This will run the server using the dev
environmental profile, which enables debug mode and sets the port to 8000.

## Directory Structure ##

    - /assets - Assets that are compiled to statically downloadable content
        - /coffeescript - Your application's coffeescript code, which
          will be compiled into static/js.
        - /sass - Your application's SASS code, which will be compiled
          into /static/css.
    - /bootstrap - The application's python code
        - /handlers - Your application's request handlers.
        - /tests - Your application's unit tests.
        - /middleware.py - Your application's middleware.
        - /models.py - Your application's models.
        - /options.py - Your application's custom options.
        - /routes.py - Your application's routes to request handlers.
    - /scripts - Bash utility scripts
        - /server - Runs the server and performs live SASS/coffeescript
          compilation
        - /update-dependencies - Updates your application dependencies
        - /using-profile - Runs an oz action within virtualenv + a custom
          environmental profile.
    - /static
        - /css - Contains your compiled SASS content.
        - /js - Contains your compiled coffeescript.
        - /lib - Contains third-party libraries.
        - /favicon.ico - Your application's favicon.
        - robots.txt - Your application's robots.txt.
    - /templates - Your application's templates.
        - /404.html - 404 error page.
        - /500.html - 500 error page.
        - /index.html - The homepage.
    - /config.py - The oz config
    - /README.md - This file :D
    - requirements.txt - The python dependencies


