# search-artist-challenge
[![Build Status](https://travis-ci.org/otaviosoares/search-artist-challenge.svg?branch=master)](https://travis-ci.org/otaviosoares/search-artist-challenge)
> Searches for artists in a JSON and sorts by the middle ages

## Choose of framework

From all the frameworks I've worked with (Django, flask, tornado), Pyramid was not one of them. The reason I've chosen it is that it's written in the job description that you use Pylons Project. The goal here, although I haven't used any advanced stuff, was to prove my best quality: I can learn fast. :)

## Prerequisites

- [Git](https://git-scm.com/)
- [Python 2.7](https://www.python.org/)
- [VirtualEnv](https://github.com/pypa/virtualenv)

## Setup

```bash
#Clone this repo

#Go to directory created by clone:
cd search-artist-challenge/

#Create virtualenv:
virtualenv env

#Activate virtualenv:
. env/bin/activate

#Install requirements:
pip install -r requirements

#Go to project directory:
cd src/search_artists

#Install pyramid's dependencies:
python setup.py develop
```

## Serving
```bash
pserve development.ini
```

Open [http://localhost:6543/](http://localhost:6543/) in browser


## Running tests
```bash
nosetests --verbose

#With coverage
nosetests --with-coverage --cover-package=search_artists
```
