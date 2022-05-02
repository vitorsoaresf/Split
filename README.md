# Split API

SPLIT API for Kenzie Academy Brasil - app by Os Coringas da boa visão, escrita e corrida!

## Create USER

`POST /users`

### Request

    {request example}

### Response CREATED

    {
        "_id": user_id,
        "name": name,
        "profession": profession,
        "cpf": cpf,
        "phone": phone,
        "email": email,
        "profession_code": profession_code,
        "address": address
    }

### Response BAD_REQUEST

    {
        "msg": "Error creating user",
        "user": data,
        "address": address
    }

## Get USERS

`Get /users`

### Request

no request

### Response OK

    [
        {
            "_id": user_id,
            "name": name,
            "profession": profession,
            "cpf": cpf,
            "phone": phone,
            "email": email,
            "profession_code": profession_code,
            "address": address
        }
    ]

## Get SPECIFIC USER

`Get /users/<user_id>`

### Request

Arg: user_id

### Response OK

    {
        "_id": user_id,
        "name": name,
        "profession": profession,
        "cpf": cpf,
        "phone": phone,
        "email": email,
        "profession_code": profession_code,
        "address": address,
        "workspaces": [name, workspace_id]
    }

### Response NOT_FOUND

    {
        "msg": "User not Found"
    }

## Update SPECIFIC USER

`PATCH /users/<user_id>`

### Request

Arg: user_id

### Response OK

    {
        "_id": user_id,
        "name": name,
        "profession": profession,
        "cpf": cpf,
        "phone": phone,
        "email": email,
        "profession_code": profession_code,
        "address": address,
        "workspaces": [name, workspace_id]
    }

### Response NOT_FOUND

    {
        "msg": "User not Found"
    }

## Delete USER

`DELETE /users/<user_id>`

### Request

Arg: user_id

### Response OK

    {
        "msg": "User name deleted"
    }

### Response NOT_FOUND

    {
        "msg": "User not Found"
    }
