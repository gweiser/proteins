from textwrap import wrap
def convert(dna_sequence):
    """Convert DNA sequence to RNA equivalent"""
    rna_sequence = []
    for i in dna_sequence:
        # Find counterpart for each organic base in DNA
        match i:
            case "A":
                rna_sequence.append("U")
            case "T":
                rna_sequence.append("A")
            case "G":
                rna_sequence.append("C")
            case "C":
                rna_sequence.append("G")

    return "".join(rna_sequence)


def sort_triplets(rna_sequence):
    """Sort triplets to start and end properly"""
    # Split RNA into triplets
    triplets_unsorted = wrap(rna_sequence, 3)

    
    start_triplet = "AUG"
    end_triplets = ["UAA", "UAG", "UGA"]

    # Find indices for start and end of useable RNA 
    start_index = triplets_unsorted.index(start_triplet)
    for i in triplets_unsorted:
        if i in end_triplets:
            end_index = triplets_unsorted.index(i)
            break
    # Cut out unnecessary organic bases from RNA
    triplets = triplets_unsorted[start_index+1:end_index]

    return triplets


def get_amino_acids(triplets):
    """Get amino acids corresponding to organic base triplets in the sorted RNA"""
    


def main():
    dna_sequence = "TACGGGTTTCCCATTGCT"

    print(sort_triplets(convert(dna_sequence)))



main()
