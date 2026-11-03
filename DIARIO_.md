# Diário de desenvolvimento — Sistema de Bibliotecas

**Integrantes:**
- Joan Pietro Fernandes de Araújo
- Eduardo Pereira da Costa
- Mateus Felipe da Costa

## 10/10

- **O que foi feito:** Começamos a discutir a atividade e pensar em qual sistema poderíamos desenvolver. Escolhemos fazer um Sistema de Bibliotecas, que teria cadastro de usuários, livros e empréstimos.
- **Dificuldade encontrada:** No começo, tivemos algumas dúvidas sobre como organizar o projeto e quais funcionalidades seriam necessárias.
- **Como resolvi:** Conversamos sobre as possibilidades e definimos as principais partes que o sistema precisaria ter.
- **Próximo passo:** Definir os dados que seriam utilizados em cada cadastro e como eles se relacionariam.

## 13/10

- **O que foi feito:** Definimos as entidades principais do sistema: usuários, livros e empréstimos. Também pensamos em como elas se relacionariam, considerando que um usuário pode realizar vários empréstimos e que cada empréstimo pode ter mais de um livro.
- **Dificuldade encontrada:** Tivemos um pouco de dificuldade para entender como funcionaria a relação entre empréstimos e livros.
- **Como resolvi:** Decidimos utilizar uma tabela intermediária para fazer a ligação entre os empréstimos e os livros.
- **Próximo passo:** Começar a montar o projeto utilizando Flask e organizar os arquivos.

## 17/10

- **O que foi feito:** Conversamos sobre a organização do projeto e decidimos utilizar MVC e Blueprints para separar melhor as partes do sistema. Também dividimos as tarefas: Eduardo ficou responsável pelos modelos e banco de dados, Joan pelos controllers e CRUD, e Mateus pelas páginas, CSS, testes e documentação.
- **Dificuldade encontrada:** Tivemos dificuldade para encontrar horários em que todos pudessem participar das reuniões.
- **Como resolvi:** Aproveitamos principalmente os horários das aulas para conversar sobre o projeto e decidir o que cada um iria fazer.
- **Próximo passo:** Começar a criar os arquivos e configurar o Flask e o banco de dados.

## 21/10

- **O que foi feito:** Começamos a montar a estrutura do sistema, criando os arquivos necessários para trabalhar com Flask e SQLite. Também começamos a organizar as pastas dos templates, arquivos CSS e demais partes da aplicação.
- **Dificuldade encontrada:** No início, foi necessário entender onde cada código deveria ficar para não deixar tudo misturado em um único arquivo.
- **Como resolvi:** Separamos os arquivos de acordo com suas funções, deixando os modelos, controllers, banco de dados e páginas em seus respectivos locais.
- **Próximo passo:** Criar os modelos do banco de dados e começar as funcionalidades de usuários, livros e empréstimos.

## 24/10

- **O que foi feito:** Trabalhamos nas páginas do sistema, criando as telas de usuários, livros e empréstimos. Também começamos a preparar os formulários e as funcionalidades para cadastrar, visualizar, editar e excluir informações.
- **Dificuldade encontrada:** Tivemos algumas dificuldades para organizar as páginas e fazer com que os formulários funcionassem junto com as rotas.
- **Como resolvi:** Utilizamos um template base para manter uma estrutura parecida entre as páginas e criamos telas separadas para cada funcionalidade.
- **Próximo passo:** Ligar as páginas aos controllers e ao banco de dados.

## 28/10

- **O que foi feito:** Trabalhamos nos modelos do banco de dados, utilizando as classes `User`, `Book` e `Loan`. Também desenvolvemos os relacionamentos entre as entidades, incluindo a relação de um usuário para vários empréstimos e a relação de muitos para muitos entre empréstimos e livros.
- **Dificuldade encontrada:** A parte mais complicada foi configurar o relacionamento entre empréstimos e livros, principalmente por envolver uma tabela intermediária.
- **Como resolvi:** Utilizamos uma tabela para fazer essa ligação e ajustamos os relacionamentos nos modelos.
- **Próximo passo:** Integrar os modelos com os controllers e verificar se as operações estavam funcionando corretamente.

## 30/10

- **O que foi feito:** Continuamos trabalhando nas rotas e nos controllers de usuários, livros e empréstimos. Também organizamos as rotas utilizando Blueprints e avançamos na ligação entre os formulários e o banco de dados.
- **Dificuldade encontrada:** Precisamos prestar atenção para que os formulários enviassem as informações corretas e que cada rota executasse sua função.
- **Como resolvi:** Separamos as rotas por funcionalidade e organizamos as operações de cadastro, edição, consulta e exclusão nos controllers.
- **Próximo passo:** Conferir a integração das partes do sistema e revisar os relacionamentos.

## 31/10

- **O que foi feito:** Continuamos a integração entre os modelos e os controllers e revisamos a organização geral do projeto. Também adicionamos os arquivos necessários para instalar as dependências e executar a aplicação.
- **Dificuldade encontrada:** Tivemos que conferir se os nomes dos campos, modelos e rotas estavam corretos para evitar problemas na comunicação entre as partes do sistema.
- **Como resolvi:** Revisamos os arquivos e ajustamos a organização para que as diferentes partes da aplicação funcionassem juntas.
- **Próximo passo:** Fazer uma revisão geral, preparar os dados de demonstração e finalizar a documentação.

## Etapas finais do projeto

- **O que foi feito:** Criamos o arquivo `seed.py` para inserir alguns usuários, livros e empréstimos de exemplo no banco de dados. Também trabalhamos no README, explicando o funcionamento do sistema, como instalar as dependências e como executar o projeto.
- **Dificuldade encontrada:** Precisamos conferir se as informações da documentação estavam de acordo com o que realmente havia sido desenvolvido.
- **Como resolvi:** Revisamos os arquivos do projeto e atualizamos as informações do README.
- **Próximo passo:** Fazer os últimos ajustes e preparar o projeto para a apresentação.
