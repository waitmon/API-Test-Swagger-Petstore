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

    schema_upd_dlt_pet = S(
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

