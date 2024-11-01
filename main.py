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
    triplets = triplets_unsorted[start_index:end_index]

    return triplets


def get_amino_acids(triplets):
    """Get amino acids corresponding to organic base triplets in the sorted RNA"""
    amino_acids = []
    for triplet in triplets:
        # Go through every base in triplet, add equivalent amino acid to list (RNA code table)
        match triplet[0]:
            case "G": 
                match triplet[1]:
                    case "G": 
                        amino_acids.append("Glys")                                                   
                    case "U":
                        amino_acids.append("Val")
                    case "A":
                        if triplet[2] == "A" or "G":
                            amino_acids.append("Glu")
                        else:
                            amino_acids.append("Asp")
                    case "C":         
                        amino_acids.append("Ala")                                      
            case "U":
                match triplet[1]:
                    case "G":
                        if triplet[2] == "G":
                            amino_acids.append("Trp") 
                        else:
                            amino_acids.append("Cys")                           
                    case "U":
                        if triplet[2] == "A" or "G":
                            amino_acids.append("Leu")
                        else:
                            amino_acids.append("Phe")
                    case "A":
                        amino_acids.append("Tyr")
                    case "C":              
                        amino_acids.append("Ser")      
            case "A":
                match triplet[1]:
                    case "G":     
                        if triplet[2] == "A" or "G":
                            amino_acids.append("Arg")
                        else:
                            amino_acids.append("Ser")                       
                    case "U":
                        if triplet[2] == "G":
                            amino_acids.append("Met")
                        else:
                            amino_acids.append("Ile")
                    case "A":
                        if triplet[2] == "A" or "G":
                            amino_acids.append("Lys")
                        else:
                            amino_acids.append("Asn")
                    case "C":           
                        amino_acids.append("Thr")         
            case "C":
                match triplet[1]:
                    case "G":      
                        amino_acids.append("Arg")                      
                    case "U":
                        amino_acids.append("Leu")
                    case "A":
                        if triplet[2] == "A" or "G":
                            amino_acids.append("Gln")
                        else:
                            amino_acids.append("His")
                    case "C":                    
                        amino_acids.append("Pro")

    return amino_acids



def main():
    dna_sequence = "TACACGAGCGATTCTATT"

    triplets = sort_triplets(convert(dna_sequence))
    print(get_amino_acids(triplets))



main()
