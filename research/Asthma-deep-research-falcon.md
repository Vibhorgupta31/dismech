---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-05T16:26:32.032164'
end_time: '2025-12-05T16:37:10.227893'
duration_seconds: 638.2
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Asthma
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 27
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Asthma
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Asthma**.
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
- **Disease Name:** Asthma
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Asthma**.
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


# Disease Pathophysiology Research Template

## Target Disease
- Disease Name: Asthma
- MONDO ID: MONDO_0004979
- Category: Complex

## Pathophysiology description (current understanding)
Asthma is a chronic, heterogeneous airway disease driven by dysregulated interactions between a vulnerable airway epithelium, innate and adaptive immunity, the nervous system, and the airway structural compartment. Injury to the bronchial epithelium by allergens, viruses, or pollutants provokes epithelial alarmins (TSLP, IL-33, IL-25) that initiate and amplify type 2 (T2) inflammation via dendritic cells, ILC2s, and Th2 cells, leading to secretion of IL‑4/IL‑13/IL‑5, eosinophilia, IgE production, mucus metaplasia, airway hyperresponsiveness (AHR), and progressive remodeling (goblet cell hyperplasia, subepithelial fibrosis, increased ASM mass, and angiogenesis) (varricchi2024airwayremodellingin pages 1-2, russell2024theairwayepithelium pages 2-3, russell2024theairwayepithelium pages 6-7). Non–T2 asthma, frequent in severe/steroid‑resistant disease, is characterized by Th1/Th17 cytokines (IFN‑γ, TNF‑α, IL‑17A/F), neutrophilic inflammation, epithelial injury and junctional disruption linked to inflammasome activation, with distinct therapeutic gaps (liu2024advancesinnontype pages 1-2, khalfaoui2023airwaysmoothmuscle pages 3-4, russell2024theairwayepithelium pages 6-7). Emerging evidence highlights neuro‑immune circuits (TRPA1/TRPV1-positive nociceptors; neuropeptides CGRP/VIP/NMU; cholinergic pathways) that modulate bronchoconstriction and inflammatory tone, providing upstream targets complementary to immunobiologics (jean2022neuroimmuneregulatorynetworks pages 10-11). The respiratory and gut microbiomes influence asthma endotypes through dysbiosis and metabolites that condition epithelial and immune responses, adding another disease-modifying axis (kato2025theimmunologyof pages 29-30).

## Gene/protein annotations with ontology terms
- See embedded artifact mapping major genes/proteins (HGNC), processes (GO), cell types (CL), cellular components (GO CC), anatomical locations (UBERON), and chemicals (CHEBI), with supporting 2023–2024 sources.

