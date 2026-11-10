# 1.1 - Retrieve Protein Sequence Data
from Bio import Entrez
from Bio import SeqIO

Entrez.email = "zariff@graduate.utm.my"
handle = Entrez.efetch(db='protein', id='P04637', rettype='fasta', retmode='text')

record = SeqIO.read(handle, 'fasta')

print(f"Raw record returned: \n{record}")
print(f"\nSequence: \n{record.seq}")
print(f"\nDescription: \n{record.description}")
print(f"\nName: \n{record.name}")

# 1.2 Basic analyses of protein sequence
from Bio.SeqUtils.ProtParam import ProteinAnalysis

# Calculate length of the protein sequene using len() 
print(len(record.seq))

seq_analysis = ProteinAnalysis(record.seq)

# Get amino acid composition of the protein sequence
print(seq_analysis.count_amino_acids())

# Get the molecular weight of the protein sequence
print(seq_analysis.molecular_weight())

# Get the isoelectric point of the protein sequence
print(seq_analysis.isoelectric_point())