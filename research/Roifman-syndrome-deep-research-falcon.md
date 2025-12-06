---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-05T15:56:21.783636'
end_time: '2025-12-05T16:03:40.577615'
duration_seconds: 438.79
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Roifman-syndrome
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 20
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Roifman-syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Roifman-syndrome**.
Focus on the molecular and cellular mechanisms underlying disease progression.

### Required Information

#### 1. Core Pathophysiology
- What are the primary pathophysiological mechanisms?
- What molecular pathways are dysregulated?
- What cellular processes are affected?

#### 2. Key Molecular Players
- **Genes/Proteins**: Which genes are causally involved or implicated?
- **Chemical Entities**: What metabolites, drugs, or small molecules are relevant?
- **Cell Types**: Which cell types are primarily affected?
- **Anatomical Locations**: Which tissues/organs are involved?

#### 3. Biological Processes (for GO annotation)
- What biological processes (GO terms) are disrupted?
- Consider: signaling pathways, metabolic processes, cellular responses, transport, etc.

#### 4. Cellular Components
- Where in the cell do key processes occur?
- Consider: organelles, membrane compartments, extracellular space, etc.

#### 5. Disease Progression
- What is the sequence of events from initial trigger to clinical manifestation?
- Are there distinct stages or phases?

#### 6. Phenotypic Manifestations
- What are the key clinical phenotypes?
- How do they relate to the underlying mechanisms?

### Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Prioritize recent reviews and landmark papers
- Include direct quotes where possible to support key statements

### Output Format

Structure your response as a narrative that could be used to populate a disease knowledge base entry with:
- Pathophysiology description
- Gene/protein annotations with ontology terms (HGNC, GO)
- Phenotype associations (HP terms)
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Evidence items with PMIDs


## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Roifman-syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Roifman-syndrome**.
Focus on the molecular and cellular mechanisms underlying disease progression.

### Required Information

#### 1. Core Pathophysiology
- What are the primary pathophysiological mechanisms?
- What molecular pathways are dysregulated?
- What cellular processes are affected?

#### 2. Key Molecular Players
- **Genes/Proteins**: Which genes are causally involved or implicated?
- **Chemical Entities**: What metabolites, drugs, or small molecules are relevant?
- **Cell Types**: Which cell types are primarily affected?
- **Anatomical Locations**: Which tissues/organs are involved?

#### 3. Biological Processes (for GO annotation)
- What biological processes (GO terms) are disrupted?
- Consider: signaling pathways, metabolic processes, cellular responses, transport, etc.

#### 4. Cellular Components
- Where in the cell do key processes occur?
- Consider: organelles, membrane compartments, extracellular space, etc.

#### 5. Disease Progression
- What is the sequence of events from initial trigger to clinical manifestation?
- Are there distinct stages or phases?

#### 6. Phenotypic Manifestations
- What are the key clinical phenotypes?
- How do they relate to the underlying mechanisms?

### Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Prioritize recent reviews and landmark papers
- Include direct quotes where possible to support key statements

### Output Format

Structure your response as a narrative that could be used to populate a disease knowledge base entry with:
- Pathophysiology description
- Gene/protein annotations with ontology terms (HGNC, GO)
- Phenotype associations (HP terms)
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Evidence items with PMIDs


Disease Pathophysiology Research Report

Target Disease
- Disease Name: Roifman syndrome (RFMN; OMIM 616651)
- MONDO ID: not specified in cited sources
- Category: Genetic (spliceosomopathy due to noncoding snRNA gene)

Pathophysiology description
Roifman syndrome is caused by biallelic pathogenic variants in RNU4ATAC, the noncoding gene for U4atac snRNA, an essential component of the U12-dependent minor spliceosome. The core mechanism is impaired minor intron (U12-type) splicing, leading to increased retention of U12-type introns and dysregulated alternative splicing around minor introns in minor-intron-containing genes (MIGs). Tissue-specific dependence on correctly spliced MIGs explains the multi-system phenotype involving skeleton (spondyloepiphyseal dysplasia, growth retardation), immune system (B-cell differentiation defect with hypogammaglobulinemia), and retina (generalized rod–cone dystrophy). Recent evidence extends pathophysiology to secondary ciliogenesis defects caused by U12-type intron retention in cilia-related MIGs, linking minor spliceosome dysfunction to ciliopathy-like features and retinal degeneration. Together, these findings position RNU4ATAC-driven minor spliceosome failure as the initiating lesion that perturbs development and function across cell types and organs rich in critical MIGs (merico2015compoundheterozygousmutations pages 6-7, schejter2017ahomozygousmutation pages 2-3, olthof2020theminorand pages 33-37, heremans2018abnormaldifferentiationof pages 6-14, khatri2023deficiencyofthe pages 1-2, khatri2023deficiencyofthe pages 6-8, ballios2023deepphenotypiccharacterization pages 8-8).

