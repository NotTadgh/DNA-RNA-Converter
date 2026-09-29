def do_transcription(dna):
    rna = ""
    if dna.startswith("5'") and dna.endswith("3'"):
        dna = dna[2:-2]

    for character in dna:
        if character == "A":
            rna += "U"
        elif character == "T":
            rna += "A"
        elif character == "C":
            rna += "G"
        elif character == "G":
            rna += "C"
        elif character == " ":
            rna += ""
        elif character == "-":
            rna += ""
    return rna

def do_translation(rna):
    amino_acid = ""

    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]

        if codon == "UUU" or codon == "UUC":
            amino_acid += "Phe"
        elif codon == "UUA" or codon == "UUG":
            amino_acid += "Leu"
        elif codon == "CUU" or codon == "CUC" or codon == "CUA" or codon == "CUG":
            amino_acid += "Leu"
        elif codon == "AUU" or codon == "AUC" or codon == "AUA":
            amino_acid += "Ile"
        elif codon == "AUG":
            amino_acid += "Met"
        elif codon == "GUU" or codon == "GUC" or codon == "GUA" or codon == "GUG":
            amino_acid += "Val"
        elif codon == "UCU" or codon == "UCC" or codon == "UCA" or codon == "UCG":
            amino_acid += "Ser"
        elif codon == "CCU" or codon == "CCC" or codon == "CCA" or codon == "CCG":
            amino_acid += "Pro"
        elif codon == "ACU" or codon == "ACC" or codon == "ACA" or codon == "ACG":
            amino_acid += "Thr"
        elif codon == "GCU" or codon == "GCC" or codon == "GCA" or codon == "GCG":
            amino_acid += "Ala"
        elif codon == "UAU" or codon == "UAC":
            amino_acid += "Tyr"
        elif codon == "UAA" or codon == "UAG" or codon == "UGA":
            amino_acid += "Stop"
        elif codon == "CAU" or codon == "CAC":
            amino_acid += "His"
        elif codon == "CAA" or codon == "CAG":
            amino_acid += "Gln"
        elif codon == "AAU" or codon == "AAC":
            amino_acid += "Asn"
        elif codon == "AAA" or codon == "AAG":
            amino_acid += "Lys"
        elif codon == "GAU" or codon == "GAC":
            amino_acid += "Asp"
        elif codon == "GAA" or codon == "GAG":
            amino_acid += "Glu"
        elif codon == "UGU" or codon == "UGC":
            amino_acid += "Cys"
        elif codon == "UGG":
            amino_acid += "Trp"
        elif codon == "CGU" or codon == "CGC" or codon == "CGA" or codon == "CGG" or codon == "AGA" or codon == "AGG":
            amino_acid += "Arg"
        elif codon == "AGU" or codon == "AGC":
            amino_acid += "Ser"
        elif codon == "GGU" or codon == "GGC" or codon == "GGA" or codon == "GGG":
            amino_acid += "Gly"
    return amino_acid

choice = input("Transcribe or Translate? (a/b): ")
if choice == "a":
    dna = input("Enter DNA Sequence: ")
    rna = do_transcription(dna)
    print("RNA Sequence: " + rna)
    choice_2 = input("Do you want to translate this RNA Sequence? (y/n): ")
    if choice_2 == "y" or choice_2 == "Y":
        amino_acid = do_translation(rna)
        print("Amino Acid Sequence: " + amino_acid)
elif choice == "b":
    rna = input("Enter RNA Sequence: ")
    amino_acid = do_translation(rna)
    print("Amino Acid Sequence: " + amino_acid)
