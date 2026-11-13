# Genome Model

## 1. Purpose

This document establishes the conceptual framework for representing the genome of an individual organism in the Genome Evolution Lab.

The genome model is one of the foundations of the simulator. It must support the representation of genetic variation, inheritance, mutation, recombination and the transmission of genetic information across generations.

The objective is not to reproduce the complete molecular complexity of the *Drosophila melanogaster* genome. Instead, the project aims to develop a scientifically grounded and computationally manageable representation that can be progressively expanded as the biological model becomes more detailed.

This document defines the general principles of the genome representation. Specific mechanisms, data structures and implementation details will be addressed in separate documents.

## 2. Biological Foundation

### 2.1. The Genome

The genome is the complete set of genetic information contained in an organism's genetic material.

In *Drosophila melanogaster*, the nuclear genome is organised into chromosomes, which contain DNA molecules carrying genes and other genomic regions.

The genome contains information involved in cellular processes, development, physiological functions and other biological characteristics.

For the purposes of this project, the genome will be treated as the primary source of inherited genetic information within each simulated individual.

### 2.2. Chromosomes

Chromosomes are organised structures of DNA and associated proteins that carry genetic information.

In diploid organisms, chromosomes are generally organised into homologous pairs. Each homologous chromosome contains corresponding genetic regions, although the DNA sequences at those regions may differ.

This distinction is fundamental to the simulation because an individual may carry different variants at corresponding positions on its homologous chromosomes.

The detailed representation of chromosomes, their organisation and their genetic positions will be defined in `chromosomal-architecture.md`.

### 2.3. Genes, Loci and Alleles

A gene is a region of DNA associated with a functional product or biological process.

A locus refers to a specific position or region within the genome. Different versions of a genetic sequence at the same locus are known as alleles.

A locus may contain multiple possible alleles within a population. Consequently, genetic variation does not necessarily consist of only two alternative forms.

For this project, it is important to distinguish between:

- **Gene:** a functional genetic region.
- **Locus:** a genomic position or region.
- **Allele:** a particular version of a genetic sequence.
- **Variant:** a difference in DNA sequence relative to a reference or another sequence.

These terms are related but are not interchangeable.

## 3. Diploid Genome Representation

*Drosophila melanogaster* is a diploid organism in its typical somatic cells. Therefore, its nuclear genetic information is represented by two chromosome sets.

For a given autosomal locus, an individual generally carries two allelic copies, one inherited from each parent.

The combination of these copies constitutes the individual's genotype at that locus.

For example, if a locus has two possible alleles, it could produce the following genotypes:

```text
AA
Aa
aa
```

This notation is only an illustrative example. It does not imply that the project will use artificial binary alleles or that every locus has exactly two possible variants.

The final model should represent alleles using identifiers that correspond to documented biological variants whenever sufficient evidence is available.

Sex chromosomes require separate consideration because their inheritance and genomic composition differ between males and females. Their representation must be addressed in the chromosomal and inheritance models rather than assumed to follow the same rules as autosomal loci.

## 4. Genotype and Genetic Information

The genotype describes the genetic constitution of an individual with respect to the loci being considered.

It is important to distinguish the genotype from the phenotype. The genotype represents inherited genetic information, whereas the phenotype represents characteristics resulting from genetic, environmental and other biological influences.

The conceptual relationship can be represented as:

```text
             GENOME
                |
                v
             GENOTYPE
                |
                v
       Genetic Information
                |
                v
      Genotype-Phenotype Model
                |
                v
             PHENOTYPE
```

This representation is intentionally simplified. The relationship between genotype and phenotype is not necessarily direct or deterministic.

A single genetic variant may influence several characteristics, while a single characteristic may depend on multiple genes and environmental conditions.

The detailed relationship between genetic variants and phenotypic traits will be defined in `genotype-phenotype-model.md`.

## 5. Genetic Variation

Genetic variation refers to differences in DNA sequences between individuals within a population.

Such variation is essential for evolutionary processes because inherited differences can influence phenotypic variation and, consequently, differences in survival and reproductive success.

For this project, genetic variation should be represented through biologically documented variants whenever reliable data are available.

The model should not assume that every variant has a known phenotypic effect. A variant may be documented without having a clearly established functional consequence.

It is therefore necessary to distinguish between:

- Variants identified in genomic data.
- Variants statistically associated with a phenotype.
- Variants with experimentally supported functional effects.
- Variants with demonstrated causal effects on a particular phenotype.

These categories represent different levels of scientific evidence and must not be treated as equivalent.

## 6. Genetic Information and Phenotypic Information

The genome and phenotype must remain conceptually separate within the simulator.

The genome contains inherited genetic information. Phenotypic characteristics are derived through biological relationships involving that information and the conditions under which the organism develops.

For example, body size should not be treated as an independent genetic value stored directly in the genome. Instead, it should be represented as a phenotypic outcome influenced by genetic variation and environmental conditions.

A simplified conceptual relationship is:

