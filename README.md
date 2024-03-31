{{ git_page_last_updated }}
# 1. Pré-requisitos

- Acesso a internet
- Windows 10 ou superior
- Conta no GitHub
- Git
- Python

# 2. O que esté projeto usa

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

# 3. PREPARANDO O AMBIENTE

## Ambiente Virtual

Com o Ambiente Virtual Python (Virtualenv), cada projeto pode ter seu próprio ambiente isolado, permitindo a instalação e gerenciamento de versões específicas de bibliotecas e suas dependências. Isso garante que cada projeto tenha um ambiente consistente e estável, sem interferir em outros projetos ou no ambiente global do Python. É uma prática recomendada para desenvolvedores Python que desejam manter a organização e a integridade de seus projetos.

### Instalando o pipenv

No prompt de comando execute:

```powershell
py -m pip install pipenv
```

#### Criando o ambiente para a aplicação

É preciso criar um ambiente virtual do Python, para rodar a sua aplicação, para isso vamos criar uma pasta:

> [!TIP]
> Pressione win+R para abrir prompt de comando

```powershell
cmd
cd Documents
```
> [!TIP]
> Documentos se estiver me português.

Depois vamos criar o diretório para a aplicação:

```powershell
mkdir projdjango
cd projdjango
```

Agora podemos criar nosso ambiente dentro da pasta, passa isso execute:

```powershell
pipenv shell
```

Veja que após a criação, o ambiente já será ativado, aparecendo o nome dele entre (projdjango-xxxxxxxx)

### Clonando o projeto do GitHub
Agora precisamos clonar a aplicação deste repositório do GitHub para isso execute:

```bash
git clone https://github.com/ConradoAlmeida/ProjDjango.git
```

### Instalando os Pré-requisitos do Python
Para instalar o pré-requisitos, precisamos navegar até o diretório que contem o arquivo requirements.txt:

```powershell
cd projdjango
pip install -r requirements.txt
```

Parabéns, você terminou.
No próximo capítulo vamos rodar a aplicação localmente.

## Rodando a aplicação
É peciso navegar até o diretório onde está o manage.py da aplicação, para isso execute:

```powershell
cd garagehub
```

Agora execute a aplicação com o comando:

```powershell
py manage.py runserver
```

Uma mensagem como esta deverá aparecer:

```powershell
System check identified no issues (0 silenced).
March 24, 2024 - 22:14:09
Django version 4.2.11, using settings 'GarageHub.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Abra o navegador com Ctrl+click no link
Se a página estiver quebrada, digite `/garage` ao fim do endereço, ficando assim:
`http://127.0.0.1:8000/garage`
