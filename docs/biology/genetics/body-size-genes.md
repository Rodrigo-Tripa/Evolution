# Body Size Genes — Genetic Regulation of Body Growth

**Project:** Genome Evolution Lab  
**Species:** *Drosophila melanogaster*  
**Functional group:** G1 — Morphology and Body Structure  
**Status:** Initial scientific research  
**Document type:** Genetic reference and candidate gene catalogue

---

## 1. Introduction

Body size in *Drosophila melanogaster* is a complex quantitative phenotype influenced by multiple genes, molecular signalling pathways and environmental conditions.

There is no single gene responsible for determining the complete body size of an individual. Instead, body growth emerges from the interaction of biological mechanisms that regulate cellular growth, cell proliferation, nutrient utilization, developmental timing and tissue differentiation.

A particularly important distinction is that some genes regulate **systemic growth**, influencing the size of the organism as a whole, whereas others regulate **local tissue growth**, influencing the dimensions of specific organs or anatomical structures.

This distinction is essential for the Genome Evolution Lab because an alteration in the size of an individual organ does not necessarily produce an equivalent alteration in total body size.

The purpose of this document is to identify and characterize genes and molecular pathways with experimental evidence linking them to growth regulation in *Drosophila melanogaster*.

The catalogue is not intended to represent every gene involved in body-size determination. It focuses on pathways with established biological importance and genes that may eventually contribute to a simplified genetic model.

## 2. Genetic Architecture of Body Size

### 2.1. A quantitative genetic trait

Body size is considered a quantitative trait because it generally exhibits continuous variation rather than a small number of clearly separated phenotypic categories.

For example, individuals from the same population may differ in thorax length, body mass or wing dimensions without belonging to distinct morphological classes.

This variation can result from:

- Differences in the alleles inherited by each individual.
- Interactions between multiple genes.
- Differences in gene expression.
- Environmental conditions during development.
- Interactions between genotype and environment.
- Developmental and physiological variation.

Consequently, the relationship between genotype and body size should be represented as a complex biological process rather than a direct association between one gene and one physical measurement.

### 2.2. Systemic growth and local tissue growth

Two levels of growth regulation must be distinguished.

**Systemic growth** concerns mechanisms that influence the growth of the organism as a whole. These mechanisms include nutrient sensing, insulin signalling, metabolic regulation and the hormonal control of developmental timing.

**Local tissue growth** concerns mechanisms that regulate the dimensions of particular organs or tissues. These mechanisms include the control of cellular proliferation, cell death and tissue-specific growth.

The insulin/insulin-like signalling pathway and TOR pathway are particularly important for systemic and nutrient-dependent growth.

The Hippo pathway is particularly important for local tissue and organ-size regulation, although it can also influence systemic growth through interactions with hormonal signalling.

The ecdysone system regulates developmental transitions and contributes to determining how long larval growth can continue.

These systems are interconnected and should not be treated as completely independent mechanisms.

### 2.3. Evidence classification

The genes included in this document are classified according to the type of scientific evidence available.

**Class A — Direct experimental evidence**

Genetic manipulation, such as gene deletion, mutation, overexpression or tissue-specific gene suppression, has produced measurable changes in growth, body size or organ size.

**Class B — Mechanistic evidence**

The gene participates in a molecular pathway with a demonstrated role in growth regulation, but its individual contribution to whole-body size may depend on tissue, developmental stage or experimental conditions.

**Class C — Natural variation evidence**

Genetic variation at the locus has been associated with morphological differences between naturally occurring populations or strains.

These classifications are not measures of scientific importance. They describe the nature of the evidence supporting the relationship between a gene and body size.

A gene may have strong experimental evidence for its role in growth while having insufficient evidence that naturally occurring alleles at that locus explain body-size variation in wild populations.

---

## 3. Insulin/Insulin-like Signalling Pathway

### 3.1. General function

The insulin/insulin-like signalling pathway, commonly abbreviated as IIS, is one of the principal regulators of growth in *Drosophila melanogaster*.

It connects nutritional and physiological information to cellular processes responsible for growth and metabolism.

Insulin-like peptides produced by specialized cells activate the insulin receptor, initiating intracellular signalling cascades.

These signals influence processes such as protein synthesis, cellular growth, cell proliferation and metabolic regulation.

The pathway is therefore particularly important during larval development, when the organism undergoes substantial growth.

Experimental studies have demonstrated that changes in insulin signalling can produce considerable differences in organismal size.

### 3.2. Candidate genes

#### 3.2.1. `InR`

**Official symbol:** `InR`  
**Gene name:** Insulin-like receptor  
**Pathway:** Insulin/insulin-like signalling  
**Evidence classification:** Class A

