# Split API

SPLIT API for CAPSTONE Q3 Kenzie Academy Brasil - app by Os Coringas da boa visão, escrita e corrida!

========== USER ==========

## Create USER

`POST /users`

### Request

    {
        "name": name,
        "profession_code": profession code,
        "cpf": cpf number,
        "phone": phone number,
        "email": email@mail.com,
        "profession": profession,
        "password": password,
        "address": {
            "street": street,
            "cep": cep number,
            "number_house": number house,
            "complement": complement
        }
    }

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

## Create USER

`POST /users/login`

### Request

    {
        "email": email@mail.com,
        "password": password
    }

### Response OK

    {
        "access_token": access_token
    }

### Response UNAUTHORIZED

    {
        "error": "Unauthorized"
    }

## Get USERS

`GET /users`

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

`GET /users/<user_id>`

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

========== WORKSPACE ==========

## Create WORKSPACES

`POST /workspaces`

### Request

    {
        "owner_id": number,
        "name": name,
        "local": local,
        "categories": [category 1 , category 2]
    }

### Response CREATED

    {
        "name": name,
        "owner_id": owner_id,
        "workspace_id": workspace_id,
        "local": local,
        "categories": categories
    }

### Response BAD_REQUEST

    KeyError

## Get WORKSPACES

`GET /workspaces`

### Request

no request

### Response OK

    [
        {
            "name": name,
            "owner_id": owner_id,
            "workspace_id": workspace_id,
            "local": local,
            "categories": categories,
            "workers": users
        }
    ]

## Get SPECIFIC WORKSPACE

`GET /workspaces/<workspace_id>`

### Request

Arg: workspace_id

### Response OK

    {
        "name": name,
        "owner_id": owner_id,
        "workspace_id": workspace_id,
        "local": local,
        "categories": categories,
        "workers": users,
        "patients": [
            {
                "info": {
                    "_id": patient_id,
                    "name": name,
                    "gender": gender,
                    "patient_code": patient_code,
                    "profession": profession,
                    "marital_status": marital_status,
                    "responsible_guardian": responsible_guardian,
                    "responsible_contact": responsible_contact,
                    "birth_date": birth_date,
                    "workspace_id": workspace_id,
                    "address": address,
                    "tags": tags,
                    "allergies": allergies,
                },
                "datas": [
                    {
                        "data_id": data_id,
                        "description": description,
                        "date": date,
                        "status": status,
                        "category_id": category_id,
                        "category_name": category,
                        "tags": tags,
                    }
                ],
                "comments": [
                    {
                        "comment_id": comment_id,
                        "comment": comment,
                        "user_name": user.name,
                        "date_time": date_time,
                        "category_name": category,
                    }
                ],
            }
        ],
    }

### Response NOT_FOUND

    {
        "msg": "Workspace not Found"
    }

## Update SPECIFIC WORKSPACE

`PATCH /workspaces/<workspace_id>`

### Request

Arg: workspace_id

### Response OK

    {
        "name": name,
        "owner_id": owner_id,
        "workspace_id": workspace_id,
        "local": local,
        "categories": categories,
        "workers": users
    }

### Response NOT_FOUND

    {
        "msg": "Workspace not Found"
    }

## Delete WORKSPACE

`DELETE /workspaces/<workspace_id>`

### Request

Arg: workspace_id

### Response OK

    {
        "msg": "Workspace name deleted"
    }

### Response NOT_FOUND

    {
        "msg": "Workspace not Found"
    }

## Add USER to WORKSPACE

`POST /workspaces/<workspace_id>`

### Request

Arg: workspace_id

Request:

    {
        "user_id": 6
    }

### Response OK

    {
        "name": name,
        "owner_id": owner_id,
        "workspace_id": workspace_id,
        "local": local,
        "categories": categories,
        "workers": users
    }

### Response NOT_FOUND

    {
        "msg": "Workspace not Found"
    }

## Add USER to WORKSPACE

`GET /workspaces/<workspace_id>/patients`

### Request

Arg: workspace_id

### Response OK

    {
        "workspace_id": workspace_id,
        "name": name,
        "local": local,
        "owner_id": owner_id,
        "patients": patients,
        "categories": categories
    }

### Response NOT_FOUND

    {
        "msg": "Workspace not Found"
    }

========== PATIENT ==========

## Create PATIENT

`POST /patients`

### Request

    {
        "name" : name,
        "gender": gender,
        "cpf" : cpf number,
        "profession" : profession,
        "marital_status" : marital status,
        "responsible_guardian" : responsible guardian,
        "responsible_contact" : responsible contact,
        "birth_date" : birth date,
        "workspace_id" : workspace id,
            "address": {
                "street": street,
                "cep": cep number,
                "number_house": house number,
                "complement": complement,
            },
        "allergies": [allergy 1, allergy 2],
            "tags": [tag 1, tag 2],
            "alerts": [alert 1, alert 2]
    }

### Response CREATED

    {
        "_id": patient_id,
        "name": name,
        "gender": gender,
        "patient_code": patient_code,
        "profession": profession,
        "marital_status": marital_status,
        "responsible_guardian": responsible_guardian,
        "responsible_contact": responsible_contact,
        "birth_date": birth_date,
        "workspace": workspace,
        "address": address,
        "allergies": allergies,
        "tags": tags
    }

### Response BAD_REQUEST

    KeyError

    {
        "error": "Error creating patient"
    }

