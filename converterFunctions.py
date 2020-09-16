#creating module

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

