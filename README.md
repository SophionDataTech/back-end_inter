# Backend do Projeto Intercessao

Segue o detalhamento para configurar o ambiente de desenvolvimento e teste do back-end.

## Instalação e Dependências

1.  **Crie um ambiente virtual (recomendado):**

    ```bash
    python -m venv venv
    # Ative o ambiente virtual (dependendo do seu sistema operacional)
    # No Linux/macOS:
    source venv/bin/activate
    # No Windows:
    .\venv\Scripts\activate
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

    O arquivo `requirements.txt` contém todas as bibliotecas Python necessárias para rodar o projeto. A lista das dependências instaladas no seu ambiente virtual é a seguinte:

    ```
    * asgiref==3.8.1
    * Django==5.2.1
    * djangorestframework==3.16.0
    * psycopg2-binary==2.9.10
    * python-decouple==3.8
    * sqlparse==0.5.3
    * e outras (ver arquivo)
    ```

## Configuração do Banco de Dados

1.  **As informações para persistência de dados são definidas no arquivo `backend/settings.py` do Django:**

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': '[Nome do seu banco de dados]',
            'USER': '[Seu usuário do banco de dados]',
            'PASSWORD': '[Sua senha do banco de dados]',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```
    Obs.: as credenciais de acesso não são versionadas e são controladas pela lib Psycopg2.


## Executando o Backend Django

1.  **Aplique as migrations para criar o esquema de armazenamento:**

    ```bash
    python manage.py migrate
    ```

2.  **Crie um superusuário (para acessar o painel de administração do Django):**

    ```bash
    python manage.py createsuperuser
    # Siga as instruções para criar seu nome de usuário e senha.
    ```

3.  **Inicie o servidor de desenvolvimento do Django (garanta que na pasta backend do Django tenha um arquivo .env com as credenciais corretas):**

    ```bash
    python manage.py runserver
    ```

    O backend estará rodando em `http://127.0.0.1:8000/` por padrão.

## Fazendo Requisições à API

Para interagir com a API do backend, você pode usar o Insomnia ou Postman. Garanta que na pasta backend do Django esteja a API_KEY no .env.
Solicite a exportação da coleção de requisições no Insomnia. 🙂
