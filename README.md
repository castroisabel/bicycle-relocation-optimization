# Processo seletivo - Mercado Livre

## Desafio: Relocação de Bicicletas

### Introdução

A RentalBike é uma empresa de compartilhamento de bicicletas que oferece aluguel de bicicletas de curta duração em várias áreas de uma cidade, com diferentes categorias de bicicletas disponíveis. Os clientes podem alugar bicicletas por qualquer período e devolvê-las em uma área diferente daquela onde as retiraram, desde que seja uma área operada pela RentalBike. Como os clientes podem mover as bicicletas, a empresa precisa redistribuir o excesso de bicicletas entre as diferentes áreas conforme a demanda. Essa decisão de redistribuição é baseada nos lucros esperados para cada volume de bicicletas a serem movidas, exigindo uma otimização antes do processo de realocação.

### Entradas

- Excedente de bicicletas de diferentes categorias na área de origem;
- Constantes para o espaço ocupado por uma bicicleta de cada categoria no caminhão;
- Lucros esperados para relocar bicicletas da área de origem para qualquer outra área.

**Desafio:** Quantas bicicletas de cada categoria devem ser transportadas para cada área de forma que a soma do lucro esperado seja maximizada?

### Pressupostos
1. Os lucros esperados são constantes em relação a cada unidade de bicicletas que podem ser relocadas para outras áreas. Portanto, é um problema de otimização determinística;
2. Neste desafio, apenas uma área é a fonte das bicicletas. Portanto, haverá apenas relocamentos começando desta área.

### Dados
Dados disponíveis na pasta `data` no arquivo: `BicyclesRelocationData.xlsx`

- Uma planilha chamada `Categories` que fornece cada categoria de bicicleta como cabeçalho, e respectivamente, duas linhas de dados:
    1. O excedente de bicicletas disponíveis na área de origem para cada categoria;
    2. Constante para quanto espaço cada categoria de bicicleta ocupa no caminhão. Por exemplo, se uma categoria de bicicleta chamada "Child" tem constante 1 e a categoria "Adult" tem constante 1.5, então uma bicicleta "Adult" ocupa 50% mais espaço no caminhão do que uma bicicleta "Child".

- Planilhas com nomes começando com `ExpectedProfitsArea` e terminando com um número. Esses números indicam qual área de destino é a planilha descrita. Cada uma dessas planilhas tem todas as categorias de bicicletas como cabeçalho e várias linhas de dados. Cada linha apresenta quanto lucro se espera ganhar ao enviar uma bicicleta adicional para aquela área de destino.

#### Características do lucro esperado:
- Os dados de lucros esperados **não são acumulados**;
- Como a demanda pelo compartilhamento de bicicletas varia de acordo com diferentes fatores, o lucro obtido pelo primeiro aluguel de uma bicicleta pode ser maior ou menor do que o lucro obtido pelo segundo aluguel da mesma bicicleta na mesma região;
- O lucro esperado pela relocacão da enésima bicicleta só é obtido se todas as bicicletas anteriores desta mesma categoria e área forem alugadas;
- A única propriedade que os valores de lucro esperado têm é que são números **não negativos**;
- O comprimento dos dados de lucros esperados pode ser diferente do excedente de bicicletas de cada categoria. No caso de não haver dados de lucro esperados para todas as bicicletas excedentes, o lucro pela relocacão de mais bicicletas do que o excedente da categoria deve ser **considerado como zero**.

## Tarefas

### 1. Formule e resolva o problema de otimização:

**a)**. Escreva uma formulação matemática para resolver este problema de otimização, considerando que a capacidade total de espaço do caminhão é representada por uma constante $T$. **Defina as constantes e variáveis**, e descreva as **restrições e a função objetivo** para maximizar a soma dos lucros esperados.

**R**: 
#### Modelagem Matemática
Considere as seguintes variáveis e constantes: 

$x_{i,j,k}$: indica se a $k$-ésima bicicleta da categoria $j$ foi movida da área de origem para a área de destino $i$

