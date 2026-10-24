<p align="center">
  <img
    src="https://capsule-render.vercel.app/api?type=waving&height=100&color=f4c531"
    alt="Header"
  />
</p>

# **`Relatórios de Laboratório e Projetos de Engenharia (Laboratory Reports and Engineering Projects)`**

>[!IMPORTANT]
> Este repositório tem como objetivo armazenar relatórios de laboratório das disciplinas **Física 1, 2 e 3**, **Eletricidade Básica** e **Análise de Circuitos em Corrente Contínua**, além de relatórios, códigos em `C` e projetos desenvolvidos nas disciplinas de **Eletrônica** e **Sistemas Microcontrolados**. Os trabalhos abrangem a elaboração de documentos técnicos com `LaTeX`, compilados no `Overleaf`, simulações de circuitos no `Falstad` e desenvolvimento de projetos utilizando linguagens como `C`, `Python` e `R`, entre outras ferramentas. 
>
> Na disciplina de **Análise de Circuitos em Corrente Contínua**, ministrada pelo professor **João Cesar Paula Salve**, os relatórios também incluem gráficos gerados em `Python` com a biblioteca `matplotlib`. Além disso, o repositório contém o código da apresentação final da disciplina, desenvolvida em `Python` utilizando a biblioteca `ManimCE`. O vídeo completo da apresentação pode ser acessado no link abaixo:
>
> [Vídeo da Apresentação Completa](https://www.youtube.com/watch?v=DIhBOLY_waU)
>
> De forma geral, o repositório busca demonstrar habilidades em **documentação técnica, elaboração de relatórios científicos, programação, simulação de circuitos, análise de dados e desenvolvimento de projetos de engenharia**.


---

## Sobre a Apresentação usando ManimCE

<b>Construção do Código</b>

Para o desenvolvimento do código, foi utilizada a 
[Documentação Oficial do Manim](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html).  
A construção do circuito foi realizada com o auxílio da biblioteca adequada e da aplicação web 
[TikZMaker](https://tikzmaker.com/editor).

Durante o desenvolvimento da plotagem do gráfico e da construção/animação do circuito, utilizaram-se como inspiração os seguintes recursos:

- [Electrical Circuit Representation with ManimCE and LaTex || ManimCE || Python](https://www.youtube.com/watch?v=sWSmd3cujK8&pp=ygUQbWFuaW0gY2UgY2lyY3VpdA%3D%3D)
- [Design, Simulate & Animate Electrical Circuits with Python](https://www.youtube.com/watch?v=Ckownv7VoxM&pp=ygUQbWFuaW0gY2UgY2lyY3VpdA%3D%3D)
- [1.1 Manim tutorial: Creating Graphs](https://www.youtube.com/watch?v=GemuXCUEBVU&t=410s)
- [Código de referência no GitHub 1](https://github.com/sayedul79/m-anim/blob/main/colored-circuit.py)
- [Código de referência no GitHub 2](https://github.com/yasser64b/Animations)


Cada trecho do vídeo foi gerado a partir de uma parcela do código. Depois que tudo ficou pronto, foi usado o [Adobe Express](https://new.express.adobe.com/home/tools/merge-videos) para concatenar os vídeos.


> Na pasta ```Presentation/``` do respositório, vão estar somente as partes principais.


Todo o código foi executado no Ubuntu 24.04.3 LTS por meio do terminal. Existem diversas alternativas, como utilizar o Google Colab, porém aqui foi adotado o Vim juntamente com o terminal padrão do sistema.



<b>Instruções de Instalação e Execução do ManimCE</b>

## 1. Instalação

A instalação foi realizada de acordo com a documentação oficial do Manim. No caso do Linux, bastou seguir as instruções específicas:

**Documentação:**  
[Instalação do Manim](https://docs.manim.community/en/stable/installation/uv.html)

```bash
sudo apt update
sudo apt install texlive-full build-essential python3-dev libcairo2-dev libpango1.0-dev
```

## 2. Criação e ativação do ambiente virtual Python

O uso de ambientes virtuais é uma prática padrão para executar programas em Python. Mais informações podem ser encontradas na [Documentação do módulo venv](https://docs.python.org/pt-br/3/library/venv.html).

```bash
python3 -m venv teste
source teste/bin/activate
```

## 3. Instalação da biblioteca dentro do ambiente virtual

Com o ambiente virtual ativado, atualize o `pip` e instale o Manim:

```bash
pip install --upgrade pip
pip install manim
```

## 4. Abrir ou editar os arquivos de código do repositório

Você pode abrir os arquivos Python do repositório em um editor de texto, como o Vim:

```bash
vim *.py
```

## 5. Executar a animação

Com o ambiente virtual ativado e o arquivo Python pronto, execute a animação com o seguinte comando:

```bash
python -m manim -pqh *.py <nomeClasse>
```

> No Youtube, tem uma breve execução do passo a passo: [Instruções simples sobre executar ManimCE pelo terminal](https://youtu.be/dnqXJ8WkLio)


---


<p align="center">
  <img
    src="https://capsule-render.vercel.app/api?type=waving&height=100&color=f4c531&section=footer"
    alt="Footer"
  />
</p>
