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

**a**. Escreva uma formulação matemática para resolver este problema de otimização, considerando que a capacidade total de espaço do caminhão é representada por uma constante $T$. **Defina as constantes e variáveis**, e descreva as **restrições e a função objetivo** para maximizar a soma dos lucros esperados.

### 2 .

### 3 .

### 4 .