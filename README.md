# Phylogenetic Analysis of Cdc42 in Fungi

## Project Overview

This project investigates the evolutionary conservation of Cdc42, a Rho-family GTPase involved in cell polarity and cytoskeleton organization. Protein sequences from multiple fungal species were compared to study evolutionary relationships.

---

## Methodology

### Data Collection

Initial sequence retrieval was attempted using Biopython. Due to inconsistencies in automated queries, sequences were manually curated from NCBI to ensure that only true Cdc42 proteins were included.

### Multiple Sequence Alignment

Protein sequences were aligned using the MAFFT online tool to identify conserved regions across species.

### Phylogenetic Analysis (Tool-based)

A phylogenetic tree was constructed using Phylogeny.fr based on the aligned sequences.

### Phylogenetic Analysis (Python-based)

A second phylogenetic tree was generated using Python (Biopython) by calculating sequence distances and constructing a Neighbor Joining tree.

---

## Results

* Cdc42 sequences are highly conserved (~190–200 amino acids)
* Strong sequence similarity observed across fungal species
* Phylogenetic trees show clustering of related organisms

---

## Phylogenetic Trees

### Tool-based Tree

![Tool Tree](tree_tool.png)

### Python-based Tree

![Code Tree](tree_code.png)

---

## Interpretation

The phylogenetic trees indicate that Cdc42 is highly conserved across fungal species. Closely related organisms cluster together, reflecting known evolutionary relationships. Similar clustering patterns in both approaches support the consistency of the analysis.

---

## Tools Used

* Python (Biopython)
* MAFFT (online)
* Phylogeny.fr

---

## Author

Pavithra Bandaru
Undergraduate Student, Biotechnology