Key concepts and definitions (current understanding)
- Minor spliceosome (U12-dependent): A specialized spliceosome that excises <1% of introns (U12-type) using U11, U12, U4atac, U6atac, and U5 snRNPs. RNU4ATAC encodes U4atac snRNA; pathogenic variants reduce minor splicing efficiency and fidelity (merico2015compoundheterozygousmutations pages 6-7). In NPJ Genomic Medicine (Jul 2017), Schejter et al. demonstrated that a homozygous Stem II domain mutation in RNU4ATAC is sufficient for typical Roifman syndrome and “consistent minor intron retention,” underscoring the centrality of U12 splicing defects (schejter2017ahomozygousmutation pages 2-3).
- Minor-intron-containing genes (MIGs): Host genes for U12-type introns; their proper expression requires intact minor spliceosome activity. Disruption causes U12 intron retention and aberrant alternative splicing around minor introns, generating isoforms that may be translated despite ORF-disrupting changes (merico2015compoundheterozygousmutations pages 6-7, olthof2020theminorand pages 33-37).
- Secondary ciliopathy mechanism in RNU4ATAC-opathies: Feb 2023 PNAS data link RNU4ATAC deficiency to primary cilium dysfunction via U12-type intron retention in cilium genes (e.g., RABL2, TMEM231, IFT80, TCTN1, PDE6D), with human fibroblast and zebrafish evidence and rescue by WT human U4atac (khatri2023deficiencyofthe pages 1-2, khatri2023deficiencyofthe pages 6-8).
- Roifman syndrome retinal disease: 2023 clinical series shows early-onset, universal, progressive retinal dystrophy with generalized rod–cone involvement, consistent with cilium-related photoreceptor biology (ballios2023deepphenotypiccharacterization pages 8-8).

Recent developments and latest research (prioritized 2023)
- Ciliogenesis defects mechanistically downstream of minor spliceosome failure: PNAS (Feb 21, 2023) reported that RNU4ATAC mutations expand to a Joubert-like ciliopathy spectrum, demonstrated U12-type intron retention in multiple ciliary transcripts, and rescued zebrafish ciliopathy phenotypes with wild-type U4atac snRNA (“deficiency of the minor spliceosome component U4atac snRNA secondarily results in ciliary defects”) (khatri2023deficiencyofthe pages 1-2, khatri2023deficiencyofthe pages 6-8).
- Retinal phenotype definition: Eye (May 2023) detailed the retinal dystrophy of RNU4ATAC-associated Roifman syndrome as universal and early onset with generalized rod–cone degeneration, aligning ocular pathophysiology with ciliary transcript mis-splicing (ballios2023deepphenotypiccharacterization pages 8-8).
- Alternative splicing around minor introns: Experimental inhibition and disease context show increased AS around U12 introns; aberrant MIG isoforms bind polysomes, implying translation despite potential NMD triggers (bioRxiv, May 2020), with direct evidence in individuals with Roifman syndrome (olthof2020theminorand pages 33-37).

Current applications and real-world implementations
- Diagnostic anchoring to RNU4ATAC: Genetic confirmation by identifying biallelic RNU4ATAC variants, often affecting the Stem II domain, with RNA-seq showing “consistent minor intron retention” in patient samples (schejter2017ahomozygousmutation pages 2-3, merico2015compoundheterozygousmutations pages 6-7).
- Functional modeling and rescue: Zebrafish u4atac models demonstrate ciliopathy phenotypes that are rescueable by wild-type human U4atac snRNA, constituting a proof-of-concept for RNA replacement strategies targeting the minor spliceosome (khatri2023deficiencyofthe pages 1-2, khatri2023deficiencyofthe pages 6-8).
- Immunophenotyping to guide management: Characterization of B-cell and megakaryocyte differentiation defects in patients provides mechanistic rationale for immunologic monitoring and platelet function assessment (heremans2018abnormaldifferentiationof pages 6-14).

