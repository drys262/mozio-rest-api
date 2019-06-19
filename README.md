# mozio-app-api

## Deployment

1. Hosted in AWS Elastic Beanstalk
2. Using RDS Aurora Postgres 9.6.9 as the Database
3. Using ElasticCache for Memcached.
4. Creating a Hosted Zone in Route 53 (app.mozioapp.tk)
5. Getting Domain from freenom.com (free domain for testing) then copy the nameserver of the Route 53 Hosted Zone to freenom nameserver configuration.
6. Creating an SSL Certificate for the domain (api.mozioapp.tk) using the AWS Certificate Manager.

## Providers

Supports registering, viewing, updating, deleting providers.

### Register a new Provider

**Request**:

`POST` `/providers`

Parameters:

| Name         | Type   | Required | Description                            |
| ------------ | ------ | -------- | -------------------------------------- |
| name         | string | Yes      | The name for the new provider.         |
| phone_number | string | Yes      | The phone number for the new provider. |
| language     | string | Yes      | The language of the provider.          |
| currency     | string | Yes      | The currency of the provider.          |
| email        | string | Yes      | The current email of the provider.     |

**Response**:

```json
Content-Type application/json
201 Created
{
    "id": "3ae7fe6e-de0e-4708-9714-97774da706f9",
    "name": "John Doe",
    "phone_number": "123455678",
    "language": "English",
    "currency": "$",
    "email": "johndoehere@gmail.com"
}
```

### Get a providers information

**Request**:

`GET` `/providers`
`GET` `/providers/:id`

Sample `GET` request http://api.mozioapp.tk/api/v1/providers

Sample `GET` request http://api.mozioapp.tk/api/v1/providers/f0c9e028-c4cb-41c0-b194-65616e823c77

**Response**:

```json
Content-Type application/json
200 OK

{
    "id": "3ae7fe6e-de0e-4708-9714-97774da706f9",
    "name": "John Doe",
    "phone_number": "123455678",
    "language": "English",
    "currency": "$",
    "email": "johndoehere@gmail.com"
}
```

### Update provider information

**Request**:

`PUT` `/users/:id`

Parameters:

| Name         | Type   | Required | Description                                |
| ------------ | ------ | -------- | ------------------------------------------ |
| name         | string | Yes      | The updated name for the provider.         |
| phone_number | string | Yes      | The updated phone number for the provider. |
| language     | string | Yes      | The updated language of the provider.      |
| currency     | string | Yes      | The updated currency of the provider.      |
| email        | string | Yes      | The updated current email of the provider. |

**Response**:

```json
Content-Type application/json
200 OK

{
    "id": "3ae7fe6e-de0e-4708-9714-97774da706f9",
    "name": "JD Blake",
    "phone_number": "34534534",
    "language": "English",
    "currency": "$",
    "email": "jd@gmail.com"
}
```

### Delete a provider

**Request**:

`DELETE` `/provider/:id`

**Response**:

```json
Content-Type application/json
200 OK
Check the status code
```

## Service Area

Supports registering, viewing, updating, deleting service areas/polygons.

### Register/Update a new Service Area

**Request**:

`POST` `/service-area`
`PUT` `/service-area/:id`

Parameters:

| Name     | Type   | Required | Description                      |
| -------- | ------ | -------- | -------------------------------- |
| provider | string | Yes      | The provider foreign key.        |
| name     | string | Yes      | The name of the service area.    |
| price    | string | Yes      | The price of the service area.   |
| geojson  | json   | Yes      | The geojson of the service area. |

**Note**:

The geojson property must have the this format to properly work. (Array of feautures then Array of coordinates)

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [-27.421875, 63.35212928507874],
            [-11.513671874999998, 63.35212928507874],
            [-11.513671874999998, 67.03316279015063],
            [-27.421875, 67.03316279015063],
            [-27.421875, 63.35212928507874]
          ]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [-6.8994140625, 60.50052541051131],
            [-13.53515625, 51.645294049305406],
            [0.8349609375, 49.83798245308484],
            [4.130859375, 52.3755991766591],
            [-6.8994140625, 60.50052541051131]
          ]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [-6.96533203125, 63.25341156651705],
            [-10.08544921875, 61.58549218152362],
            [-5.42724609375, 61.05828537037916],
            [-4.28466796875, 62.1655019058381],
            [-6.96533203125, 63.25341156651705]
          ]
        ]
      }
    }
  ]
}
```

**Response**:

```json
Content-Type application/json
201 Created
{
	"name": "LONDON Service Area",
	"price": 17.0,
	"provider": "6216768a-c259-43b1-b624-28b05179ba15",
	"geojson": {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [-27.421875, 63.35212928507874],
                            [-11.513671874999998, 63.35212928507874],
                            [-11.513671874999998, 67.03316279015063],
                            [-27.421875, 67.03316279015063],
                            [-27.421875, 63.35212928507874]
                        ]
                    ]
                }
            },
            {
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [-6.8994140625, 60.50052541051131],
                            [-13.53515625, 51.645294049305406],
                            [0.8349609375, 49.83798245308484],
                            [4.130859375, 52.3755991766591],
                            [-6.8994140625, 60.50052541051131]
                        ]
                    ]
                }
            },
            {
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [-6.96533203125, 63.25341156651705],
                            [-10.08544921875, 61.58549218152362],
                            [-5.42724609375, 61.05828537037916],
                            [-4.28466796875, 62.1655019058381],
                            [-6.96533203125, 63.25341156651705]
                        ]
                    ]
                }
            }
        ]
    }
}
```

### Get a service area information

**Request**:

`GET` `/service-area`
`GET` `/service-area/:id`

Sample `GET` request http://api.mozioapp.tk/api/v1/service-area

Sample `GET` request http://api.mozioapp.tk/api/v1/service-area/7e3e9cf2-d4a7-4736-96b8-19c4dabe0d52

**Response**:

```json
Content-Type application/json
200 OK

{
    "count": 60,
    "next": "http://api.mozioapp.tk/api/v1/service-area?page=2",
    "previous": null,
    "result": ["list of service area with geojson polygons"]
}
```

### Delete a service area

**Request**:

`DELETE` `/service-area/:id`

**Response**:

```json
Content-Type application/json
200 OK
Check the status code
```

### Get Service Area based on Latitude and Longitude

**Request**:

`GET` `/get-service-areas?lat=<:lat>&lng=<:lng>`

Parameters:

| Name | Type  | Required | Description                          |
| ---- | ----- | -------- | ------------------------------------ |
| lat  | float | Yes      | One of the latitude of the polygon.  |
| lng  | float | Yes      | One of the longitude of the polygon. |

Sample `GET` request http://api.mozioapp.tk/api/v1/get-service-areas?lat=120.95947265624999&lng=25.77021384896025

**Response**:

```json
Content-Type application/json
200 OK
[
    {
        "Name": "Taiwan Service Area",
        "Price": 500,
        "Provider name": "John Doe",
        "geojson": {"geojson information here"}
    },
    {
        "Name": "Philippines Service Area",
        "Price": 100,
        "Provider name": "John Doe",
        "geojson": {"geojson information here"}
    },
    {
        "Name": "Japan Service Area",
        "Price": 500,
        "Provider name": "John Doe",
        "geojson": {"geojson information here"}
    },
    {
        ...
    }
]
```
