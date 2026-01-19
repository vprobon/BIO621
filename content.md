# BIO621 - Computational and Systems Biology I - Content and Schedule (Spring 2026)

## Instructor: Asscociate Prof. [Vasilis J Promponas](https://www.ucy.ac.cy/dir/el/component/comprofiler/userprofile/vprobon). [vprobon@ucy.ac.cy](mailto:vprobon@ucy.ac.cy)

### DETAILED TEACHING SCHEDULE (Check regularly for updates)

# Weeks 1–4 (19/01-13/02/2026): Python crash course

---

## Week 1 – Python fundamentals & biological data
**Lecture topics**
- What is computational & systems biology?
- Python, Jupyter, Google Colab basics
- Variables, data types, control flow
- Strings & biological sequences

**Practical examples**
- Reading FASTA files
- Counting nucleotide and amino acid frequencies
- GC content calculation

**Exercises**
- Write a script to compute GC content for multiple sequences
- Identify longest ORF in a DNA sequence

**Tutorial focus**
- Debugging, indentation, common Python errors

---

## Week 2 – Data structures & file handling
**Lecture topics**
- Lists, tuples, dictionaries, sets
- File I/O (FASTA, TSV)
- Writing simple reusable scripts

**Practical examples**
- Codon usage analysis
- k-mer counting
- Parsing UniProt FASTA headers

**Exercises**
- Compute codon usage bias for a bacterial genome
- Compare k-mer profiles between two sequences

**Tutorial focus**
- Designing clean functions

---

## Week 3 – Libraries for biological data analysis
**Lecture topics**
- NumPy basics
- Pandas for tabular biological data
- Introduction to Biopython

**Practical examples**
- Parsing GenBank files
- Sequence translation & transcription
- Handling expression matrices

**Exercises**
- Extract CDS features from GenBank and compute protein lengths
- Build a summary table of genes per chromosome

**Tutorial focus**
- Pandas indexing, filtering, plotting

---

## Week 4 – Visualization, statistics & reproducibility
**Lecture topics**
- Matplotlib & Seaborn
- Basic statistics (mean, variance, correlation)
- Reproducible notebooks & documentation

**Practical examples**
- GC content distribution plots
- Length distributions of proteins

**Exercises**
- Compare GC content across genomes
- Visualize amino acid composition biases

**Tutorial focus**
- Notebook hygiene, markdown, commenting

---

# Weeks 5–6: Protein sequence analysis

---

## Week 5 – Protein composition & intrinsic disorder
**Lecture topics**
- Amino acid composition & bias
- Low-complexity regions
- Intrinsically Disordered Regions (IDRs)

**Practical examples**
- AA composition profiling
- Using IUPred / DISOPRED (web + batch)
- Sliding-window disorder analysis

**Exercises**
- Compare disorder content between eukaryotic and bacterial proteomes
- Identify disorder-enriched functional classes

**Tutorial focus**
- Interpreting disorder predictions biologically

---

## Week 6 – Transmembrane proteins & topology
**Lecture topics**
- Alpha-helical vs beta-barrel membrane proteins
- Hydropathy scales
- Topology prediction

**Practical examples**
- Kyte–Doolittle plots
- TMHMM / Phobius predictions
- Consensus TM prediction

**Exercises**
- Identify membrane proteins in a proteome
- Compare predicted vs annotated TM proteins

**Tutorial focus**
- Automating web tools & parsing outputs

---

# Weeks 7–8: Nucleotide sequence analysis

---

## Week 7 – GC content, isochores & genome organization
**Lecture topics**
- GC bias & genome evolution
- Isochores
- Sliding window analyses

**Practical examples**
- GC content along chromosomes
- Detecting GC-rich/poor regions

**Exercises**
- Identify isochores in a eukaryotic chromosome
- Correlate GC content with gene density

**Tutorial focus**
- Window-based algorithms

---

## Week 8 – Gene prediction
**Lecture topics**
- ORFs, signals, content sensors
- Prokaryotic vs eukaryotic gene prediction

**Practical examples**
- ORF finding
- Using Prodigal / AUGUSTUS
- Evaluating predictions

**Exercises**
- Compare gene prediction tools on the same genome
- Analyze false positives/negatives

**Tutorial focus**
- Evaluation metrics (sensitivity, specificity)

---

# Weeks 9–10: Protein structure prediction & analysis

---

## Week 9 – Protein structure basics & prediction
**Lecture topics**
- Levels of protein structure
- Homology modeling
- AlphaFold overview & limitations

**Practical examples**
- Using AlphaFold DB
- Structure visualization (PyMOL / NGLView)

**Exercises**
- Compare predicted vs experimental structures
- Identify disordered regions in structures

**Tutorial focus**
- Structural interpretation

---

## Week 10 – Structural analysis
**Lecture topics**
- Secondary structure assignment
- Structural alignment
- RMSD, TM-score

**Practical examples**
- DSSP
- Structural comparison using BioPython

**Exercises**
- Compare folds within a protein family
- Relate structure to function

**Tutorial focus**
- Automating structure analysis

---

# Weeks 11–12: Gene expression & functional enrichment

---

## Week 11 – Gene expression analysis
**Lecture topics**
- RNA-seq overview
- Normalization concepts
- Differential expression

**Practical examples**
- Analyzing preprocessed RNA-seq matrices
- Using DESeq2-style logic in Python

**Exercises**
- Identify differentially expressed genes
- Visualize MA & volcano plots

**Tutorial focus**
- Interpreting expression results

---

## Week 12 – Functional enrichment & networks
**Lecture topics**
- GO, KEGG, Reactome
- Over-representation analysis
- Gene set enrichment analysis

**Practical examples**
- g:Profiler, Enrichr
- Building functional networks

**Exercises**
- Interpret enriched pathways
- Compare enrichment methods

**Tutorial focus**
- Biological storytelling with data

---

# Week 13: Final projects & synthesis

## Final project examples
- Proteome-wide disorder and function analysis
- Membrane protein landscape of a pathogen
- GC bias and gene density in a eukaryotic genome
- Structure–function analysis of a protein family
- Differential expression & pathway analysis in disease vs control

**Deliverables**
- Colab notebook (reproducible)
- Short written report
- 10–15 min presentation

---

## Skills students will acquire
- Python-based biological data analysis
- Practical experience with real datasets
- Integration of sequence, structure & expression data
- Reproducible research practices

---

[Bioinformatics Research Laboratory @UCY](https://vprobon.github.io/BRL-UCY) 2005-2026.