## Get PATIENTS

`GET /patients`

### Request

no request

### Response OK

    [
        {
            "_id": patient_id,
            "name": name,
            "gender": gender,
            "patient_code": patient_code,
            "profession": profession,
            "marital_status": marital_status,
            "responsible_guardian": responsible_guardian,
            "responsible_contact": responsible_contact,
            "birth_date": birth_date,
            "workspace": workspace,
            "address": address,
            "allergies": allergies,
            "tags": tags
        }
    ]

## Get SPECIFIC PATIENT

`GET /patients/<patient_id>`

### Request

Arg: patient_id

### Response OK

    {
        "_id": patient_id,
        "name": name,
        "gender": gender,
        "patient_code": patient_code,
        "profession": profession,
        "marital_status": marital_status,
        "responsible_guardian": responsible_guardian,
        "responsible_contact": responsible_contact,
        "birth_date": birth_date,
        "workspace": workspace,
        "address": address,
        "allergies": allergies,
        "tags": tags
    }

### Response NOT_FOUND

    {
        "msg": "Patient not Found"
    }

## Update SPECIFIC USER

`PATCH /patients/<patient_id>`

### Request

Arg: patient_id
Request: any patient field.

### Response OK

    {
        "_id": patient_id,
        "name": name,
        "gender": gender,
        "patient_code": patient_code,
        "profession": profession,
        "marital_status": marital_status,
        "responsible_guardian": responsible_guardian,
        "responsible_contact": responsible_contact,
        "birth_date": birth_date,
        "workspace": workspace,
        "address": address,
        "allergies": allergies,
        "tags": tags
    }

### Response NOT_FOUND

    {
        "msg": "UPatient not Found"
    }

### Response BAD_REQUEST

    {
        "error": "Error updating patient"
    }

## Delete USER

`DELETE /patients/<patient_id>`

### Request

Arg: patient_id

### Response NO_CONTENT

### Response NOT_FOUND

    {
        "error": "Patient not Found"
    }

========== DATA ==========

## Create DATA

`POST /datas`

### Request

    {
        "description": data_description,
        "patient_id": patient_id,
        "category_id": category_id,
        "tags": [data_tags],
        "alerts": [alert_data_tags]
    }

### Response CREATED

    {
        "data_id": data_id
        "status": Boolean
        "description": description
        "date": datetime
        "patient_id": patient_id
        "category_id": category_id
    }

### Response BAD_REQUEST

    {
        "error": "Error creating data for patient"
    }

## Get DATAS

`GET /datas`

### Request

no request

### Response OK

    [
        {
            "data_id": data_id,
            "status": status,
            "description": description,
            "date": date,
            "patient": patient,
            "tags": tags
        }
    ]

## Get SPECIFIC DATA

`GET /datas/<data_id>`

### Request

Arg: data_id

### Response OK

    {
        "data_id": data_id,
        "status": status,
        "description": description,
        "date": date,
        "patient": patient,
        "tags": tags
    }

### Response NOT_FOUND

    {
        "msg": "Data not Found"
    }

## Update SPECIFIC DATA

`PATCH /datas/<data_id>`

### Request

Arg: data_id
Request: any data field.

### Response OK

    {
        "data_id": data_id,
        "status": status,
        "description": description,
        "date": date,
        "patient": patient,
        "tags": tags
    }

### Response NOT_FOUND

    {
        "msg": "Data not Found"
    }

### Response BAD_REQUEST

    {
        "error": "Error updating data"
    }

## Delete DATA

`DELETE /datas/<data_id>`

### Request

Arg: data_id

### Response OK

    {
        "msg": "data description deleted"
    }

### Response NOT_FOUND

    {
        "msg": "Data not Found"
    }

========== COMMENTS ==========

## Create COMMENT

`POST /comments`

### Request

    {
        "patient_id": patient id,
        "user_id": user id,
        "category_id": category id,
        "comment": comment
    }

### Response CREATED

    {
        "comment_id": comment id,
        "comment": comment,
        "date_time": date time,
        "user_id": user id,
        "patient_id": patient id,
        "category_id": category id
    }

### Response BAD_REQUEST

    {
        "error": "User not Found"
    }

### Response BAD_REQUEST

    {
        "error": "Category not Found"
    }

### Response BAD_REQUEST

    {
        "error": "Patient not Found"
    }

### Response BAD_REQUEST

    ValidationError

    {
        "msg": """Error creating comment,
            give the give the appropriate keys""",
        "appropriate_keys": {
            "comment": "string",
            "patient_id": "integer",
            "user_id": "integer",
            "category_id": "integer",
            },
    }

## Update SPECIFIC COMMENT

`PATCH /comments/<comment_id>`

### Request

Arg: comment_id
Request:

    {
        "comment": "tESTE"
    }

### Response OK

    {
        "comment_id": comment id,
        "comment": comment,
        "date_time": date time,
        "user_id": user id,
        "patient_id": patient id,
        "category_id": category id
    }

### Response BAD_REQUEST

    ValidationError

    {
        "msg": """Error updating comment,
            give the give the appropriate keys""",
        "appropriate_keys": {"comment": "string"},
    }

## Delete COMMENT

`DELETE /comments/<comment_id>`

### Request

Arg: data_id

### Response OK

    {
        "msg": "Comment deleted"
    }

### Response NOT_FOUND

    {
        "error": "Comment not Found"
    }
