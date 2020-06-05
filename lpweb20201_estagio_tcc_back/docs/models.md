# Models <!-- omit in toc -->

- [Perfil](#perfil)
- [Curso](#curso)
- [Aluno](#aluno)
- [AlunoUsuario](#alunousuario)
- [Matricula](#matricula)
- [Funcionario](#funcionario)
- [FuncionarioUsuario](#funcionariousuario)
- [Professor](#professor)
- [ColaboradorExterno](#colaboradorexterno)
- [ColaboradorExternoUsuario](#colaboradorexternousuario)
- [Orientacao](#orientacao)
- [Proposta](#proposta)
- [PropostaDeEstagio](#propostadeestagio)
- [PropostaDeTCC](#propostadetcc)
- [MembroDeBancaDeProposta](#membrodebancadeproposta)
- [AvaliacaoDeProposta](#avaliacaodeproposta)

O backend utiliza os models `User`, `Group` e `Permission`, disponíveis no pacote `django.contrib.auth.models`. Outros models são descritos a seguir.

## Perfil

| nome            |      tipo       | descrição                                                                                                                       |
| :-------------- | :-------------: | :------------------------------------------------------------------------------------------------------------------------------ |
| `cadastrado_em` | `DateTimeField` | a data e a hora em que o perfil foi criado                                                                                      |
| `atualizado_em` | `DateTimeField` | a data e a hora em que o perfil foi editado                                                                                     |
| `usuario`       | `OneToOneField` | relacionamento um-para-um com o model `User`; indica que o perfil pertence a um usuário; relacionamento com exclusão em cascata |
| `nome`          |   `CharField`   | máximo de 128 caracteres; representa o nome do usuário; indexado no banco de dados                                              |
| `sexo`          |   `CharField`   | máximo de 1 caractere; pode ter os valores 'F' ou 'M'; pode ser nulo                                                            |
| `cpf`           |   `CharField`   | máximo de 14 caracteres; indexado no banco de dados como valor único; pode ser nulo                                             |
| `telefone`      |   `CharField`   | máximo de 15 caracteres; pode ser nulo caracteres                                                                               |
| `endereco`      |   `TextField`   | máximo de 512 caracteres; pode ser nulo caracteres                                                                              |
| `cep`           |   `CharField`   | máximo de 10 caracteres; pode ser nulo caracteres                                                                               |
| `estado_uf`     |   `CharField`   | máximo de 2 caracteres; pode ser nulo caracteres                                                                                |
| `cidade`        |   `CharField`   | máximo de 64 caracteres; pode ser nulo                                                                                          |

## Curso

| nome            |      tipo       | descrição                                  |
| :-------------- | :-------------: | :----------------------------------------- |
| `cadastrado_em` | `DateTimeField` | a data e a hora em que o curso foi criado  |
| `atualizado_em` | `DateTimeField` | a data e a hora em que o curso foi editado |
| `nome`          |   `CharField`   | máximo de 256 caracteres                   |
| `slug`          |   `SlugField`   | máximo de 256 caracteres                   |

O campo `slug` é criado e atualizado a partir do `nome` sempre quando um registro do model é salvo.

## Aluno

| nome            |      tipo       | descrição                                  |
| :-------------- | :-------------: | :----------------------------------------- |
| `cadastrado_em` | `DateTimeField` | a data e a hora em que o aluno foi criado  |
| `atualizado_em` | `DateTimeField` | a data e a hora em que o aluno foi editado |
| `nome`          |   `CharField`   | máximo de 256 caracteres                   |
| `cgu`           | `IntegerField`  | o CGU do aluno; um número inteiro          |

## AlunoUsuario

O model `AlunoUsuario` representa a informação de que um aluno possui um usuário para acessar o sistema.

| nome      |      tipo       | descrição                                     |
| :-------- | :-------------: | :-------------------------------------------- |
| `aluno`   | `OneToOneField` | relacionamento um-para-um com o model `Aluno` |
| `usuario` | `OneToOneField` | relacionamento um-para-um com o model `User`  |

## Matricula

O model `Matricula` representa a informação de que um aluno está matriculado em um curso no ano e semestre indicados. A matrícula ocorre uma vez a cada ano e semestre.

| nome            |            tipo             | descrição                                         |
| :-------------- | :-------------------------: | :------------------------------------------------ |
| `cadastrado_em` |       `DateTimeField`       | a data e a hora em que o registro foi criado      |
| `atualizado_em` |       `DateTimeField`       | a data e a hora em que o registro foi editado     |
| `aluno`         |        `ForeignKey`         | relacionamento muitos-para-um com o model `Aluno` |
| `curso`         |        `ForeignKey`         | relacionamento muitos-para-um com o model `Curso` |
| `ano`           |   `PositiveIntegerField`    | o ano da matrícula                                |
| `semestre`      | `PositiveSmallIntegerField` | o semestre da matrícula                           |

## Funcionario

| nome            |      tipo       | descrição                                     |
| :-------------- | :-------------: | :-------------------------------------------- |
| `cadastrado_em` | `DateTimeField` | a data e a hora em que o registro foi criado  |
| `atualizado_em` | `DateTimeField` | a data e a hora em que o registro foi editado |
| `nome`          |   `CharField`   | máximo de 128 caracteres                      |
| `cgu`           | `IntegerField`  | o CGU do funcionário                          |

## FuncionarioUsuario

O model `FuncionarioUsuario` representa a informação de que um funcionário possui um usuário para acessar o sistema.

| nome          |      tipo       | descrição                                           |
| :------------ | :-------------: | :-------------------------------------------------- |
| `funcionario` | `OneToOneField` | relacionamento um-para-um com o model `Funcionario` |
| `usuario`     | `OneToOneField` | relacionamento um-para-um com o model `User`        |

## Professor

O model `Professor` representa a informação de que um usuário atua em um curso exercendo (ou realizando) uma função, dentre as seguintes:

- coordenador de curso
- coordenador de Estágio e TCC
- professor

Neste modelo, é necessário entender que as duas primeiras funções também representam que o funcionário é um professor no curso, assim não é necessário cadastrar o registro duas vezes para o mesmo funcionário para indicar funções diferentes.

Um funcionário pode ser professor em zero ou mais cursos.

| nome            |      tipo       | descrição                                               |
| :-------------- | :-------------: | :------------------------------------------------------ |
| `cadastrado_em` | `DateTimeField` | a data e a hora em que o registro foi criado            |
| `atualizado_em` | `DateTimeField` | a data e a hora em que o registro foi editado           |
| `curso`         |  `ForeignKey`   | relacionamento muitos-para-um com o model `Curso`       |
| `funcionario`   |  `ForeignKey`   | relacionamento muitos-para-um com o model `Funcionario` |
| `funcao`        |   `CharField`   | máximo de 64 caracteres                                 |

## ColaboradorExterno

O model `ColaboradorExterno` representa a informação de uma pessoa que atua como membro de uma banca de Estágio ou TCC, mas não é funcionário, ou seja, é um colaborador externo à instituição.

| nome          |     tipo     | descrição                          |
| :------------ | :----------: | :--------------------------------- |
| `nome`        | `CharField`  | máximo de 128 caracteres           |
| `cpf`         | `CharField`  | máximo de 14 caracteres; opcional  |
| `email`       | `EmailField` | opcional                           |
| `instituicao` | `CharField`  | máximo de 512 caracteres; opcional |

## ColaboradorExternoUsuario

O model `ColaboradorExternoUsuario` representa a informação de que um colaborador externo possui um usuário para acessar o sistema.

| nome                  |      tipo       | descrição                                                  |
| :-------------------- | :-------------: | :--------------------------------------------------------- |
| `colaborador_externo` | `OneToOneField` | relacionamento um-para-um com o model `ColaboradorExterno` |
| `usuario`             | `OneToOneField` | relacionamento um-para-um com o model `User`               |

## Orientacao

O model `Orientacao` epresenta informações de uma orientação. Uma orientação representa um processo acadêmico
no qual um aluno (orientando) realiza uma monografia sob a condução do professor (orientador). O tipo da orientação pode ser: de Estágio ou de TCC.

| nome            |            tipo             | descrição                                             |
| :-------------- | :-------------------------: | :---------------------------------------------------- |
| `cadastrado_em` |       `DateTimeField`       | a data e a hora em que o registro foi criado          |
| `atualizado_em` |       `DateTimeField`       | a data e a hora em que o registro foi editado         |
| `curso`         |        `ForeignKey`         | relacionamento muitos-para-um com o model `Curso`     |
| `aluno`         |        `ForeignKey`         | relacionamento muitos-para-um com o model `Aluno`     |
| `professor`     |        `ForeignKey`         | relacionamento muitos-para-um com o model `Professor` |
| `tipo`          |         `CharField`         | máximo de 8 caracteres                                |
| `ano`           |   `PositiveIntegerField`    | o ano da orientação                                   |
| `semestre`      | `PositiveSmallIntegerField` | o semestre da orientação                              |

## Proposta

O model `Proposta` representa as informações de uma proposta. Uma proposta (de Estágio ou de TCC, com
models específicos para cada situação) representa uma intenção de um aluno em realizar uma monografia. Desta forma, a proposta faz parte da orientação e contém elementos de projeto da monografia que são avaliados pelos membros da banca da orientação. A proposta é aprovada por um coordenador de Estágio e TCC.

| nome                   |        tipo        | descrição                                          |
| :--------------------- | :----------------: | :------------------------------------------------- |
| `cadastrado_em`        |  `DateTimeField`   | a data e a hora em que o registro foi criado       |
| `atualizado_em`        |  `DateTimeField`   | a data e a hora em que o registro foi editado      |
| `orientacao`           |  `OneToOneField`   | relacionamento um-para-um com o model `Orientacao` |
| `titulo`               |    `TextField`     | máximo de 512 caracteres                           |
| `conceitos`            |    `TextField`     | máximo de 4.000 caracteres                         |
| `resultados_esperados` |    `TextField`     | máximo de 4.000 caracteres                         |
| `aprovada`             | `NullBooleanField` | opcional                                           |
| `aprovada_em`          |  `DataTimeField`   | a data e a hora em que a proposta foi aprovada     |
| `aprovada_por`         |    `ForeignKey`    | relacionamento muitos-para-um com o model `User`   |

## PropostaDeEstagio

O model `PropostaDeEstagio` é uma especialização do model `Proposta` para representa uma proposta de Estágio. Não adiciona atributos ou comportamento.

## PropostaDeTCC

O model `PropostaDeEstagio` é uma especialização do model `Proposta` para representa uma proposta de TCC.

| nome          |    tipo     | descrição                  |
| :------------ | :---------: | :------------------------- |
| `objetivo`    | `TextField` | máximo de 4.000 caracteres |
| `tecnologias` | `TextField` | máximo de 4.000 caracteres |
| `metodologia` | `TextField` | máximo de 4.000 caracteres |

## MembroDeBancaDeProposta

O model `MembroDeBancaDeProposta` representa a informação de um membro de banca de uma proposta, podendo ser um membro interno (Funcionário) ou externo (Colaborador externo).

| nome             |      tipo       | descrição                                                                |
| :--------------- | :-------------: | :----------------------------------------------------------------------- |
| `cadastrado_em`  | `DateTimeField` | a data e a hora em que o registro foi criado                             |
| `atualizado_em`  | `DateTimeField` | a data e a hora em que o registro foi editado                            |
| `proposta`       |  `ForeignKey`   | relacionamento muitos-para-um com o model `Proposta`                     |
| `membro_interno` |  `ForeignKey`   | relacionamento muitos-para-um com o model `Funcionario`; opcional        |
| `membro_externo` |  `ForeignKey`   | relacionamento muitos-para-um com o model `ColaboradorExterno`; opcional |

## AvaliacaoDeProposta

O model `AvaliacaoDeProposta` representa a informação de uma avaliação de uma proposta (de Estágio ou TCC). Considera-se que uma proposta tenha uma quantidade de avaliações igual à quantidade de membros da banca (ou seja, um membro da banca vai registrar uma avaliação da proposta). A proposta pode ser aprovada ou não. A avaliação pode estar publicada (disponível para todos) ou não (disponível apenas para o usuário que cadastrou).

| nome            |        tipo        | descrição                                            |
| :-------------- | :----------------: | :--------------------------------------------------- |
| `cadastrado_em` |  `DateTimeField`   | a data e a hora em que o registro foi criado         |
| `atualizado_em` |  `DateTimeField`   | a data e a hora em que o registro foi editado        |
| `proposta`      |    `ForeignKey`    | relacionamento muitos-para-um com o model `Proposta` |
| `usuario`       |    `ForeignKey`    | relacionamento muitos-para-um com o model `User`     |
| `comentario`    |    `TextField`     | máximo de 5.000 caracteres                           |
| `aprovada`      | `NullBooleanField` | opcional                                             |
| `publicada`     | `NullBooleanField` | opcional                                             |
