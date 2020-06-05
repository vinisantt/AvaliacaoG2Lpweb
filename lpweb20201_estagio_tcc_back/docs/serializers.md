# Serializers <!-- omit in toc -->

- [`UserSerializer`](#userserializer)
- [`GroupSerializer`](#groupserializer)
- [`PermissionSerializer`](#permissionserializer)
- [`UsuarioDetalhadoSerializer`](#usuariodetalhadoserializer)
- [`PerfilSerializer`](#perfilserializer)
- [`CursoSerializer`](#cursoserializer)
- [`AlunoSerializer`](#alunoserializer)
- [`MatriculaSerializer`](#matriculaserializer)
- [`FuncionarioSerializer`](#funcionarioserializer)
- [`ProfessorSerializer`](#professorserializer)
- [`OrientacaoSerializer`](#orientacaoserializer)
- [`PropostaDeEstagioSerializer`](#propostadeestagioserializer)
- [`PropostaDeTCCSerializer`](#propostadetccserializer)
- [`AvaliacaoDePropostaSerializer`](#avaliacaodepropostaserializer)
- [`ColaboradorExternoSerializer`](#colaboradorexternoserializer)

Os serializers estendem a classe `ModelSerializer` e especificam a estrutura de dados utilizada na entrada e saída de dados da API.

## `UserSerializer`

O `UserSerializer` está associado ao model `User` e possui os campos: `id`, `username`, `email` e `groups`.

## `GroupSerializer`

O `GroupSerializer` está associado ao model `Group` e possui os campos: `id` e `name`.

## `PermissionSerializer`

O `PermissionSerializer` está asosciado ao model `Permission` e possui os campos: `id`, `nome`, `content_type` e `codename`.

## `UsuarioDetalhadoSerializer`

O `UsuarioDetalhadoSerializer` está associado ao model `User` e possui os campos: `email`, `groups`, `id`, `is_superuser`, `last_login`, `date_joined`, `user_permissions`, `username`.

O campo `groups` é um objeto com os campos `id`, `name`, e `permissions`, este último uma lista de objetos serializados por `PermissionSerializer`, representando as permissões do grupo.

O campo `permissions` é uma lista de objetos serializos por `PermissionSerializer`, representando as permissões do usuário.

## `PerfilSerializer`

O `PerfilSerializer` está associado ao model `Perfil` e possui os campos: `id`, `cadastrado_em`, `atualizado_em`, `usuario`, `nome`, `sexo`, `cpf`, `telefone`, `endereco`, `estado_uf`, `cidade` e `cep`.

## `CursoSerializer`

O `CursoSerializer` está associado ao model `Curso` e possui os campos: `id`, `cadastrado_em`, `atualizado_em`, `nome`, `slug`, `professores`.

O campo `professores` é uma lista de objetos serializados por `ProfessorSerializer`, que possui os campos: `id`, `funcionario`, `funcao`. Sendo que o campo `funcionario` é serializado pelo `FuncionarioSerializer`, que possui os campos: `id`, `nome`, `cgu`.

## `AlunoSerializer`

O `AlunoSerializer` está associado ao model `Aluno` e possui os campos: `id`, `cadastrado_em`, `atualizado_em`, `nome`, `cgu`.

## `MatriculaSerializer`

O `MatriculaSerializer` está associado ao model `Matricula` e possui os campos: `id`, `cadastrado_em`, `atualizado_em`, `curso`, `aluno`, `curso_id`, `aluno_id`, `ano`, `semestre`.

O campo `curso` é serializado pelo `CursoSerializer`, com os campos: `id`, `nome`, `slug`.

O campo `aluno` é serializado pelo `AlunoSerializer`, com os campos: `id`, `nome`, `cgu`.

## `FuncionarioSerializer`

O `FuncionarioSerializer` está associado ao model `Funcionario` e possui os campos: `id`, `cadastrado_em`, `atualizado_em`, `nome`, `cgu`, `cursos`.

O campo `cursos` uma lista de objetos serializados pelo `ProfessorSerializer`, com os campos: `id`, `curso`, `funcao`. O campo `curso` é serializado pelo `CursoSerializer`, que possui os campos: `id`, `nome`, `slug`.

## `ProfessorSerializer`

O `ProfessorSerializer` está associado ao model `Professor` e possui os campos: `id`, `cadastrado_em`, `atualizado_em`, `curso_id`, `funcionario_id`, `curso`, `funcionario`, `funcao`.

O campo `curso` é serializado pelo `CursoSerializer`, com os campos: `id`, `nome`, `slug`.

O campo `funcionario` é serializado pelo `FuncionarioSerializer`, com os campos: `id`, `nome`, `cgu`.

## `OrientacaoSerializer`

O `OrientacaoSerializer` está associado ao model `Orientacao` e possui os campos: `id`, `cadastrado_em`, `atualizado_em`, `curso`, `curso_id`, `aluno`, `aluno_id`, `professor`, `professor_id`, `tipo`, `ano`, `semestre`.

O campo `professor` é serializado pelo `ProfessorSerializer`, com os campos: `id`, `funcionario`, `funcao`. O campo `funcionario` é serializado pelo `FuncionarioSerializer`, com os campos: `id`, `nome`, `cgu`.

O campo `curso` é serializado pelo `CursoSerializer`, com os campos: `id`, `nome`, `slug`.

O campo `aluno` é serializado pelo `AlunoSerializer`, com os campos: `id`, `nome`, `cgu`.

## `PropostaDeEstagioSerializer`

O `PropostaDeEstagioSerializer` está associado ao model `PropostaDeEstagio` e possui os campos: `id`, `cadastrado_em`, `atualizado_em`, `orientacao`, `orientacao_id`, `titulo`, `conceitos`, `resultados_esperados`, `aprovada`, `aprovada_em`, `aprovada_por`, `aprovada_por_id`, `membros_da_banca`, `avaliacoes`.

O campo `aprovada_por` é serializado pelo `UserSerializer`, com os campos: `id`, `username`.

O campo `avaliacoes` é uma lista de objetos serializados pelo `AvaliacaoDePropostaSerializer`, com os campos: `id`, `cadastrado_em`, `atualizado_em`, `usuario`, `comentario`, `aprovada`, `publicada`. O campo `usuario` é serializado pelo `UserSerializer`, com os campos: `id`, `username`.

O campo `membros_da_banca` é uma lista de objetos serializados pelo `MembroDaBancaSerializer`, com os campos: `id`, `cadastrado_em`, `atualizado_em`, `membro_interno`, `membro_interno_id`, `membro_externo`, `membro_externo_id`. O campo `membro_interno` é serializado pelo `FuncionarioSerializer`, com os campos: `id`, `nome`, `cgu`. O campo `membro_externo` é serializado pelo `ColaboradorExternoSerializer`, com os campos: `id`, `nome`, `cpf`, `email`, `instituicao`.

O capmo `orientacao` é serializado pelo [`OrientacaoSerializer`](#orientacaoserializer).

## `PropostaDeTCCSerializer`

O `PropostaDeTCCSerializer` tem a mesma estrutura do [`PropostaDeEstagioSerializer`](#propostadeestagioserializer), com a diferença de que está associado ao model `PropostaDeTCC` e acrescenta os campos: `objetivo`, `tecnologias`, `metodologia`.

## `AvaliacaoDePropostaSerializer`

O `AvaliacaoDePropostaSerializer` está associado ao model `AvaliacaoDeProposta` e possui os campos: `id`, `cadastrado_em`, `atualizado_em`, `usuario`, `usuario_id`, `comentario`, `aprovada`, `publicada`, `proposta`, `avaliador`.

O campo `avaliador` retorna as informações do avaliador da proposta:

- se for **membro interno**, retorna os campos: `usuario_id`, `usuario_username`, `nome`, `tipo`, `cgu` (o campo `tipo` contém o valor `"interno"`)
- se for membro externo, retorna os campos: `usuario_id`, `usuario_username`, `nome`, `tipo`, `email`, `instituicao` (o campo `tipo` contém o valor `"externo"`)

## `ColaboradorExternoSerializer`

O `ColaboradorExternoSerializer` está associado ao model `ColaboradorExterno` e possui os campos: `id`, `nome`, `cpf`, `email` e `instituicao`.