| HGNC gene/protein | Role in pathophysiology (concise) | Canonical pathway / GO processes (GO IDs/terms) | Primary cell types (CL terms) | Cellular components (GO CC) | Anatomical locations (UBERON) | Key chemical entities (CHEBI) | Supporting evidence (DOI / year & context ID) |
|---|---|---|---|---|---|---|---|
| TSLP | Epithelial alarmin that initiates downstream type‑2 responses and activates DCs/ILC2s | GO:0005125 cytokine activity; GO:0007165 signal transduction | Airway epithelial cells; dendritic cells; ILC2s | GO:0005615 extracellular space; GO:0005886 plasma membrane | Bronchial epithelium (lung) | TSLP protein | ERJ 2024 doi:10.1183/13993003.01397-2023 (russell2024theairwayepithelium pages 2-3); Biomedicines 2024 doi:10.3390/biomedicines12102312 (hansi2024regulationofairway pages 21-22) |
| IL33 | Epithelial alarmin promoting ILC2/Th2 activation and eosinophilia | GO:0005125 cytokine activity; GO:0006954 inflammatory response | Airway epithelial cells; ILC2s; mast cells | GO:0005615 extracellular space | Bronchial epithelium | IL-33 cytokine | ERJ 2024 doi:10.1183/13993003.01619-2023 (varricchi2024airwayremodellingin pages 1-2); ERJ 2024 doi:10.1183/13993003.01397-2023 (russell2024theairwayepithelium pages 2-3) |
| IL1RL1 (ST2) | Receptor for IL-33 mediating alarmin signalling to ILC2/Th2 | GO:0007165 signal transduction; GO:0005125 cytokine receptor activity | ILC2s; Th2 cells; mast cells | GO:0005886 plasma membrane | Lung mucosa | IL-33 / receptor complex | ERJ 2024 doi:10.1183/13993003.01619-2023 (varricchi2024airwayremodellingin pages 1-2); ERJ 2024 doi:10.1183/13993003.01397-2023 (russell2024theairwayepithelium pages 2-3) |
| IL4R | Mediates IL-4/IL-13 signalling driving Th2 differentiation and IgE class switching | GO:0007165 signal transduction; GO:0006355 regulation of transcription | Th2 CD4+ T cells; B cells; epithelial cells | GO:0005886 plasma membrane | Airways | IL-4, IL-13, IgE | Expert Opin Ther Targets 2023 doi:10.1080/14728222.2023.2177533 (khalfaoui2023airwaysmoothmuscle pages 12-14); ERJ 2024 (russell2024theairwayepithelium pages 2-3) |
| IL13 | Effector cytokine driving mucus metaplasia, goblet cell hyperplasia and remodelling | GO:0005125 cytokine activity; GO:0001525 angiogenesis (remodelling links) | Th2 cells; ILC2s; epithelial cells | GO:0005615 extracellular space | Bronchi, airways | IL-13 cytokine | ERJ 2024 doi:10.1183/13993003.01619-2023 (varricchi2024airwayremodellingin pages 1-2) |
| IL5 | Promotes eosinophil maturation, survival and airway eosinophilia | GO:0005125 cytokine activity; GO:0030593 neutrophil chemotaxis (contrast) | Eosinophils; Th2 cells | GO:0005615 extracellular space | Airways | IL-5 cytokine | Expert Opin Ther Targets 2023 doi:10.1080/14728222.2023.2177533 (khalfaoui2023airwaysmoothmuscle pages 12-14); ERJ 2024 (russell2024theairwayepithelium pages 6-7) |
| IL5RA | IL-5 receptor alpha; mediates eosinophil responses targeted by biologics | GO:0007165 signal transduction | Eosinophils | GO:0005886 plasma membrane | Bone marrow; airways | IL-5 | ERJ 2024 (russell2024theairwayepithelium pages 2-3); Expert Opin Ther Targets 2023 (khalfaoui2023airwaysmoothmuscle pages 12-14) |
| FCER1A | High‑affinity IgE receptor alpha linking IgE sensitization to mast cell activation | GO:0005125 cytokine receptor activity; GO:0006954 inflammatory response | Mast cells; basophils | GO:0005886 plasma membrane | Airway mucosa | IgE (CHEBI:17563) | ERJ 2024 doi:10.1183/13993003.01397-2023 (russell2024theairwayepithelium pages 2-3) |
| GATA3 | Master transcription factor for Th2 differentiation and type‑2 program | GO:0003700 DNA‑binding transcription factor activity; GO:0006954 inflammatory response | CD4+ Th2 cells; ILC2s | GO:0005634 nucleus | Lymphoid tissues; airway mucosa | — | Expert Opin Ther Targets 2023 (khalfaoui2023airwaysmoothmuscle pages 12-14); ERJ 2024 (varricchi2024airwayremodellingin pages 1-2) |
| STAT6 | Signal transducer downstream of IL-4/IL-13 mediating mucus and remodelling gene expression | GO:0007165 signal transduction; GO:0006355 regulation of transcription | Epithelial cells; Th2 cells | GO:0005634 nucleus | Airways | — | Expert Opin Ther Targets 2023 (khalfaoui2023airwaysmoothmuscle pages 12-14); ERJ reviews (russell2024theairwayepithelium pages 2-3) |
| TGFB1 | Profibrotic mediator driving subepithelial fibrosis, EMT and airway remodelling | GO:0001525 angiogenesis; GO:0006954 inflammatory response | Fibroblasts; epithelial cells; airway smooth muscle (ASM) | GO:0005615 extracellular space | Subepithelial lamina propria; airways | TGF‑β1 cytokine | ERJ 2024 doi:10.1183/13993003.01619-2023 (varricchi2024airwayremodellingin pages 1-2) |
| MUC5AC | Gel‑forming mucin upregulated in goblet cell metaplasia and mucus plugging | GO:0019236 response to toxin; GO:0006954 inflammatory response | Goblet cells; secretory epithelial cells | GO:0005576 extracellular region | Airway lumen; bronchi | Mucin glycoproteins | ERJ 2024 (varricchi2024airwayremodellingin pages 1-2); ERJ 2024 (russell2024theairwayepithelium pages 2-3) |
| CHRM3 | Muscarinic M3 receptor mediating cholinergic bronchoconstriction and mucus secretion | GO:0007186 G‑protein coupled receptor signalling; GO:0007165 signal transduction | Parasympathetic nerve terminals; ASM; glandular epithelium | GO:0005886 plasma membrane | Bronchial smooth muscle; airway glands | Acetylcholine (CHEBI:16412) | Jean et al. J Leuk Biol 2022 doi:10.1002/jlb.3ru0121-023r (jean2022neuroimmuneregulatorynetworks pages 10-11); Khalfaoui 2023 (khalfaoui2023airwaysmoothmuscle pages 12-14) |
| TRPA1 | Sensory ion channel sensing irritants → neuropeptide release and neurogenic inflammation | GO:0005244 ion channel activity; GO:0006954 inflammatory response | Sensory nociceptor neurons; epithelial cells | GO:0005886 plasma membrane | Airway sensory nerves; epithelium | Reactive irritants (pollutants) | Jean et al. J Leuk Biol 2022 (jean2022neuroimmuneregulatorynetworks pages 10-11); Yao 2025 (yao2025modulatingtrpv1and pages 2-4) |
| TRPV1 | Nociceptor channel involved in cough, neuropeptide release and airway hyperresponsiveness | GO:0005244 ion channel activity; GO:0006954 inflammatory response | Sensory neurons; epithelial cells | GO:0005886 plasma membrane | Airways (sensory nerve endings) | Capsaicin‑like agonists | Jean et al. J Leuk Biol 2022 (jean2022neuroimmuneregulatorynetworks pages 10-11); Yao 2025 (yao2025modulatingtrpv1and pages 2-4) |
| NLRP3 | Inflammasome sensor driving IL‑1β/IL‑18 maturation — implicated in neutrophilic/non‑T2 exacerbations | GO:0006954 inflammatory response; GO:0039528 inflammasome complex | Macrophages; epithelial cells; neutrophils | GO:0005576 extracellular region (released cytokines) | Airway mucosa | IL‑1β (CHEBI:16655) | Clin Exp Med 2024 doi:10.1007/s10238-024-01492-z (hansi2024regulationofairway pages 21-22); Liu et al. ERJ 2024 (liu2024advancesinnontype pages 1-2) |
| IL17A | Th17 / ILC3 cytokine driving neutrophilic inflammation and steroid resistance | GO:0005125 cytokine activity; GO:0030593 neutrophil chemotaxis | Th17 cells; ILC3s; neutrophils | GO:0005615 extracellular space | Airways | IL‑17A cytokine | Expert Opin Ther Targets 2023 (khalfaoui2023airwaysmoothmuscle pages 12-14); Khalfaoui 2023 (khalfaoui2023airwaysmoothmuscle pages 3-4) |
| IFNG | Interferon‑gamma mediator implicated in antiviral responses and non‑T2 pathways | GO:0034341 response to interferon‑gamma; GO:0006954 inflammatory response | NK cells; Th1 cells; epithelial cells | GO:0005615 extracellular space | Airways; lymphoid tissue | IFN‑γ cytokine | Liu et al. ERJ 2024 (liu2024advancesinnontype pages 1-2); Russell et al. ERJ 2024 (russell2024theairwayepithelium pages 2-3) |
| KIT | c‑Kit receptor (SCF/c‑Kit) — supports ILC3 proliferation and IL‑17A production (neutrophilic axis) | GO:0007165 signal transduction; GO:0008284 positive regulation of cell proliferation | ILC3s; mast cells; fibroblasts (SCF source) | GO:0005886 plasma membrane | Lung fibroblast niche; airways | Stem cell factor (SCF) | Mechanistic summaries in ERJ/Expert reviews (varricchi2024airwayremodellingin pages 1-2, khalfaoui2023airwaysmoothmuscle pages 12-14) |
| FN1 | Fibronectin — ECM component involved in wound healing, ECM remodelling and altered repair in asthma | GO:0007229 integrin‑mediated signaling; GO:0001525 angiogenesis | Fibroblasts; epithelial cells; myofibroblasts | GO:0005576 extracellular region / matrix | Subepithelial lamina propria (airways) | ECM proteins (fibronectin) | Multi‑omics nasal epithelium & remodelling reviews (varricchi2024airwayremodellingin pages 1-2, russell2024theairwayepithelium pages 6-7) |


