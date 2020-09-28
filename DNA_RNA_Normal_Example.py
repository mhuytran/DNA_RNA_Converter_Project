import nucleicfunctions as nf 

#--------------------------------------------------------------------------------------------------------

# This is a basic use of the functions in the converterFunctions script.
# The convert_dna_5_3 function will copy the outputted mRNA strand to the clipboard, 
# and can be inputted into the convert_rna function. This process can also be done with
# the convert_dna_5_3 function

#--------------------------------------------------------------------------------------------------------

#Assuming that you know the directionality, the DNA strand example will have a 5-3 directionality

dna_strand = 'ACTGATCATCGATCGATGCATGCTACGTAGCTAGCTAGCGATCGTCGTAGCTAGCTAGCTAGC'

print(nf.convert_dna_5_3(dna_strand))

x = input('\n\nEnter a mRNA strand: ')

print(nf.convert_rna(x))

#-------END OF CODE---------------------- END OF CODE--------------------------END OF CODE-------------------------