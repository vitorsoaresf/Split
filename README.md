\*\*\*\*# json-server-base

Esse é o repositório com a base de JSON-Server + JSON-Server-Auth já configurada, feita para ser usada no desenvolvimento de um sistema que integra tatuadores a usuários. E que usuários podem solicitar a reserva de sessões de tatuagens disponibilizadas pelos tatuadores.

## Endpoints

Assim como a documentação do JSON-Server-Auth traz (https://www.npmjs.com/package/json-server-auth), existem 3 endpoints que podem ser utilizados para cadastro e 2 endpoints que podem ser usados para login.
<br><br>

## Link da API

- https://server-capstone-book-ink.herokuapp.com

> <br><br>

# Users

<br>

### <strong> \* CADASTRO \*</strong>

- POST /register <br/>
- POST /signup <br/>
- POST /users

<pre>
Formato da Requisição - 

{<br>
    "name": "Fulano",<br>
    "email": "fulano@mail.com",<br>
    "password": "123456",<br>
    "img": "url",<br>
    "bio": "lorem ipsum",<br>
    "isTattooist": false,<br>
}

Formato da Resposta - 

{<br>
    "accessToken": "token",<br>
    "user": {<br>
        "name": "Fulano",<br>
        "email": "fulano@mail.com",<br>
        "password": "123456",<br>
        "img": "url",<br>
        "bio": "lorem ipsum",<br>
        "isTattooist": false,<br>
        "id": 1
    }
}
</pre>

Qualquer um desses 3 endpoints irá cadastrar o usuário na lista de "Users", sendo que os campos obrigatórios são os de email e password.
Você pode ficar a vontade para adicionar qualquer outra propriedade no corpo do cadastro dos usuários.<br><br><br>

### <strong> \* LOGIN \*</strong>

- POST /login <br/>
- POST /signin

<pre>
Formato da Requisição - 

{<br>
    "email": "fulano@mail.com",<br>
    "password": "123456",<br>
}

Formato da Resposta - 

{<br>
    "accessToken": "token",<br>
    "user": {<br>
        "name": "Fulano",<br>
        "email": "fulano@mail.com",<br>
        "img": "url",<br>
        "bio": "lorem ipsum",<br>
        "isTattooist": false,<br>
        "id": 1
    }
}
</pre>

Qualquer um desses 2 endpoints pode ser usado para realizar login com um dos usuários cadastrados na lista de "Users"<br><br><br>

### <strong> \* LEITURA DE USUÁRIOS\*</strong><br><br>

- GET/users

Esse endpoint pode ser usado para realizar leitura dos usuários cadastrados na lista de "Users". Esses dados serão trazidos com os comentários que o usuário fez no perfil do tatuadores cadastrados e a sessões de reserva que estão pendentes, quando for tatuador, e quando foi respondida, quando for cliente<br><br>

- GET/users/:id

Esse endpoint pode ser usado para realizar leitura de um usuário em específico e trará todas as informações que o endpoint acima traz.

> <br><br>

# Tatooists<br>

- GET /tatooists <br/>

Esse endpoint listará somente os tatuadores cadastrados na plataforma junto com os comentários relacionados a ele e as sessões que estão pendentes e que precisam ser respondidas.<br><br>

> <br><br>

# Comments<br>

- POST /comments <br/>

<pre>
Formato da Requisição - 

{
    "comment": "Esse tatuador é de muita qualidade",
    "rate": 5,
    "name": "Fulano",
    "userId": 1,
    "id": 1
}

Formato da Resposta - 

{
    "comment": "Esse tatuador é de muita qualidade",
    "rate": 5,
    "name": "Fulano",
    "userId": 1,
    "id": 1
}
</pre>

Esse endpoint pode ser usado para realizar o registro de um novo cometário com um dos usuários cadastrados na lista de "Users" em um dos perfis dos tatuadores cadastrados na plataforma,como também, precisa que o token de acesso esteja em igualdade com o userId passado no corpo do objeto JSON, ou seja, é necessário estar logado na plataforma<br><br>

- GET /comments <br/>

Esse endpoint retornará todos os comentários feitos por todos os usuários.

> <br><br>

# Sessions<br>

- GET /sessions <br/>

Esse endpoint listará todas as sessões de tatuagem incluindo as partes interessadas.
<br><br>

- POST /sessions <br/>

<pre>
Formato da Requisição - 

{
    "allEvents": {
        "title": "Big Meeting",
        "allDay": true,
        "start": "Thu, 10 Feb 2022 09:49:26 GMT",
        "end": "Thu, 10 Feb 2022 15:49:26 GMT"
    },
    "accepted": false,
    "pending": true,
    "client": "fulano@gmail.com",
    "clientId": 12,
    "userId": 1,
    "messageRequest": "lorem",
    "messageResponse": "",
}

Formato da Resposta - 

{
    "allEvents": {
        "title": "Big Meeting",
        "allDay": true,
        "start": "Thu, 10 Feb 2022 09:49:26 GMT",
        "end": "Thu, 10 Feb 2022 15:49:26 GMT"
    },
    "accepted": false,
    "pending": true,
    "client": "fulano@gmail.com",
    "clientId": 12,
    "userId": 1,
    "messageRequest": "lorem",
    "messageResponse": "",
    "id": 1
}
</pre>

Esse endpoint permite o cadastro de novas sessões com as partes envolvidas<br><br>

- PATCH /sessions/:id <br/>

Esse endpoint atualizará os dados de alguma sessão já cadastrada<br><br>

- DELETE /sessions/:id <br/>

Esse endpoint permite remover uma sessão já cadastrada<br><br>

- GET /allsessions/:id <br/>

Esse endpoint listará todas as sessões de tatuagem incluindo as partes interessadas, de um tatuador em específico<br><br>

> <br><br>

# Portifolio<br>

- GET /portilofio/:id <br/>

Esse endpoint listará todas as imagens de tatuagem relacionadas com o id informado, sendo ele o dono od recurso<br><br>
