## Quiz Django API

API de uma aplicação para a criação de um quiz de perguntas e respostas

Tecnologias utilizadas:

* **Python (3.9.6 ou acima)**
* **Django**
* **Django REST Framework**

Você irá desenvolver a API de uma aplicação para a criação de um quiz de perguntas e respostas!

**A aplicação provê o registro e autenticação de dois tipos de usuários**:

* Admin
* Player

**Cada quiz é composto por**:

* Perguntas com 3 respostas onde apenas 1 é correta.
* Cada resposta correta acumula 1 ponto.
* Cada resposta errada perde 1 ponto. A menor pontuação possível é 0.
* Uma categoria.

**Ao iniciar o jogo**:

* O player deve se registrar, escolher uma categoria válida e receber um quiz com perguntas referentes a categoria escolhida.

**Ao finalizar o jogo**:

* O player recebe a contabilização dos seus pontos. Não há limitação de quantos quizzes o player pode responder.

**Permissões**:

* Os endpoints estão protegidos por autenticação.
* Usuários do tipo **Admin** tem permissão para criar perguntas e respostas para os quizzes.
* Usuários do tipo **Player** tem permissão para jogar.

**Para rodar a API devemos executar os seguintes comandos**:

* git clone https://github.com/gabrielricardo7/quiz-backend.git
* cd quiz-backend/ && python3 -m venv venv
* . venv/bin/activate && pip install -r requirements.txt
* ./manage.py runserver

## URL_BASE: 

http://localhost

## Endpoints

* **/**: *Index* - Página principal (Quiz)
* **/admin**: Página de acesso do Administrador, que pode criar novos quizzes com uma categoria
* **/entrar**: Página de *login* - entrada do usuário ou admin 
* **/nova_pergunta**: Página para adicionar nova pergunta ao quiz (Somente admins)
* **/registro**: Página de registro de usuário (Player/Jogador)
* **/resultado** Página de resultados - Exibida quando se termina de responder o Quiz

## Instruções

Quando estiver rodando a aplicação, acesse a *URL_BASE* (http://localhost), registre uma conta de usuário, entre com sua senha e escolha uma categoria da lista de quizzes.

## OBS (Admin padrão):

* **usuário**: admin
* **senha**: admin
