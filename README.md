# Trilha Python
# Repositório de Projetos em Python

Este repositório contém uma coleção de projetos desenvolvidos em Python. Python é uma linguagem de programação de alto nível, amplamente utilizada por sua simplicidade e legibilidade. Ideal para desenvolvimento web, ciência de dados, automação e muito mais, Python é conhecido por sua sintaxe clara e sua vasta gama de bibliotecas e frameworks.

**Link:** [Ebook - Introdução ao Python - Editora IFRN](https://memoria.ifrn.edu.br/bitstream/handle/1044/2090/EBOOK%20-%20INTRODU%C3%87%C3%83O%20A%20PYTHON%20%28EDITORA%20IFRN%29.pdf?sequence=1&isAllowed=y)

Primeiro de tudo, **instalação**. Se em sua máquina já tiver o python instalado, então tudo certo xD

No entanto, o passo a passo a seguir é eficaz para ajudar aqueles que não possuem o Python instalado.

OBS: Também pode servir para quem não sabe (esqueceu) é só verificar se você tem o Python instalado na sua máquina.


**NO CMD:**

**Digite:** `python --version`

O retorno esperado para (caso) você tiver o python instalado, seria o nome a versão: `python 3.13.0. `

Caso contrário, vamos ver agora um passo a passo da instalação (depois irei adicionar uma imagens e deixar mais claro no que for possível):

1. Acesse o site oficial do Python (<https://www.python.org>) e procure a seção de downloads.
2. Na página de downloads, escolha a versão mais recente estável (por exemplo, `Python 3.9.6`). Não esqueça que deve corresponder ao seu sistema operacional(x64, x86). Se você estiver em um ambiente Windows, é só baixar o instalador executável para ele.
3. Clique no link de download para iniciar o download do instalador.
4. Depois de concluído o download, execute o instalador.
5. <span style="color:red">IMPORTANTE -</span> Na primeira tela do instalador, marque a opção "Add Python to PATH" (Adicionar Python ao PATH). Isso adicionará automaticamente o Python ao PATH do sistema, que é o que permite executar comandos Python em qualquer diretório no prompt de comando ou terminal.
6. Selecione a opção "Customize installation" (Personalizar instalação) para ter mais controle sobre as opções de instalação. Aqui você pode escolher os recursos adicionais que deseja instalar (como pip, IDLE etc.) e selecionar o diretório de instalação.
7. Depois de fazer as seleções desejadas, clique em "Next" (Avançar) e aguarde a instalação ser concluída.
8. Após a instalação ser concluída, você pode abrir o prompt de comando (no Windows, pressione Win + R, digite "cmd" e pressione Enter) e digitar "python" para verificar se o Python foi instalado corretamente, como fizemos inicialmente.

------

### Linguagem Pyton

##### Interpretador IDLE

Bem... há varias formas de utilizarmos na prática o python. Aqui, utilizei o IDLE para testes iniciais com a linguagem e o Pycharm. Para aprender um pouco sobre a IDE que vem junto a instalação padrão do Pyhton. Segue apenas um resuminho sobre:

*IDLE* oferece uma interface gráfica simples que facilita a interação com o interpretador Python. Ele inclui recursos como um editor de texto com realce de sintaxe, suporte para execução interativa de código, histórico de comandos, visualização de resultados, depuração passo a passo, a capacidade de abrir múltiplos editores de código, autocompletar, exibição da árvore de análise sintática e suporte a extensões de terceiros. Uma das principais características do IDLE é a capacidade de executar código Python interativamente, o que significa que você pode digitar instruções e ver os resultados imediatamente. 

##### Pycharm 

O PyCharm é um ambiente de desenvolvimento integrado (IDE) altamente popular e amplamente utilizado para programação em Python. Ele é desenvolvido pela JetBrains e oferece uma série de recursos e 
ferramentas que visam facilitar o processo de desenvolvimento de software em Python.



------

### Resumão Sobre Variáveis e Atribuição de Valores

**Declaração de variáveis:**

1. Em Python, você não precisa declarar explicitamente o tipo de dado de uma variável. Apenas atribua um valor a ela e Python cuidará do resto.
2. **Atribuição de valores:**
   Para atribuir um valor a uma variável, utilize o operador de atribuição (=) seguido pelo valor que deseja armazenar.
3. **Nomes de variáveis:**

- O nome de uma variável pode conter letras, números e o caractere de sublinhado (_).
- O primeiro caractere do nome da variável não pode ser um número.
- Python é sensível a maiúsculas e minúsculas, ou seja, diferencia maiúsculas de minúsculas. Por exemplo, "valor" e "Valor" são duas variáveis diferentes.

4. **Reatribuição de valores:**
   Você pode alterar o valor de uma variável simplesmente atribuindo um novo valor a ela.
5. **Tipos de dados**
   As variáveis em Python podem conter diferentes tipos de dados, como 
   inteiros (int), números de ponto flutuante (float), strings (str), 
   listas (list), dicionários (dict), entre outros. O tipo de dado é 
   inferido automaticamente quando você atribui um valor à variável.

------

### Expressões em Python

Expressões são combinações válidas de variáveis, constantes e operadores que retornam um resultado após a sua avaliação. Existem três tipos principais de expressões em Python: aritméticas, lógicas e relacionais.

#### **Expressões Aritméticas:**

- Operam sobre valores inteiros ou reais.
- Os operadores aritméticos são: + (adição), - (subtração), * (multiplicação), / (divisão), // (parte inteira da divisão), % (resto da divisão) e ** (exponenciação).
- A precedência dos operadores é: primeiro **, depois *, /, // e %, e por último + e -.
- Parênteses podem ser usados para forçar a avaliação de operadores com menor precedência.

Exemplos:

- 5 + 3 → Resultado: 8
- 10 * 2 / 5 → Resultado: 4.0
- 2 ** 3 + 4 → Resultado: 12
- (5 + 3) * 2 → Resultado: 16

<center>.....................................................................................................................................................................</center>

#### Expressões Lógicas:

- São formadas por operadores lógicos: 'or' (ou), 'and' (e) e 'not' (não).
- O resultado da avaliação é sempre True (verdadeiro) ou False (falso).
- A precedência é: primeiro 'not', depois 'and', e por último 'or'.

Exemplos:

- True and False → Resultado: False
- not (5 == 3) → Resultado: True
- (2 > 1) or (3 < 1) → Resultado: True

<Exemplos em código - ex003>

<center>.....................................................................................................................................................................</center>

#### Expressões Relacionais:

- São usadas para fazer comparações entre expressões.
- Os operadores relacionais são: == (igual a), > (maior que), < (menor que), >= (maior ou igual a), <= (menor ou igual a) e != (diferente de).
- O resultado da comparação é True se a condição for satisfeita, ou False caso contrário.

Exemplos:

- 5 == 5 → Resultado: True
- 10 > 5 → Resultado: True
- 7 <= 6 → Resultado: False

É importante entender a ordem de precedência dos operadores para avaliar corretamente as expressões. Se necessário, é possível usar parênteses para controlar a ordem de avaliação.

Lembre-se de que as expressões são fundamentais para realizar cálculos, comparações e testes em Python, tornando-se uma parte essencial na programação com essa linguagem.

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

### Controle de Fluxo

O controle de fluxo em Python é essencial para direcionar a execução do código, permitindo que certas partes do programa sejam executadas apenas sob determinadas condições ou repetidas várias vezes. As principais estruturas de controle de fluxo em Python são:

#### Estrutura Condicional (if, elif, else):

- Permite executar um bloco de código somente se uma condição for verdadeira.
- A estrutura é composta por um "if" seguido por uma condição. Se a condição for verdadeira, o bloco de código dentro do "if" é executado. Caso contrário, o programa verifica se existem cláusulas "elif" (abreviação de "else if") com condições adicionais. Se alguma dessas condições for verdadeira, o bloco de código associado à primeira condição verdadeira "elif" é executado. Caso nenhuma das condições anteriores seja verdadeira, o bloco de código dentro de "else" (opcional) é executado.

#### Estrutura de Repetição (for):

- Permite executar um bloco de código repetidamente para cada elemento de uma sequência (por exemplo, uma lista, string, tupla, etc.).
- O loop "for" itera sobre os elementos da sequência, e a cada iteração, o bloco de código associado é executado.

#### Estrutura de Repetição (while):

- Permite executar um bloco de código repetidamente enquanto uma condição for verdadeira.
- O bloco de código é executado repetidamente até que a condição especificada seja falsa.

#### Controle de Loop (break e continue):

- O "break" é usado para interromper um loop prematuramente, quando uma condição é atendida.
- O "continue" é usado para pular a iteração atual de um loop e passar para a próxima iteração.

#### Cores no Terminal

Os códigos ANSI são uma forma de adicionar formatação de texto ao imprimir no terminal, permitindo que você altere cores de fundo, cores do texto, estilo do texto e até mesmo a posição do cursor. No Python, você pode utilizar esses códigos ANSI para adicionar cores e outros efeitos visuais ao seu texto.

Códigos ANSI para cores no terminal:Os códigos ANSI são sequências de escape que começam com o caractere de escape `\033` (também representado como `\x1b` ou `\u001b`). Eles são seguidos por um conjunto de números separados por ponto e vírgula, que especificam as propriedades de formatação. Para adicionar cores, geralmente usamos códigos ANSI que começam com `\033[`, seguidos por um número para representar a cor desejada.

Exemplo:

- `\033[31m` para cor vermelha
- `\033[32m` para cor verde
- `\033[33m` para cor amarela

1. Estilos de texto:Você pode usar códigos ANSI para adicionar estilos ao texto, como negrito, sublinhado e piscando. Alguns exemplos:

- `\033[1m` para negrito
- `\033[4m` para sublinhado
- `\033[5m` para piscando

1. Resetar a formatação:Após usar códigos ANSI para formatar o texto, é recomendado que você adicione `\033[0m` para redefinir as configurações e evitar que a formatação se aplique ao texto posterior.


------

### Estrutura de Repetição - FOR

Em Python, existem duas estruturas principais de repetição: `while` e `for`. Ambas permitem que você execute um bloco de código várias vezes com base em uma condição ou em um conjunto de elementos.

**Estrutura de repetição com while:**

O `while` repete um bloco de código enquanto uma condição específica for verdadeira. ssa estrutura de repetição executa um ciclo para cada elemento do objeto que está sendo iterado. Nas vezes em que precisamos que determinada variável seja incrementado ou decrementada a cada ciclo, a forma mais simples, é gerando uma lista com a função **range()**.

Sintaxe do comando **WHILE** em Python é a seguinte:

**while** condição:

​           **comando_verdadeiro**

Os comandos (ou instruções) dentro do corpo da estrutura **while** são executados (ou repetidos) ENQUANTO a condição for verdadeira 
(True).
​                    Quando a condição se torna falsa (False), os 
comandos não são executados e o programa continua depois da instrução **while**.

**Estrutura de repetição com for:**

O `for` é usado para percorrer uma sequência de elementos, como uma lista, tupla ou string. Ele executará um bloco de código para cada elemento na sequência.

Sintaxe do comando **FOR** em Python é a seguinte:

**for** item **in range**(início, fim, passo):

​           **item **    

Podemos usar o `break` para sair de um loop antes que a condição seja falsa, e o `continue` para pular a iteração atual e ir para a próxima.

------

### Estrutura de Dados

Estas estruturas resolvem um tipo de problema e podem ser úteis em diversas situações.  As principais estruturas são as Listas, Sets, Dicionários e Tuplas.

####     **Listas**

Uma lista é a estrutura de dados mais básica do Python e armazena os dados em sequência, onde cada elemento possui sua posição na lista, denominada de índice. O primeiro elemento é sempre o índice zero e a cada elemento inserido na lista esse valor é    incrementado.

No Python, uma lista pode armazenar qualquer tipo de dado primitivo (string, inteiro, float, etc).

##### **Declarando Listas**

Para a criação de uma lista no Python, a sintaxe é a seguinte:

```python
nome_da_lista = []
# Criação de uma lista vazianome_da_lista = [1, 2, 3]
# Criação de uma lista de inteirosnome_da_lista = [1, "Olá, mundo!", 1.1]
# Criação de uma lista com vários tipos diferentes
```

Podemos também criar listas dentro de outras listas. Essas são chamadas de nested lists e sua sintaxe é a seguinte:

```python
nome_da_lista = ["Olá, mundo",  [1, 2, 3], ["outra_lista"]]
```

####     **Tuplas**

Uma tupla é uma estrutura bastante similar a uma lista, com apenas uma diferença: **os elementos inseridos em uma tupla não podem ser alterados**, diferente de uma lista onde podem ser    alterados livremente. Sendo assim, em um primeiro momento, podemos pensar em uma tupla como uma lista que não pode ser alterada, mas não é bem assim…

É certo que as tuplas possuem diversas características das listas, porém os usos são distintos. As listas são destinadas a serem sequências homogêneas, enquanto que as Tuplas são estruturas de dados heterogêneas.

Sendo assim, apesar de bastante similares, a tupla é utilizada para armazenar dados de tipos diferentes, enquanto que a lista é para dados do mesmo tipo.

##### **Tuplas x Listas**

As tuplas possuem algumas vantagens com relação às listas, que são:

- Como as tuplas são imutáveis, a iteração sobre elas é mais rápida e, consequentemente, possuem um ganho de desempenho com relação às listas;
- Tuplas podem ser utilizadas como chave para um dicionário, já que seus elementos são imutáveis. Já com a lista, isso não é possível;
- Se for necessário armazenar dados que não serão alterados, utilize uma tupla. Isso garantirá que esses sejam protegidos de alterações posteriores.

##### **Declarando Tuplas**

A sintaxe para criação de uma tupla, assim como uma lista, também é bem simples. Ao invés de se utilizar colchetes (listas), são utilizados parênteses, como podemos ver abaixo:

```python
nome_da_tupla = (1, 2, 3)
#tupla de inteirosnome_da_tupla = (1, "olá", 1.5) #tupla heterogênea
```

####     **Sets**

No Python, os sets são uma coleção de itens desordenada, parcialmente imutável e que não podem conter elementos duplicados. Por ser parcialmente imutável, os sets possuem permissão de adição e remoção de elementos.

Além disso, os sets são utilizados, normalmente, com operações matemáticas de união, interseção e diferença simétrica, conforme veremos nos próximos tópicos.

##### **Declarando Sets**

Para a criação de um set no Python há duas formas: A primeira é bem similar às listas e tuplas, porém utilizando chaves **{}** para determinar os elementos do set:

```python
nome_do_set = {1, 2, 3, 4}

```

A segunda é utilizando o método **set** presente no Python:

```python
nome_do_set = set([1, 2, 3, 4])
```

####     **Dicionários**

No Python, os dicionários são coleções de itens desordenados com uma diferença bem grande quando comparados às outras coleções (*listas, sets, tuplas, etc*): **um elemento dentro de um dicionário possui uma chave atrelada a ele, uma espécie de identificador**.    Sendo assim, é muito utilizado quando queremos armazenar dados de forma organizada e que possuem identificação única (como acontece em bancos de dados).

| Chaves | Valores         |
| ------ | --------------- |
| Nome   | Aelin           |
| Idade  | 31              |
| Cidade | Areia Branca/RN |

Onde cada valor é “atrelado” à uma chave, seu identificador. Vale lembrar que, por necessitar que cada valor possua uma chave relacionada a ele, as chaves dos dicionários devem ser únicas para que possam ser acessadas, também, através do seu índice.

**ATENÇÃO:** As chaves também não são armazenadas em qualquer ordem, elas apenas são associadas aos valores que pertencem.

##### **Declarando Dicionários**

Existem duas formas de se criar um dicionário utilizando o Python. A primeira delas é utilizando chaves ( {} ) e separando os elementos das chaves com dois pontos ( : ) e os outros elementos por vírgula ( , ):

```python
nome_do_dicionario = {1: ‘João’, 2: ‘José’}
nome_do_dicionario = {‘nome’: ‘João’, ‘sobrenome’: ‘Silva’}
```

A segunda forma é utilizando o método **dict()** com o dicionário sendo passado como parâmetro:

```python
nome_do_dicionario = dict({1: ‘João’, 2: ‘José’})
nome_do_dicionario = dict({‘nome’: ‘João’, ‘sobrenome’: ‘Silva’})
```



### Listas

Vamos agora aprofundar o nosso estudo em torno da estrutura de dados* "lista"*. Não se preocupe, que o estudo anterior também irá se aplicar aqui, pois precisamos das estruturas de repetição    para percorrer as listas.

Trabalhar com listas nos permite resolver vários problemas. Você pode criar listas de cada um dos tipos básicos e até mesmo de outras listas. 

**Mas, o quem vem a ser uma lista?** 

*Ora tenho certeza que você já criou uma lista alguma vez na vida. Podemos citar diversos exemplos, como uma lista de compras no supermercado, a lista dos seus filmes favoritos, a lista das matérias que você precisa estudar mais.*

Em Python, uma lista é uma sequência mutável de n valores que podem ser de qualquer tipo
(inclusive outras listas, tuplas e dicionários).
De forma simples, uma lista pode ser entendida como um vetor de elementos que podem ser de
qualquer tipo. As listas são exatamente iguais às Strings, exceto pelo fato de Strings serem
imutáveis e listas serem mutáveis.

As listas podem ser percorridas, “fatiadas” e concatenadas da mesma forma que as Strings. A diferença é que em se tratando de Strings, cada elemento é um caractere e, em se tratando de listas, cada elemento pode ser qualquer tipo de variável. Além disso, uma String pode ser convertida para uma lista (como já foi visto) e uma lista pode ser convertida para uma string.

____________

### Modularização

Técnica de programação que visa a organização do código em partes menores, reutilizáveis e mais gerenciáveis. Ao dividir o código em módulos ou funções, o programador pode focar em resolver pequenas partes do problema por vez, tornando o código mais legível e facilitando a manutenção. 

##### Escopo de Variáveis 

O escopo de uma variável refere-se ao contexto no qual essa variável está definida e por onde pode ser acessada. 

- **Variáveis Locais:** São definidas dentro de uma função e não podem ser acessadas fora dela.

- **Variáveis Globais:** São definidas no corpo principal do código e podem ser acessadas através
   de sua palavra-chave em outra parte do código e, até mesmo, em funções.

  ​

##### Funções

Funções são blocos de 
código que executam uma tarefa específica e que podem ser reutilizados. 
Elas permitem a modularização do código, reduzindo a repetição de 
trechos específicos e tornando o código mais legível.

- **Definição:** Uma função é definida usando a palavra-chave `def`, seguida pelo nome da função e parênteses.
- **Chamada:** Uma vez definida, uma função pode ser chamada pelo seu nome, seguida de parênteses.



##### Passagem de Parâmetro

Python tem um comportamento interessante ao passar argumentos para funções. A depender do tipo de dado, a passagem pode se comportar como por valor ou por referência.

- **Por Valor:** Tipos imutáveis como inteiros, strings e tuplas são passados por valor. Isso significa que qualquer alteração feita no parâmetro dentro da função não afeta o valor original.
- **Por Referência:** Tipos mutáveis como listas, dicionários e conjuntos são passados por referência. Portanto, se você modificar o parâmetro dentro da função, o valor original também será alterado.

<Exemplos em código - ex030, ex035>

### Bibliotecas

As bibliotecas em Python são uma das principais razões para a popularidade e extensão da linguagem. Eles nos permitem que aproveitemos os recursos preexistentes sem ter que reinventar a roda e, que assim, acelerar o nosso processo de desenvolvimento.

**Uma biblioteca em Python é uma coleção de módulos que fornecem funcionalidades prontas para uso.** Estas funcionalidades podem variar de operações matemáticas simples a complexos frameworks de desenvolvimento web.

- **Bibliotecas Padrão**: Python inclui uma vasta biblioteca padrão que oferece funcionalidades para muitas operações comuns, como manipulação de arquivos, operações de rede e gerenciamento de sistema. Essas bibliotecas são parte integrante da instalação do Python e podem ser acessadas sem qualquer instalação adicional.
- **Bibliotecas de Terceiros**: Além das bibliotecas padrão, há uma imensa variedade de bibliotecas de terceiros disponíveis para Python que podem ser instaladas usando ferramentas como pip. Essas bibliotecas abrangem uma vasta gama de funcionalidades, de análise de dados a desenvolvimento de jogos.
  
## Confira as principais bibliotecas Python separadas por finalidade.

### Criação de sites e APIs
1. **Biblioteca Requests:** É muito boa para fazer interações entre APIs e interação com sites.
2. **FrameWork Flask:** É um conjunto de bibliotecas/funcionalidades. É uma ferramenta feita para o Python para que você possa criar sites e APIs e é uma ferramenta muita leve. Muito flexível e muito simples de utilizar.
3. **FrameWork Django:** Ele também é utilizado para a criação de sites e APIs. O Django já vem mais pronto, mas é algo um pouco mais complexo, então para quem está começando talvez não seja a melhor opção.

### Ciência de dados e inteligência artificial
4. **Biblioteca NumPy e Biblioteca Pandas:** Essas duas bibliotecas Python permitem trabalhar com dados, tabelas, análises, manipulações de dados. São muito conhecidas para tratamento de dados python, então você provavelmente já deve ter ouvido falar de pelo menos uma das duas.
5. **TensorFlow e Keras:** São ferramentas que funcionam muito bem para a criação dos seus modelos de inteligência artificial.
6. **Biblioteca OpenCV:** Essa é uma biblioteca para tratamento de imagens, então vai te auxiliar na manipulação tanto de vídeo quanto de imagem. Um exemplo é controlar a sua Webcam utilizando o OpenCV.
7. **Biblioteca Pillow:** Essa é uma biblioteca para tratamento de imagens, só que diferente do OpenCV ela é específica para imagens. Um exemplo que temos é utilizar essa biblioteca para converter imagens no Python (converter a extensão de arquivos).
8. **Biblioteca Scikit-learn:** É uma biblioteca excelente para modelos de classificação, modelos de regressão, modelos de clustering, entre outras coisas que você queira fazer dentro de inteligência artificial.
9. **Biblioteca NLTK:** Essa biblioteca é feita para tratamento de linguagens, análise de sentimento, tratamento de texto, análise de textos, previsão de escrita e outros tipos de linguagem natural.
10. **Biblioteca PyTorch:** É uma ferramenta muito boa para deep learning e para acelerar o seu processamento e o processo de construção do seu modelo de inteligência artificial. Mais uma boa opção para tratamento de dados python.

### Visualização de dados
11. **Biblioteca Ploty:**  Biblioteca gráfica de código aberto gratuita, é construída sobre a biblioteca Plotly JavaScript (plotly.js). Você pode usar para criar visualizações de dados baseadas na web. São mais de 40 tipos de gráficos, inclusive alguns não tão comuns em outras bibliotecas de visualização de dados. Pode ser usado offline.
12. **Biblioteca Matplotlib:** É uma das bibliotecas Python para visualização de dados que permite a criação de gráficos e plotagem 2D. É muito útil para uma representação amigável de dados. Você pode usá-la para aplicações matemáticas ou científicas que exigem mais do que eixos únicos na representação gráfica, por exemplo.
13. **Biblioteca Seaborn:** É uma das principais bibliotecas python para visualização de dados, pois se baseia em Matplotlib e se integra com as estruturas de dados numpy e pandas. Além das funções de plotagem, executa as funções de agregação estatística e mapeamento para criar gráficos informativos para o usuário. 

### Automações
14. **Biblioteca Selenium:** É muito utilizada quando falamos de automação web, funciona para busca na internet (web scraping) e automações de processos completos. Funciona até mesmo para o preenchimento de formulários!
15. **Biblioteca Scrapy e Beautiful Soup:** Também são bibliotecas que vão te ajudar com o web scraping, que é a obtenção de dados da web de forma automática para que você não precise fazer todo o procedimento de forma manual.
14. **Biblioteca PyAutoGUI:** É uma biblioteca que permite você automatizar o seu mouse, teclado e a tela do seu computador. Então vai permitir que você faça uma automação de uma atividade repetitiva você tenha que fazer no seu computador. Isso quer dizer que você consegue automatizar qualquer ação dentro do computador independente do programa.
16. **Biblioteca Pyodbc:** É uma biblioteca de integração com banco de dados.
17. **Biblioteca Pywin32**: Ela te permite automatizar uma série de coisas no Windows, então isso pode te facilitar bastante caso utilize o Windows. Você vai notar que boa parte das empresas utiliza esse sistema operacional, então vai te ajudar nesses casos.
C8iação de interfaces gráficos
19. **Biblioteca Kivy:** É uma ferramenta para criação de telas onde as pessoas podem interagir sem precisar visualizar o código por trás. O mesmo código no Kivy funciona em qualquer plataforma, seja Linux, Windows, Mac, IOs ou Android.
20. **Biblioteca Tkinter:** É a biblioteca mais simples para poder começar com interfaces gráficas, então para telas simples é a mais recomendada. Ele já vem dentro do Python, então nem vai precisar fazer a instalação.
21. **Biblioteca PyQt5:** Também serve para criar telas para os seus programas, mas para programas mais complexos diferente do tkinter que é mais simples.

##### Utilização

Usar uma biblioteca em Python geralmente requer duas etapas. Primeiro, você precisa instalar a biblioteca (a menos que seja parte da biblioteca padrão). Isso geralmente é feito utilizando pip. Depois de instalado, você pode importar a biblioteca ou partes dela em seu código e usar suas funcionalidades.

##### Criação

Criar sua própria biblioteca pode parecer uma tarefa assustadora, mas é essencial para organizar seu código de forma modular e reutilizável. Se você tem um conjunto de funções que você acha que pode utilizar em múltiplos projetos, ou acredita que outros possam se beneficiar, pode ser hora de empacotá-los em uma biblioteca.

- **Organização do Código**: O primeiro passo é organizar seu código. Crie um diretório para sua biblioteca e coloque seu código em um ou mais arquivos `.py` neste diretório.
- **Criar setup.py**: Este é o arquivo de configuração necessário para empacotar sua biblioteca para distribuição. Ele contém informações sobre a biblioteca e suas dependências.

#### Conclusão
As diversas bibliotecas Python podem ser utilizadas em inúmeras situações. Em alguns momentos, você usará muitas em conjunto para obter o melhor resultado em seu trabalho. Conhecer as principais bibliotecas Python contribui para que você saiba quando optar por cada uma delas. 
Enquanto Pywin32 e Selenium são bibliotecas Python para automação, NumPy e Pandas são bibliotecas Python data science. Se você precisa fazer tratamento de dados Python, essas últimas duas podem ser úteis.
Entender as bibliotecas e como elas operam é fundamental para qualquer desenvolvedor Python, seja utilizando funcionalidades preexistentes para acelerar seu trabalho ou compartilhando suas próprias criações com a comunidade de desenvolvedores Python.

## Recursos:
- **Versão**: Python 3.13.0.
- **Bibliotecas **: [listar bibliotecas]
- **Documentação**: Cada projeto inclui uma documentação detalhada sobre como instalar e executar o código.

  Sinta-se a vontade para contribuir,  contribuições são sempre bem-vindas!🙂

