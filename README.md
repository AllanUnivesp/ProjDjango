# GarageHub
Mechanical workshop management application. It's related to the integrative project subject of the computer engineering degree.

POP<sub>Procedimento Operacionao Padrão</sub>

Criação de projeto Inicial em Django

Autor: Conrado Almeida

Email: <conrado.almeida@outlook.com>

# Pré-requisitos

- Computador com Windows 10 ou superior.

# Acesso a internet

- Conta no github;
- Conhecimentos básicos de informática,

# O que vamos usar

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

# Passo a passo

Este passo a passo foi elaborado para possibilitar ao leitor, ter seu projeto Django inicial funcionado, exibindo a tela incial de “_Congratulations!_”, que significando que o projeto está funcionando.

Vale lembrar que ao fim desse POC, seu projeto Django não terá funcionalidades, estas deverão ser criadas e programadas posteriormente, de acordo com as regras de negócios específicas da necessidade.

Para seguir esse passo a passo, baster conhecimentos básicos de informática, já que vamos instalar alguns programas.

Prompt de Comando (cmd): Não tenha medo, vamos usar de forma bastante superficial e os comandos a serem executados serão autoexplicativos.

Importante: O comando de Enter no teclado, será tratado apenas exibindo: \[↵ ENTER\]

## Instalar Visual Code

- [Download Visual Studio Code - Mac, Linux, Windows](https://code.visualstudio.com/download);
- Instalar o Visual Studio Code;
- Verificar a instalação e versão:
  - Abra o Prompt de Comando (pressione Win + R, digite cmd e \[↵ ENTER\]);
  - Execute o comando:

`code --version`

- - Para abrir o vscode pelo prompt, execute:

`code`

- Para abrir o vscode, referenciando um diretório, pelo prompt:
  - Navege até o diretório que deseja, utilizando o prompt:
    - Use os comandos **cd** (_Change Directory_) ir para o diretório e **cd ..** para recuar um diretório;
    - Dentro do diretório, execute:

`code .`

- Exemplo de como navegar entre os diretórios do Windows utilizando o promp de comando:
  - Suponha que você esteja em C:\\Users\\SeuUsuario.
  - Para entrar na pasta Documentos, digite:

`cd documentos`

- - Para voltar para C:\\Users, use:

`cd ..`  

## Instalar o Python 3.12.0

- [Download Python | Python.org](https://www.python.org/downloads/);
- Instalar o Python.
- Verificar a instalação e versão:
  - Abra o Prompt de Comando (pressione Win + R, digite cmd e \[↵ ENTER\]);
  - Execute o comando:

`python --version`

## Instalar pipenv (através do prompt de comando)

- Abra o Prompt de Comando (pressione Win + R, digite cmd e \[↵ ENTER\]);
- Execute o comando:

`py -m pip install pipenv`

- Verifique a instalação e versão do pipenv instalado, executando o comando:

`pipenv --version`

Se estiver tudo certo, deverá aparecer uma mensagem com a versão do pipenv instalado, parecido com:

<blockquote>1.87.2 <br> 863d2581ecda6849923a2118d93a088b0745d9d6 <br> x64</blockquote>

## Criar um diretório para o projeto (através do prompt de comando)

Nesse documento, o nome do diretório será ProjDjango e vamos criar nosso diretório dentro de C:\\Users\\Usuario\\Documents, fique livre para criar o seu próprio nome, se quiser.

> [!TIP]
> O endereço de diretório acima está genérico e em inglês, isso significa que onde está escrito NomeUsuario, vai estar com o nome do seu usário logado no Windows também que se o seu Windows estiver em português o endereço deverá aparecer um pouco diferente:

`C:\\Usuario\\NomeUsusario\\Documentos`

- Abra o Prompt de Comando (pressione Win + R, digite cmd e \[↵ ENTER\]);
- Ao abrir, você estará no nível **C:\\Users\\Usuario>**, portanto execute os comandos:
- `cd documents` (ou documentos se for em português)
- `mkdir ProjDjango`
- `cd ProjDjango`
- `code .`

1. Criar um ambiente virtual para o projeto (virtual environment) através do prompt de comando
