# xkcd API

This is a simple API for the xkcd comic strip. It is a simple wrapper around the xkcd JSON API.

The API pulls data from the xkcd JSON API and saves it to a local database. The API then serves the data from the local database.

## API Reference

#### Get  item from DB

```http
  GET /api/comics/?title=${title}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

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