**Molecular function**

`InR` encodes the insulin-like receptor, a transmembrane receptor tyrosine kinase.

When activated by insulin-like peptides, the receptor initiates intracellular signalling events that regulate cellular metabolism and growth.

**Evidence related to body size**

Experimental manipulation of the Drosophila insulin receptor has demonstrated that its activity influences organ growth through changes in cell size and cell number.

Reduced insulin receptor activity can result in substantial growth impairment.

**Importance for the model**

`InR` is a strong candidate for representing the connection between nutritional signalling and growth.

However, the effect of an allele cannot be assumed to be a simple fixed percentage change in body size.

The magnitude of its effect may depend on developmental stage, tissue and environmental conditions.

#### 3.2.2. `chico`

**Official symbol:** `chico`  
**Gene name:** Chico  
**Protein function:** Insulin receptor substrate  
**Pathway:** Insulin/insulin-like signalling  
**Evidence classification:** Class A

**Molecular function**

`chico` encodes an intracellular adaptor protein that participates in insulin receptor signalling.

It is functionally related to insulin receptor substrate proteins found in other organisms.

The protein contributes to the transmission of signals from the insulin receptor to downstream signalling components.

**Evidence related to body size**

Böhni et al. (1999) demonstrated that mutations in `chico` produce significantly smaller flies.

The observed phenotype resulted from reductions in both cell size and cell number.

The study also showed that the effects of `chico` mutations could be observed at the cellular and organ levels.

This provides strong experimental evidence that `chico` participates in the regulation of organismal growth.

**Importance for the model**

`chico` is one of the strongest candidates for an initial simplified representation of genetic variation affecting growth.

Nevertheless, the severe phenotypes associated with some experimental mutations should not be interpreted as representative of ordinary natural genetic variation.

#### 3.2.3. `Pi3K92E`

**Official symbol:** `Pi3K92E`  
**Gene name:** Phosphatidylinositol 3-kinase 92E  
**Pathway:** Insulin/insulin-like signalling  
**Evidence classification:** Class A/B

**Molecular function**

`Pi3K92E` encodes the catalytic subunit of class I phosphatidylinositol 3-kinase.

This enzyme participates in the intracellular transmission of insulin receptor signals.

It contributes to the production of phosphatidylinositol-3,4,5-trisphosphate, a lipid signalling molecule involved in the recruitment and activation of downstream signalling proteins.

**Evidence related to body size**

The PI3K pathway is an important component of insulin-dependent growth regulation.

Experimental alterations in PI3K activity can affect cellular growth, tissue dimensions and organismal size.

**Importance for the model**

This gene is a possible candidate for representing an intermediate stage of insulin-dependent growth signalling.

However, its inclusion may be unnecessary in the earliest version of the simulator if `InR` and `chico` already represent the principal biological mechanism being investigated.

#### 3.2.4. `Akt1`

**Official symbol:** `Akt1`  
**Gene name:** Protein kinase B  
**Pathway:** Insulin/insulin-like signalling  
**Evidence classification:** Class A/B

**Molecular function**

`Akt1` encodes a serine/threonine protein kinase that acts downstream of PI3K.

It participates in the regulation of cellular growth, metabolism and survival.

One of its important functions is to regulate downstream targets involved in protein synthesis and cellular metabolism.

**Evidence related to body size**

Experimental studies of the insulin pathway identify Akt1 as an important component of growth regulation.

Alterations in Akt signalling can modify cellular growth and tissue development.

**Importance for the model**

`Akt1` is a candidate for representing downstream insulin signalling.

Its effects should not be treated as independent of other components of the pathway.

#### 3.2.5. `dilp` family

**Genes:** `dilp1`, `dilp2`, `dilp3`, `dilp4`, `dilp5`, `dilp6`, `dilp7`, `dilp8` and `dilp9`  
**Gene family:** Drosophila insulin-like peptides  
**Pathway:** Insulin/insulin-like signalling  
**Evidence classification:** Class A/B, depending on the individual gene

**Molecular function**

The `dilp` genes encode insulin-like peptides that participate in metabolic, developmental and physiological regulation.

Different members of the family exhibit different expression patterns and biological functions.

They should not be treated as interchangeable genes.

**Evidence related to body size**

Brogiolo et al. (2001) demonstrated that overexpression of an insulin-like peptide can alter growth in a manner dependent on the insulin receptor.

This supports the role of insulin-like peptides in growth regulation.

However, the contribution of each individual `dilp` gene to final adult body size must be considered separately.

**Importance for the model**

