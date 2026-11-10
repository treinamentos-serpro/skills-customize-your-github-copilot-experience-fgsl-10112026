# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST com FastAPI para praticar métodos HTTP, parâmetros de caminho e consulta, modelos de requisição e resposta e códigos de status.

## 📝 Tasks

### 🛠️ Criar a API e Consultar Livros

#### Descrição
Use o código inicial fornecido para criar uma API local de catálogo de livros. Com Python 3.10 ou superior, instale `fastapi` e `uvicorn`, renomeie `starter-code.py` para `main.py` e inicie o servidor com `uvicorn main:app --reload`. Use a documentação interativa em `/docs` para enviar requisições.

#### Requisitos
O programa concluído deve:

- Retornar todos os livros em `GET /books`.
- Retornar um livro em `GET /books/{book_id}`.
- Responder com HTTP 404 quando o ID solicitado não existir.
- Representar cada livro com ID, título, autor e ano de publicação usando o modelo `Book`.


### 🛠️ Adicionar Operações de Criação, Atualização e Exclusão

#### Descrição
Implemente as demais operações para gerenciar livros no catálogo mantido em memória, usando o método HTTP apropriado para cada operação.

#### Requisitos
O programa concluído deve:

- Criar um livro com `POST /books` e responder com HTTP 201 e os dados do livro criado.
- Substituir um livro com `PUT /books/{book_id}` e retornar os dados atualizados.
- Excluir um livro com `DELETE /books/{book_id}` e responder com HTTP 204 em caso de sucesso.
- Responder com HTTP 404 quando a atualização ou exclusão solicitar um ID inexistente.


### 🛠️ Filtrar Livros por Autor

#### Descrição
Amplie o endpoint de listagem com um parâmetro de consulta opcional para permitir buscas por autor sem alterar a rota.

#### Requisitos
O programa concluído deve:

- Aceitar um parâmetro de consulta opcional `author` em `GET /books`.
- Retornar somente livros cujo autor corresponda à consulta, ignorando diferenças entre letras maiúsculas e minúsculas.
- Retornar todos os livros quando o parâmetro `author` não for informado.