*Table: Ontological mapping table of principal asthma genes/proteins (roles, GO processes, cell and anatomical locations, chemicals) with supporting recent literature DOIs and context citations; useful for knowledge‑base annotation and linking mechanisms to therapeutics.*

## Phenotype associations (HP terms)
- HP:0002099 Wheezing; HP:0002091 Dyspnea; HP:0002105 Cough; HP:0030876 Airway hyperreactivity; HP:0006531 Eosinophilia (T2-high); HP:0031417 Neutrophilia (T2-low) supported mechanistically by epithelial alarmin–driven T2 cascades and, in non‑T2, IL‑17/inflammasome–linked neutrophilic inflammation (russell2024theairwayepithelium pages 6-7, liu2024advancesinnontype pages 1-2, khalfaoui2023airwaysmoothmuscle pages 3-4).

## Cell type involvement (CL terms)
- Airway epithelial cells (CL:0002328); Goblet cells (CL:0000160); Basal cells (CL:0011109); Dendritic cells (CL:0000451); Group 2 innate lymphoid cells, ILC2 (CL:0001065); Th2 cells (CL:0000910); Eosinophils (CL:0000771); Neutrophils (CL:0000775); Mast cells (CL:0000097); Airway smooth muscle cells (CL:0000650); Sensory nociceptors (CL:0000648). Evidence across epithelial alarmins/Th2 axis, non‑T2 pathways, and ASM remodeling (varricchi2024airwayremodellingin pages 1-2, russell2024theairwayepithelium pages 2-3, khalfaoui2023airwaysmoothmuscle pages 3-4, khalfaoui2023airwaysmoothmuscle pages 12-14, jean2022neuroimmuneregulatorynetworks pages 10-11).

## Anatomical locations (UBERON terms)
- Bronchus (UBERON:0002185); Bronchial epithelium (UBERON:0004782); Lamina propria of bronchus (UBERON:0004821); Airway smooth muscle layer (UBERON:0004277). Remodeling and barrier dysfunction localized to these compartments (varricchi2024airwayremodellingin pages 1-2, russell2024theairwayepithelium pages 2-3).

## Chemical entities (CHEBI)
- IgE (CHEBI:17563); Acetylcholine (CHEBI:16412); IL‑4/IL‑5/IL‑13 cytokines (protein entities); TGF‑β1; IL‑33/TSLP (alarmins). Functional roles detailed under molecular players and neuro‑immune sections (russell2024theairwayepithelium pages 2-3, jean2022neuroimmuneregulatorynetworks pages 10-11, khalfaoui2023airwaysmoothmuscle pages 12-14).