The insulin-like peptide family is biologically relevant, but representing every member would introduce unnecessary complexity into an initial model.

A smaller selection should be made only after reviewing the specific functions and experimental evidence for individual family members.

---

## 4. TOR Signalling Pathway

### 4.1. General function

The Target of Rapamycin pathway, commonly abbreviated as TOR, is a major regulator of cellular growth and metabolism.

It integrates information about nutrient availability, cellular energy status and other physiological signals.

TOR signalling influences protein synthesis, cellular metabolism and growth.

In *Drosophila*, TOR signalling is closely connected to insulin signalling and nutritional conditions.

This relationship makes the pathway particularly relevant for studying the influence of food availability on body size.

### 4.2. Candidate genes

#### 4.2.1. `Tor`

**Official symbol:** `Tor`  
**Gene name:** Target of rapamycin  
**Pathway:** TOR signalling  
**Evidence classification:** Class A/B

**Molecular function**

`Tor` encodes the central kinase of the TOR signalling pathway.

It participates in the regulation of protein synthesis, cellular growth and metabolic activity.

TOR operates through different protein complexes, particularly TOR complex 1 and TOR complex 2.

TORC1 is especially important for nutrient-dependent regulation of cellular growth.

**Evidence related to body size**

Experimental manipulation of TOR signalling affects cellular growth and tissue development.

Its activity is closely connected to the nutritional state of the organism.

**Importance for the model**

`Tor` is a strong candidate for representing the relationship between food availability and cellular growth.

However, TOR activity should not be treated as a direct measurement of body size.

It is an upstream regulatory mechanism whose effects emerge through several downstream processes.

#### 4.2.2. `Rheb`

**Official symbol:** `Rheb`  
**Gene name:** Ras homolog enriched in brain  
**Pathway:** TOR signalling  
**Evidence classification:** Class A/B

**Molecular function**

`Rheb` encodes a small GTPase that activates TORC1 signalling.

Its activity is regulated by the TSC1/TSC2 complex.

**Evidence related to body size**

Experimental activation of Rheb can increase TOR-dependent growth.

Studies in Drosophila tissues have demonstrated that increased Rheb activity can promote cellular and tissue overgrowth.

**Importance for the model**

`Rheb` is a candidate for representing a regulatory connection between upstream nutrient signals and TOR activity.

Its inclusion should be evaluated against the complexity of the model.

#### 4.2.3. `Tsc1`

**Official symbol:** `Tsc1`  
**Gene name:** Tuberous sclerosis complex 1  
**Pathway:** TOR signalling  
**Evidence classification:** Class A/B

**Molecular function**

`Tsc1` encodes a component of the TSC1/TSC2 protein complex.

Together with TSC2, it participates in the negative regulation of Rheb and consequently TORC1 activity.

**Evidence related to body size**

Experimental loss of TSC1 function can increase TOR-dependent growth in Drosophila tissues.

The resulting phenotypes may include cellular enlargement and tissue overgrowth.

**Importance for the model**

`Tsc1` provides a possible mechanism for representing genetic variation that reduces the negative regulation of growth signalling.

Its effects are particularly relevant to tissue growth and nutrient-dependent regulation.

#### 4.2.4. `Tsc2`

**Official symbol:** `Tsc2`  
**Gene name:** Tuberous sclerosis complex 2  
**Pathway:** TOR signalling  
**Evidence classification:** Class A/B

**Molecular function**

`Tsc2` encodes a protein that forms a functional complex with TSC1.

The complex acts as a negative regulator of Rheb and TORC1.

**Evidence related to body size**

Experimental suppression of TSC2 can produce increased TOR signalling and tissue growth.

The resulting phenotype depends on the tissue and experimental conditions.

**Importance for the model**

`Tsc2` is biologically relevant because it participates in the same regulatory complex as TSC1.

However, modelling both genes independently may not be necessary in an initial simplified model.

#### 4.2.5. `S6k`

**Official symbol:** `S6k`  
**Gene name:** S6 kinase  
**Pathway:** TOR signalling  
**Evidence classification:** Class A/B

**Molecular function**

`S6k` encodes a protein kinase involved in downstream growth regulation.

It participates in the control of protein synthesis and cellular growth.

**Evidence related to body size**

S6 kinase is a downstream component of nutrient-sensitive growth signalling.

Experimental changes in its activity can influence cellular growth and organismal development.

**Importance for the model**

`S6k` may be useful if the simulator eventually distinguishes between upstream nutrient sensing and downstream protein synthesis.

It is not essential for the first conceptual representation of TOR signalling.

---

## 5. Ecdysone and Developmental Timing

