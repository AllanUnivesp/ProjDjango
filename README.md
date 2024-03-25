



# Pré-requisitos

- Acesso a internet
- Windows 10 ou superior
- Conta no github
- Git
- Python

# O que esté projeto usa

## Django Framework 5.0.3

O Django é um framework web Python de código aberto que simplifica a criação de soluções web escaláveis. Ele oferece um ambiente para desenvolvimento rápido, promovendo um design limpo e ferramentas eficientes para pessoas desenvolvedoras. Com o Django, é possível construir sites e aplicações web de alto desempenho de forma mais simples, rápida e com menos código.

## Python 3.12.0

O Python é uma linguagem de programação de alto nível, o que significa que sua sintaxe é mais simplificada e próxima da linguagem humana. Ela é amplamente utilizada em diversas aplicações, como desenvolvimento web, análise de dados, machine learning e inteligência artificial.

## Visual Code 1.87.2

O VS Code é uma ferramenta leve, gratuita e multiplataforma. Além de ser amplamente utilizado para desenvolvimento web, ele também oferece suporte a várias linguagens, como Python, Ruby e C++. Sua interface intuitiva e extensibilidade por meio de plugins o tornam uma escolha popular entre desenvolvedores em todo o mundo.

## Git 2.44

O Git é um sistema de controle de versão distribuído (DVCS), sendo um dos mais famosos e populares do mundo se tornando essencial para colaboração, rastreamento de mudanças e garantia de integridade do código-fonte em projetos de desenvolvimento.

## GitHub

O GitHub é uma plataforma de hospedagem de código-fonte e arquivos com controle de versão usando o Git. Ele permite que programadores, utilitários ou qualquer usuário cadastrado na plataforma contribuam em projetos privados e/ou Open Source de qualquer lugar do mundo.

## pipenv 2023.12.1

O Pipenv é uma ferramenta que visa trazer o melhor de todos os mundos de empacotamento (bundler, composer, npm, cargo, yarn, etc) para o ecossistema Python, casando o instalador de pacotes pip e virtualenv e substituindo o requirements.txt.

## Windows 11 Version 10.0.22631.3296

O Windows 11 é um sistema operacional e a versão atual do sistema Microsoft Windows desenvolvido pela Microsoft, anunciada e lançado em 2021, como o sucessor da versão Windows 10. No final de 2020, foi anunciado que era planejado uma grande atualização para o Windows 10 denominada "Sun Valley".

# PREPARANDO O AMBIENTE

## Ambiente Virtual

Com o Ambiente Virtual Python (Virtualenv), cada projeto pode ter seu próprio ambiente isolado, permitindo a instalação e gerenciamento de versões específicas de bibliotecas e suas dependências. Isso garante que cada projeto tenha um ambiente consistente e estável, sem interferir em outros projetos ou no ambiente global do Python. É uma prática recomendada para desenvolvedores Python que desejam manter a organização e a integridade de seus projetos.

### Instalação do pipenv

No prompt de comando execute: `py -m pip install pipenv`

#### Criação do ambiente para a aplicação

É preciso criar um ambiente virtual do Python, para rodar a sua aplicação, para isso vamos criar uma pasta:
`win+R`
`cmd`
`cd Documents` Documentos se estiver me português
`mkdir projdjango`
`cd projdjango`
Agora podemos criar nosso ambiente dentro da pasta, passa isso execute:
`pipenv shell`
Veja que após a criação, o ambiente já será ativado, aparecendo o nome dele entre (projdjango-xxxxxxxx)

### Clone do projeto no GiHub
Agora precisamos clonar a aplicação deste repositório do GitHub para isso execute:
`git clone https://github.com/ConradoAlmeida/ProjDjango.git`

### Instalaçção dos Pré-requisitos do Python
Para instalar o pré-requisitos, precisamos navegar até o diretório que contem o arquivo requirements.txt:
`cd projdjango`
`pip install -r requirements.txt`



Once you've cloned the repository, navigate into the repository.

Create a virtual environment and activate it using the following commands:
`python3 -m venv venv`
> fazer com pipenv
`source venv/bin/activate`
Once you've activated your virtual environment install your python packages by running:
`pip install -r requirements.txt`
Now let's migrate our django project:
`python manage.py migrate`
If there are no hitches here you should now be able to open your server by running:
`python manage.py runserver`
Quick and painless. If there are any issues or problems, leave a comment below!