Expert opinions and analysis from authoritative sources
- Merico et al. (Nature Communications, 2015) established causality and emphasized minor-spliceosome pathway dysfunction as core pathology in Roifman syndrome: “Compound heterozygous mutations in the noncoding RNU4ATAC cause Roifman Syndrome by disrupting minor intron splicing,” with RNA-seq evidence for extensive U12 intron retention and suggestion of RNA surveillance interplay (NEXT/exosome factors) (merico2015compoundheterozygousmutations pages 6-7).
- Schejter et al. (NPJ Genomic Medicine, 2017) refined genotype–phenotype correlations (Stem II domain sufficiency) and documented systemic features (immunodeficiency, skeletal dysplasia, retinal dystrophy) tied to consistent minor intron retention (schejter2017ahomozygousmutation pages 2-3).
- Heremans et al. (JACI, 2018) provided a mechanistic cellular framework for humoral immunodeficiency and thrombocytopathy via mis-spliced MIGs in B cells and megakaryocytes, adding granularity to hematologic pathophysiology (heremans2018abnormaldifferentiationof pages 6-14).
- Khatri et al. (PNAS, 2023) extended pathogenesis to secondary ciliopathy, providing multi-system developmental context and experimental rescue data that suggest tractable therapeutic avenues (khatri2023deficiencyofthe pages 1-2, khatri2023deficiencyofthe pages 6-8).

Relevant statistics and data from recent studies
- Universal retinal involvement: “Retinal involvement is universal, early-onset,” with generalized rod–cone dystrophy patterns on multimodal imaging in RNU4ATAC-associated Roifman syndrome (Eye, May 2023) (ballios2023deepphenotypiccharacterization pages 8-8).
- Cilium gene enrichment among MIGs: PNAS (2023) reports U12-type intron retention across cilium-related genes and demonstrates rescue by WT U4atac; representative genes include RABL2, TMEM231, IFT80, TCTN1, PDE6D (khatri2023deficiencyofthe pages 1-2, khatri2023deficiencyofthe pages 6-8).
- Systemic phenotype and U12 IR: Patient RNA-seq consistently shows elevated U12 intron retention following RNU4ATAC mutations (Nature Communications, 2015; NPJ Genomic Medicine, 2017) (merico2015compoundheterozygousmutations pages 6-7, schejter2017ahomozygousmutation pages 2-3).

Core Pathophysiology
- Primary mechanisms: RNU4ATAC variants (especially in the Stem II domain) impair U4atac function, decreasing efficiency/accuracy of U12-type intron excision. RNA-seq in patients demonstrates widespread minor intron retention; additional aberrant alternative splicing around minor introns yields isoforms that can associate with polysomes (schejter2017ahomozygousmutation pages 2-3, merico2015compoundheterozygousmutations pages 6-7, olthof2020theminorand pages 33-37).
- Dysregulated molecular pathways: Minor spliceosome pathway; cilium assembly and function; B-cell differentiation and class-switched immunoglobulin production; megakaryocyte maturation/platelet granule biology (khatri2023deficiencyofthe pages 1-2, khatri2023deficiencyofthe pages 6-8, heremans2018abnormaldifferentiationof pages 6-14).
- Affected cellular processes: Pre-mRNA splicing (U12-type), RNA surveillance/decay dynamics (accumulation of U12-intron–retaining transcripts); ciliogenesis; photoreceptor outer segment maintenance; lymphocyte development; megakaryopoiesis (merico2015compoundheterozygousmutations pages 6-7, olthof2020theminorand pages 33-37, khatri2023deficiencyofthe pages 1-2, heremans2018abnormaldifferentiationof pages 6-14).

Key Molecular Players
- Genes/Proteins: RNU4ATAC/U4atac (causal); MIGs across cell-cycle, cilium, and immune pathways (representative ciliary MIGs: RABL2, TMEM231, IFT80, TCTN1, PDE6D); exosome/NEXT factors implicated in transcript persistence (ZCCHC8, EXOSC1, EXOSC5) (merico2015compoundheterozygousmutations pages 6-7, khatri2023deficiencyofthe pages 1-2, khatri2023deficiencyofthe pages 6-8).
- Chemical entities: Not directly implicated as causative; pathway-level processes include spliceosome ribonucleoprotein interactions and RNA decay complexes (merico2015compoundheterozygousmutations pages 6-7).
- Cell types: B cells (defective differentiation), megakaryocytes (abnormal maturation/platelet morphology), photoreceptors, chondrocytes (inferred from skeletal phenotype), ciliated epithelial cells and neuronal progenitors (ciliopathy spectrum) (heremans2018abnormaldifferentiationof pages 6-14, ballios2023deepphenotypiccharacterization pages 8-8, khatri2023deficiencyofthe pages 1-2, khatri2023deficiencyofthe pages 6-8).
- Anatomical locations: Skeleton/growth plate; retina; immune system (lymphoid organs); multi-organ ciliated tissues (brainstem/cerebellar structures in ciliopathy spectrum, kidney pronephros in zebrafish models) (ballios2023deepphenotypiccharacterization pages 8-8, khatri2023deficiencyofthe pages 1-2, khatri2023deficiencyofthe pages 6-8).