### 5.1. General function

Ecdysone is a steroid hormone that regulates developmental transitions in insects.

In *Drosophila melanogaster*, ecdysone signalling is essential for moulting, metamorphosis and the progression from larval to adult development.

Its relationship with body size is particularly important because adult structural growth is largely determined before metamorphosis.

The timing of developmental transitions influences how long the larva can continue feeding and growing.

Consequently, final adult size depends not only on growth rate but also on the duration of the growth period.

This distinction is essential:

- Insulin and TOR signalling contribute to the regulation of growth rate.
- Ecdysone signalling contributes to the regulation of developmental timing and growth termination.

These mechanisms interact rather than operating independently.

### 5.2. Candidate genes

#### 5.2.1. `ptth`

**Official symbol:** `ptth`  
**Gene name:** Prothoracicotropic hormone  
**Pathway:** Neuroendocrine regulation of ecdysone production  
**Evidence classification:** Class A

**Molecular function**

`ptth` encodes a neuropeptide produced by specialized neurons in the brain.

It stimulates signalling in the prothoracic gland, contributing to the regulation of ecdysone production.

**Evidence related to body size**

McBrayer et al. (2007) demonstrated that loss of PTTH-producing neurons delays larval development and produces larger adult flies.

The resulting increase in body size was associated with prolonged larval feeding and growth.

This provides direct experimental evidence connecting developmental timing with final body size.

**Importance for the model**

`ptth` is a strong candidate for representing the relationship between developmental duration and final body size.

It is particularly relevant if the simulator eventually models larval growth as a process occurring over time.

#### 5.2.2. `EcR`

**Official symbol:** `EcR`  
**Gene name:** Ecdysone receptor  
**Pathway:** Ecdysone signalling  
**Evidence classification:** Class A/B

**Molecular function**

`EcR` encodes the ecdysone receptor, a nuclear receptor that participates in the transcriptional response to ecdysone.

It forms a functional receptor complex with Ultraspiracle.

This complex regulates the expression of genes involved in moulting, metamorphosis and developmental transitions.

**Evidence related to body size**

Experimental changes in ecdysone receptor activity can alter developmental timing and growth.

Research has demonstrated that tissue-specific suppression of EcR in PTTH-producing neurons can delay development and increase pupal size.

**Importance for the model**

`EcR` is relevant for representing the hormonal mechanism that regulates developmental transitions.

However, its effects are tissue-dependent, and it should not be modelled as a universal direct controller of body size.

#### 5.2.3. `usp`

**Official symbol:** `usp`  
**Gene name:** Ultraspiracle  
**Pathway:** Ecdysone signalling  
**Evidence classification:** Class A/B

**Molecular function**

`usp` encodes a nuclear receptor that forms a functional complex with EcR.

The EcR/Usp complex regulates transcriptional responses to ecdysone.

**Evidence related to body size**

Because Usp participates in ecdysone receptor signalling, alterations in its activity can affect developmental transitions.

Experimental suppression in specific developmental neurons has been associated with developmental delay and increased pupal size.

**Importance for the model**

`usp` is a candidate for representing the transcriptional response to ecdysone.

Its inclusion should be considered alongside `EcR`, rather than treating both as unrelated growth regulators.

#### 5.2.4. `torso`

**Official symbol:** `torso`  
**Gene name:** Torso receptor  
**Pathway:** Developmental timing and ecdysone regulation  
**Evidence classification:** Class A/B

**Molecular function**

`torso` encodes a receptor tyrosine kinase involved in developmental signalling.

During larval development, Torso participates in the regulation of the prothoracic gland and ecdysone production.

**Evidence related to body size**

Torso signalling contributes to the timing of developmental transitions.

Changes in this regulatory system can therefore influence the duration of larval growth and final body size.

**Importance for the model**

`torso` is a candidate for a more detailed representation of developmental timing.

It should not be confused with `Tor`, which encodes the Target of Rapamycin kinase. They are different genes involved in different signalling systems.

---

## 6. Hippo Signalling Pathway

### 6.1. General function

The Hippo pathway is a major regulator of tissue growth and organ size.

It controls processes such as cellular proliferation and apoptosis.

Its principal function is to regulate the activity of Yorkie, a transcriptional co-activator that promotes growth-related gene expression.

When Hippo signalling is active, Yorkie is inhibited.

When Hippo signalling is reduced, Yorkie becomes more active and can promote cellular proliferation and tissue growth.

The pathway is particularly important for understanding how individual organs acquire their appropriate dimensions.

However, evidence of organ overgrowth does not automatically imply an equivalent increase in total organismal size.