## 1) Core Pathophysiology
- Primary mechanisms: epithelial barrier dysfunction (tight/adherens junction disruption), defective antiviral responses, and alarmin overproduction (TSLP/IL‑33/IL‑25) that orchestrate downstream T2 pathways (IL‑4/IL‑5/IL‑13) with eosinophilic inflammation, mucus metaplasia, AHR, and airway remodeling (russell2024theairwayepithelium pages 2-3, varricchi2024airwayremodellingin pages 1-2, russell2024theairwayepithelium pages 6-7).
- Molecular dysregulation: epithelial cytokine networks (TSLP/IL‑33/IL‑25), Th2 transcriptional programs (GATA3/STAT6), eosinophil survival (IL‑5/IL‑5R), IgE–FcεRI axis, and remodeling mediators (TGF‑β1, ECM components such as fibronectin) (russell2024theairwayepithelium pages 2-3, varricchi2024airwayremodellingin pages 1-2, khalfaoui2023airwaysmoothmuscle pages 12-14).
- Affected cellular processes: antiviral interferon responses (attenuated), epithelial repair and EMT, mucus production (MUC5AC), ASM contraction/proliferation, mast cell–ASM cross‑talk (russell2024theairwayepithelium pages 6-7, varricchi2024airwayremodellingin pages 1-2, khalfaoui2023airwaysmoothmuscle pages 12-14).

## 2) Key Molecular Players
- Genes/Proteins (examples; see artifact for extended mapping): TSLP, IL33, IL1RL1(ST2), IL4R, IL13, IL5/IL5RA, FCER1A, GATA3, STAT6, TGFB1, MUC5AC, CHRM3, TRPA1, TRPV1, NLRP3, IL17A, IFNG, KIT, FN1 (varricchi2024airwayremodellingin pages 1-2, russell2024theairwayepithelium pages 2-3, khalfaoui2023airwaysmoothmuscle pages 3-4, jean2022neuroimmuneregulatorynetworks pages 10-11, khalfaoui2023airwaysmoothmuscle pages 12-14).
- Chemical entities: IgE; acetylcholine; nitric oxide (derived from epithelial iNOS in IL‑4/IL‑13 milieu); epithelial cytokines and neuropeptides (CGRP, VIP, NMU) (russell2024theairwayepithelium pages 6-7, jean2022neuroimmuneregulatorynetworks pages 10-11).
- Cell types: epithelium, DCs, ILC2s, Th2 cells, eosinophils (T2-high); Th1/Th17 cells, neutrophils, ILC3s (T2-low); ASM; mast cells; nociceptors (varricchi2024airwayremodellingin pages 1-2, liu2024advancesinnontype pages 1-2, khalfaoui2023airwaysmoothmuscle pages 3-4, jean2022neuroimmuneregulatorynetworks pages 10-11).
- Anatomical locations: bronchial epithelium, subepithelial matrix, ASM, airway lumen (varricchi2024airwayremodellingin pages 1-2, russell2024theairwayepithelium pages 2-3).

## 3) Biological Processes (GO annotation; disrupted)
- Epithelial barrier and response: inflammatory response (GO:0006954), response to interferon‑gamma (GO:0034341), cytokine activity (GO:0005125), signal transduction (GO:0007165), epithelial to mesenchymal transition, mucociliary dysfunction (russell2024theairwayepithelium pages 2-3, varricchi2024airwayremodellingin pages 1-2).
- Type 2 pathways: Th2 differentiation and signaling (IL‑4/IL‑13/STAT6), eosinophil chemotaxis/survival, IgE‑mediated activation (russell2024theairwayepithelium pages 2-3, khalfaoui2023airwaysmoothmuscle pages 12-14).
- Non‑T2 pathways: IL‑17 signaling, neutrophil chemotaxis (GO:0030593), inflammasome activation (NLRP3), interferon and STING‑linked innate pathways described in non‑T2 endotypes (liu2024advancesinnontype pages 1-2, khalfaoui2023airwaysmoothmuscle pages 3-4).
- Remodeling: integrin‑mediated signaling (GO:0007229), ECM deposition, angiogenesis (GO:0001525), ASM proliferation/contractility (varricchi2024airwayremodellingin pages 1-2, khalfaoui2023airwaysmoothmuscle pages 12-14).

## 4) Cellular Components (where processes occur)
- Extracellular space (alarmins/cytokines; GO:0005615) and plasma membrane (receptors including IL1RL1/ST2, IL4R, CHRM3, TRP channels; GO:0005886) (russell2024theairwayepithelium pages 2-3, jean2022neuroimmuneregulatorynetworks pages 10-11).
- Nucleus (transcription factors GATA3/STAT6; GO:0005634); extracellular matrix (ECM) in the subepithelium (FN1) (varricchi2024airwayremodellingin pages 1-2, khalfaoui2023airwaysmoothmuscle pages 12-14).

## 5) Disease Progression
- Initiation: epithelial injury (allergen, virus, pollutant) → alarmin release (TSLP/IL‑33/IL‑25), reduced antiviral IFNs, barrier disruption (russell2024theairwayepithelium pages 2-3, russell2024theairwayepithelium pages 6-7).
- Amplification: DC/ILC2/Th2 activation → IL‑4/IL‑13/IL‑5 → eosinophilia, IgE‑mediated mast cell activation, mucus metaplasia, AHR (varricchi2024airwayremodellingin pages 1-2, russell2024theairwayepithelium pages 2-3).
- Remodeling: TGF‑β–driven fibrosis, ASM hyperplasia/hypercontractility, angiogenesis; can also be driven by mechanical stress of bronchoconstriction independent of inflammation (varricchi2024airwayremodellingin pages 1-2).
- Alternative endotypes: non‑T2 pathways (IL‑17/inflammasome/IFN‑γ) with neutrophilic or paucigranulocytic inflammation, corticosteroid insensitivity (liu2024advancesinnontype pages 1-2, khalfaoui2023airwaysmoothmuscle pages 3-4).

