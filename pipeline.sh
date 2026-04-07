#!/bin/bash

# Define filenames
INPUT="cdc42_fungi_raw.fasta"
ALIGNED="cdc42_fungi_aligned.fasta"
TRIMMED="cdc42_fungi_trimmed.fasta"

# 1. Multiple Sequence Alignment with MAFFT
echo "--- Running MAFFT (Alignment) ---"
mafft --auto $INPUT > $ALIGNED

# 2. Trim low-quality regions with trimAl
echo "--- Running trimAl (Cleaning) ---"
trimal -in $ALIGNED -out $TRIMMED -automated1

# 3. Maximum Likelihood Tree Building with IQ-TREE
echo "--- Running IQ-TREE (Tree Reconstruction) ---"
iqtree -s $TRIMMED -m MFP -bb 1000 -nt AUTO

echo "--- Project Pipeline Complete! ---"
echo "Your tree file is: $TRIMMED.treefile"
