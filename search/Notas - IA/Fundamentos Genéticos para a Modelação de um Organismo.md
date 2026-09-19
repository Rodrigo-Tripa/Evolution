# Fundamentos Genéticos para a Modelação de um Organismo

## 1. Gene

Um **gene** pode ser definido, de forma simplificada, como uma região do DNA que contém informação funcional e que contribui para a determinação de características ou processos biológicos. A expressão genética ocorre através de mecanismos moleculares que permitem que a informação contida no DNA influencie a atividade celular e, consequentemente, o fenótipo do organismo.

Para efeitos de modelação computacional, um gene pode ser tratado como uma unidade de informação genética associada a uma determinada função ou característica. Esta representação constitui uma simplificação deliberada da realidade biológica, uma vez que muitas características resultam da interação entre múltiplos genes e entre fatores genéticos e ambientais.

---

## 2. Alelo

Um **alelo** corresponde a uma variante de um determinado gene. Diferentes alelos podem apresentar sequências de DNA distintas e, em determinadas circunstâncias, contribuir para diferenças fenotípicas entre indivíduos.

Por exemplo, considerando um gene hipotético associado ao tamanho corporal, podem existir dois alelos, representados abstratamente por `A` e `a`.

```text
Gene: tamanho corporal

Alelos:
A
a
```

A existência de múltiplos alelos constitui uma fonte fundamental de **variabilidade genética** numa população. Essa variabilidade é essencial para compreender processos evolutivos, uma vez que alterações nas frequências das variantes genéticas podem ocorrer ao longo das gerações.

---

## 3. Genótipo

O **genótipo** corresponde à constituição genética de um indivíduo relativamente aos loci considerados. Num organismo diploide, cada locus possui, em condições simplificadas, duas cópias, geralmente uma de origem materna e outra de origem paterna.

Considerando dois alelos possíveis, `A` e `a`, podem existir três combinações genotípicas:

```text
AA
Aa
aa
```

O genótipo constitui, portanto, a informação genética subjacente ao indivíduo. No contexto do projeto, esta distinção é particularmente importante porque o simulador deverá ser capaz de representar informação genética independentemente das características fenotípicas que dela resultam.

---

## 4. Fenótipo

O **fenótipo** corresponde ao conjunto de características observáveis ou funcionalmente relevantes de um organismo, resultantes da interação entre a sua constituição genética e as condições ambientais.

Uma representação conceptual simplificada pode ser expressa por:

```text
Genótipo + Ambiente → Fenótipo
```

Esta relação não deve ser interpretada como uma função exclusivamente determinística. Dependendo da característica considerada, podem existir efeitos genéticos complexos, interações entre genes, efeitos ambientais e componentes estocásticas.

Por exemplo, dois indivíduos geneticamente semelhantes podem apresentar diferenças fenotípicas se forem submetidos a condições ambientais distintas durante o desenvolvimento.

Para o simulador, esta distinção permite separar o **estado genético** do indivíduo das **características derivadas** desse estado. Assim, uma característica como o tamanho corporal pode ser modelada como uma propriedade resultante do genótipo e, eventualmente, de fatores ambientais, em vez de ser armazenada como informação genética independente.

---

## 5. Homozigotia e Heterozigotia

Quando um indivíduo diploide possui dois alelos iguais num determinado locus, diz-se que é **homozigótico** para esse locus. Quando possui dois alelos diferentes, é **heterozigótico**.

Assim:

```text
AA → homozigótico
Aa → heterozigótico
aa → homozigótico
```

Esta distinção é relevante porque a combinação de alelos pode influenciar a expressão fenotípica de uma característica.

Em modelos genéticos introdutórios, pode assumir-se que um alelo apresenta **dominância** relativamente a outro. Nesse caso, indivíduos com genótipos `AA` e `Aa` podem apresentar o mesmo fenótipo para a característica considerada, apesar de possuírem genótipos diferentes.

Contudo, esta representação constitui uma simplificação. Na biologia real existem mecanismos como dominância incompleta, codominância, múltiplos alelos e características determinadas pela ação conjunta de vários loci. Consequentemente, qualquer mecanismo de dominância implementado no simulador deverá ser entendido como uma hipótese específica do modelo e não como uma propriedade universal da hereditariedade.