```text
             GENOTYPE
                 |
                 |
                 v
        Genetic Contributions
                 |
                 |
ENVIRONMENT ---> PHENOTYPE
```

The model must allow individuals with similar genotypes to exhibit different phenotypes under different environmental conditions, where biologically justified.

Likewise, individuals with different genotypes may exhibit similar phenotypes.

This separation is necessary to study genotype-environment interactions and phenotypic variation across generations.

## 7. Genome Inheritance

Genetic information is transmitted from parents to offspring through reproduction.

In diploid organisms, offspring inherit genetic material from both parents. The resulting genome is therefore a combination of inherited genetic information.

However, inheritance is not simply the transfer of complete parental chromosomes without modification. During gamete formation, genetic recombination can generate new combinations of alleles.

The inheritance model must therefore account for:

- The transmission of alleles from parents to offspring.
- The contribution of both parental genomes.
- The formation of gametes.
- Chromosomal recombination.
- The possibility of new mutations.

The precise mechanisms and assumptions will be established in `inheritance-model.md`, `recombination-model.md` and `mutation-model.md`.

## 8. Modelling Principles

The genome representation should follow several principles.

### 8.1. Biological Grounding

Whenever possible, genetic information should correspond to documented biological variants in *Drosophila melanogaster*.

Artificial alleles with arbitrary phenotypic effects should not be presented as real biological variants.

If simplified or hypothetical genetic representations become necessary for testing specific mechanisms, they must be explicitly identified as model abstractions.

### 8.2. Separation of Genetic and Phenotypic Data

Genetic information must be stored independently from phenotypic characteristics derived from it.

This separation prevents the simulator from treating phenotypic values as if they were directly inherited genetic information.

### 8.3. Explicit Assumptions

Every simplification must be documented.

The model should distinguish between established biological facts, modelling decisions, assumptions and unresolved questions.

### 8.4. Expandability

The genome model should allow additional loci, alleles and chromosomes to be incorporated without requiring a complete redesign of the conceptual framework.

However, expandability must not justify unnecessary complexity. The number of represented variants should be determined by scientific relevance and available evidence.

### 8.5. Computational Efficiency

The representation should avoid unnecessary duplication of genetic information.

The simulator may eventually need to represent very large populations over thousands or millions of generations. Therefore, memory usage and computational cost must be considered from the beginning.

The appropriate data representation will be evaluated separately from the biological model.

## 9. Current Modelling Decisions

The following decisions establish the initial direction of the project.

| Subject | Current direction |
|---|---|
| Reference organism | *Drosophila melanogaster* |
| Genome type | Diploid nuclear genome |
| Genetic representation | Based on real biological variants where evidence is available |
| Allele representation | Identifiable variants rather than arbitrary A/a effects |
| Genetic variation | Multiple possible alleles and variants |
| Phenotype | Derived from genotype and environmental influences |
| Inheritance | Biparental inheritance |
| Recombination | To be modelled explicitly |
| Mutation | To be modelled explicitly |
| Genotype-phenotype relationship | Evidence-based where possible; assumptions documented |

These decisions establish the conceptual direction, not a complete biological specification. Some details remain unresolved and must be investigated before implementation.

## 10. Limitations and Unresolved Questions

Several aspects of the genome model require further investigation.

1. Which chromosomes and genomic regions should initially be represented?
2. Which biological variants have sufficiently reliable evidence to be included?
3. Which reference genome assembly should be used to identify genomic positions?
4. How should multiple alleles at the same locus be represented?
5. How should sex chromosomes and sex-specific inheritance be handled?
6. How much chromosomal linkage and recombination detail is computationally necessary?
7. How should variants with unknown or uncertain phenotypic effects be treated?
8. How should the model represent missing or incomplete genetic information?

These questions should not be resolved through arbitrary implementation decisions. They require biological evidence, explicit modelling assumptions or controlled simplifications.

## 11. Relationship with Other Documents

This document establishes the conceptual foundation for the following architecture documents:

- `chromosomal-architecture.md` — chromosome organisation, genomic positions and linkage.
- `variant-model.md` — representation and classification of genetic variants.
- `inheritance-model.md` — transmission of genetic information between generations.
- `recombination-model.md` — chromosomal recombination and allele combinations.
- `mutation-model.md` — introduction of new genetic variation.
- `genotype-phenotype-model.md` — relationship between genetic information and phenotypic characteristics.
- `model-assumptions.md` — explicit assumptions, simplifications and limitations.

These documents should remain consistent with the principles established here.

## 12. Final Considerations

The genome model is a foundational component of the Genome Evolution Lab.

Its purpose is to provide a structured and biologically meaningful representation of inherited genetic variation, allowing the simulator to investigate how genetic differences are transmitted and how they may influence phenotypic characteristics across generations.

The model must remain sufficiently simple to be computationally manageable while retaining the biological mechanisms necessary for the scientific questions being investigated.

The objective is not to simulate every molecular process occurring within a real organism. It is to construct a transparent, quantitative and scientifically defensible model whose assumptions and limitations are explicitly documented.