Biological Processes (GO-like annotations, descriptive)
- Minor (U12-type) intron splicing; RNA splicing via spliceosome; regulation of alternative splicing around minor introns; cilium assembly and function; B-cell differentiation and activation; megakaryocyte differentiation and platelet granule biogenesis; photoreceptor maintenance (merico2015compoundheterozygousmutations pages 6-7, olthof2020theminorand pages 33-37, khatri2023deficiencyofthe pages 1-2, heremans2018abnormaldifferentiationof pages 6-14, ballios2023deepphenotypiccharacterization pages 8-8).

Cellular Components
- Nuclear spliceosomal snRNPs of the minor spliceosome (U11, U12, U4atac, U6atac, U5); primary cilium/axoneme; photoreceptor outer segment; B-cell developmental niches; megakaryocyte cytoskeleton and granules (merico2015compoundheterozygousmutations pages 6-7, khatri2023deficiencyofthe pages 1-2, ballios2023deepphenotypiccharacterization pages 8-8, heremans2018abnormaldifferentiationof pages 6-14).

Disease Progression (sequence of events)
1) Germline biallelic RNU4ATAC variants (often including a Stem II allele) reduce U4atac snRNA function in the minor spliceosome (schejter2017ahomozygousmutation pages 2-3, merico2015compoundheterozygousmutations pages 6-7).
2) System-wide increase in U12-type intron retention with compensatory but insufficient upregulation of minor-spliceosome snRNAs, and increased alternative splicing around minor introns; aberrant isoforms may bind polysomes (schejter2017ahomozygousmutation pages 2-3, merico2015compoundheterozygousmutations pages 6-7, olthof2020theminorand pages 33-37).
3) Downstream cellular dysfunction in tissues dependent on high-fidelity MIG expression: ciliogenesis/photoreceptor function (retinal dystrophy); B-cell development (antibody deficiency); megakaryopoiesis (platelet abnormalities); skeletal development (spondyloepiphyseal dysplasia and growth retardation) (khatri2023deficiencyofthe pages 1-2, khatri2023deficiencyofthe pages 6-8, ballios2023deepphenotypiccharacterization pages 8-8, heremans2018abnormaldifferentiationof pages 6-14, merico2015compoundheterozygousmutations pages 6-7).
4) Clinical manifestations emerge early and progress: universal early-onset retinal dystrophy, humoral immunodeficiency, skeletal dysplasia with short stature, developmental delay; additional ciliopathy-like features may be present depending on genotype (ballios2023deepphenotypiccharacterization pages 8-8, heremans2018abnormaldifferentiationof pages 6-14, schejter2017ahomozygousmutation pages 2-3, khatri2023deficiencyofthe pages 1-2, khatri2023deficiencyofthe pages 6-8).

Phenotypic Manifestations (selected HP terms, linked to mechanism)
- Retinal dystrophy (rod–cone; early-onset; progressive): due to impaired splicing of photoreceptor/ciliary MIGs (ballios2023deepphenotypiccharacterization pages 8-8, khatri2023deficiencyofthe pages 1-2).
- Hypogammaglobulinemia with poor vaccine responses; B-cell lymphopenia: B-cell differentiation defects from mis-splicing of critical MIGs (schejter2017ahomozygousmutation pages 2-3, heremans2018abnormaldifferentiationof pages 6-14).
- Spondyloepiphyseal dysplasia; growth retardation/short stature: skeletal development disruption from broad MIG mis-splicing (merico2015compoundheterozygousmutations pages 6-7).
- Developmental delay/microcephaly spectrum: global impact of minor splicing defects; potential contribution from ciliary dysfunction (schejter2017ahomozygousmutation pages 2-3, khatri2023deficiencyofthe pages 1-2).

Evidence items (selected quotes)
- “Compound heterozygous mutations in the noncoding RNU4ATAC cause Roifman Syndrome by disrupting minor intron splicing.” Nature Communications, Nov 2015 (merico2015compoundheterozygousmutations pages 6-7).
- “We demonstrate that a homozygous mutation in Stem II is sufficient to cause the full spectrum of features associated with typical Roifman syndrome… [and] the same pattern of aberration in minor intron retention.” NPJ Genomic Medicine, Jul 2017 (schejter2017ahomozygousmutation pages 2-3).
- “Deficiency of the minor spliceosome component U4atac snRNA secondarily results in ciliary defects in human and zebrafish,” with rescue by wild-type U4atac (PNAS, Feb 2023) (khatri2023deficiencyofthe pages 1-2, khatri2023deficiencyofthe pages 6-8).
- “Retinal involvement is universal, early-onset,” with generalized rod–cone dystrophy (Eye, May 2023) (ballios2023deepphenotypiccharacterization pages 8-8).
- “Elevated alternative splicing around minor introns… aberrant isoforms… bound to polysomes” in minor spliceosome diseases including Roifman syndrome (bioRxiv, May 2020) (olthof2020theminorand pages 33-37).
- “Abnormal differentiation of B cells and megakaryocytes in patients with Roifman syndrome” (J Allergy Clin Immunol, Aug 2018) (heremans2018abnormaldifferentiationof pages 6-14).

