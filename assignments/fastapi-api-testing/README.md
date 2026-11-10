# 📘 Assignment: Automated Testing for FastAPI

## 🎯 Objective

Write automated tests for a FastAPI REST API using `pytest` and `TestClient`, validating response data and status codes while keeping in-memory test data isolated.

## 📝 Tasks

### 🛠️ Configure the Test Client and Verify Read Routes

#### Descrição
Conclua a atividade Building REST APIs with FastAPI e use a implementação do catálogo de livros como sistema sob teste. Em uma pasta de trabalho fora de `assignments/`, deixe o arquivo da API com o nome `main.py`, renomeie o código inicial desta atividade para `test_main.py` e instale `pytest` e `httpx` com `python -m pip install pytest httpx`. Execute os testes na pasta que contém os dois arquivos.

#### Requisitos
O programa concluído deve:

- Criar um `TestClient` para a aplicação FastAPI.
- Testar `GET /books` e verificar o status HTTP 200 e os dados da lista retornada.
- Testar `GET /books/{book_id}` para um livro existente e verificar o status HTTP 200 e os campos retornados.
- Executar a suíte com `pytest -v`.


### 🛠️ Testar Erros e Operações CRUD

#### Descrição
Adicione testes para confirmar que os endpoints de criação, atualização e exclusão cumprem o contrato da API, incluindo respostas para IDs inexistentes.

#### Requisitos
O programa concluído deve:

- Testar a criação de um livro e verificar o status HTTP 201 e os dados retornados.
- Testar a atualização de um livro e verificar o status HTTP 200 e os valores atualizados.
- Testar a exclusão de um livro e verificar o status HTTP 204 sem tentar decodificar um corpo JSON.
- Verificar o status HTTP 404 ao consultar, atualizar ou excluir um ID inexistente.


### 🛠️ Isolar os Testes e Verificar Filtros

#### Descrição
Garanta que as alterações feitas por um teste não afetem os demais e valide o filtro de livros por autor.

#### Requisitos
O programa concluído deve:

- Usar uma fixture do `pytest` para restaurar os dados em memória antes de cada teste.
- Verificar que `GET /books?author=...` retorna apenas livros do autor solicitado, sem diferenciar maiúsculas de minúsculas.
- Verificar que `GET /books` retorna todos os livros quando o filtro `author` não é informado.
- Executar toda a suíte mais de uma vez e obter os mesmos resultados, sem depender de um banco de dados externo.
