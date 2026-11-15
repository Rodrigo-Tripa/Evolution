# Contributing to Genome Evolution Lab

Thank you for your interest in contributing to Genome Evolution Lab!

Genome Evolution Lab is an open-source computational biology project focused on exploring evolutionary processes, genetic variation, phenotypic expression, and environmental selection, using *Drosophila melanogaster* as its initial reference organism.

Contributions from developers, biology students, researchers, and other interested individuals are welcome.

Our goal is to build a scientifically grounded, maintainable, and transparent computational research project.

## 1. Ways to Contribute

There are several ways to contribute to Genome Evolution Lab.

### 1.1. Scientific Research

Scientific contributions are particularly important to this project.

You can contribute by:

- Researching genes and their biological functions.
- Identifying genetic pathways associated with specific phenotypic traits.
- Reviewing scientific literature.
- Improving existing biological documentation.
- Identifying limitations in current scientific models.
- Suggesting new biological variables or evolutionary mechanisms.

All scientific contributions must be supported by reliable sources, preferably peer-reviewed scientific publications.

### 1.2. Software Development

Developers can contribute to the computational infrastructure by:

- Implementing genetic models.
- Developing population and evolutionary mechanisms.
- Improving simulation architecture.
- Implementing environmental variables.
- Developing phenotype representation.
- Improving computational efficiency.
- Implementing data analysis tools.

Contributions should respect the project's existing modular architecture and avoid introducing unnecessary dependencies.

### 1.3. Documentation

Documentation contributions are also welcome.

These include:

- Improving technical explanations.
- Correcting scientific inaccuracies.
- Expanding biological documentation.
- Improving architectural documentation.
- Adding references to scientific publications.
- Clarifying mathematical and computational models.

### 1.4. Testing and Validation

Contributors can help improve the reliability of the project by:

- Identifying unexpected behaviour.
- Developing unit tests.
- Developing integration tests.
- Validating mathematical models.
- Checking simulation consistency.
- Reporting reproducible bugs.

Scientific and computational correctness are both essential.

## 2. Scientific Standards

Genome Evolution Lab aims to maintain scientific accuracy and distinguish established evidence from theoretical assumptions.

All scientific contributions must follow these principles:

**Reliable references**

Scientific claims must be supported by verifiable sources. Peer-reviewed publications and established scientific databases should be prioritised.

**Evidence classification**

When documenting gene-phenotype relationships, contributors should distinguish between direct experimental evidence, mechanistic evidence, and associations observed in natural populations.

**Correlation and causation**

A statistical association between a genetic variant and a phenotype must not automatically be interpreted as a causal relationship.

**Model limitations**

Simplifications and assumptions introduced into biological or mathematical models must be explicitly documented.

**Reproducibility**

Scientific claims and computational results should provide enough information for other contributors to understand and, where possible, reproduce the underlying methodology.

## 3. Development Guidelines

The project follows a modular architecture.

Contributors should respect the existing organisation of the `src/` directory and place new functionality in the appropriate module.

Before introducing significant architectural changes, discuss the proposal with the project maintainer.

Development contributions should:

- Have a clearly defined purpose.
- Avoid unnecessary complexity.
- Use descriptive names.
- Include appropriate documentation.
- Avoid introducing unnecessary dependencies.
- Maintain consistency with existing project conventions.

Do not assume that every planned module is already implemented.

## 4. Documentation Guidelines

Documentation should be clear, technically accurate, and accessible to other contributors.

When adding scientific information:

- Include the relevant scientific references.
- Identify the organism and biological context.
- Explain relevant limitations.
- Avoid unsupported conclusions.

When modifying technical documentation, ensure that descriptions accurately reflect the current implementation rather than planned functionality.

## 5. Contribution Workflow

We recommend the following workflow:

**1. Explore the project**

Read the README and relevant documentation before starting work.

**2. Identify an opportunity**

Find an existing issue or identify an area where the project could benefit from improvement.

**3. Discuss significant changes**

For substantial scientific, architectural, or computational changes, open an issue before beginning implementation.

**4. Fork the repository**

Create your own fork and work on a separate branch.

**5. Make your contribution**

Keep changes focused and ensure that they follow the project's scientific and technical standards.

**6. Submit a Pull Request**

Explain what was changed, why it was necessary, and how the contribution can be reviewed.

Include relevant references for scientific contributions.

**7. Review**