Gene/protein annotations with ontology terms (examples)
- RNU4ATAC (HGNC:18460): U4atac snRNA; function—U12-type intron splicing (minor spliceosome). Process: RNA splicing via minor spliceosome. Component: U4atac-containing snRNP complex (merico2015compoundheterozygousmutations pages 6-7, schejter2017ahomozygousmutation pages 2-3).
- Representative MIGs (cilium-related): RABL2, TMEM231, IFT80, TCTN1, PDE6D; process—cilium assembly/transport; phenotype—ciliopathy-like traits; retina involvement via photoreceptor ciliary function (khatri2023deficiencyofthe pages 1-2, khatri2023deficiencyofthe pages 6-8).

Phenotype associations (HP terms; examples)
- Retinal dystrophy (rod–cone): Eye 2023 (ballios2023deepphenotypiccharacterization pages 8-8).
- Hypogammaglobulinemia; B-cell lymphopenia; impaired vaccine responses: JACI 2018; NPJ Genomic Med 2017 (heremans2018abnormaldifferentiationof pages 6-14, schejter2017ahomozygousmutation pages 2-3).
- Spondyloepiphyseal dysplasia; short stature/growth retardation: Nat Commun 2015 (merico2015compoundheterozygousmutations pages 6-7).

Cell type involvement (CL terms; examples)
- B cells; megakaryocytes; photoreceptors; chondrocytes; ciliated epithelial and neuronal cells (heremans2018abnormaldifferentiationof pages 6-14, ballios2023deepphenotypiccharacterization pages 8-8, khatri2023deficiencyofthe pages 1-2, khatri2023deficiencyofthe pages 6-8, merico2015compoundheterozygousmutations pages 6-7).

Anatomical locations (UBERON terms; examples)
- Retina; skeletal system/growth plate cartilage; lymphoid tissues; multi-organ ciliated epithelia and neural structures (ballios2023deepphenotypiccharacterization pages 8-8, merico2015compoundheterozygousmutations pages 6-7, khatri2023deficiencyofthe pages 1-2, khatri2023deficiencyofthe pages 6-8).

Chemical entities (CHEBI-like; conceptual)
- Spliceosomal snRNP RNAs (U4atac) and ribonucleoprotein complexes; RNA surveillance complexes (NEXT/exosome) implicated in persistence of mis-spliced transcripts (merico2015compoundheterozygousmutations pages 6-7).

