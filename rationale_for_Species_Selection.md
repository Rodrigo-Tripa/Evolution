# Rationale for Species Selection

## 1. Selected Species

The reference organism selected for the Genome Evolution Lab is *Drosophila melanogaster*, commonly known as the fruit fly.

This species was selected because it provides a scientifically relevant and computationally manageable biological model for studying genetic variation, phenotypic expression, environmental adaptation, and population evolution across multiple generations.

The objective is not to reproduce every biological mechanism of the species. Instead, *Drosophila melanogaster* will serve as a biological reference for constructing a simplified, evidence-based computational model.

## 2. Scientific Justification

### 2.1. Extensive Genetic Research

*Drosophila melanogaster* is one of the most extensively studied model organisms in genetics and molecular biology. More than a century of research has produced substantial knowledge about its genome, inheritance mechanisms, gene expression, development, and phenotypic variation.

Its genome has been sequenced and extensively annotated, and numerous genetic databases and scientific publications are available. This provides a foundation for identifying real genes, investigating their biological functions, and establishing evidence-based relationships between genetic variation and phenotypic characteristics.

This is particularly important for the Genome Evolution Lab because the genetic architecture of the simulated organisms should be based on documented biological mechanisms rather than arbitrary genetic variables.

### 2.2. Short Generation Time

One of the most important advantages of *Drosophila melanogaster* is its relatively short life cycle.

Under laboratory conditions at approximately 25 °C, development from fertilized egg to adult typically takes around 9–10 days. The exact duration depends on environmental conditions, particularly temperature.

This characteristic makes the species particularly suitable for studying evolutionary processes across multiple generations. It also provides a useful biological reference for investigating how environmental conditions influence development and reproductive timing.

For the computational model, a short generation time is relevant because it allows evolutionary processes to be represented and analysed across large numbers of generations without requiring unrealistic assumptions about the organism's reproductive biology.

### 2.3. High Reproductive Capacity

Female fruit flies can produce large numbers of offspring, allowing populations to grow rapidly under suitable conditions.

This reproductive capacity is relevant to the study of population dynamics, genetic transmission, allele-frequency changes, competition, and natural selection.

It also provides a useful biological basis for investigating how differences in reproductive success can influence the genetic composition of subsequent generations.

### 2.4. Observable Phenotypic Variation

*Drosophila melanogaster* exhibits a variety of observable and measurable characteristics, including:

- Body size and morphology.
- Wing structure and dimensions.
- Eye pigmentation.
- Body pigmentation.
- Locomotor behaviour.
- Developmental timing.
- Reproductive characteristics.
- Physiological responses to environmental stress.

These characteristics provide potential starting points for modelling the relationship between genotype and phenotype.

Importantly, these traits should not automatically be represented as characteristics controlled by individual genes. Many biological traits are polygenic and may also be influenced by environmental conditions and interactions between genes.

### 2.5. Environmental Adaptation

*Drosophila melanogaster* has a broad geographical distribution and has been extensively studied in the context of environmental adaptation.

Temperature is particularly relevant because it influences several biological processes, including development, metabolism, survival, and reproduction.

Research involving natural and experimental populations has investigated how environmental conditions influence phenotypic variation and evolutionary responses.

This makes the species appropriate for the project's initial research direction: investigating how environmental variation, particularly temperature, can influence survival, reproductive success, and genetic composition across generations.

### 2.6. Computational and Experimental Suitability

The relatively small size of the organism, its short generation time, high reproductive capacity, and extensive scientific documentation make it a practical reference for computational modelling.

Its biology is sufficiently complex to support the study of interactions between genetics, physiology, behaviour, reproduction, and environmental conditions.

At the same time, its extensive research history reduces the difficulty of finding scientific references for the mechanisms represented in the simulator.

The availability of genetic databases, including FlyBase, also provides access to information about genes, alleles, genetic interactions, and phenotypic effects.

## 3. Relevance to the Genome Evolution Lab

The selection of *Drosophila melanogaster* is compatible with the main conceptual structure of the project:

**Genome → Genotype → Phenotype → Environment → Fitness → Survival → Reproduction → Next Generation**

Its biological characteristics provide a foundation for investigating several functional areas:

| Functional area | Potential characteristics |
|---|---|
| Morphology | Body size, wing morphology, pigmentation |
| Nervous system | Sensory processing, learning and memory |
| Behaviour | Locomotion, exploration, stimulus responses |
| Metabolism and physiology | Energy utilization, growth and physiological reserves |
| Reproduction and development | Fertility, maturation and developmental duration |
| Resistance and adaptation | Thermal tolerance and stress responses |

These categories are intended to organize the model's functional characteristics. They do not represent independent genetic systems. A single gene may influence multiple characteristics, while a single phenotype may depend on several genes and environmental factors.

