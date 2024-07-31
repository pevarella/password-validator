# Password Validator - Case Itaú

## Desafio

Construa uma aplicação que exponha uma api web que valide se uma senha é válida.

Input: uma senha (string).

Output: um boolean indicando se a senha é valida.

Considere uma senha sendo válida quando a mesma possuir as seguintes definições: 

- Nove ou mais caracteres
- Ao menos 1 número
- Ao menos 1 letra minúscula
- Ao menos 1 letra maiúscula
- Ao menos 1 caractere especial
	- Considere como especial os seguintes caracteres: !@#$%^&*()-+
- Não possuir caracteres repetidos dentro do conjunto

Exemplo:

IsValid("") // false  
IsValid("aa") // false  
IsValid("ab") // false  
IsValid("AAAbbbCc") // false  
IsValid("AbTp9!foo") // false  
IsValid("AbTp9!foA") // false
IsValid("AbTp9 fok") // false
IsValid("") // true

Nota: Espaços em branco não devem ser considerados como caracteres válidos.

## Instruções de Execução

1. Clone o repositório:
```cmd
git clone https://github.com/pevarella/password-validator.git
```
2. Crie um ambiente virtual
```cmd
python -m venv venv
```
3. Ative o ambiente
```cmd
venv\scripts\activate
```
4. Instale as dependências listadas no arquivo pyptoject.toml
```cmd
pip install Poetry
poetry install
```
5. Execute a aplicação
```cmd
fastapi dev password_validator/app.py

# ou

uvicorn password_validator.app:app --reload

```

A API Swagger será exposta em http://localhost:8000/docs

Autenticação 

```cmd
# comando para receber o token via autenticação clientcrendentials
curl -X POST "http://127.0.0.1:8000/token" ^
     -H "Content-Type: application/x-www-form-urlencoded" ^
     -d "client_id=myclientid" ^
     -d "client_secret=myclientsecret" ^
     -d "grant_type=client_credentials"

```

Validar Senha

```cmd
# comando para enviar uma senha para ser validada
curl -X POST -H "Content-Type: application/json" -d "{\"password\": \"SenhaAqui\"}" http://localhost:8000/validador-senhas

```
## Testes

Para rodar os testes unitários utilizando o Pytest:

Faça a instalação utilizando o pip
```cmd
pip install pytest
```
Rode os testes com o comando
```cmd
pytest -s -x --cov=password_validator -vv
```
```cmd
coverage html
```
## Solução

Organizei a API em uma estrutura de pastas 'core', 'routers', 'schemas' e 'services' onde:
- core: contém utilitários de configuração e segurança. No exemplo desse projeto essa pasta ficou "ociosa" para futuras melhores de arquitetura e segurança que não foram possíveis de implamentar no momento.
- routers: contém as definições das rotas da API.
- schemas: contém os modelos de dados usados para validar entrada e saída.
- services: contém a lógica de negócio.

### Lógica de Validação 

Para validação dos critérios de senha defini uma função que recebe a senha e retorna a True ou False. Ela inicializa a variável is_valid como True e faz um checagem por critério, retornando falso se for atendida a condição:

- Nove ou mais caracteres
Verifica se o tamanho da string recebida é menor que 9 com a função len(), caso sim retorna False.
- Ao menos 1 número
- Ao menos 1 letra minúscula
- Ao menos 1 letra maiúscula
- Ao menos 1 caractere especial
Para esses casos utilizei a função re.search() para identificar os respectivos padrões na string por meio de expressões regulares e retornar False caso algum deles não estivesse presente.
- Não possuir caracteres repetidos dentro do conjunto
Converti a string em um conjunto já que conjuntos não podem ter caracteres duplicados e comparei com a string original, caso o número fosse diferente, algum caracter repetido foi removido na conversão e então retorna False.
- Espaços em brancos não devem ser considerados como caracteres válidos
Verificação básica para ver se existe algum espaço em branco na string e caso sim, retornar False.

## Tecnologias e Ferramentas

- VSCodium
- Python 3.12.3
- FastAPI
- Poetry (Gerenciador de Pacotes Python)
- Git
- Pipx (Instalador de aplicativos Python em ambientes virtuais)
- Ignr (Gerenciador de arquivos .gitignore)
- gh (Linha de comando para GitHub)
- Pyenv (Gerenciador de versões de Python)
- Ruff (Linter Python)
- Pytest (Ferramenta de Teste Unitário para Python)
- Taskipy (Gerenciador de Tarefas de projetos Python)

## Melhorias

- Permitir o acesso ao endpoint de validação apenas para o client que possuir o token
- Adicionar testes de integração
- Adicionar um Middleware para Logs e Telemetria
- Dockenização da API
- CI/CD
- Melhorar a validação clientcredentials