Embedded summary artifact
| Category | Entity (ontology hint) | Mechanistic role in Roifman syndrome (1–2 sentences) | Evidence (PMID or DOI) | Year & journal | URL |
|---|---|---|---|---|---|
| Causal gene | RNU4ATAC (HGNC:18460; encodes U4atac snRNA) | Biallelic variants in RNU4ATAC disrupt U4atac function, causing defective minor (U12-type) intron splicing and increased minor intron retention. | DOI:10.1038/ncomms9718 (merico2015compoundheterozygousmutations pages 6-7), DOI:10.1038/s41525-017-0024-5 (schejter2017ahomozygousmutation pages 2-3) | 2015 Nat Commun; 2017 NPJ Genomic Med | https://doi.org/10.1038/ncomms9718, https://doi.org/10.1038/s41525-017-0024-5 |
| Spliceosomal complex | Minor spliceosome (U11/U12/U4atac/U6atac/U5) | U4atac is an essential minor-spliceosome snRNA; dysfunction reduces efficient U12 intron excision, selectively affecting ~700–800 MIGs. | DOI:10.1038/ncomms9718 (merico2015compoundheterozygousmutations pages 6-7), bioRxiv:10.1101/2020.05.18.101246 (olthof2020theminorand pages 33-37), DOI:10.1073/pnas.2102569120 (khatri2023deficiencyofthe pages 1-2) | 2015 Nat Commun; 2020 bioRxiv; 2023 PNAS | https://doi.org/10.1038/ncomms9718, https://doi.org/10.1101/2020.05.18.101246, https://doi.org/10.1073/pnas.2102569120 |
| MIGs & splicing regulation | U12-type intron-containing genes (MIGs) / alternative splicing around minor introns (GO:RNA splicing) | RNU4ATAC defects cause elevated U12 intron retention and increased alternative splicing around minor introns, producing aberrant isoforms that alter protein coding potential. | bioRxiv:10.1101/2020.05.18.101246 (olthof2020theminorand pages 33-37), DOI:10.1038/ncomms9718 (merico2015compoundheterozygousmutations pages 6-7) | 2020 bioRxiv; 2015 Nat Commun | https://doi.org/10.1101/2020.05.18.101246, https://doi.org/10.1038/ncomms9718 |
| Ciliogenesis / ciliary MIGs | IFT80, TMEM231, TCTN1, PDE6D, RABL2 (examples; CL/UBERON links to cilium/retina) | Several cilium-related genes are MIGs; U12 intron retention in these genes causes secondary ciliary defects in patient cells and zebrafish models, linking minor-spliceosome dysfunction to ciliopathy-like phenotypes. | DOI:10.1073/pnas.2102569120 (khatri2023deficiencyofthe pages 1-2, khatri2023deficiencyofthe pages 6-8) | 2023 PNAS | https://doi.org/10.1073/pnas.2102569120 |
| Hematopoiesis / immune cells | B-cell differentiation (CL), megakaryopoiesis (CL) | Mis-splicing of MIGs perturbs B-cell and megakaryocyte differentiation, producing CD19 lymphopenia, hypogammaglobulinemia, defective vaccine responses, and abnormal platelet morphology/function. | DOI:10.1016/j.jaci.2017.11.061 (heremans2018abnormaldifferentiationof pages 6-14) | 2018 J Allergy Clin Immunol | https://doi.org/10.1016/j.jaci.2017.11.061 |
| Skeletal / cartilage development | Cartilage / chondrocyte (UBERON/CL); skeletal growth plate genes | Minor-spliceosome impairment alters splicing of genes important for skeletal development, producing spondyloepiphyseal dysplasia and growth retardation observed in patients. | DOI:10.1038/ncomms9718 (merico2015compoundheterozygousmutations pages 6-7), bioRxiv:10.1101/2020.05.18.101246 (olthof2020theminorand pages 33-37) | 2015 Nat Commun; 2020 bioRxiv | https://doi.org/10.1038/ncomms9718, https://doi.org/10.1101/2020.05.18.101246 |
| Retina / photoreceptors | Retina / photoreceptors (UBERON) — rod–cone dystrophy phenotype | RNU4ATAC-associated Roifman syndrome presents an early-onset, progressive generalized rod–cone retinal dystrophy; retinal involvement may reflect mis-splicing of cilia/photoreceptor MIGs (e.g., PDE6D). | DOI:10.1038/s41433-023-02581-1 (ballios2023deepphenotypiccharacterization pages 8-8), DOI:10.1073/pnas.2102569120 (khatri2023deficiencyofthe pages 1-2) | 2023 Eye; 2023 PNAS | https://doi.org/10.1038/s41433-023-02581-1, https://doi.org/10.1073/pnas.2102569120 |
| Immunodeficiency phenotype | Humoral antibody deficiency (HP terms) | Clinical immunodeficiency (hypogammaglobulinemia, poor vaccine responses) arises from disrupted expression of MIGs required for B-cell development and immune function. | DOI:10.1038/s41525-017-0024-5 (schejter2017ahomozygousmutation pages 2-3), DOI:10.1016/j.jaci.2017.11.061 (heremans2018abnormaldifferentiationof pages 6-14) | 2017 NPJ Genomic Med; 2018 J Allergy Clin Immunol | https://doi.org/10.1038/s41525-017-0024-5, https://doi.org/10.1016/j.jaci.2017.11.061 |
| RNA surveillance / decay | Exosome / NEXT complex components (ZCCHC8, EXOSC1, EXOSC5 — CHEBI/GO links) | RNA-seq in patients prioritized exosome/NEXT factors, suggesting impaired clearance of U12-intron-retaining transcripts contributes to accumulation of aberrant RNAs. | DOI:10.1038/ncomms9718 (merico2015compoundheterozygousmutations pages 6-7) | 2015 Nat Commun | https://doi.org/10.1038/ncomms9718 |
| Systems-level clinical features | Multisystem: skeleton, immune, retina, CNS (developmental delay) | Tissue-specific dependence on correct MIG splicing explains the multisystem phenotype including growth retardation, spondyloepiphyseal dysplasia, immunodeficiency, retinal dystrophy and neurodevelopmental delay. | DOI:10.1038/ncomms9718 (merico2015compoundheterozygousmutations pages 6-7), DOI:10.1038/s41525-017-0024-5 (schejter2017ahomozygousmutation pages 2-3), DOI:10.1016/j.jaci.2017.11.061 (heremans2018abnormaldifferentiationof pages 6-14) | 2015 Nat Commun; 2017 NPJ Genomic Med; 2018 J Allergy Clin Immunol | https://doi.org/10.1038/ncomms9718, https://doi.org/10.1038/s41525-017-0024-5, https://doi.org/10.1016/j.jaci.2017.11.061 |
| Alternative splicing consequence | Aberrant isoforms bound to polysomes; NMD escape | AS around minor introns produces alternatively spliced MIG isoforms that can escape nonsense-mediated decay and associate with polysomes, implying potential translation of aberrant proteins. | bioRxiv:10.1101/2020.05.18.101246 (olthof2020theminorand pages 33-37) | 2020 bioRxiv | https://doi.org/10.1101/2020.05.18.101246 |
| Experimental therapeutic proof-of-concept | Wild-type U4atac snRNA rescue (RNA-replacement concept) | In zebrafish u4atac models, coinjection of human WT U4atac rescues splicing and ciliopathy-related phenotypes, supporting RNA-replacement as a potential strategy. | DOI:10.1073/pnas.2102569120 (khatri2023deficiencyofthe pages 1-2, khatri2023deficiencyofthe pages 6-8) | 2023 PNAS | https://doi.org/10.1073/pnas.2102569120 |


