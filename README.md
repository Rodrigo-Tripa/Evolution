# Evolution

A simple computational model of genetic inheritance and population evolution written in Python.

The simulation represents a population of individuals with diploid genomes, where each genome contains two alleles:

\[
G \in \{AA,\ Aa,\ aa\}
\]

Each genotype produces a phenotype with a genotype-dependent expected value and stochastic variation.

## Model

The current model uses a single gene with two alleles:

- `A` — dominant allele
- `a` — recessive allele

The expected phenotype is determined by genotype:

\[
\mu(AA)=80
\]

\[
\mu(Aa)=65
\]

\[
\mu(aa)=50
\]

Individual phenotype values are sampled from a Gaussian distribution:

\[
H \sim \mathcal{N}(\mu_g, 4^2)
\]

where \(H\) is the individual's height and \(\mu_g\) is the expected value associated with its genotype.

## Reproduction

Two individuals are randomly selected from the population.

Each parent contributes one randomly selected allele to the offspring:

\[
G_{offspring} =
(A_{parent_1}, A_{parent_2})
\]

After inheritance, each allele has a mutation probability of:

\[
\mu = 0.1
\]

A mutation changes the allele:

\[
A \leftrightarrow a
\]

The resulting genotype determines the offspring's phenotype.

## Population Genetics

For a population of \(N\) individuals, the simulator calculates genotype frequencies:

\[
f(AA)=\frac{N_{AA}}{N}
\]

\[
f(Aa)=\frac{N_{Aa}}{N}
\]

\[
f(aa)=\frac{N_{aa}}{N}
\]

Allele frequencies are calculated as:

\[
p(A)=\frac{2N_{AA}+N_{Aa}}{2N}
\]

\[
q(a)=\frac{N_{Aa}+2N_{aa}}{2N}
\]

Therefore:

\[
p+q=1
\]

The simulation also tracks the mean phenotype of the complete population and the mean phenotype for each genotype.

## Structure

```text
Evolution/
├── src/
│   ├── agent.py
│   └── simulation.py
└── README.md
```

`agent.py` contains the individual-level model:

- `Genome` — represents the two alleles and mutation.
- `Phenotype` — generates the phenotype from the genotype.
- `Agent` — represents an individual and handles reproduction.

`simulation.py` contains the population-level model:

- `Population` — manages individuals and population statistics.
- `Simulation` — controls the generational process.

## Running

Run the simulation from the project root:

```bash
python src/simulation.py
```

The default configuration creates a population of 1,000 individuals and simulates 20 generations.

Example output:

```text
Initial population:
  Genotypes: (160, 520, 320)
  Genotype frequencies: {'AA': 0.16, 'Aa': 0.52, 'aa': 0.32}
  Allele frequencies: {'A': 0.42, 'a': 0.58}

Generation 1: 1000 agents
  Genotypes: (...)
  Alleles: (...)
  Height: mean=...
  Height by genotype: AA=..., Aa=..., aa=...
```

Because reproduction, mutation, and phenotype generation are stochastic, each execution can produce a different result.

## Scope

This is a simplified computational model intended to explore the relationship between:

\[
\text{Genotype}
\rightarrow
\text{Inheritance}
\rightarrow
\text{Mutation}
\rightarrow
\text{Phenotype}
\rightarrow
\text{Population dynamics}
\]

The model is not intended to accurately represent human genetics. Human height is a complex polygenic trait influenced by many genetic and environmental factors; the single-locus model used here is an abstraction for studying inheritance and population-level behaviour.