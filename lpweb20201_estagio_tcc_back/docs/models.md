# Models

O backend utiliza os models `User` e `Group`, disponíveis no pacote `django.contrib.auth.models`. Além disso, declara o model `Perfil`, com os seguintes campos:

| nome          |     tipo      | descrição                                                                                                                       |
| :------------ | :-----------: | :------------------------------------------------------------------------------------------------------------------------------ |
| `cadastrado_em` | `DateTimeField` | a data e a hora em que o perfil foi criado                                                                                      |
| `atualizado_em` | `DateTimeField` | a data e a hora em que o perfil foi editado                                                                                     |
| `usuario`       | `OneToOneField` | relacionamento um-para-um com o model `User`; indica que o perfil pertence a um usuário; relacionamento com exclusão em cascata |
| `nome`          |   `CharField`   | máximo de 128 caracteres; representa o nome do usuário; indexado no banco de dados                                              |
| `sexo`          |   `CharField`   | máximo de 1 caractere; pode ter os valores 'F' ou 'M'; pode ser nulo                                                            |
| `cpf`           |   `CharField`   | máximo de 14 caracteres; indexado no banco de dados como valor único; pode ser nulo                                             |
| `telefone`      |   `CharField`   | máximo de 15; pode ser nulo caracteres                                                                                          |
| `endereco`      |   `TextField`   | máximio de 512; pode ser nulo caracteres                                                                                        |
| `cep`           |   `CharField`   | máximo de 10; pode ser nulo caracteres                                                                                          |
| `estado_uf`     |   `CharField`   | máximo de 2; pode ser nulo caracteres                                                                                           |
| `cidade`        |   `CharField`   | máximo de 64 caracteres; pode ser nulo                                                                                          |