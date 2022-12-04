# xkcd API

This is a simple API for the xkcd comic strip. It is a simple wrapper around the xkcd JSON API.

The API pulls data from the xkcd JSON API and saves it to a local database. The API then serves the data from the local database.
## Build and Run

To build and run the API, you need to have [Docker](https://www.docker.com/) installed.

```

docker-compose up

```

## Management command

To load data to the db run the following command:

```
python manage.py load_data_to_db
```

## Usage
1. Create user account
To create user account make a request to the `/create_user` endpoint with the following JSON body:
```
{
    "username": "username",
    "password": "password"
}
```
2. Get token
The api is secured with a simple API token. The API token is passed in the header to access apis.
To generate an API token, Make a POST request to `http://0.0.0.0:8000/get_token/` with the following body:
```
{
    "username": "admin",
    "password": "admin1234"

}
```

The response will be a JSON object with the API key. The API key will be used to access the API.

### (All API's are secured with the API token)

## API Reference

### Get all comics

```
GET api/comics/
Authorization Token <token>
```

#### Get  item from DB

```http
  GET /api/comics/?title=${title}
```

| Parameter | Type     | Description                  |
| :-------- | :------- |:-----------------------------|
| `Token ` | `string` | **Required**. Your API token |

#### Create item in DB
This will create a new item in the DB. If the item already exists, it will be updated.

```http
  POST /api/comics/
```

| Parameter     | Type     | Description                         |
|:--------------| :------- |:------------------------------------|
| `title`       | `string` | **Required**. Name of item to fetch |
| `img`         | `string` | Image URL                           |
| `description` | `string` | description of the comic            |
| `issue`       | `string` | issue number                        |
| `date`        | `string` | date of issue                       |
| `month`       | `string` | month of issue                      |
| `year`        | `string` | year of issue                       |

#### Update item in DB
This will update the item in the DB with the new values.

```http
  PUT /api/comics/
```

| Parameter     | Type     | Description                         |
|:--------------| :------- |:------------------------------------|
| `title`       | `string` | **Required**. Name of item to fetch |
| `img`         | `string` | Image URL                           |
| `description` | `string` | description of the comic            |
| `issue`       | `string` | issue number                        |
| `date`        | `string` | date of issue                       |
| `month`       | `string` | month of issue                      |
| `year`        | `string` | year of issue                       |

#### Delete item from DB

```http
  DELETE /api/comics/

{ "title": "string" }
```
This will delete the data from the database.

## env variables 
Add a .env file in the root directory with the following variables:
```
DEBUG=1
SECRET_KEY=foo
DJANGO_ALLOWED_HOSTS=0.0.0.0 127.0.0.1 [::1]

DJANGO_SU_NAME=admin
DJANGO_SU_EMAIL=admin@admin.com
DJANGO_SU_PASSWORD=admin1234

POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_DB=comic_store
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

```
## Tests

To run the tests, run the following command:

```
coverage run manage.py test
```
![Screenshot 2022-12-04 at 12 27 18 PM](https://user-images.githubusercontent.com/36413448/205488168-4849fb90-984d-459f-b01c-5fd5316d179a.png)

Coverage report will be generated in the `htmlcov` directory.
