# Serializers

## `UserSerializer`

O `UserSerializer` estende o tipo `ModelSerializer` e, por meio da classe `Meta`, indica que está associado ao model `User` e lida com os campos: `id`, `username`, `email` e `groups`.

## `GroupSerializer`

O `GroupSerializer` estende o tipo `ModelSerializer` e, por meio da classe `Meta`, indica que está associado ao model `Group` e lida com os campos: `id` e `name`.

## `PerfilSerializer`

O `PerfilSerializer` estende o tipo `ModelSerializer` e, por meio da classe `Meta`, indica que está associado ao model [`Perfil`](models.md) e lida com os campos: `id`, `cadastrado_em`, `atualizado_em`, `usuario`, `nome`, `sexo`, `cpf`, `telefone`, `endereco`, `estado_uf`, `cidade` e `cep`.
