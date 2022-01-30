# MongREST

[![build](https://github.com/meyer1994/mongrest/actions/workflows/build.yml/badge.svg)](https://github.com/meyer1994/mongrest/actions/workflows/build.yml)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

[MongoDB][3], but with HTTP

## Table of Contents

- [About](#about)
- [Install](#install)
- [Usage](#usage)
- [Thanks](#thanks)

## About

A small server that creates an HTTP interface to interact with MongoDB.

### Ednpoints

HTTP:

```
GET    /count/{coll}/?query=dict

GET    /rest/{coll}/?query=dict&skip=int&limit=int
POST   /rest/{coll}/
DELETE /rest/{coll}/?query=dict

GET    /index/{coll}/
POST   /index/{coll}/
DELETE /index/{coll}/{index}

GET    /schema/{coll}/
POST   /schema/{coll}/
DELETE /schema/{coll}/
```

WebSocket:

```
/realtime/?query=dict
```

## Install

```sh
$ pip install -r requirements.txt
```

## Usage

To run a local version of this project, just execute:

```sh
$ docker-compose up  # mongodb cluster
$ uvicorn main:app --reload
```

## Thanks

This project would not have been possible without the code in the following
projects:

- [PostgREST][1]
- [RestHeart][2]

[1]: https://postgrest.org/en/stable/
[2]: https://restheart.org/
[3]: https://www.mongodb.com/