*Table: Key genes, pathways, cell types, and organs implicated in Roifman syndrome pathophysiology with direct supporting citations from the included sources.*

References (URLs and publication dates)
- Merico D et al. Compound heterozygous mutations in the noncoding RNU4ATAC cause Roifman Syndrome by disrupting minor intron splicing. Nature Communications. Nov 2015. https://doi.org/10.1038/ncomms9718 (merico2015compoundheterozygousmutations pages 6-7)
- Schejter YD et al. A homozygous mutation in the stem II domain of RNU4ATAC causes typical Roifman syndrome. NPJ Genomic Medicine. Jul 2017. https://doi.org/10.1038/s41525-017-0024-5 (schejter2017ahomozygousmutation pages 2-3)
- Olthof AM et al. The minor and major spliceosome interact to regulate alternative splicing around minor introns. bioRxiv. May 2020. https://doi.org/10.1101/2020.05.18.101246 (olthof2020theminorand pages 33-37)
- Heremans J et al. Abnormal differentiation of B cells and megakaryocytes in patients with Roifman syndrome. Journal of Allergy and Clinical Immunology. Aug 2018. https://doi.org/10.1016/j.jaci.2017.11.061 (heremans2018abnormaldifferentiationof pages 6-14)
- Khatri D et al. Deficiency of the minor spliceosome component U4atac snRNA secondarily results in ciliary defects in human and zebrafish. Proceedings of the National Academy of Sciences. Feb 2023. https://doi.org/10.1073/pnas.2102569120 (khatri2023deficiencyofthe pages 1-2, khatri2023deficiencyofthe pages 6-8)
- Ballios BG et al. Deep phenotypic characterization of the retinal dystrophy in patients with RNU4ATAC-associated Roifman syndrome. Eye. May 2023. https://doi.org/10.1038/s41433-023-02581-1 (ballios2023deepphenotypiccharacterization pages 8-8)

Notes on open questions and limitations
- While the central role of U12-type intron mis-splicing is clear, the precise MIG subsets that drive each organ system’s phenotype remain incompletely defined in humans. The mechanistic contribution of RNA surveillance (e.g., exosome/NEXT) to disease variability requires further validation beyond initial transcriptomic prioritization (merico2015compoundheterozygousmutations pages 6-7). Additional longitudinal data on retinal and immunologic progression will refine staging and potential windows for intervention.


References

1. (merico2015compoundheterozygousmutations pages 6-7): Daniele Merico, Maian Roifman, Ulrich Braunschweig, Ryan K. C. Yuen, Roumiana Alexandrova, Andrea Bates, Brenda Reid, Thomas Nalpathamkalam, Zhuozhi Wang, Bhooma Thiruvahindrapuram, Paul Gray, Alyson Kakakios, Jane Peake, Stephanie Hogarth, David Manson, Raymond Buncic, Sergio L. Pereira, Jo-Anne Herbrick, Benjamin J. Blencowe, Chaim M. Roifman, and Stephen W. Scherer. Compound heterozygous mutations in the noncoding rnu4atac cause roifman syndrome by disrupting minor intron splicing. Nature Communications, Nov 2015. URL: https://doi.org/10.1038/ncomms9718, doi:10.1038/ncomms9718. This article has 164 citations and is from a highest quality peer-reviewed journal.

2. (schejter2017ahomozygousmutation pages 2-3): Yael Dinur Schejter, Adi Ovadia, Roumiana Alexandrova, Bhooma Thiruvahindrapuram, Sergio L. Pereira, David E. Manson, Ajoy Vincent, Daniele Merico, and Chaim M. Roifman. A homozygous mutation in the stem ii domain of rnu4atac causes typical roifman syndrome. NPJ Genomic Medicine, Jul 2017. URL: https://doi.org/10.1038/s41525-017-0024-5, doi:10.1038/s41525-017-0024-5. This article has 25 citations and is from a peer-reviewed journal.