The species therefore provides an appropriate biological reference for progressively investigating these relationships.

## 4. Limitations of the Selected Species

Despite its advantages, *Drosophila melanogaster* is not a universal representation of animal biology.

It is an insect, and its anatomy, physiology, development, and ecological interactions differ substantially from those of vertebrates and other animal groups.

Several limitations must therefore be considered:

- **Biological specificity:** Mechanisms observed in fruit flies cannot automatically be generalized to other species.
- **Genetic complexity:** Many traits involve multiple genes, regulatory mechanisms, and interactions that cannot be represented accurately through simple genetic models.
- **Environmental complexity:** Laboratory conditions do not reproduce the full complexity of natural ecosystems.
- **Phenotypic plasticity:** Environmental conditions can influence phenotypic characteristics independently of changes in allele frequencies.
- **Developmental differences:** The organism passes through distinct developmental stages, which may respond differently to environmental conditions.
- **Model simplification:** The computational representation will necessarily omit many biological mechanisms.

Consequently, the simulator should not be interpreted as a complete representation of the real evolutionary biology of *Drosophila melanogaster*.

Its purpose is to model selected evolutionary mechanisms under explicitly defined assumptions.

## 5. Alternative Species Considered

Other organisms could also serve as references for an evolutionary simulation.

| Species | Potential advantages | Main limitations for this project |
|---|---|---|
| *Caenorhabditis elegans* | Short generation time, extensive genetic research | Its anatomy and behavioural complexity are more limited for the intended animal model |
| *Mus musculus* | Mammalian physiology and extensive genetic research | Longer generation time, higher maintenance requirements and greater experimental complexity |
| *Danio rerio* | Vertebrate development and observable physiology | More demanding biological and computational modelling |
| *Drosophila melanogaster* | Short generation time, extensive genetic knowledge, observable traits and high reproductive capacity | Insect-specific biology and substantial genetic complexity |

The alternatives are scientifically valid model organisms. However, *Drosophila melanogaster* offers a particularly useful balance between biological complexity, available scientific knowledge, and practical suitability for studying evolution across many generations.

## 6. Final Justification

*Drosophila melanogaster* was selected because it combines several characteristics that are particularly relevant to the objectives of the Genome Evolution Lab:

1. Extensive scientific knowledge about its genetics and biology.
2. A relatively short generation time.
3. High reproductive capacity.
4. Observable and measurable phenotypic characteristics.
5. Extensive research into environmental adaptation.
6. Availability of genetic databases and scientific literature.
7. Suitability for studying population evolution across multiple generations.

The species provides a sufficiently complex biological reference without introducing the experimental and computational difficulties associated with modelling larger and more biologically demanding organisms.

The choice is therefore based on scientific relevance, available evidence, and practical suitability rather than on the assumption that *Drosophila melanogaster* is a biologically simple organism.

It will serve as the initial reference species for the project. The model may be revised as the scientific scope and understanding of the biological mechanisms improve.

## 7. Scientific References

1. Hales, K. G., et al. (2015). **Genetics on the Fly: A Primer on the Drosophila Model System.** *Genetics*, 201(3), 815–842.  
   https://doi.org/10.1534/genetics.115.183392

2. Flatt, T. (2020). **Life-History Evolution and the Genetics of Fitness Components in Drosophila melanogaster.** *Genetics*, 214(1), 3–48.  
   https://doi.org/10.1534/genetics.119.300160

3. Tobler, R., Hermisson, J., & Schlötterer, C. (2015). **Parallel trait adaptation across opposing thermal environments in experimental Drosophila melanogaster populations.** *Evolution*, 69(7), 1745–1759.  
   https://doi.org/10.1111/evo.12705

4. Bogaerts-Márquez, M., et al. (2021). **Temperature, rainfall and wind variables underlie environmental adaptation in natural populations of Drosophila melanogaster.** *Molecular Ecology*, 30(4), 938–954.  
   https://doi.org/10.1111/mec.15783

5. Huang, W., et al. (2020). **Genotype by environment interaction for gene expression in Drosophila melanogaster.** *Nature Communications*, 11, 5451.  
   https://doi.org/10.1038/s41467-020-19131-y

## 8. Biological Databases

- **FlyBase:** https://flybase.org/
- **NCBI:** https://www.ncbi.nlm.nih.gov/
- **Ensembl:** https://www.ensembl.org/
- **PubMed:** https://pubmed.ncbi.nlm.nih.gov/

---

**Document:** Species Selection Rationale  
**Project:** Genome Evolution Lab  
**Reference organism:** *Drosophila melanogaster*  
**Status:** Initial scientific justification