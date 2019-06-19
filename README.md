# mozio-app-api

# Providers

Supports registering, viewing, and updating providers.

## Register a new Provider

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

_Note:_

- Not Authorization Protected

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

## Get a providers information

**Request**:

`GET` `/providers/:id`

Parameters:

_Note:_

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

## Update provider information

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
