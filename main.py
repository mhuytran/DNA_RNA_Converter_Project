import converterFunctions as cf

print("Please type DNA or RNA into the search bar for what you desire to do:\n ")

strand = input().strip()

print("\nPlease type 5-3 or 3-5 for the directionality of your template strand: \n")

checkStrand = input().strip()

print("\n" "Confirmation: " + strand + ", " + checkStrand)

if checkStrand == '5-3' and strand == 'DNA':
    print("Now, please type in your 'DNA' strand: ")
    dnaOriginalStrand = input()
    print("\n" + "5'-" + dnaOriginalStrand + "-'3" + "\n" + "3'-" + cf.convertDNA(dnaOriginalStrand) + "-'5")

elif checkStrand == '3-5' and strand == 'DNA':
    print("Now, please type in your 'DNA' strand: ")
    dnaOriginalStrand = input()
    print("\n" + "3'-" + dnaOriginalStrand + "-'5" + "\n" + "5'-" + cf.convertDNA(dnaOriginalStrand) + "-'3")

elif checkStrand == '5-3' and strand == 'RNA':
    print("Now, please type in your 'RNA' strand: ")
    rnaOriginalStrand = input()
    print("\n" + "5'-" + rnaOriginalStrand + "-'3" + "\n" + "3'-" + cf.convertRNA(rnaOriginalStrand) + "-'5")

elif checkStrand == '3-5' and strand == 'RNA':
    print("Now, please type in your 'RNA' strand: ")
    rnaOriginalStrand = input()
    print("\n" + "3'-" + rnaOriginalStrand + "-'5" + "\n" + "5'-" + cf.convertRNA(rnaOriginalStrand) + "-'3")


