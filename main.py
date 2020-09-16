import converterFunctions as cf
#------------------------------------------------------------------------------------------------------------------
print("\n"+"Prompt".center(86, "-"))
print("Please type DNA or RNA into the search bar:\n")

strand = input().strip()

print("\nPlease type 5-3 or 3-5 for the directionality of your template strand:\n")

check_strand = input().strip()

print("\n" + "Confirmation: " + strand + ", " + check_strand)

#-----------------------------------------------------------------------------------------------------------------
if check_strand == '5-3' and strand == 'DNA':
    
    print("\nNow, please type in your 'DNA' template strand: \n")
    dna_template_strand = input().upper()
    print(cf.convert_dna_5_3(dna_template_strand))

elif check_strand == '3-5' and strand == 'DNA':
    
    print("\nNow, please type in your 'DNA' template strand: \n")
    dna_template_strand = input().upper()
    print(cf.convert_dna_3_5(dna_template_strand))
    
#------------------------------------------------------------------------------------------------------------------
if check_strand == '5-3' and strand == 'RNA':
    
    print("\nNow, please type in your 'RNA' template strand: \n")
    rna_template_strand = input().upper()
    print(cf.convert_rna_5_3(rna_template_strand))

elif check_strand == '3-5' and strand == 'RNA':
    
    print("Now, please type in your 'RNA' template strand: ")
    rna_template_strand = input().upper()
    print(cf.convert_rna_3_5(rna_template_strand))

