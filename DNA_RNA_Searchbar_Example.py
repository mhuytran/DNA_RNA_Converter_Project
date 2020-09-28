import nucleicfunctions as nf

# This is a searchbar program that showcases what each function outputs.

#----------------------------------------------------------------------------------------------------------------
print("\n"+"Prompt".center(86, "-"))
print("Please enter DNA or mRNA into the search bar:\n")

strand = input().strip().lower()

print("\nPlease enter 5-3 or 3-5 for the directionality of your DNA template strand. If mRNA strand, enter 5-3. \n")

check_strand = input().strip()

print("\n" + "Confirmation: " + strand + ", " + check_strand)

#-----------------------------------------------------------------------------------------------------------------
if (check_strand == '5-3' and strand == 'dna'):
    
    print("\nNow, please type in your 'DNA' template strand: \n")
    dna_template_strand = input().upper()
    print(nf.convert_dna_5_3(dna_template_strand))

elif (check_strand == '3-5' and strand == 'dna'):
    
    print("\nNow, please type in your 'DNA' template strand: \n")
    dna_template_strand = input().upper()
    print(nf.convert_dna_3_5(dna_template_strand))

elif (check_strand == "5-3" and strand == 'mrna'):
    
    print("\nNow, please type in your 'mRNA' template strand: \n")
    mRNA_template_strand = input().upper()
    print(nf.convert_rna(mRNA_template_strand))
  
else:
    raise Exception("Please re-run code, you either not enter the correct syntax or input the nucleic acid and directionality")

#-------END OF CODE---------------------- END OF CODE--------------------------END OF CODE-------------------------
