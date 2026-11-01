# Sistema de Bibliotecas

Aplicação web acadêmica para gerenciar usuários/leitores, livros e empréstimos. Interface escura inspirada na referência fornecida.

## Tema e tecnologias

- **Tema:** Sistema de Bibliotecas
- **Tecnologias:** Python, Flask, Flask-SQLAlchemy, SQLAlchemy ORM, SQLite, HTML e CSS.
- **Arquitetura:** MVC com modelos, controllers/rotas e templates.

## Integrantes e responsabilidades

Preencha com os nomes reais e as responsabilidades acordadas pelo grupo:

- Integrante 1: `Nome completo` — Modelos e banco de dados.
- Integrante 2: `Nome completo` — Controllers e operações CRUD.
- Integrante 3: `Nome completo` — Views, CSS, testes e documentação.

## Entidades

- **Usuário:** nome, e-mail e telefone.
- **Livro:** título, autor, gênero, ISBN e quantidade de exemplares.
- **Empréstimo:** usuário responsável, datas, situação e conjunto de livros emprestados.

## Relacionamentos

### 1:N — Usuário → Empréstimos

Um usuário pode ter vários empréstimos; cada empréstimo pertence a um único usuário. Implementado por `Loan.user_id` como chave estrangeira para `usuarios.id` e pelos `relationship()` entre `User.loans` e `Loan.user`. A tela de detalhes do usuário exibe o histórico.

### N:N — Empréstimos ↔ Livros

Um empréstimo pode incluir vários livros, e um livro pode aparecer em vários empréstimos ao longo do tempo. Implementado pela tabela intermediária `emprestimo_livro`, com chaves estrangeiras para `emprestimos.id` e `livros.id`. O formulário de empréstimo permite selecionar vários livros, editar a seleção e remover vínculos. Os detalhes do empréstimo listam seus livros e os detalhes do livro listam os empréstimos relacionados.

## Requisitos

- Python 3.10 ou superior recomendado.
- Git opcional para versionamento.

## Instalação

No terminal, entre na pasta do projeto e crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual:

**Windows (PowerShell):**
```powershell
.venv\\Scripts\\Activate.ps1
```

**Windows (Prompt de Comando):**
```bat
.venv\\Scripts\\activate.bat
```

**Linux/macOS:**
```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Criar e popular o banco

A criação das tabelas ocorre automaticamente quando a aplicação é inicializada. Para inserir dados de demonstração:

```bash
python seed.py
```

O banco SQLite `biblioteca.db` será criado na pasta de instância gerenciada pelo Flask. O arquivo do banco local não deve ser enviado ao GitHub.

## Executar

```bash
python app.py
```

Acesse http://127.0.0.1:5000 no navegador.

## Funcionalidades

- CRUD de usuários e livros.
- CRUD de empréstimos.
- Vínculo de vários livros a um empréstimo e remoção/alteração desses vínculos.
- Histórico de empréstimos por usuário e por livro.
- Marcação de empréstimo como devolvido.
- Indicadores no painel inicial.

## Estrutura

```text
sistema_bibliotecas/
├── app.py
├── database.py
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── book.py
│   └── loan.py
├── controllers/
│   ├── __init__.py
│   ├── main.py
│   ├── users.py
│   ├── books.py
│   └── loans.py
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── users/
│   ├── books/
│   └── loans/
├── static/css/style.css
├── seed.py
├── requirements.txt
├── README.md
└── DIARIO.md
```

## Dificuldades encontradas

Registre aqui as dificuldades que o grupo realmente encontrou durante a implementação e como foram resolvidas. Exemplos possíveis para discutir: tabela intermediária do relacionamento N:N, validação de formulários e separação das responsabilidades MVC.

## Declaração de autoria

Cada integrante deve revisar o projeto, compreender as partes que desenvolveu e adaptar esta declaração à sua participação real.

**Uso de IA:** esta base de código foi gerada com auxílio de IA generativa. O grupo deve declarar esse uso conforme as regras do professor e revisar, testar e compreender o código antes da entrega.