Research has also demonstrated interactions between Hippo signalling and systemic hormonal regulation.

### 6.2. Candidate genes

#### 6.2.1. `hpo`

**Official symbol:** `hpo`  
**Gene name:** Hippo  
**Pathway:** Hippo signalling  
**Evidence classification:** Class A

**Molecular function**

`hpo` encodes a serine/threonine protein kinase that participates in the core Hippo signalling cascade.

It forms a functional complex with Salvador and contributes to the activation of Warts.

**Evidence related to body size**

Loss of Hippo pathway activity can produce tissue overgrowth in Drosophila.

Mutations affecting `hpo` have been associated with increased organ dimensions, particularly in tissues such as the wing and eye.

**Importance for the model**

`hpo` is a strong candidate for representing local tissue growth regulation.

It should not initially be interpreted as a direct regulator of total body size.

#### 6.2.2. `sav`

**Official symbol:** `sav`  
**Gene name:** Salvador  
**Pathway:** Hippo signalling  
**Evidence classification:** Class A/B

**Molecular function**

` sav` encodes an adaptor protein that interacts with Hippo.

It contributes to the organization and activation of the Hippo kinase complex.

**Evidence related to body size**

Loss of Salvador function can disrupt Hippo signalling and produce tissue overgrowth.

Its role is therefore associated with the regulation of organ dimensions and cellular proliferation.

**Importance for the model**

` sav` is a candidate for representing the regulatory structure of the Hippo pathway.

Its contribution is primarily relevant to local tissue growth.

#### 6.2.3. `wts`

**Official symbol:** `wts`  
**Gene name:** Warts  
**Pathway:** Hippo signalling  
**Evidence classification:** Class A

**Molecular function**

`wts` encodes a serine/threonine protein kinase that acts downstream of Hippo and Salvador.

It participates in the inhibition of Yorkie.

**Evidence related to body size**

Loss of Warts activity can produce considerable tissue overgrowth.

The pathway therefore provides strong evidence that `wts` is involved in the regulation of organ size.

Importantly, Warts also participates in systemic growth regulation through interactions with ecdysone production.

**Importance for the model**

`wts` is particularly interesting because it connects local tissue-growth regulation with systemic hormonal control.

It may become relevant if the simulator eventually models interactions between organ growth and overall body growth.

#### 6.2.4. `mats`

**Official symbol:** `mats`  
**Gene name:** Mob as tumor suppressor  
**Pathway:** Hippo signalling  
**Evidence classification:** Class A/B

**Molecular function**

`mats` encodes an adaptor protein that interacts with Warts and contributes to its kinase activity.

**Evidence related to body size**

Disruption of Mats function can reduce Hippo pathway activity and contribute to tissue overgrowth.

**Importance for the model**

`mats` is a component of the core Hippo regulatory mechanism.

Its inclusion would be more relevant in a detailed representation of tissue-specific growth than in an initial systemic body-size model.

#### 6.2.5. `yki`

**Official symbol:** `yki`  
**Gene name:** Yorkie  
**Pathway:** Hippo signalling  
**Evidence classification:** Class A

**Molecular function**

`yki` encodes a transcriptional co-activator that promotes the expression of genes involved in cellular proliferation and survival.

It acts as the principal functional output of the Hippo pathway.

**Evidence related to body size**

Increased Yorkie activity can produce tissue overgrowth through increased cellular proliferation and reduced apoptosis.

Its activity is therefore directly relevant to the determination of organ size.

**Importance for the model**

`yki` is a strong candidate for representing local growth-promoting activity.

However, the simulator should distinguish organ-specific growth from systemic body-size regulation.

---

## 7. Additional Candidate Genes and Regulatory Factors

The pathways described above represent important components of growth regulation, but they do not explain all genetic variation in body size.

Additional genes may influence development, tissue growth and morphological dimensions.

Their inclusion should depend on the specific phenotype being studied and the strength of available evidence.

### 7.1. `Pten`

**Official symbol:** `Pten`  
**Gene name:** Phosphatase and tensin homolog  
**Pathway:** PI3K/Akt regulation  
**Evidence classification:** Class A/B

`Pten` encodes a phosphatase that negatively regulates PI3K signalling.

It reduces the levels of phosphatidylinositol-3,4,5-trisphosphate and therefore antagonizes downstream insulin-dependent signalling.

Experimental reduction of PTEN activity can increase growth signalling and produce tissue overgrowth.

It is a relevant candidate for understanding how insulin signalling is regulated.

### 7.2. `foxo`

**Official symbol:** `foxo`  
**Gene name:** Forkhead box O  
**Pathway:** Insulin signalling and metabolic regulation  
**Evidence classification:** Class B

