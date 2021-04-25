
# Driver location Tracker

#Explanation
Currently this project contains two rest endpoints. The first endpoint return all the drivers near to given location and
other endpoint allow us to update drivers locations.
All the data is stored in mongodb.

You can checkout deployed api at 
`https://or-demo.herokuapp.com/`



## API Reference

#### Get all the drivers within 200 meters

```http
  GET /api/v1/drivers/lng/lat
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `lng` | `string` | **Required**. longitute of the pessanger |
|  `lat` | `string` | **Required**. Latitude of the pessanger |

#### Update drivers location

```http
  POST /api/v1/drivers/location
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of the driver |
| `lng` | `string` | **Required**. longitute of the Driver |
|  `lat` | `string` | **Required**. Latitude of the Driver |





  
## API Reference

#### Get all the drivers within 200 meters

```http
  GET /api/v1/drivers/[lng]/[lat]
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `lng` | `string` | **Required**. longitute of the pessanger |
|  `lat` | `string` | **Required**. Latitude of the pessanger |

#### Update drivers location

```http
  POST /api/v1/drivers/location
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of the driver |
| `lng` | `string` | **Required**. longitute of the Driver |
|  `lat` | `string` | **Required**. Latitude of the Driver |

>> make sure post request contains `content-type: application/json` header


# Deployment

## Prerequisite
1. Python3
2. Mongodb

## Installation backend
1. Git clone current project
2. Run `pip install pipenv`
3. run `pipenv install`
4. run `export FLASK_APP=app.py`
5. run `export FLASK_ENV=[development|production|testing]`
6. run `export FLASK_DEBUG=[1|0]`
7. run `export DATABASE_URL=[mongodb connection url]`
8. run `flask run` to start server

## Database
1. Create mongodb database with `or` name
2. Create `drivers` collection
3. Add `2dsphere` index on `loc` field by running `db.createIndex({"loc": "2dsphere"})`



  