# Phylogenetic Analysis of Cdc42 in Fungi
**Exploring the Evolutionary Conservation of Cell Polarity Regulators**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Bioinformatics](https://img.shields.io/badge/Field-Bioinformatics-green.svg)](https://en.wikipedia.org/wiki/Bioinformatics)
[![Lab](https://img.shields.io/badge/Target-IISc%20Palani%20Lab-red.svg)](https://palani-lab.github.io/)

---

##  Project Overview
This project investigates the evolutionary history of **Cdc42**, a critical Rho-family GTPase that governs cell polarity and cytoskeleton organization. By performing a comparative phylogenetic analysis across diverse fungal species, we identify highly conserved functional domains essential for cell division.

This repository demonstrates a complete bioinformatics pipeline—from automated sequence retrieval to Maximum Likelihood tree reconstruction.

##  Research Workflow
The analysis follows a rigorous 4-step computational pipeline:

1.  **Data Acquisition:** Automated retrieval of protein sequences from **NCBI Protein DB** using `Biopython`.
2.  **Multiple Sequence Alignment (MSA):** Sequence alignment performed using **MAFFT** to identify homologous regions.
3.  **Alignment Quality Control:** Trimming of gaps and non-informative sites using **trimAl** to enhance phylogenetic signal.
4.  **Phylogenetic Reconstruction:** Building a Maximum Likelihood tree using **IQ-TREE** with automated model selection (**ModelFinder**) and **Ultrafast Bootstrapping** (1000 replicates).

##  Tech Stack & Tools
| Tool | Purpose |
| :--- | :--- |
| **Python** | Scripting & Data Retrieval (Biopython) |
| **Bash** | Pipeline Automation & Shell Scripting |
| **MAFFT** | High-speed Sequence Alignment |
| **trimAl** | Automated Alignment Trimming |
| **IQ-TREE** | Maximum Likelihood Phylogeny |
| **iTOL** | Tree Visualization & Annotation |

##  Repository Structure
```text
├── fetch_sequences.py   # Python script for NCBI data mining
├── pipeline.sh          # Master bash script to run the bio-tools
├── README.md            # Project documentation
└── [Output Files]       # Alignment and Tree files (generated after run)
```

##  How to Reproduce
### 1. Prerequisites
Ensure you have the following installed:
*   Python 3.x (`pip install biopython`)
*   Conda (`conda install -c bioconda mafft trimal iqtree`)

### 2. Execution
```bash
# Clone the repository
git clone https://github.com/Pavithra-Bandaru/Phylogenetic-Analysis.git
cd Phylogenetic-Analysis

# 1. Fetch sequences from NCBI
python fetch_sequences.py

# 2. Run the full alignment and tree pipeline
bash pipeline.sh
```

##  Expected Insights
The resulting phylogenetic tree (`.treefile`) reveals the divergence of Cdc42 across:
*   **Ascomycota** (e.g., *S. cerevisiae*, *N. crassa*)
*   **Basidiomycota** (e.g., *C. neoformans*, *P. graminis*)

High bootstrap values at internal nodes indicate a robust evolutionary signal, confirming Cdc42 as one of the most conserved proteins in the fungal kingdom.

---
**Author:** Pavithra Bandaru  
*3rd Year Biotechnology Student | Ramaiah Institute of Technology*