`foxo` encodes a transcription factor regulated by insulin signalling.

When insulin signalling is reduced, FOXO activity can increase and modify the expression of genes involved in metabolism, stress responses and growth regulation.

Its effects depend strongly on developmental and nutritional conditions.

It is therefore relevant to the interaction between growth and environmental stress, although it should not be treated as a direct body-size determinant.

### 7.3. `myc`

**Official symbol:** `Myc`  
**Gene name:** Myc  
**Pathway:** Cellular growth and proliferation  
**Evidence classification:** Class A/B

`Myc` encodes a transcription factor involved in the regulation of cellular growth, metabolism and proliferation.

Experimental reduction of Myc function in Drosophila can reduce organismal growth.

It is relevant because cellular growth is one of the fundamental processes contributing to final body dimensions.

However, Myc has broad biological functions and should not be interpreted as a body-size-specific gene.

### 7.4. `Alk` and `Pvr`

**Official symbols:** `Alk`, `Pvr`  
**Gene names:** Anaplastic lymphoma kinase; PDGF/VEGF receptor-related  
**Pathway:** Receptor tyrosine kinase signalling and developmental timing  
**Evidence classification:** Class A/B

Both genes encode receptor tyrosine kinases involved in developmental signalling.

Research has demonstrated that Alk and Pvr participate in the regulation of ecdysone production and developmental timing in coordination with PTTH/Torso signalling.

Their effects on the timing of metamorphosis can consequently influence final body size.

These genes illustrate that developmental timing is regulated by several interacting signals rather than by PTTH alone.

---

## 8. Natural Genetic Variation and Body Size

A crucial distinction must be made between genes that influence growth when experimentally manipulated and genes whose naturally occurring variants contribute to body-size differences in populations.

Experimental mutations can produce large phenotypic effects, but those effects do not necessarily occur in natural populations.

For evolutionary modelling, natural genetic variation is particularly important because the simulator aims to study changes in allele frequencies over generations.

### 8.1. Quantitative genetic evidence

Gockel et al. (2002) investigated natural variation in body size in *Drosophila melanogaster* using chromosome substitution and quantitative trait locus mapping.

Their results identified substantial genetic contributions to body-size variation, with particularly important effects associated with chromosome three.

However, identifying a genomic region associated with body size does not automatically identify the specific causal gene or allele.

The study therefore supports the polygenic nature of body-size variation but does not provide a complete list of causal genes suitable for direct simulation.

### 8.2. Candidate genes associated with natural morphological variation

Research on natural genetic variation in Drosophila morphology has identified candidate loci associated with traits such as thorax length, head width and wing dimensions.

Examples reported in studies of morphological variation include:

- `CG14478`
- `Fasciclin 3` (`Fas3`)
- `invected` (`inv`)
- `Reticulon-like 1` (`Rtnl1`)
- `toucan` (`tou`)

These genes have been investigated in relation to natural morphological variation, including thorax length.

However, their presence in this catalogue does not mean that all have been established as direct regulators of systemic growth.

Their reported associations concern particular morphological measurements and genetic backgrounds.

They should therefore be treated as candidates for further investigation rather than as confirmed universal body-size genes.

### 8.3. Implications for the simulator

The initial genetic model should prioritize genes with strong experimental evidence for their role in growth regulation.

Natural-variation candidates should be considered separately.

A future version could investigate whether variants associated with thorax length are suitable for representing heritable morphological variation.

Before assigning any allele a numerical effect, the relevant experimental evidence must be identified and evaluated.

---

## 9. Summary of Candidate Genes

The following table summarizes the genes identified in this document.

