from Bio import AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio import Phylo

# Load aligned sequences
alignment = AlignIO.read("aligned.fasta", "fasta")

# Calculate distance matrix
calculator = DistanceCalculator('identity')
dm = calculator.get_distance(alignment)

# Build tree (Neighbor Joining)
constructor = DistanceTreeConstructor()
tree = constructor.nj(dm)

# Save tree
Phylo.write(tree, "tree_code.xml", "phyloxml")

# Show tree
Phylo.draw(tree)