Contributions are subject to review by the project maintainer. Changes may require revisions before being accepted.

## 6. Pull Request Guidelines

Every Pull Request should provide:

- A clear and descriptive title.
- An explanation of the proposed changes.
- The motivation behind the contribution.
- Relevant scientific references, where applicable.
- Testing or validation information, where applicable.

Keep Pull Requests focused on a single objective whenever possible.

Large changes should be discussed before submission.

## 7. Code of Conduct

All contributors are expected to maintain a respectful, constructive, and professional environment.

Scientific disagreements are welcome when supported by evidence and reasoned arguments.

Personal attacks, harassment, discrimination, and disrespectful behaviour are not acceptable.

## 8. Document Formatting and Standards

All contributors creating or modifying documents for Genome Evolution Lab must follow the project's established document formatting standards.

The existing `data/reference/webliography.docx` and `data/reference/webliography.pdf` serve as the formatting references.

### 8.1. DOCX and PDF Requirements

Every new `.docx` document created for the project must also be provided in `.pdf` format.

Both versions must contain equivalent content and follow the same formatting standards.

Contributors are responsible for ensuring that the PDF version accurately reflects the original DOCX document.

### 8.2. Header and Footer

All DOCX and PDF documents created by contributors must include the following header and footer:

**Header — Left aligned**

https://github.com/Rodrigo-Tripa/Evolution/

**Footer — Centre aligned**

`Contributor Name · Role, Genome Evolution Lab`

The contributor's name and assigned role must be included in the footer.

The available contributor roles are:

- **Co-Founder** — A person formally recognised as having co-founded the project.
- **Sponsor** — A person or organisation providing financial, material, or other significant support to the project.
- **Contributor** — A person who has made an accepted contribution to the project.

Roles are assigned exclusively by the project maintainer and must accurately reflect each individual's involvement.

The **Creator** designation is reserved exclusively for the original creator of Genome Evolution Lab and is not an assignable contributor role.

### 8.3. Formatting Consistency

All documents must follow the visual and typographical standards established in the existing webliography documents.

This includes:

- Header and footer formatting.
- Typography and font hierarchy.
- Heading styles and section organisation.
- Paragraph formatting and spacing.
- Tables, captions, and other document elements.
- Reference and citation formatting.

The existing webliography documents should be treated as the primary formatting reference rather than introducing an unrelated visual style.

## 9. Research Sources and Attribution

Genome Evolution Lab requires transparent attribution of external sources used during research and development.

Any research, scientific information, technical explanation, or software implementation that relies on information or work obtained from external websites must be properly referenced.

This requirement applies to websites and online resources. External files and documents follow the project's separate file-reference procedure.

### 9.1. Webliography Requirements

Every external website used as a source must be documented in:

`data/reference/webliography.docx`

and its corresponding PDF version:

`data/reference/webliography.pdf`

Contributors must ensure that new references are added consistently with the existing webliography format.

References should contain sufficient information to identify and retrieve the original source.

### 9.2. References in Contributions

External website sources must also be cited in the document or file produced by the contributor, wherever applicable.

This requirement applies to scientific documents, technical documentation, reports, research notes, and other non-code files.

**Exception:** Source code files are not required to contain inline website citations. However, external websites used to inform their implementation must still be recorded in the project's webliography.

### 9.3. Attribution Principles

Contributors must:

- Give credit to the original authors and publishers.
- Reference the original source rather than an unrelated secondary source whenever possible.
- Avoid presenting external work or ideas as original contributions.
- Distinguish between independently developed work and implementations based on external references.
- Ensure that citations accurately support the claims or implementation decisions they accompany.

Failure to provide appropriate attribution may result in a contribution being returned for correction before it can be accepted.

## 10. Licensing and Attribution

By contributing to Genome Evolution Lab, you agree that your contributions will be distributed under the project's Apache License 2.0, unless explicitly stated otherwise.

Please ensure that you have the right to submit any code, documentation, datasets, or other materials included in your contribution.

Do not submit copyrighted material or third-party resources without appropriate permission or licensing.

## 11. Questions and Contact

If you have questions about the project, its scientific direction, or how to contribute, open a GitHub issue to discuss your proposal.

We appreciate every contribution that helps make Genome Evolution Lab more scientifically accurate, technically reliable, and useful to the community.

---

**Genome Evolution Lab**

Originally created by Rodrigo Tripa.

Repository: https://github.com/Rodrigo-Tripa/Evolution