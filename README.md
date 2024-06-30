# Python project Fußballmannschaften v0.1
 
## Local setup 

**Create python environment**

```
$ python3 -m venv .venv
```

**Activete python environment**

```
$ source .venv/bin/activete
```

**Install dependencies**

```
$ pip install -r requirements.txt
```

**Run dtatbase container**

```
$ docker-compose up -d db
```

**Add migrations to database**

```
$ flask db migrate
```

**Run aplication**

```
$ flask run
```

## Setup with docker

```
$ docker-compose up -d --build
```
