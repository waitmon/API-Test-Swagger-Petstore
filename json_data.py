from conftest import *
from pytest_voluptuous import S


class JsonData:
    """Contains payloads for https methods and json schema validation tests."""

    # JSON data for CRUD requests

    update_pet = {
        "id": 2,
        "category": {
            "id": 0,
            "name": "salem"
        },
        "name": 'kitty',
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "update_info"
            }
        ],
        "status": 'on vacation'
    }

    add_new_pet = {
        "id": 5,
        "category": {
            "id": 0,
            "name": "jerry"
        },
        "name": "quokka",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

    new_order = {

        "id": 2,
        "petId": 2,
        "quantity": 12,
        "shipDate": "2023-04-12T11:17:27.357Z",
        "status": "placed",
        "complete": True
    }

    new_order_2 = {

        "id": 3,
        "petId": 3,
        "quantity": 2,
        "shipDate": "2023-04-12T11:17:27.357Z",
        "status": "placed",
        "complete": True
    }


    new_user = {
        "id": 2,
        "username": "Tommy",
        "firstName": "Tommy",
        "lastName": "Vercetti",
        "email": "tommy@user.com",
        "password": "12345",
        "phone": "712345769",
        "userStatus": 0
    }

    new_user_2 = {
        "id": 3,
        "username": "CJ",
        "firstName": "User",
        "lastName": "Johnson",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
    }

    update_user = {
        "id": 3,
        "username": 'CJ',
        "firstName": 'Carl',
        "lastName": "Johnson",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
    }
    new_user_3 = {
        "id": 4,
        "username": 'Paul',
        "firstName": "",
        "lastName": "",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
    }

    users_array = [
        {
            "id": 7,
            "username": "Phil",
            "firstName": "Phil",
            "lastName": "Anselmo",
            "email": "string",
            "password": "string",
            "phone": "string",
            "userStatus": 0
        },
        {
            "id": 8,
            "username": "Masami",
            "firstName": "Masami",
            "lastName": "Akita",
            "email": "string",
            "password": "string",
            "phone": "string",
            "userStatus": 0
        }
    ]

    # JSON response schemas for schemas validation tests

    schema_pet_get_put_post = S(
        {
            "id": int,
            "category": {
                "id": int,
                "name": str
            },
            "name": str,
            "photoUrls": [
                str
            ],
            "tags": [
                {
                    "id": int,
                    "name": str
                }
            ],
            "status": str
        }
    )

    schema_post_upd_dlt = S(
        {
            "code": int,
            "type": str,
            "message": str
        }
    )

    schema_upload_image = S(
        {
            "code": int,
            "type": str,
            "message": str
        }
    )

    schema_new_order = S(
        {
            "id": int,
            "petId": int,
            "quantity": int,
            "shipDate": str,
            "status": str,
            "complete": bool
        }
    )
