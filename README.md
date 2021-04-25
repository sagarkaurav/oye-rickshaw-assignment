
# Driver location Tracker

#Explanation
Currently this project contains two rest endpoints. The first endpoint return all the drivers near to given location and
other endpoint allow us to update drivers locations.
All the data is stored in mongodb.

You can checkout deployed api at 
`https://or-demo.herokuapp.com/`

Try out `https://or-demo.herokuapp.com/api/v1/drivers/77.054411/28.643839` it will return all the drivers within 200 meter of the given location

If you want to update the location of one the drivers make post request to 
`https://or-demo.herokuapp.com/api/v1/drivers/location` with following json data
```json
{
    "id": "string",
    "lng": "string",
    "lat": "string"
}
```

Please don't forgot to use `content-type: application/json` on headers.
I am sharing all the drivers `id`s so you can try out and change driver locations

Driver IDS
```
6082d33e409f9fdcaaae741e
60840890e136e7e1e8be4fc5
6085730fda7e60533c098a94
```


## Things can we improved 
Currently this demo application does not have complete data validation. If you send some random data it may crash. This can be easily avoided by adding more validations.

## API Reference

#### Get all the drivers within 200 meters

```http
  GET /api/v1/drivers/lng/lat
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `lng` | `string` | **Required**. longitude of the pessanger |
|  `lat` | `string` | **Required**. Latitude of the pessanger |

#### Update drivers location

```http
  POST /api/v1/drivers/location
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of the driver |
| `lng` | `string` | **Required**. longitude of the Driver |
|  `lat` | `string` | **Required**. Latitude of the Driver |





  
## API Reference

#### Get all the drivers within 200 meters

```http
  GET /api/v1/drivers/[lng]/[lat]
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `lng` | `string` | **Required**. longitude of the pessanger |
|  `lat` | `string` | **Required**. Latitude of the pessanger |

#### Update drivers location

```http
  POST /api/v1/drivers/location
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of the driver |
| `lng` | `string` | **Required**. longitude of the Driver |
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
4. `drivers` collections schema 
```json
{
    "name": "string",
    "license": "string"
    "loc": {
        "type": "Point",
        "coordinates": ["longitude", "latitude"]
    }
}
```

The `loc` field is `GeoJson` format you can read about it here `https://docs.mongodb.com/manual/reference/geojson/`


  