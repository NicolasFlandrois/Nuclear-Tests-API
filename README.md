# Nuclear-Tests-API
Training Practice - Creating a RESTFul API backed by a MongoDB - Using known data of nuclear weapons tests

![](https://img.shields.io/badge/Python-3.8-blue.svg)  ![](https://img.shields.io/badge/Flask-1.1.2-9cf.svg) ![](https://img.shields.io/badge/MongoDB-3.2.11-success.svg)

------------------------------------------------------------------------------
**Date**: Fri 22 May 2020 17:17:40 CEST

**Author**: Nicolas Flandrois

**Licence**: MIT License - Copyright (c) 2020 - Nicolas Flandrois

------------------------------------------------------------------------------
## Description:

This project is a training practice to create a RESTFul API backed by a MongoDB (NoSQL).

In this practice, the Flask API requests information about official/known nuclear weapons tests.
Data are stored in MongoDB. Flask uses Flask-PyMongo (v 2.3.0) module to communicate with the database.

All data are compiled from the wiki page [List of nuclear weapons tests](https://en.wikipedia.org/wiki/List_of_nuclear_weapons_tests#Known_tests), in the known section.
Not all test bomb are listed, I compiled the operation and testing series, focusing on known testings.
All compiled data are formated in Json file, ready to be imported to your MongoDB.


You can search data through different GET methods.

Your can insert/add data through a POST method, given the data in json format.

------------------------------------------------------------------------------
## Install:

1. To install this RESTful API in Flask and MongoDB, first install:

- Python 3.7 or higher (with `pip3`)

- MongoDB 3.2.11 or higher

2. To install python modules:

`pip3 install -r requirements.txt`

3. To create the database and import all data

- Lauch MongoDB

- `use mongo_rest`

- `db.createCollection("nucleartest")`

- `db.nucleartest.insert(` *Copy-Paste data from json file here* `)`


------------------------------------------------------------------------------
## Use the API:

In your terminal lauch the command `python3 nucleartestapi.py`.