| Gene | Main pathway or function | Principal evidence | Initial relevance |
|---|---|---|---|
| `InR` | Insulin receptor signalling | Systemic and organ growth | High |
| `chico` | Insulin receptor adaptor | Cell size, cell number and body growth | High |
| `Pi3K92E` | PI3K signalling | Cellular growth and nutrient signalling | Medium |
| `Akt1` | Downstream insulin signalling | Cellular growth and metabolism | Medium |
| `dilp` family | Insulin-like peptides | Nutritional and growth regulation | Medium |
| `Tor` | Nutrient-dependent growth | Cellular growth and metabolism | High |
| `Rheb` | TORC1 activation | Tissue and cellular growth | Medium |
| `Tsc1` | TORC1 inhibition | Regulation of tissue growth | Medium |
| `Tsc2` | TORC1 inhibition | Regulation of tissue growth | Medium |
| `S6k` | Protein synthesis regulation | Downstream growth signalling | Medium |
| `ptth` | Developmental timing | Larval duration and final body size | High |
| `EcR` | Ecdysone receptor | Developmental transitions | High |
| `usp` | Ecdysone receptor co-factor | Developmental transitions | Medium |
| `torso` | Developmental signalling | Ecdysone production and timing | Medium |
| `hpo` | Hippo pathway | Organ and tissue growth | Medium |
| `sav` | Hippo pathway | Organ and tissue growth | Medium |
| `wts` | Hippo pathway | Organ and systemic growth regulation | Medium |
| `mats` | Hippo pathway | Organ and tissue growth | Medium |
| `yki` | Growth-promoting transcriptional co-activator | Cellular proliferation and organ growth | Medium |
| `Pten` | PI3K regulation | Growth signalling | Medium |
| `foxo` | Metabolic and stress regulation | Growth response to nutritional conditions | Low–Medium |
| `Myc` | Cellular growth | Cell growth and proliferation | Medium |
| `Alk` | Receptor tyrosine kinase | Developmental timing and body size | Medium |
| `Pvr` | Receptor tyrosine kinase | Developmental timing and body size | Medium |

The relevance levels are preliminary research priorities, not numerical estimates of effect size or definitive rankings of biological importance.

---

## 10. Implications for the Genome Evolution Lab

The research presented here suggests that body-size determination should not be represented through a single gene.

Instead, a biologically coherent model should eventually distinguish at least three interacting mechanisms.

**1. Growth rate**

Insulin and TOR signalling contribute to the regulation of cellular growth and nutrient-dependent development.

**2. Growth duration**

Ecdysone and associated neuroendocrine signals regulate developmental transitions and determine when larval growth terminates.

**3. Tissue-specific growth**

The Hippo pathway regulates cellular proliferation and organ dimensions, helping determine the size of individual anatomical structures.

These mechanisms provide a conceptual framework for translating genetic variation into phenotypic variation.

### 10.1. Proposed initial genetic scope

For the first scientifically motivated version of the model, the most reasonable approach is to prioritize a small number of genes or functional genetic modules.

The initial research priority should be:

- `InR` and `chico` for insulin-dependent growth regulation.
- `Tor` for nutrient-dependent cellular growth.
- `ptth` and `EcR` for developmental timing.
- `yki` or a simplified Hippo pathway representation if organ-specific growth is introduced.

This is a research shortlist, not a final implementation specification.

Including all listed genes immediately would create unnecessary complexity and introduce interactions that may be difficult to parameterize.

### 10.2. From genes to quantitative traits

A future model could represent body size through a quantitative relationship involving genetic contributions, environmental conditions and residual variation.

Conceptually:

\[
S = f(G,E,D,\varepsilon)
\]

where:

- \(S\) represents the selected body-size phenotype.
- \(G\) represents genetic contributions.
- \(E\) represents environmental conditions.
- \(D\) represents developmental processes.
- \(\varepsilon\) represents residual variation.

This expression is a conceptual framework, not a calibrated biological equation.

The genetic component should eventually account for interactions between loci and should not assume that every gene contributes independently.

### 10.3. Avoiding unsupported numerical effects

No numerical allelic effects should be assigned to the genes in this catalogue without suitable experimental evidence.

For example, the fact that experimental loss of `chico` produces smaller flies does not justify assigning every hypothetical `chico` allele a particular percentage reduction in thorax length.

Experimental mutations can produce strong loss-of-function phenotypes that are not representative of ordinary natural polymorphisms.

The simulator should therefore distinguish between:

- experimentally demonstrated gene function;
- known naturally occurring genetic variants;
- experimentally measured phenotypic effects;
- numerical parameters introduced as model assumptions.

This distinction is essential for scientific reproducibility.

---

## 11. Scientific Limitations and Open Questions

The catalogue provides an initial overview of important growth-related genes, but several questions remain unresolved.

First, the exact genetic architecture of naturally occurring body-size variation is not fully represented by the genes listed here.

Second, many experimental studies investigate cell size, organ size, pupal size or body mass rather than the exact primary phenotype proposed for the simulator.

Third, the effect of a genetic variant may depend on developmental stage, sex, environmental conditions and genetic background.

Fourth, genes within the same pathway interact. Treating their effects as independent would introduce an important simplification.

Fifth, some genes included here have strong evidence for tissue-specific growth but less direct evidence for whole-body size.

The catalogue must therefore be expanded and refined as additional research is conducted.

The next research stage should investigate individual genes through FlyBase, PubMed and primary experimental literature.

For every gene eventually selected for the simulator, the following information should be collected:

