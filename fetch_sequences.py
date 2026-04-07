import os
from Bio import Entrez, SeqIO

#  Configuration 
# Enter your email address so NCBI can contact you if there's a problem
Entrez.email = "your_email@example.com"

# List target fungal species (model organisms + others for diversity)
species_list = [
    "Saccharomyces cerevisiae",
    "Schizosaccharomyces pombe",
    "Candida albicans",
    "Neurospora crassa",
    "Aspergillus nidulans",
    "Cryptococcus neoformans",
    "Ustilago maydis",
    "Coprinopsis cinerea",
    "Puccinia graminis",
    "Rhizopus delemar"
]

def fetch_cdc42_sequence(species_name):
    """
    Search NCBI Protein database for 'Cdc42' in a given species
    and return the first matching sequence record.
    """
    search_term = f"Cdc42[Protein Name] AND {species_name}[Organism]"
    print(f"Searching for: {search_term}...")
    
    try:
        # 1. Search for the protein
        with Entrez.esearch(db="protein", term=search_term) as handle:
            record = Entrez.read(handle)
        
        if not record["IdList"]:
            print(f"  [!] No sequences found for {species_name}")
            return None
        
        # 2. Fetch the top result (IdList[0])
        protein_id = record["IdList"][0]
        with Entrez.efetch(db="protein", id=protein_id, rettype="fasta", retmode="text") as handle:
            fasta_data = handle.read()
            
        return fasta_data
        
    except Exception as e:
        print(f"  [!] Error fetching {species_name}: {e}")
        return None

def main():
    all_fasta_content = []
    
    for species in species_list:
        fasta_record = fetch_cdc42_sequence(species)
        if fasta_record:
            all_fasta_content.append(fasta_record)
            
    # Save all sequences into one multi-FASTA file
    output_filename = "cdc42_fungi_raw.fasta"
    with open(output_filename, "w") as f:
        f.write("\n".join(all_fasta_content))
    
    print(f"\nSuccess! All sequences saved to: {output_filename}")

if __name__ == "__main__":
    main()