## 6) Phenotypic Manifestations (clinical)
- Episodic wheeze, cough, chest tightness, and variable airflow limitation due to bronchoconstriction and mucus. Elevated FeNO and blood/sputum eosinophils in T2‑high; low FeNO and neutrophilic/pauci‑granulocytic profiles in T2‑low (russell2024theairwayepithelium pages 6-7, liu2024advancesinnontype pages 1-2).
- Imaging/histopathology: mucus plugging, RBM thickening, ECM deposition, increased ASM mass, angiogenesis—detectable even in mild disease and early life (varricchi2024airwayremodellingin pages 1-2).

## Recent developments and latest research (2023–2024 priority)
- Epithelial centrality and alarmins: 2024 ERS reviews consolidate the epithelium as “orchestrator” of inflammation/remodeling and highlight upstream alarmins (TSLP, IL‑33, IL‑25) as disease drivers and targets. Anti‑TSLP (tezepelumab) showed broad biomarker/exacerbation and mannitol AHR improvements, including in patients without elevated T2 biomarkers (russell2024theairwayepithelium pages 2-3, russell2024theairwayepithelium pages 6-7, varricchi2024airwayremodellingin pages 1-2). 
- Non‑T2 severe asthma: 2024 ERJ review delineates inflammasome/IL‑17/interferon pathways underpinning neutrophilic, steroid‑resistant phenotypes and frames precision medicine needs (liu2024advancesinnontype pages 1-2). ASM‑centric mechanisms remain critical for hyperreactivity/remodeling (khalfaoui2023airwaysmoothmuscle pages 12-14).
- Neuro‑immune: contemporary reviews synthesize how TRPA1/TRPV1 nociceptors and neuropeptides (VIP, NMU promote; CGRP, adrenergic signals may restrain) regulate Type 2 inflammation and bronchomotor tone—providing new targets upstream of immune effectors (jean2022neuroimmuneregulatorynetworks pages 10-11).
- Microbiome and epithelial barrier theory: updated reviews emphasize dysbiosis and exposome‑induced barrier disruption as common threads in asthma pathogenesis across tissues, integrating multi‑omic signatures (kato2025theimmunologyof pages 29-30, brightling2024theepithelialera pages 4-5).

## Current applications and real‑world implementations
- Targeted biologics anchored in mechanism:
  - Upstream alarmin pathway: tezepelumab (anti‑TSLP) reduces exacerbations across biomarker strata and lowers airway IL‑33 and multiple T2 biomarkers; early data suggest improvements in mucus plugging and AHR (russell2024theairwayepithelium pages 6-7, russell2024theairwayepithelium pages 2-3).
  - Downstream T2 effectors: dupilumab (IL‑4Rα blockade), anti‑IL‑5 class (mepolizumab, reslizumab, benralizumab), and omalizumab (anti‑IgE) reduce exacerbations and address eosinophilia/IgE‑mediated inflammation; effects on structural remodeling vary by pathway (russell2024theairwayepithelium pages 6-7, russell2024theairwayepithelium pages 2-3).
  - ASM/remodeling: evidence indicates some biologics can reduce ECM markers or ASM mass (e.g., benralizumab via eosinophil depletion), yet consistent reversal of remodeling remains an open goal (russell2024theairwayepithelium pages 4-5, varricchi2024airwayremodellingin pages 1-2).

## Expert opinions and analysis (authoritative sources)
- ERS/ERJ expert groups argue that restoring epithelial barrier integrity and targeting epithelial cytokines may modify disease course and potentially remodeling, elevating the epithelium as a therapeutic target along with immune pathways (varricchi2024airwayremodellingin pages 1-2, brightling2024theepithelialera pages 4-5, russell2024theairwayepithelium pages 6-7).
- Precision endotyping for non‑T2 phenotypes is a pressing unmet need; pathways involving IL‑17, inflammasome, and interferon signaling highlight alternative, steroid‑resistant mechanisms requiring new targets (liu2024advancesinnontype pages 1-2, khalfaoui2023airwaysmoothmuscle pages 3-4).
- Neuro‑immune nodes (TRPA1/TRPV1; cholinergic/neuropeptide circuits) represent promising, underexploited upstream control points for both bronchomotor and inflammatory responses (jean2022neuroimmuneregulatorynetworks pages 10-11).

## Relevant statistics and data from recent studies
- Airway remodeling is present even in mild asthma and may start early in life, with epithelial cytokines (TSLP/IL‑33/IL‑25) facilitating remodeling via cross‑talk with fibroblasts, mast cells, and ASM (varricchi2024airwayremodellingin pages 1-2).
- Anti‑TSLP (tezepelumab) reduces exacerbations and improves FEV1 and mannitol AHR while lowering multiple T2 biomarkers and airway IL‑33, including in patients without classical T2 biomarker elevation—supporting its upstream breadth (russell2024theairwayepithelium pages 6-7).
- Non‑T2 endotypes exhibit low FeNO, low eosinophils, and frequent steroid resistance, with mechanistic involvement of IL‑17/inflammasome/interferon pathways (liu2024advancesinnontype pages 1-2).

