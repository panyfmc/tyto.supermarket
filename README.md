# 🛒 Tyto Supermarket API


Projeto backend desenvolvido com Django e Django REST Framework para gerenciamento de clientes, produtos e vendas, com autenticação via JWT.

---


## 🚀 Tecnologias usadas

- **Python**
- **Django**
- **Django REST Framework**
- **SimpleJWT (autenticação)**

---

## ⚙️ Como rodar o projeto localmente

### 1. Criar e ativar ambiente virtual

Bash:
```bash
python -m venv venv
```
Windows:
```bash
.\venv\Scripts\activate
```
Se der erro de política:
```bash
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\activate
```

### 2. Instalar dependências

```bash
pip install django djangorestframework djangorestframework-simplejwt
```


### 3. Entrar na pasta do projeto

```bash
cd tyto_supermarket
```

### 4. Rodar migrações

```bash
python manage.py migrate
```


### 5. Criar um usuário

```bash
python manage.py createsuperuser
```


### 6. Rodar o servidor

```bash
python manage.py runserver
```

-- 
## 🔐 Autenticação (JWT)

### Obter token:

```bash
POST /token/
```

### Body

```bash
{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```
### Resposta:

```bash
{
  "refresh": "...",
  "access": "..."
}
```
## Usar token nas requisições:

### Header:

```bash
Authorization: Bearer SEU_ACCESS_TOKEN
```

--

## 📦 Endpoints principais

### Produtos
- **GET /api/products/** → listar todos os produtos
- **GET /api/products/{id}/** → detalhar um produto
- **POST /api/products/** → criar produto
- **PUT /api/products/{id}/** → atualizar tudo
- **PATCH /api/products/{id}/** → atualizar parcial
- **DELETE /api/products/{id}/** → deletar

### Clientes
- GET /api/clients/
- GET /api/clients/{id}/
- POST /api/clients/
- PUT /api/clients/{id}/
- PATCH /api/clients/{id}/
- DELETE /api/clients/{id}/
### Vendas
- GET /api/sales/
- POST /api/sales/
- PUT /api/sales/{id}/
- PATCH /api/sales/{id}/
- DELETE /api/sales/{id}/

--

## 📌 Observações importantes

- O projeto usa autenticação JWT → endpoints protegidos exigem token
- Datas e CPF são formatados no serializer (saída da API)
- O banco armazena dados sem formatação (boas práticas)
