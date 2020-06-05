# Endpoints da API  <!-- omit in toc -->

- [Autenticação](#autenticação)
  - [`POST /api/token-auth/`](#post-apitoken-auth)
- [User](#user)
  - [`GET /api/users/`](#get-apiusers)
  - [`GET /api/users/:id/`](#get-apiusersid)
  - [`POST /api/users/`](#post-apiusers)
  - [`PUT /api/users/:id/`](#put-apiusersid)
  - [`PATCH /api/users/:id`](#patch-apiusersid)
- [Group](#group)
- [Perfil logado](#perfil-logado)
- [Usuário logado](#usuário-logado)
- [Perfis](#perfis)
  - [`GET /api/perfis/`](#get-apiperfis)
- [Cursos](#cursos)
- [Alunos](#alunos)
- [Matrículas](#matrículas)
- [Funcionários](#funcionários)
- [Professores](#professores)
- [Orientações](#orientações)
  - [`POST /api/orientacoes/`](#post-apiorientacoes)
- [Propostas de Estágio](#propostas-de-estágio)
  - [`POST /api/propostas-de-estagio/`](#post-apipropostas-de-estagio)
- [Propostas de TCC](#propostas-de-tcc)
  - [`POST /api/propostas-de-tcc/`](#post-apipropostas-de-tcc)
- [Avaliações de propostas](#avaliações-de-propostas)
- [Colaboradores externos](#colaboradores-externos)

Este documento descreve os endpoints da API, agrupados por elementos principais da API.

## Autenticação

Os endpoints permitem autenticar e atualizar o token.

- `POST /api/token-auth/`
- `POST /api/token-refresh/`

### `POST /api/token-auth/`

Realiza a autenticação do usuário conforme as credenciais, que são informadas no corpo da requisição representando um objeto com os atributos:

| atributo   | tipo   | detalhes           |
| :--------- | :----- | :----------------- |
| `username` | string | o nome do usuário  |
| `password` | string | a senha do usuário |

**Exemplo:**

```json
{
    "username": "admin",
    "password": "admin123"
}
```

O retorno é um objeto que contém o atributo `token` (string), o qual representa o token gerado no padrão JWT que contém informações do usuário da requisição e permite autorizar requisições subsequentes.

Códigos de retorno:

- **200**: ok
- **403**: credenciais incorretas

## User

**Base da URL: `/api/users/`.**

Utiliza a view `UserViewSet` e o serializer `UserSerializer`.

Só pode ser acessada por uma requisição autenticada (com informações do usuário da requisição).

Os endpoints permitem consultar, cadastrar, excluir e editar informações de usuários do sistema:

- `GET /api/users/`
- `GET /api/users/:id/`
- `POST /api/users/`
- `PUT /api/users/:id/`
- `PATCH /api/users/:id/`
- `DELETE /api/users/:id/`

O objeto que representa as informações de usuário contém os atributos:

| atributo   |  tipo   | detalhes                                                                     |
| :--------- | :-----: | :--------------------------------------------------------------------------- |
| `id`       | integer | identificador do usuário                                                     |
| `username` | string  | obrigatório; 150 caracteres ou menos; letras, números e @/./+/-/_ apenas     |
| `email`    | string  | precisa ser um endereço de e-mmail válido; 254 caracteres ou menos           |
| `groups`   |  array  | os grupos do usuário, na forma de um array com os identificadores dos grupos |

**Exemplo:**

```json
{
    "id": 1,
    "username": "admin",
    "email": "admin@gmail.com",
    "groups": [
        1
    ]
}
```

### `GET /api/users/`

Retorna os usuários cadastrados. A estrutura do retorno segue a definição-padrão de resultados paginados do djangorestframework: um objeto com os atributos:

| atributo   | tipo    | descrição                                                        |
| :--------- | :------ | :--------------------------------------------------------------- |
| `count`    | integer | indica a quantidade de usuários cadastrados                      |
| `next`     | string  | indica a URL para requisição da próxima página dos resultados    |
| `previous` | string  | indica a URL para a requisição da página anterior dos resultados |
| `results`  | array   | um array contendo os dados dos usuários                          |

O parâmetro de URL `ordering` permite ordenar a lista de usuários conforme os valores:

- `id` e `-id`: ordena de forma crescente e decrescente pelo valor do campo `id`
- `username` e `-username`: ordena de forma crescente e decrescente pelo valor do campo `username`
- `email` e `-email`: ordena de forma crescente e decrescente pelo valor do campo `email`

Este padrão de ordenar de forma crescente considerando o nome do campo da ordenação e de forma decrescente considerando "-" seguido do nome do campo é definido no djangorest

O parâmetro de URL `search` permite pesquisar a lista de usuários conforme o campo `search_fields` da view `UserViewSet`.

**Exemplo:**

```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
    ]
}
```

Códigos de retorno:

- **200**: ok

### `GET /api/users/:id/`

Retorna os dados de um usuário específico, com base no parâmetro de rota `id`, que representa o identificador do usuário.

**Exemplo:**

```json
{
    "id": 1,
    "username": "admin",
    "email": "admin@gmail.com",
    "groups": [
        1
    ]
}
```

Códigos de retorno:

- **200**: ok
- **404**: usuário não encontrado

### `POST /api/users/`

Cadastra um usuário. Os dados da requisição devem representar um objeto com os atributos:

| atributo   | requerido |
| :--------- | :-------: |
| `username` |    sim    |
| `email`    |    sim    |
| `groups`   |    não    |

**Exemplo:**

```json
{
    "username": "admin",
    "email": "admin@gmail.com",
    "groups": []
}
```

Códigos de retorno:

- **201**: usuário cadastrado
- **400**: erro na requisição; geralmente ocorre quando um dado não está de acordo com o esperado, como quando a requisição envia um nome de usuário (username) que já está cadastrado. Neste caso, o conteúdo do retorno contém um objeto que descreve o erro encontrado e contém um atributo conforme o nome do campo onde ocorreu erro e seu valor é um array de string com mensagem descritiva do erro
- **500**: erro na requisição correspondendo a um erro de execução no servidor; o retorno é um objeto com o atributo `detail`, que descreve o erro

### `PUT /api/users/:id/`

Atualiza os dados de um usuário específico, com base no parâmetro de rota `id`, que representa o identificador do usuário. Os dados da requisição devem representar um objeto com os atributos:

| atributo   | requerido | somente leitura |
| :--------- | :-------: | :-------------: |
| `id`       |    não    |       sim       |
| `username` |    sim    |       não       |
| `email`    |    não    |       não       |
| `groups`   |    não    |       não       |

Códigos de retorno:

- **200**: usuário atualizado
- **400**: erro na requisição; geralmente ocorre quando um dado não está de acordo com o esperado, como quando a requisição envia um nome de usuário (username) que já está cadastrado. Neste caso, o conteúdo do retorno contém um objeto que descreve o erro encontrado e contém um atributo conforme o nome do campo onde ocorreu erro e seu valor é um array de string com mensagem descritiva do erro
- **500**: erro na requisição correspondendo a um erro de execução no servidor; o retorno é um objeto com o atributo `detail`, que descreve o erro

### `PATCH /api/users/:id`

Atualiza os dados de um usuário específico, com base no parâmetro de rota `id`, que representa o identificador do usuário. Opera de forma semelhante ao endpoint `PUT /api/users/:id`, com a diferença de que os dados da requisição não precisam conter todos os atributos para serem atualizados. Geralmente é utilizado para atualizar apenas uma parte do objeto.

## Group

**Base da URL: `/api/groups/`.**

Utiliza a view `GroupViewSet` e o serializer `GroupSerializer`.

Só pode ser acessada por uma requisição autenticada (com informações do usuário da requisição).

Os endpoints permitem consultar, cadastrar, excluir e editar informações de grupos de usuários do sistema:

- `GET /api/groups/`
- `GET /api/groups/:id/`
- `POST /api/groups/`
- `PUT /api/groups/:id/`
- `PATCH /api/groups/:id/`
- `DELETE /api/groups/:id/`

O objeto que representa as informações de usuário contém os atributos:

| atributo |  tipo   | detalhes                             |
| :------- | :-----: | :----------------------------------- |
| `id`     | integer | identificador do grupo               |
| `name`   | string  | obrigatório; 150 caracteres ou menos |

**Exemplo:**

```json
{
    "id": 1,
    "name": "Administradores"
}
```

## Perfil logado

**Base da URL: `/api/perfil-logado/`.**

Utiliza a view `PerfilLogadoViewSet` e o serializer `PerfilSerializer`.

Só pode ser acessada por uma requisição autenticada (com informações do usuário da requisição).

O endpoint permite consultar informações do perfil do usuário da requisição.

O objeto que representa as informações do perfil contém os atributos:

| atributo        |   tipo   | detalhes                                               |
| :-------------- | :------: | :----------------------------------------------------- |
| `id`            | integer  | identificador do perfil                                |
| `cadatrado_em`  | datetime | data de criação do registro                            |
| `atualizado_em` | datetime | data de atualização do registro                        |
| `usuario`       | integer  | obrigatório; identificador do usuário que tem o perfil |
| `nome`          |  string  | obrigatório; 128 caracteres ou menos                   |
| `sexo`          |  string  | um caractere: 'F' ou 'M'                               |
| `cpf`           |  string  | 14 carateres ou menos; não pode repetir                |
| `telefone`      |  string  | 15 caracteres ou menos                                 |
| `endereco`      |  string  | 512 caracteres ou menos                                |
| `estado_uf`     |  string  | 2 caracteres                                           |
| `cidade`        |  string  | 64 caracteres ou menos                                 |
| `cep`           |  string  | 10 caracteres ou menos                                 |

**Exemplo:**

```json
{
    "id": 1,
    "cadastrado_em": "2020-05-14T15:47:14.792525-03:00",
    "atualizado_em": "2020-05-14T16:09:20.083284-03:00",
    "usuario": 2,
    "nome": "José S. da Silva",
    "sexo": "M",
    "cpf": "032.964.254-54",
    "telefone": "(63) 98432-0123",
    "endereco": "Quadra 204 Sul, Alameda 2",
    "estado_uf": "TO",
    "cidade": "Palmas",
    "cep": "77.000-00"
}
```

Códigos de retorno:

- **200**: ok
- **404**: usuário não possui perfil

## Usuário logado

**Base da URL: `/api/usuario-logado/`.**

Utiliza a view `UsuarioLogadoDetailsViewSet` e o serializer `UsuarioDetalhadoSerializer`. Só pode ser acessada por uma requisição autenticada. O endpoint disponível é `GET /api/usuario-logado/', que retorna as informações detalhadas do usuário logado, contendo:

- informações do usuário
- permissões específicas do usuário
- grupos do usuário e, para cada grupo, suas permissões

## Perfis

**Base da URL: `/api/perfis/`.**

Utiliza a view `PerfilViewSet` e o serializer `PerfilSerializer`.

Só pode ser acessada por uma requisição autenticada (com informações do usuário da requisição).

Os endpoints permitem consultar, cadastrar, editar e excluir informações de perfis de usuários:

- `GET /api/perfis/`
- `GET /api/perfis/:id/`
- `POST /api/perfis/`
- `PUT /api/perfis/:id/`
- `PATCH /api/perfis/:id/`
- `DELETE /api/perfis/:id/`

### `GET /api/perfis/`

Este endpoint retorna a lista de perfis e está configurado para permitir os recursos:

- ordenação: o parâmetro de URL `ordering` é utilizado para determinar a ordenação da lista
- busca: o parâmetro de URL `search` é utilizado para realizar uma busca na lista de perfis, considerando valores dos campos: `usuario.username`, `usuario.email`, `nome`, `cpf`, `telefone`, `endereco`, `estado_uf`, `cidade`, `cep`
- filtragem: parâmetros de URL correspondentes aos campos: `usuario`, `estado_uf` e `cidade` podem ser usados para filtrar a lista de perfis.

Em relação à filtragem, é particularmente interessante observar as possibilidades:

- parâmetro de URL `usuario` tem o valor do identificador do usuário para o qual se deseja encontrar um perfil. Como um usuário só tem um perfil, é esperado que o array `results` tenha zero ou um elemento. Exemplo: `/api/perfis?usuario=1` retorna o perfil do usuário com identificador 1
- parâmetro de URL `estado_uf` tem o valor da UF para a qual se deseja encontrar perfis, ou seja, para o exemplo `/api/perfis?estado_uf=TO` serão encontrados todos os perfis de usuários do Tocantins (TO)
- parâmetro de URL `cidade` tem o valor da cidade para a qual se deseja encontrar perfis, ou seja, para o exemplo `/api/perfis?cidade=Palmas` serão encontrados todos os perfis de usuários de Palmas
- os parâmetros podem ser compostos para filtragens como `/api/perfis?estado_UF=TO&cidade=Palmas`, que retorna todos os perfis de usuários da cidade de Palmas do Tocantins (TO)

Exemplo:

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "cadastrado_em": "2020-05-14T15:47:14.792525-03:00",
            "atualizado_em": "2020-05-14T16:09:20.083284-03:00",
            "usuario": 2,
            "nome": "José S. da Silva",
            "sexo": "M",
            "cpf": "032.964.254-54",
            "telefone": "(63) 98432-0123",
            "endereco": "Quadra 204 Sul, Alameda 2",
            "estado_uf": "TO",
            "cidade": "Palmas",
            "cep": "77.000-00"
        }
    ]
}
```

## Cursos

**Base da URL: `/api/cursos/`.**

Utiliza a view `CursoViewSet` e o serializer `CursoSerializer`.

Os endpoints permitem consultar, cadastrar, editar e excluir informações de cursos:

- `GET /api/cursos/`
- `GET /api/cursos/:id/`
- `POST /api/cursos/`
- `PUT /api/cursos/:id/`
- `PATCH /api/cursos/:id/`
- `DELETE /api/cursos/:id/`

Exemplo para `GET /api/cursos/`:

```json
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "cadastrado_em": "2020-05-21T11:51:39.334608-03:00",
            "atualizado_em": "2020-05-21T11:51:39.334608-03:00",
            "nome": "Ciência da Computação",
            "slug": "ciencia-da-computacao",
            "professores": [
                {
                    "id": 1,
                    "funcionario": {
                        "id": 1,
                        "nome": "PAULA FONSECA OLIVEIRA",
                        "cgu": 100430001
                    },
                    "funcao": "coordenador"
                },
                {
                    "id": 2,
                    "funcionario": {
                        "id": 2,
                        "nome": "JORGE SANTOS",
                        "cgu": 100430002
                    },
                    "funcao": "coordenador-estagio-tcc"
                }
            ]
        },
        {
            "id": 3,
            "cadastrado_em": "2020-05-21T11:58:11.581098-03:00",
            "atualizado_em": "2020-05-21T11:58:11.581098-03:00",
            "nome": "Sistemas de Informação",
            "slug": "sistemas-de-informacao",
            "professores": []
        }
    ]
}
```

## Alunos

**Base da URL: `/api/alunos/`.**

Utiliza a view `AlunoViewSet` e o serializer `AlunoSerializer`.

Os endpoints permitem consultar, cadastrar, editar e excluir informações de alunos:

- `GET /api/alunos/`
- `GET /api/alunos/:id/`
- `POST /api/alunos/`
- `PUT /api/alunos/:id/`
- `PATCH /api/alunos/:id/`
- `DELETE /api/alunos/:id/`

Exemplo para `GET /api/alunos/`:

```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "cadastrado_em": "2020-05-21T12:01:19.113582-03:00",
            "atualizado_em": "2020-05-21T13:28:32.637574-03:00",
            "nome": "JOSE DA SILVA",
            "cgu": 100000001
        },
        {
            "id": 2,
            "cadastrado_em": "2020-05-21T12:47:10.058885-03:00",
            "atualizado_em": "2020-05-21T12:47:10.058885-03:00",
            "nome": "MARIA NOGUEIRA",
            "cgu": 100000002
        }
    ]
}
```

## Matrículas

**Base da URL: `/api/matriculas/`.**

Utiliza a view `MatriculaViewSet` e o serializer `MatriculaSerializer`.

Os endpoints permitem consultar, cadastrar, editar e excluir informações de matrículas de alunos nos cursos:

- `GET /api/matriculas/`
- `GET /api/matriculas/:id/`
- `POST /api/matriculas/`
- `PUT /api/matriculas/:id/`
- `PATCH /api/matriculas/:id/`
- `DELETE /api/matriculas/:id/`

Em relação à filtragem, é possível filtrar a lista de matrículas por curso, aluno, ano e semestre. É interessante observar as possibilidades:

- parâmetro de URL `curso` tem o valor do identificador do curso para o qual se deseja encontrar as matrículas. Exemplo: `/api/matriculas/?curso=1` retorna as matrículas de alunos do curso de identificador 1
- parâmetro de URL `aluno` retorna a lista de matrículas do aluno cujo identificador é informado. Exemplo: `/api/matriculas/?aluno=1` retorna a lista das matrículas do aluno de identificador 1
- parâmetro de URL `ano` retorna a lista de matrículas de alunos do ano informado. Exemplo: `/api/matriculas/?ano=2020` retorna as matrículas de alunos do ano 2000
- parâmetro de URL `semestre` retorna a lista de matrículas de alunos do semestre informado. Exemplo: `/api/matriculas/?semestre=2` retorna a lista de matrículas de alunos do semestre 2
- os parâmetros podem ser compostos para filtragens como `/api/matriculas/?curso=1&ano=2020`, que retorna todos a lista das matrículas de alunos do curso de identificador 1 no ano 2020

Exemplo para `GET /api/matriculas/`:

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "cadastrado_em": "2020-05-21T12:11:21.673661-03:00",
            "atualizado_em": "2020-05-21T12:11:21.673661-03:00",
            "curso": {
                "id": 1,
                "nome": "Ciência da Computação",
                "slug": "ciencia-da-computacao"
            },
            "aluno": {
                "id": 1,
                "nome": "JOSE DA SILVA",
                "cgu": 100000001
            },
            "ano": 2020,
            "semestre": 1
        }
    ]
}
```

## Funcionários

**Base da URL: `/api/funcionarios/`.**

Utiliza a view `FuncionarioViewSet` e o serializer `FuncionarioSerializer`.

Os endpoints permitem consultar, cadastrar, editar e excluir informações de funcionários:

- `GET /api/funcionarios/`
- `GET /api/funcionarios/:id/`
- `POST /api/funcionarios/`
- `PUT /api/funcionarios/:id/`
- `PATCH /api/funcionarios/:id/`
- `DELETE /api/funcionarios/:id/`

Exemplo para `GET /api/funcionarios/`:

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 2,
            "cadastrado_em": "2020-05-21T16:42:03.474052-03:00",
            "atualizado_em": "2020-05-21T16:42:03.474052-03:00",
            "nome": "JORGE SANTOS",
            "cgu": 100430002,
            "cursos": [
                {
                    "id": 2,
                    "curso": {
                        "id": 1,
                        "nome": "Ciência da Computação",
                        "slug": "ciencia-da-computacao"
                    },
                    "funcao": "coordenador-estagio-tcc"
                }
            ]
        }
    ]
}
```

## Professores

**Base da URL: `/api/professores/`.**

Utiliza a view `ProfessorViewSet` e o serializer `ProfessorSerializer`.

Os endpoints permitem consultar, cadastrar, editar e excluir informações de professores de cursos:

- `GET /api/professores/`
- `GET /api/professores/:id/`
- `POST /api/professores/`
- `PUT /api/professores/:id/`
- `PATCH /api/professores/:id/`
- `DELETE /api/professores/:id/`

Em relação à filtragem, é possível filtrar a lista de professores por curso e funcionário. É interessante observar as possibilidades:

- parâmetro de URL `curso`. Exemplo: `/api/professores/?curso=1` retorna os professores do curso de identificador 1
- parâmetro de URL `funcionario`. Exemplo: `/api/professores/?funcionario=1` retorna a lista das cursos em que o funcionário de identificador 1 atua como professor

Exemplo para `GET /api/professores/`:

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 2,
            "cadastrado_em": "2020-05-21T16:43:34.260857-03:00",
            "atualizado_em": "2020-05-21T16:43:34.260857-03:00",
            "curso": {
                "id": 1,
                "nome": "Ciência da Computação",
                "slug": "ciencia-da-computacao"
            },
            "funcionario": {
                "id": 2,
                "nome": "JORGE SANTOS",
                "cgu": 100430002
            },
            "funcao": "coordenador-estagio-tcc"
        }
    ]
}
```

## Orientações

**Base da URL: `/api/orientacoes/`.**

Utiliza a view `OrientacaoViewSet` e o serializer `OrientacaoSerializer`.

Os endpoints permitem consultar, cadastrar, editar e excluir informações de orientações:

- `GET /api/orientacoes/`
- `GET /api/orientacoes/:id/`
- `POST /api/orientacoes/`
- `PUT /api/orientacoes/:id/`
- `PATCH /api/orientacoes/:id/`
- `DELETE /api/orientacoes/:id/`

Em relação à filtragem, é possível filtrar a lista de orientações por curso, aluno e professor. É interessante observar as possibilidades:

- parâmetro de URL `curso`. Exemplo: `/api/orientacoes/?curso=1` retorna orientações do curso de identificador 1
- parâmetor de URL `aluno`. Exemplo: `/api/orientacoes/?aluno=1` retorna orientações do aluno de identificador 1 (o aluno é o orientando)
- parâmetro de URL `professor`. Exemplo: `/api/orientacoes/?professor=1` retorna a lista das orientações em que o professor de identificador 1 é orientador

Exemplo para `GET /api/orientacoes/`:

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "cadastrado_em": "2020-05-21T17:56:41.347157-03:00",
            "atualizado_em": "2020-05-21T17:56:41.347157-03:00",
            "curso": {
                "id": 1,
                "nome": "Ciência da Computação",
                "slug": "ciencia-da-computacao"
            },
            "aluno": {
                "id": 1,
                "nome": "JOSE DA SILVA",
                "cgu": 100000001
            },
            "professor": {
                "id": 1,
                "funcionario": {
                    "id": 1,
                    "nome": "PAULA FONSECA OLIVEIRA",
                    "cgu": 100430001
                },
                "funcao": "coordenador"
            },
            "tipo": "estagio",
            "ano": 2020,
            "semestre": 1
        }
    ]
}
```

### `POST /api/orientacoes/`

O cadastro da orientação envolve o envio dos dados:

- `curso_id`: o identificador do curso
- `aluno_id`: o identificador do aluno (orientando)
- `professor_id`: o identificador do professor (orientador)
- `tipo`: o tipo da orientação (estágio ou tcc)
- `ano`
- `semestre`

## Propostas de Estágio

**Base da URL: `/api/propostas-de-estagio/`.**

Utiliza a view `PropostaDeEstagioViewSet` e o serializer `PropostaDeEstagioSerializer`.

Os endpoints permitem consultar, cadastrar, editar e excluir informações de propostas de Estágio:

- `GET /api/propostas-de-estagio/`
- `GET /api/propostas-de-estagio/:id/`
- `POST /api/propostas-de-estagio/`
- `PUT /api/propostas-de-estagio/:id/`
- `PATCH /api/propostas-de-estagio/:id/`
- `DELETE /api/propostas-de-estagio/:id/`

Exemplo para `GET /api/propostas-de-estagio/`:

```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "cadastrado_em": "2020-05-21T20:48:36.276167-03:00",
            "atualizado_em": "2020-06-04T04:33:00.419072-03:00",
            "orientacao": {
                "id": 1,
                "cadastrado_em": "2020-05-21T17:56:41.347157-03:00",
                "atualizado_em": "2020-05-21T17:56:41.347157-03:00",
                "curso": {
                    "id": 1,
                    "nome": "Ciência da Computação",
                    "slug": "ciencia-da-computacao"
                },
                "aluno": {
                    "id": 1,
                    "nome": "JOSE DA SILVA",
                    "cgu": 100000001
                },
                "professor": {
                    "id": 1,
                    "funcionario": {
                        "id": 1,
                        "nome": "PAULA FONSECA OLIVEIRA",
                        "cgu": 100430001
                    },
                    "funcao": "coordenador"
                },
                "tipo": "estagio",
                "ano": 2020,
                "semestre": 1
            },
            "titulo": "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
            "conceitos": "Cras fringilla odio eget malesuada sodales.\r\nVestibulum tempus risus at tortor feugiat congue.\r\nPraesent ullamcorper lorem in neque molestie malesuada.",
            "resultados_esperados": "Vestibulum faucibus eros finibus, consectetur lectus eu, tempus leo.\r\nIn molestie diam a nulla pulvinar, ut sodales magna eleifend.\r\nMaecenas ac sapien maximus, imperdiet sapien et, mollis arcu.\r\nVestibulum ut ipsum interdum, ullamcorper metus quis, finibus ante.\r\nCras tempor sem eu sem feugiat ullamcorper.",
            "aprovada": true,
            "aprovada_em": "2020-06-04T04:33:00.418077-03:00",
            "aprovada_por": {
                "id": 4,
                "username": "jorge"
            },
            "membros_da_banca": [
                {
                    "id": 11,
                    "cadastrado_em": "2020-06-04T04:33:00.419072-03:00",
                    "atualizado_em": "2020-06-04T04:33:00.419072-03:00",
                    "membro_interno": {
                        "id": 3,
                        "nome": "MARINHO SANTANA",
                        "cgu": 100430003
                    },
                    "membro_externo": null
                }
            ],
            "avaliacoes": []
        }
    ]
}
```

### `POST /api/propostas-de-estagio/`

O cadastro de propostas de Estágio envolve o envio dos dados:

- `orientacao_id`: o identificador da orientação associada à proposta
- `titulo`
- `conceitos`
- `resultados_esperados`
- `aprovada`: se `true` indica que a proposta está aprovada; se `false`, que não está aprovada; opcional
- `aprovada_por_id`: o identificador do usuário que está aprovando a proposta; opcional
- `membros_da_banca`: um array de objetos que podem ter um dos atributos `membro_interno_id` (contendo o identificador do funcionário membro da banca -- membro interno) ou `membro_externo_id` (contendo o identificador do colaborador externo -- membro externo)

## Propostas de TCC

**Base da URL: `/api/propostas-de-tcc/`.**

Utiliza a view `PropostaDeTCCViewSet` e o serializer `PropostaDeTCCSerializer`.

Os endpoints permitem consultar, cadastrar, editar e excluir informações de propostas de TCC:

- `GET /api/propostas-de-tcc/`
- `GET /api/propostas-de-tcc/:id/`
- `POST /api/propostas-de-tcc/`
- `PUT /api/propostas-de-tcc/:id/`
- `PATCH /api/propostas-de-tcc/:id/`
- `DELETE /api/propostas-de-tcc/:id/`

Exemplo para `GET /api/propostas-de-tcc/`:

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 2,
            "cadastrado_em": "2020-05-28T18:22:32.383652-03:00",
            "atualizado_em": "2020-05-28T18:22:32.384654-03:00",
            "orientacao": {
                "id": 2,
                "cadastrado_em": "2020-05-21T18:55:15.653201-03:00",
                "atualizado_em": "2020-05-21T18:55:15.653201-03:00",
                "curso": {
                    "id": 2,
                    "nome": "Engenharia de Software",
                    "slug": "engenharia-de-software"
                },
                "aluno": {
                    "id": 2,
                    "nome": "MARIA NOGUEIRA",
                    "cgu": 100000002
                },
                "professor": {
                    "id": 3,
                    "funcionario": {
                        "id": 1,
                        "nome": "PAULA FONSECA OLIVEIRA",
                        "cgu": 100430001
                    },
                    "funcao": "professor"
                },
                "tipo": "tcc",
                "ano": 2020,
                "semestre": 1
            },
            "titulo": "TCC da Maria Nogueira",
            "conceitos": "* Engenharia de Software\r\n* Teste de Software",
            "resultados_esperados": "* Relatório de teste de software",
            "aprovada": null,
            "aprovada_em": null,
            "aprovada_por": null,
            "objetivo": "* Definir plano de teste\r\n* Criar relatório da execução do plano de teste",
            "tecnologias": "* NodeJs",
            "metodologia": "* Estudar o software e avaliar suas funcionalidades\r\n* Definir plano de teste\r\n* Executar plano de teste\r\n* Avaliar resultado da execução do plano de teste\r\n* Criar relatório da execução do plano de teste",
            "membros_da_banca": [
                {
                    "id": 2,
                    "cadastrado_em": "2020-05-28T18:23:06.225006-03:00",
                    "atualizado_em": "2020-05-28T18:23:06.225006-03:00",
                    "membro_interno": {
                        "id": 2,
                        "nome": "JORGE SANTOS",
                        "cgu": 100430002
                    },
                    "membro_externo": null
                },
                {
                    "id": 3,
                    "cadastrado_em": "2020-05-28T18:23:16.214671-03:00",
                    "atualizado_em": "2020-06-04T04:16:20.376960-03:00",
                    "membro_interno": null,
                    "membro_externo": {
                        "id": 1,
                        "nome": "MARCIA REGINA",
                        "cpf": null,
                        "email": null,
                        "instituicao": "UNIVERSIDADE FEDERAL"
                    }
                }
            ]
        }
    ]
}
```

### `POST /api/propostas-de-tcc/`

O cadastro de propostas de TCC envolve o envio dos dados:

- `orientacao_id`: o identificador da orientação associada à proposta
- `titulo`
- `objetivos`
- `conceitos`
- `tecnologias`
- `resultados_esperados`
- `metodologia`
- `aprovada`: se `true` indica que a proposta está aprovada; se `false`, que não está aprovada; opcional
- `aprovada_por_id`: o identificador do usuário que está aprovando a proposta; opcional
- `membros_da_banca`: um array de objetos que podem ter um dos atributos `membro_interno_id` (contendo o identificador do funcionário membro da banca -- membro interno) ou `membro_externo_id` (contendo o identificador do colaborador externo -- membro externo)

## Avaliações de propostas

**Base da URL: `/api/avaliacoes-de-propostas/`.**

Utiliza a view `AvaliacaoDePropostaViewSet` e o serializer `AvaliacaoDePropostaSerializer`.

Os endpoints permitem consultar, cadastrar, editar e excluir informações de avaliações de propostas de Estágio e TCC:

- `GET /api/avaliacoes-de-propostas/`
- `GET /api/avaliacoes-de-propostas/:id/`
- `POST /api/avaliacoes-de-propostas/`
- `PUT /api/avaliacoes-de-propostas/:id/`
- `PATCH /api/avaliacoes-de-propostas/:id/`
- `DELETE /api/avaliacoes-de-propostas/:id/`

Em relação à filtragem, é possível filtrar a lista de avaliações de propostas por pproposta, usuário e aprovada. É interessante observar as possibilidades:

- parâmetro de URL `proposta`: permite retornar as avaliações de uma proposta com o identificador informado
- parâmetor de URL `aluno`: permite retornar as avaliações de propostas do aluno (o aluno é orientando)
- parâmetro de URL `aprovada`: permite retornar as avaliações de propostas aprovadas (com valor `true`) e não aprovadas (com valor `false`)

Exemplo para `GET /api/avaliacoes-de-propostas/`:

```json
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "cadastrado_em": "2020-05-28T18:24:33.373831-03:00",
            "atualizado_em": "2020-05-28T18:24:33.373831-03:00",
            "usuario": 4,
            "comentario": "A proposta está bem redigida.",
            "aprovada": true,
            "publicada": true,
            "proposta": 2,
            "avaliador": {
                "usuario_id": 4,
                "usuario_username": "jorge",
                "nome": "JORGE SANTOS",
                "tipo": "interno",
                "cgu": 100430002
            }
        },
        {
            "id": 2,
            "cadastrado_em": "2020-05-28T18:24:45.600281-03:00",
            "atualizado_em": "2020-06-04T04:16:35.171445-03:00",
            "usuario": 7,
            "comentario": "Gostei. Está ok.",
            "aprovada": true,
            "publicada": true,
            "proposta": 2,
            "avaliador": {
                "usuario_id": 7,
                "usuario_username": "marciaregina",
                "nome": "MARCIA REGINA",
                "tipo": "externo",
                "email": null,
                "instituicao": "UNIVERSIDADE FEDERAL"
            }
        },
        {
            "id": 3,
            "cadastrado_em": "2020-05-28T18:24:57.420339-03:00",
            "atualizado_em": "2020-05-28T18:24:57.420339-03:00",
            "usuario": 3,
            "comentario": "Muito bem. Está ok.",
            "aprovada": true,
            "publicada": true,
            "proposta": 2,
            "avaliador": {
                "usuario_id": 3,
                "usuario_username": "paula"
            }
        }
    ]
}
```

## Colaboradores externos

**Base da URL: `/api/colaboradores-externos/`.**

Utiliza a view `ColaboradorExternoViewSet` e o serializer `ColaboradorExternoSerializer`.

Os endpoints permitem consultar, cadastrar, editar e excluir informações colaboradores externos:

- `GET /api/colaboradores-externos/`
- `GET /api/colaboradores-externos/:id/`
- `POST /api/colaboradores-externos/`
- `PUT /api/colaboradores-externos/:id/`
- `PATCH /api/colaboradores-externos/:id/`
- `DELETE /api/colaboradores-externos/:id/`

Exemplo para `GET /api/colaboradores-externos/`:

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "nome": "MARCIA REGINA",
            "cpf": null,
            "email": null,
            "instituicao": "UNIVERSIDADE FEDERAL"
        }
    ]
}
```