3. (olthof2020theminorand pages 33-37): Anouk M. Olthof, Alisa K. White, Madisen F. Lee, Almahdi Chakroun, Alice K. Abdel Aleem, Justine Rousseau, Cinzia Magnani, Philippe M. Campeau, and Rahul N. Kanadia. The minor and major spliceosome interact to regulate alternative splicing around minor introns. bioRxiv, May 2020. URL: https://doi.org/10.1101/2020.05.18.101246, doi:10.1101/2020.05.18.101246. This article has 2 citations and is from a poor quality or predatory journal.

4. (heremans2018abnormaldifferentiationof pages 6-14): Jessica Heremans, Josselyn E. Garcia-Perez, Ernest Turro, Susan M. Schlenner, Ingele Casteels, Roxanne Collin, Francis de Zegher, Daniel Greene, Stephanie Humblet-Baron, Sylvie Lesage, Patrick Matthys, Christopher J. Penkett, Karen Put, Kathleen Stirrups, Chantal Thys, Chris Van Geet, Erika Van Nieuwenhove, Carine Wouters, Isabelle Meyts, Kathleen Freson, and Adrian Liston. Abnormal differentiation of b cells and megakaryocytes in patients with roifman syndrome. Journal of Allergy and Clinical Immunology, 142:630-646, Aug 2018. URL: https://doi.org/10.1016/j.jaci.2017.11.061, doi:10.1016/j.jaci.2017.11.061. This article has 45 citations and is from a highest quality peer-reviewed journal.

5. (khatri2023deficiencyofthe pages 1-2): Deepak Khatri, Audrey Putoux, Audric Cologne, Sophie Kaltenbach, Alicia Besson, Eloïse Bertiaux, Justine Guguin, Adèle Fendler, Marie A. Dupont, Clara Benoit-Pilven, Leila Qebibo, Samira Ahmed-Elie, Séverine Audebert-Bellanger, Pierre Blanc, Thomas Rambaud, Martin Castelle, Gaëlle Cornen, Sarah Grotto, Agnès Guët, Laurent Guibaud, Caroline Michot, Sylvie Odent, Lyse Ruaud, Elise Sacaze, Virginie Hamel, Rémy Bordonné, Anne-Louise Leutenegger, Patrick Edery, Lydie Burglen, Tania Attié-Bitach, Sylvie Mazoyer, and Marion Delous. Deficiency of the minor spliceosome component u4atac snrna secondarily results in ciliary defects in human and zebrafish. Proceedings of the National Academy of Sciences of the United States of America, Feb 2023. URL: https://doi.org/10.1073/pnas.2102569120, doi:10.1073/pnas.2102569120. This article has 17 citations and is from a highest quality peer-reviewed journal.

6. (khatri2023deficiencyofthe pages 6-8): Deepak Khatri, Audrey Putoux, Audric Cologne, Sophie Kaltenbach, Alicia Besson, Eloïse Bertiaux, Justine Guguin, Adèle Fendler, Marie A. Dupont, Clara Benoit-Pilven, Leila Qebibo, Samira Ahmed-Elie, Séverine Audebert-Bellanger, Pierre Blanc, Thomas Rambaud, Martin Castelle, Gaëlle Cornen, Sarah Grotto, Agnès Guët, Laurent Guibaud, Caroline Michot, Sylvie Odent, Lyse Ruaud, Elise Sacaze, Virginie Hamel, Rémy Bordonné, Anne-Louise Leutenegger, Patrick Edery, Lydie Burglen, Tania Attié-Bitach, Sylvie Mazoyer, and Marion Delous. Deficiency of the minor spliceosome component u4atac snrna secondarily results in ciliary defects in human and zebrafish. Proceedings of the National Academy of Sciences of the United States of America, Feb 2023. URL: https://doi.org/10.1073/pnas.2102569120, doi:10.1073/pnas.2102569120. This article has 17 citations and is from a highest quality peer-reviewed journal.

7. (ballios2023deepphenotypiccharacterization pages 8-8): Brian G. Ballios, Amarilla Mandola, Alaa Tayyib, Anupreet Tumber, Jenny Garkaby, Linda Vong, Elise Heon, Chaim M. Roifman, and Ajoy Vincent. Deep phenotypic characterization of the retinal dystrophy in patients with rnu4atac-associated roifman syndrome. Eye, 37:3734-3742, May 2023. URL: https://doi.org/10.1038/s41433-023-02581-1, doi:10.1038/s41433-023-02581-1. This article has 3 citations and is from a peer-reviewed journal.