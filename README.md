# Nuclear-Tests-API
Training Practice - Creating a RESTFul API backed by MongoDB - Using known nuclear weapons testing operations' data from various countries.

![](https://img.shields.io/badge/Python-3.8-blue.svg)  ![](https://img.shields.io/badge/Flask-1.1.2-9cf.svg) ![](https://img.shields.io/badge/MongoDB-3.2.11-success.svg)

------------------------------------------------------------------------------
**Date**: Fri 22 May 2020 17:17:40 CEST

**Author**: Nicolas Flandrois

**Licence**: MIT License - Copyright (c) 2020 - Nicolas Flandrois

------------------------------------------------------------------------------
## Description:

This project is a training practice to create a **Flask RESTFul API** backed by **MongoDB (NoSQL)**.

In this practice, the Flask API requests information about official/known nuclear weapons tests.
Data are stored in MongoDB. Flask uses Flask-PyMongo (v 2.3.0) module to communicate with the database.

All data are compiled from the wiki page [List of nuclear weapons tests](https://en.wikipedia.org/wiki/List_of_nuclear_weapons_tests#Known_tests), in the known section.
Not all tests bombs are listed, I compiled the 'operations' and testing series, focusing on known testings.

All compiled data are formated in Json file, ready to be imported to your MongoDB.
Feel free to modify those data with your own compilation, or datasets.


You can search data through different **GET** methods. The API will return the query results in json format.

Your can insert/add data through a **POST** method, given the data in json format. The API will return the input data in json format.

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

### Start the API:

In your terminal lauch the command `python3 nucleartestapi.py`.
Open the url link in local, in your web browser `http://127.0.0.1:5000/nucleartest`

### Query the API:

Paste/type the corresponding url in your web browser, to show the results from your query:

- To query all data: `http://127.0.0.1:5000/nucleartest`

- To query a specific nuclear test by name: `http://127.0.0.1:5000/nucleartest/<name>`

    - e.g.: `http://127.0.0.1:5000/nucleartest/Trinity`

- To query all nuclear test by country: `http://127.0.0.1:5000/nucleartest/country/<country>`

    - e.g.:
        - `http://127.0.0.1:5000/nucleartest/country/USA`

        - `http://127.0.0.1:5000/nucleartest/country/USSR`

- To query all nuclear test by year: `http://127.0.0.1:5000/nucleartest/year/<year>`

    - e.g.: `http://127.0.0.1:5000/nucleartest/year/1961`

### Add data through the API:

Send the data in Json format, through a POST method, to `http://127.0.0.1:5000/nucleartest`.