1. Official gene symbol.
2. Full gene name.
3. Molecular function.
4. Biological pathway.
5. Developmental stage of relevant activity.
6. Relevant tissue or organ.
7. Experimental evidence for growth effects.
8. Evidence for naturally occurring variants.
9. Measured phenotypic effects.
10. Known interactions with other genes.
11. Scientific references.
12. Suitability for quantitative modelling.

---

## 12. References

### Insulin/insulin-like signalling

**Böhni, R., Riesgo-Escovar, J., Oldham, S., Brogiolo, W., Stocker, H., Andruss, B. F., Beckingham, K., & Hafen, E. (1999).** Autonomous control of cell and organ size by CHICO, a Drosophila homolog of vertebrate IRS1-4. *Cell*, 97(7), 865–875.

DOI: https://doi.org/10.1016/S0092-8674(00)80799-0

**Brogiolo, W., Stocker, H., Ikeya, T., Rintelen, F., Fernandez, R., & Hafen, E. (2001).** An evolutionarily conserved function of the Drosophila insulin receptor and insulin-like peptides in growth control. *Current Biology*, 11(4), 213–221.

DOI: https://doi.org/10.1016/S0960-9822(01)00068-9

**Oldham, S., & Hafen, E. (2003).** Insulin/IGF and target of rapamycin signaling: a TOR de force in growth control. *Trends in Cell Biology*, 13(2), 79–85.

DOI: https://doi.org/10.1016/S0962-8924(02)00042-9

### TOR signalling

**Grewal, S. S. (2009).** Insulin/TOR signaling in growth and homeostasis: a view from the fly world. *The International Journal of Biochemistry & Cell Biology*, 41(5), 1006–1010.

DOI: https://doi.org/10.1016/j.biocel.2008.11.023

**Edgar, B. A. (2006).** How flies get their size: genetics meets physiology. *Nature Reviews Genetics*, 7, 907–916.

DOI: https://doi.org/10.1038/nrg1989

### Ecdysone and developmental timing

**McBrayer, Z., Ono, H., Shimell, M., Parvy, J.-P., Beckstead, R. B., Warren, J. T., Thummel, C. S., Dauphin-Villemant, C., Gilbert, L. I., & O'Connor, M. B. (2007).** Prothoracicotropic hormone regulates developmental timing and body size in Drosophila. *Developmental Cell*, 13(6), 857–871.

DOI: https://doi.org/10.1016/j.devcel.2007.11.003

**Yamanaka, N., Rewitz, K. F., & O'Connor, M. B. (2013).** Ecdysone control of developmental transitions: lessons from Drosophila research. *Annual Review of Entomology*, 58, 497–516.

DOI: https://doi.org/10.1146/annurev-ento-120811-153608

**Coordination among multiple receptor tyrosine kinase signals controls Drosophila developmental timing and body size. (2021).** *Cell Reports*, 36(9), 109644.

DOI: https://doi.org/10.1016/j.celrep.2021.109644

### Hippo signalling and organ growth

**Pan, D. (2010).** The hippo signaling pathway in development and cancer. *Developmental Cell*, 19(4), 491–505.

DOI: https://doi.org/10.1016/j.devcel.2010.09.011

**Warts Signaling Controls Organ and Body Growth through Regulation of Ecdysone. (2017).** *Current Biology*.

PubMed: https://pubmed.ncbi.nlm.nih.gov/28528906/

**Grusche, F. A., Degoutin, J. L., Richardson, H. E., & Harvey, K. F. (2011).** The Salvador/Warts/Hippo pathway controls regenerative tissue growth in Drosophila melanogaster. *Developmental Biology*.

DOI: https://doi.org/10.1016/j.ydbio.2010.11.020

### Natural genetic variation

**Gockel, J., Robinson, S. J. W., Kennington, W. J., Goldstein, D. B., & Partridge, L. (2002).** Quantitative genetic analysis of natural variation in body size in Drosophila melanogaster. *Heredity*, 89, 145–153.

DOI: https://doi.org/10.1038/sj.hdy.6800121

**Natural Genetic Variation and Candidate Genes for Morphological Traits in Drosophila melanogaster. (2016).**

Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC4961385/

### Scientific databases

- FlyBase: https://flybase.org/
- NCBI Gene: https://www.ncbi.nlm.nih.gov/gene/
- PubMed: https://pubmed.ncbi.nlm.nih.gov/
- Ensembl Metazoa: https://metazoa.ensembl.org/

---

**Document status:** Initial candidate gene catalogue. Gene inclusion does not imply that a naturally occurring allele has a known quantitative effect on body size. All genes and proposed modelling roles require further evaluation before implementation.