## Evidence items (selected, with PMIDs/DOIs and dates; see also embedded table)
- The airway epithelium as orchestrator; epithelial barrier dysfunction → alarmins → T2 pathways; remodeling features and therapeutic implications (ERJ, Mar 2024; DOI: 10.1183/13993003.01397-2023; URL: https://doi.org/10.1183/13993003.01397-2023) (russell2024theairwayepithelium pages 2-3, russell2024theairwayepithelium pages 6-7).
- Airway remodeling and the epithelium; alarmins (TSLP/IL‑33/IL‑25) in remodeling; early‑life origins; potential for therapies to modify remodeling (ERJ, Apr 2024; DOI: 10.1183/13993003.01619-2023; URL: https://doi.org/10.1183/13993003.01619-2023) (varricchi2024airwayremodellingin pages 1-2).
- Epithelial era expert summary; links between barrier loss, alarmins, and severity; genetic/omic evidence implicating epithelial genes (ERR, Oct 2024; DOI: 10.1183/16000617.0221-2024; URL: https://doi.org/10.1183/16000617.0221-2024) (brightling2024theepithelialera pages 4-5).
- ASM contractility/remodeling mechanisms and cytokine/Th17 contributions; clinical translation to biologics and CASCADE (Expert Opin Ther Targets, Jan 2023; DOI: 10.1080/14728222.2023.2177533; URL: https://doi.org/10.1080/14728222.2023.2177533) (khalfaoui2023airwaysmoothmuscle pages 12-14, khalfaoui2023airwaysmoothmuscle pages 3-4).
- Non‑T2 severe asthma mechanisms: inflammasome, IL‑17, interferons; clinical features and precision medicine gaps (ERJ, May 2024; DOI: 10.1183/13993003.00826-2023; URL: https://doi.org/10.1183/13993003.00826-2023) (liu2024advancesinnontype pages 1-2).
- Neuro‑immune regulation: TRPA1/TRPV1, neuropeptides (CGRP, VIP, NMU), cholinergic influences on type 2 responses and bronchomotor tone (J Leukoc Biol, Apr 2022; DOI: 10.1002/jlb.3ru0121-023r; URL: https://doi.org/10.1002/jlb.3ru0121-023r) (jean2022neuroimmuneregulatorynetworks pages 10-11).
- Microbiome and epithelial barrier theory syntheses emphasizing dysbiosis and exposome impacts on barrier function across allergic disease including asthma (Nat Rev Microbiol, May 2024; DOI: 10.1038/s41579-024-01048-8; URL: https://doi.org/10.1038/s41579-024-01048-8) (kato2025theimmunologyof pages 29-30).

## Structured narrative by required sections

1. Core pathophysiology
- Primary mechanisms: epithelial barrier impairment and alarmin release (TSLP/IL‑33/IL‑25) are now recognized as upstream drivers that orchestrate downstream T2 immunity and remodeling. These alarmins activate DCs/ILC2s/Th2 cells, induce IL‑4/IL‑13/IL‑5, and drive eosinophilia, mucus metaplasia, and AHR. Viral/allergen exposure simultaneously reduces epithelial antiviral IFNs and repair capacity, perpetuating barrier loss (russell2024theairwayepithelium pages 2-3, varricchi2024airwayremodellingin pages 1-2, russell2024theairwayepithelium pages 6-7).
- Non‑T2 mechanisms: severe, steroid‑resistant endotypes are underpinned by IL‑17, inflammasome activation (e.g., NLRP3), and interferon-related pathways, correlating with neutrophilia and corticosteroid insensitivity (liu2024advancesinnontype pages 1-2, khalfaoui2023airwaysmoothmuscle pages 3-4).

2. Key molecular players
- Upstream alarmins (TSLP/IL‑33/IL‑25) and receptors (IL1RL1/ST2, IL4R) link the epithelium to T2 effector cytokines (IL‑4/IL‑13/IL‑5) and cell types (ILC2, Th2, eosinophils), while remodeling mediators (TGF‑β1; ECM proteins) and ASM pathways sustain structural changes. Non‑T2: IL‑17A(Th17/ILC3), IFN‑γ, and NLRP3 highlight alternative inflammatory axes. Neuro‑immune: TRPA1/TRPV1 ion channels and muscarinic M3 receptors (CHRM3) couple environmental/neuronal stimuli to bronchomotor and inflammatory responses (varricchi2024airwayremodellingin pages 1-2, russell2024theairwayepithelium pages 2-3, khalfaoui2023airwaysmoothmuscle pages 3-4, jean2022neuroimmuneregulatorynetworks pages 10-11, khalfaoui2023airwaysmoothmuscle pages 12-14).

3. Biological processes (GO)
- Disrupted processes include inflammatory response, cytokine signaling, epithelial repair/EMT, mucociliary function, T2 cytokine signaling, neutrophil chemotaxis, inflammasome activation, and ECM/angiogenesis (varricchi2024airwayremodellingin pages 1-2, russell2024theairwayepithelium pages 2-3, liu2024advancesinnontype pages 1-2).

4. Cellular components
- Key loci of action are extracellular space (alarmins/cytokines), plasma membrane (alarmin/T2/neurogenic receptors), nucleus (Th2 transcriptional mediators), and ECM/subepithelial matrix (fibrosis) (russell2024theairwayepithelium pages 2-3, varricchi2024airwayremodellingin pages 1-2, jean2022neuroimmuneregulatorynetworks pages 10-11).

5. Disease progression
- From initial epithelial insult to chronic inflammation and remodeling, with an alternative non‑T2 trajectory dominated by neutrophilic/Th17–inflammasome pathways and steroid resistance (russell2024theairwayepithelium pages 2-3, varricchi2024airwayremodellingin pages 1-2, liu2024advancesinnontype pages 1-2, khalfaoui2023airwaysmoothmuscle pages 3-4).

6. Phenotypic manifestations
- Clinical variability reflects underlying endotypes. T2‑high: eosinophilia, high FeNO, mucus plugging, robust responses to anti‑IL‑4Rα/anti‑IL‑5/anti‑IgE; Upstream anti‑TSLP shows efficacy across biomarker strata. T2‑low: low FeNO, neutrophilia/pauci‑granulocytic profiles, corticosteroid insensitivity, paucity of targeted options to date (russell2024theairwayepithelium pages 6-7, liu2024advancesinnontype pages 1-2, khalfaoui2023airwaysmoothmuscle pages 3-4).

## Clinical translation: targets, drugs, and ongoing directions
- Anti‑TSLP (tezepelumab) exemplifies upstream epithelial‑alarmin targeting with broad efficacy, biomarker reductions (including airway IL‑33), improved FEV1 and mannitol AHR, and potential structural benefits (e.g., mucus plugging) in severe asthma (russell2024theairwayepithelium pages 6-7, russell2024theairwayepithelium pages 2-3).
- Established T2‑pathway biologics (dupilumab, anti‑IL‑5 class, omalizumab) improve exacerbations and biomarkers; selected studies suggest variable effects on remodeling indices (russell2024theairwayepithelium pages 4-5, russell2024theairwayepithelium pages 6-7).
- Future opportunities: non‑T2 targets (IL‑17/ILC3/inflammasome/IFN‑pathways) and neuro‑immune targets (TRPA1/TRPV1, cholinergic/neuropeptide axes) to address T2‑low/steroid‑resistant disease and upstream drivers of both bronchomotor and inflammatory responses (liu2024advancesinnontype pages 1-2, khalfaoui2023airwaysmoothmuscle pages 3-4, jean2022neuroimmuneregulatorynetworks pages 10-11).

Key recent sources with URLs and publication dates
- Russell RJ et al., The airway epithelium: ERJ, Mar 2024. DOI: 10.1183/13993003.01397-2023. URL: https://doi.org/10.1183/13993003.01397-2023 (russell2024theairwayepithelium pages 2-3, russell2024theairwayepithelium pages 6-7)
- Varricchi G et al., Airway remodelling and the epithelium: ERJ, Apr 2024. DOI: 10.1183/13993003.01619-2023. URL: https://doi.org/10.1183/13993003.01619-2023 (varricchi2024airwayremodellingin pages 1-2)
- Brightling CE et al., The epithelial era: ERR, Oct 2024. DOI: 10.1183/16000617.0221-2024. URL: https://doi.org/10.1183/16000617.0221-2024 (brightling2024theepithelialera pages 4-5)
- Liu T et al., Non‑type 2 severe asthma: ERJ, May 2024. DOI: 10.1183/13993003.00826-2023. URL: https://doi.org/10.1183/13993003.00826-2023 (liu2024advancesinnontype pages 1-2)
- Khalfaoui L & Pabelick CM, ASM in asthma: Expert Opin Ther Targets, Jan 2023. DOI: 10.1080/14728222.2023.2177533. URL: https://doi.org/10.1080/14728222.2023.2177533 (khalfaoui2023airwaysmoothmuscle pages 12-14, khalfaoui2023airwaysmoothmuscle pages 3-4)
- Jean EE et al., Neuroimmune regulatory networks: J Leukoc Biol, Apr 2022. DOI: 10.1002/jlb.3ru0121-023r. URL: https://doi.org/10.1002/jlb.3ru0121-023r (jean2022neuroimmuneregulatorynetworks pages 10-11)
- Özçam M & Lynch SV, Gut–airway microbiome axis: Nat Rev Microbiol, May 2024. DOI: 10.1038/s41579-024-01048-8. URL: https://doi.org/10.1038/s41579-024-01048-8 (kato2025theimmunologyof pages 29-30)

Notes on evidence limitations
- Direct histologic reversal of established remodeling by biologics remains incompletely defined; reviews emphasize a need for longer-term structural endpoints and epithelial-targeted strategies (varricchi2024airwayremodellingin pages 1-2, russell2024theairwayepithelium pages 6-7). 
- Non‑T2 targets are mechanistically supported, but late‑phase clinical validation is still limited (liu2024advancesinnontype pages 1-2, khalfaoui2023airwaysmoothmuscle pages 3-4).


References

1. (varricchi2024airwayremodellingin pages 1-2): Gilda Varricchi, Christopher E. Brightling, Christopher Grainge, Bart N. Lambrecht, and Pascal Chanez. Airway remodelling in asthma and the epithelium: on the edge of a new era. The European Respiratory Journal, 63:2301619, Apr 2024. URL: https://doi.org/10.1183/13993003.01619-2023, doi:10.1183/13993003.01619-2023. This article has 88 citations.

2. (russell2024theairwayepithelium pages 2-3): Richard J. Russell, Louis-Philippe Boulet, Christopher E. Brightling, Ian D. Pavord, Celeste Porsbjerg, Del Dorscheid, and Asger Sverrild. The airway epithelium: an orchestrator of inflammation, a key structural barrier and a therapeutic target in severe asthma. The European Respiratory Journal, 63:2301397, Mar 2024. URL: https://doi.org/10.1183/13993003.01397-2023, doi:10.1183/13993003.01397-2023. This article has 78 citations.

3. (russell2024theairwayepithelium pages 6-7): Richard J. Russell, Louis-Philippe Boulet, Christopher E. Brightling, Ian D. Pavord, Celeste Porsbjerg, Del Dorscheid, and Asger Sverrild. The airway epithelium: an orchestrator of inflammation, a key structural barrier and a therapeutic target in severe asthma. The European Respiratory Journal, 63:2301397, Mar 2024. URL: https://doi.org/10.1183/13993003.01397-2023, doi:10.1183/13993003.01397-2023. This article has 78 citations.

4. (liu2024advancesinnontype pages 1-2): Tao Liu, Prescott G. Woodruff, and Xiaobo Zhou. Advances in non-type 2 severe asthma: from molecular insights to novel treatment strategies. The European Respiratory Journal, 64:2300826, May 2024. URL: https://doi.org/10.1183/13993003.00826-2023, doi:10.1183/13993003.00826-2023. This article has 45 citations.

5. (khalfaoui2023airwaysmoothmuscle pages 3-4): Latifa Khalfaoui and Christina M. Pabelick. Airway smooth muscle in contractility and remodeling of asthma: potential drug target mechanisms. Expert Opinion on Therapeutic Targets, 27:19-29, Jan 2023. URL: https://doi.org/10.1080/14728222.2023.2177533, doi:10.1080/14728222.2023.2177533. This article has 36 citations and is from a peer-reviewed journal.

6. (jean2022neuroimmuneregulatorynetworks pages 10-11): E Evonne Jean, Olivia Good, Juan M Inclan Rico, Heather L Rossi, and De'Broski R Herbert. Neuroimmune regulatory networks of the airway mucosa in allergic inflammatory disease. Journal of Leukocyte Biology, 111:209-221, Apr 2022. URL: https://doi.org/10.1002/jlb.3ru0121-023r, doi:10.1002/jlb.3ru0121-023r. This article has 32 citations and is from a peer-reviewed journal.

7. (kato2025theimmunologyof pages 29-30): Atsushi Kato and Hirohito Kita. The immunology of asthma and chronic rhinosinusitis. Nature reviews. Immunology, 25:569-587, Apr 2025. URL: https://doi.org/10.1038/s41577-025-01159-0, doi:10.1038/s41577-025-01159-0. This article has 10 citations.

8. (hansi2024regulationofairway pages 21-22): Ravneet K. Hansi, Maral Ranjbar, Christiane E. Whetstone, and Gail M. Gauvreau. Regulation of airway epithelial-derived alarmins in asthma: perspectives for therapeutic targets. Biomedicines, 12:2312, Oct 2024. URL: https://doi.org/10.3390/biomedicines12102312, doi:10.3390/biomedicines12102312. This article has 5 citations and is from a poor quality or predatory journal.

9. (khalfaoui2023airwaysmoothmuscle pages 12-14): Latifa Khalfaoui and Christina M. Pabelick. Airway smooth muscle in contractility and remodeling of asthma: potential drug target mechanisms. Expert Opinion on Therapeutic Targets, 27:19-29, Jan 2023. URL: https://doi.org/10.1080/14728222.2023.2177533, doi:10.1080/14728222.2023.2177533. This article has 36 citations and is from a peer-reviewed journal.

10. (yao2025modulatingtrpv1and pages 2-4): Xiang Yao, Xuejian Zhang, Tao Cui, Meiling Jian, Hao Wu, Chunjie Wu, and Feiyan Tao. Modulating trpv1 and trpa1 channels: a viable strategy for treating asthma using chinese herbal medicines. Frontiers in Pharmacology, Jul 2025. URL: https://doi.org/10.3389/fphar.2025.1573901, doi:10.3389/fphar.2025.1573901. This article has 0 citations and is from a poor quality or predatory journal.

11. (brightling2024theepithelialera pages 4-5): Christopher E. Brightling, Gianni Marone, Helena Aegerter, Pascal Chanez, Enrico Heffler, Ian D. Pavord, Klaus F. Rabe, Lena Uller, and Del Dorscheid. The epithelial era of asthma research: knowledge gaps and future direction for patient care. European Respiratory Review, 33:240221, Oct 2024. URL: https://doi.org/10.1183/16000617.0221-2024, doi:10.1183/16000617.0221-2024. This article has 7 citations and is from a peer-reviewed journal.

12. (russell2024theairwayepithelium pages 4-5): Richard J. Russell, Louis-Philippe Boulet, Christopher E. Brightling, Ian D. Pavord, Celeste Porsbjerg, Del Dorscheid, and Asger Sverrild. The airway epithelium: an orchestrator of inflammation, a key structural barrier and a therapeutic target in severe asthma. The European Respiratory Journal, 63:2301397, Mar 2024. URL: https://doi.org/10.1183/13993003.01397-2023, doi:10.1183/13993003.01397-2023. This article has 78 citations.