$i$: Área de destino;

$j$: Categoria da bicicleta;

$k$: $k$-ésima bicicleta a ser movida;

$a_j$: Disponibilidade de bicicletas na área de origem da categoria $j$;

$s_j$: Espaço que a bicicleta de categoria $j$ ocupa no caminhão;

$l_{i,j,k}$: Lucro esperado na área de destino $i$ devido a relocação da $k$-ésima bicicleta da categoria $j$;

$T$: Capacidade máxima do caminhão.

Considere as seguintes restrições:

Binária:

$x_{i,j,k} \in \{0, 1\}$;

Disponibilidade de bicicletas na área de origem:

$\sum_i \sum_k x_{i,j,k} \leq a_j $;

Capacidade máxima do caminhão:

$\sum_i \sum_j \sum_k x_{i,j,k} \times s_j \leq T$;

Condição relocação sequencial das bicicletas:

$x_{i,j,k} \leq x_{i,j,k-1}$.

A função objetivo para o problema será dada por:

$\max L = \sum_{i} \sum_{j} \sum_{k} l_{i,j,k} \times x_{i,j,k}$

Apesar de usar a variável de decisão $x_{i,j,k}$ para a solução computacional, iremos reportar $x_{i,j} =  \sum_k x_{i,j,k}$ que representa exatamente a resposta que buscamos: quantas bicicletas de cada categoria devem ser realocadas para cada área.


**b)** Escolha uma linguagem de programação e um solucionador (como CBC ou GLPK) para otimizar a formulação que você propõe na tarefa 1 a). Considerando a capacidade do caminhão como $T=80$, resolva o problema e mostre seu código, a solução ótima e o valor objetivo ótimo.

**R**: 

#### Modelagem Computacional
Disponível no arquivo: *src/solver.py* e *notebooks/03.modeling.ipynb*

Solução ótima:

$x_{i,j} = \begin{bmatrix}
1.0 & 0.0 & 0.0 & 0.0 & 0.0 & 0.0 \\\
0.0 & 0.0 & 0.0 & 0.0 & 0.0 & 0.0 \\\
69.0 & 1.0 & 0.0 & 0.0 & 0.0 & 0.0 \\\
7.0 & 0.0 & 0.0 & 0.0 & 0.0 & 0.0 \\\
0.0 & 0.0 & 0.0 & 0.0 & 0.0 & 0.0 \\\
0.0 & 1.0 & 0.0 & 0.0 & 0.0 & 0.0 \\\
0.0 & 0.0 & 0.0 & 0.0 & 0.0 & 0.0 \\
\end{bmatrix} $

Valor objetivo ótimo: $4358.7834$

**c)** Agora, a empresa RentalBike deseja avaliar o impacto na função objetivo ao utilizar um caminhão com capacidade variada. Variando a capacidade de $T$ de $100$ até $4000$, com incrementos de $100$ (ou seja, $T= [100, 200, 300, ..., 3900, 4000]$. Execute novamente seu modelo de otimização para cada um desses parâmetros. Plote um gráfico com os valores ótimos da função objetivo obtidos para cada valor de $T$. O gráfico deve mostrar a capacidade no eixo $x$ e os valores da função objetivo no eixo $y$.

![capacity](data/results/truck_capacity.png)

### 2. Resolvendo com algoritmos:

**a)** Voltando à tarefa 1, imagine o mesmo problema, mas sem as restrições referentes à capacidade do caminhão. Ao fazer isso, a otimização pode assumir que o caminhão tem capacidade ilimitada e ignorar a verificação disso. Sabendo disso, implemente um algoritmo que encontre uma boa solução para este problema. É preferível (mas não obrigatório) que seu algoritmo sempre encontre uma solução ótima, tendo o menor tempo e complexidade de espaço possível. Mostre seu código, a melhor solução encontrada e seu valor objetivo.

### 3 . Indo além na tarefa 2 (problema sem a restrição de capacidade).

### 4 . Indo mais além no negócio.