---

## 6. Relação entre Genótipo e Fenótipo

A relação entre genótipo e fenótipo constitui uma das bases conceptuais da modelação evolutiva.

De forma simplificada:

```text
Genoma
   ↓
Genótipo
   ↓
Expressão das características
   ↓
Fenótipo
```

Contudo, uma representação mais adequada é:

```text
Genótipo + Ambiente
        ↓
     Fenótipo
```

O fenótipo não deve, portanto, ser considerado uma simples cópia do genótipo. A constituição genética estabelece determinadas possibilidades e predisposições, enquanto o ambiente pode modificar a expressão dessas características.

Para o projeto, esta separação permite estabelecer uma arquitetura conceptual na qual o genoma funciona como fonte de informação genética, enquanto o fenótipo constitui um conjunto de propriedades derivadas utilizadas posteriormente na interação com o ambiente.

---

## 7. Herdabilidade

Uma característica apresenta uma componente **herdável** quando parte da variação observada nessa característica está associada a diferenças genéticas transmissíveis entre gerações.

Este conceito é particularmente importante em evolução. Se indivíduos diferirem numa determinada característica e parte dessa diferença tiver uma base genética transmissível, então alterações nas frequências das variantes genéticas podem conduzir a alterações sistemáticas na distribuição da característica ao longo das gerações.

É importante distinguir herdabilidade de uma afirmação mais forte segundo a qual uma característica seria exclusivamente determinada pelos genes. Uma característica pode apresentar uma componente genética significativa e, simultaneamente, ser fortemente influenciada pelo ambiente.

---

## 8. Da Genética Individual à Evolução Populacional

Os conceitos anteriores descrevem principalmente o indivíduo. A evolução, contudo, é um fenómeno que se manifesta ao nível das **populações ao longo das gerações**.

Uma sequência conceptual simplificada é:

```text
Variação genética
       ↓
Variação fenotípica
       ↓
Diferenças na sobrevivência e/ou reprodução
       ↓
Transmissão diferencial de variantes genéticas
       ↓
Alteração das frequências alélicas
       ↓
Mudança da população ao longo das gerações
```

Assim, um indivíduo não constitui, por si só, uma unidade evolutiva completa. O indivíduo possui um determinado genótipo e fenótipo; a evolução manifesta-se quando a composição genética da população se altera através das gerações.

Esta distinção será fundamental para o desenvolvimento posterior do simulador. A primeira etapa pode consistir na representação de um único organismo, mas o objetivo evolutivo final exige a introdução de múltiplos indivíduos, reprodução, transmissão genética, mutação, seleção e dinâmica populacional.

---

## 9. Implicações para o Modelo Computacional

A partir destes conceitos pode estabelecer-se uma arquitetura conceptual inicial:

```text
        GENOMA
           ↓
        GENÓTIPO
           ↓
    ┌──────┴──────┐
    ↓             ↓
Características   Outros
 fenotípicas     atributos
    ↓
 AMBIENTE
    ↓
 Desempenho /
 Interação
```

Nesta fase inicial, o objetivo não deverá ser reproduzir toda a complexidade genética conhecida. O propósito é construir uma representação suficientemente simples para ser compreendida, testada e posteriormente expandida.

Uma implementação cientificamente coerente deverá distinguir explicitamente entre aquilo que constitui **facto biológico estabelecido** e aquilo que constitui **pressuposto do modelo**. Por exemplo, a existência de genes e alelos é um conceito biológico estabelecido, enquanto a decisão de representar uma determinada característica através de um único gene é uma simplificação do modelo.

Consequentemente, o desenvolvimento deverá proceder de forma incremental: primeiro representar corretamente um organismo individual, depois estabelecer uma relação controlada entre genótipo e fenótipo e, apenas posteriormente, introduzir reprodução, mutação, seleção e dinâmica populacional.

O objetivo não é reproduzir computacionalmente toda a complexidade de um organismo real, mas construir um modelo explícito, quantitativo e experimentalmente analisável dos mecanismos selecionados.