import nucleicfunctions as nf 

#--------------------------------------------------------------------------------------------------------

# This is a basic use of the functions in the converterFunctions script. The 
# nucleic acid strands are assigned to variables that specify the type of nucleic acid.
# Lastly, the program passes the variables to the functions of the converterFunctins script, and
# prints out the results: the complementary strand of the specified nucleic acid, the base-pairing
# representation, and the amino acid sequence if the variable that was passed was the variable assigned
# an mRNA strand. 

#--------------------------------------------------------------------------------------------------------

#DNA strand 5-3 directionality
first_dna_strand_example_5_3 = 'ACTGATCATCGATCGATGCATGCTACGTAGCTAGCTAGCGATCGTCGTAGCTAGCTAGCTAGC'

#DNA strand 3-5 directionality
second_dna_strand_example_3_5 = 'CGCGATGCTAGCTAGCTAGCTAGCTAGCTAGCTGACTGATCGTACGTAGCTAGCTACTGACTG'

#mRNA strand 
mRNA_strand_example = 'GACCUCGUCCGGGAUGAAACGUCUCAAUGAGGAAGGUGGACAUAUGCU'


print(nf.convert_dna_5_3(first_dna_strand_example_5_3))

print(nf.convert_dna_3_5(second_dna_strand_example_3_5))

print(nf.convert_rna(mRNA_strand_example))



#-------END OF CODE---------------------- END OF CODE--------------------------END OF CODE-------------------------