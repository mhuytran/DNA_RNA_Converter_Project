# First Prompt Question

print("Please type DNA or RNA into the search bar for what you desire to do:\n ")

strand = input().strip()

#Second Prompt Question 

print("\nPlease type 5-3 or 3-5 for the directionality of your template strand: \n")

checkStrand = input().strip()

print("\n" "Confirmation: " + strand + ", " + checkStrand)

# DNA Convert to Complementary Strand Function
def convertDNA(dnaOriginalStrand):
    flag = True
    while flag == True:
        for letter in dnaOriginalStrand:
            if letter == '5' or letter == '3' or letter == 'U':
                print("I'm sorry, please correctly type your DNA strand. DO NOT INCLUDE A U, 5'CAP, or 3'CAP")
                dnaOriginalStrand = input()
        else:
            flag = False
            break

    if "5" or "3" not in dnaOriginalStrand:
        dnaCStrand = []
        for base in dnaOriginalStrand:
            if base == 'A':
                dnaCStrand.append('T')
            elif base == 'T':
                dnaCStrand.append('A')
            elif base == 'C':
                dnaCStrand.append('G')
            elif base == 'G':
                dnaCStrand.append('C')
        else:
            dnaComplementaryStrand = ''.join(dnaCStrand)

    return dnaComplementaryStrand


# RNA Convert to Complementary Strand Function
def convertRNA(rnaOriginalStrand):
    flag = True
    while flag == True:
        for letter in rnaOriginalStrand:
            if letter == '5' or letter == '3' or letter == 'T':
                print(
                    "I'm sorry, please correctly type your RNA strand, and DO NOT INCLUDE A T, 5' CAP, or 3' CAP ends")
                rnaOriginalStrand = input()
        else:
            flag = False
            break

    if "5" or "3" not in rnaOriginalStrand:
        rnaCStrand = []
        for base in rnaOriginalStrand:
            if base == 'A':
                rnaCStrand.append('U')
            elif base == 'U':
                rnaCStrand.append('A')
            elif base == 'C':
                rnaCStrand.append('G')
            elif base == 'G':
                rnaCStrand.append('C')
        else:
            rnaComplementaryStrand = ''.join(rnaCStrand)

    return rnaComplementaryStrand


# flow control to get certain directionality and strand type
# khan academy example 'CGCATGTAGCGA'

if checkStrand == '5-3' and strand == 'DNA':
    print("Now, please type in your 'DNA' strand: ")
    dnaOriginalStrand = input()
    print("\n" + "5'-" + dnaOriginalStrand + "-'3" + "\n" + "3'-" + convertDNA(dnaOriginalStrand) + "-'5")

elif checkStrand == '3-5' and strand == 'DNA':
    print("Now, please type in your 'DNA' strand: ")
    dnaOriginalStrand = input()
    print("\n" + "3'-" + dnaOriginalStrand + "-'5" + "\n" + "5'-" + convertDNA(dnaOriginalStrand) + "-'3")

elif checkStrand == '5-3' and strand == 'RNA':
    print("Now, please type in your 'RNA' strand: ")
    rnaOriginalStrand = input()
    print("\n" + "5'-" + rnaOriginalStrand + "-'3" + "\n" + "3'-" + convertRNA(rnaOriginalStrand) + "-'5")

elif checkStrand == '3-5' and strand == 'RNA':
    print("Now, please type in your 'RNA' strand: ")
    rnaOriginalStrand = input()
    print("\n" + "3'-" + rnaOriginalStrand + "-'5" + "\n" + "5'-" + convertRNA(rnaOriginalStrand) + "-'3")


