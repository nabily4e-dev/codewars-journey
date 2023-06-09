# def dna_to_rna(dna):
#   """Converts DNA to RNA.

#   Args:
#     dna: A string of DNA.

#   Returns:
#     A string of RNA.
#   """

#   rna = ""
#   for c in dna:
#     if c == "T":
#       rna += "U"
#     else:
#       rna += c

#   return rna

def dna_to_rna(dna):
    retun dna.replace('T', 'U')


if __name__ == "__main__":
  dna = "ACGTACGT"
  rna = dna_to_rna(dna)
  print(rna)
