#--------------------------------------------------------------------------------------------------------------------------

import functools
import sys
import re
import pyperclip

#---------------------------------------------------------------------------------------------------------------------------
def convert_dna_decorator_5_3(func): 
    
    """
       This convert_dna_decorator_5_3 decorator prints out the results of the convert_dna_5_3 function: 
       the complementary DNA strand, the base-pairing representation, and the mRNA strand that is synthesized from 
       the complementary DNA strand. In addition, the mRNA strand is copied to the clipboard if the user wants utilize the 
       convert_rna function.
        
    Args:
        func([str]): The return value of convert_dna_5_3: a tuple consisting of the complementary_dna_strand,
        the dna_template_strand, and the mRNA_strand. 
        
    Returns:
        str: "Program Status: Done"; to specify that the results have finished printing. 
    """
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        
        print("\n"+"Results".center(86, "-"))
        result = "3'-" + func(*args, **kwargs)[0] + "-'5"
        print("Complementary DNA Strand: " + "\n") 
        print(result + "\n\n")
        print("DNA Template and DNA Complementary Strand Base-Pairing Representation: " + "\n") 
        print("DNA Temp.: "+"5'-" + func(*args, **kwargs)[1] + "-'3" + "\n" + "DNA Comp.: " + "3'-" + func(*args, *kwargs)[0] + "-'5" + "\n\n")
        print("RNA Strand Synthesis Result: " + "\n")
        print("RNA Strand:"+"5'-" + func(*args, **kwargs)[2] + "-'3" + "\n")
        copy_rna_to_clipboard = pyperclip.copy(func(*args, **kwargs)[2])
        
        return "Program Status: Done"

    return wrapper

@convert_dna_decorator_5_3
def convert_dna_5_3(dna_template_strand):
    
    """
       The convert_dna_5_3 function takes in a input DNA strand that has a 5 to 3 directionality,
       and returns a complementary DNA strand that has a 3 to 5 directionality. Function also
       returns an mRNA strand that is synthesized from the complementary strand. 
       
    Args:
        dna_template_strand (str): The template strand.
        
    Returns:
        complementary_dna_strand (str): The complementary strand.
        mRNA_strand (str): The mRNA strand synthesized from the complementary strand. 
        
    """
    
    dna_characters = ['A', 'T', 'C', 'G']
    
    flag = True
    
    while flag == True:
        
        for letter in dna_template_strand:
            
            if letter not in dna_characters:
                raise Exception("DNA Strand Error: Your string contains a 5, 3, or unrecognized characters. Please re-run your code to avoid this problem") 
                sys.exit()
                
        else:
            flag = False
            break
                                   

    if ("5" or "3" or "U" not in dna_template_strand):
        
        c_dna_strand = []
        
        for base in dna_template_strand:
            
            if base == 'A':
                
                c_dna_strand.append('T')
                
            elif base == 'T':
                
                c_dna_strand.append('A')
                
            elif base == 'C':
                
                c_dna_strand.append('G')
                
            elif base == 'G':
                
                c_dna_strand.append('C')
                
        else:
            complementary_dna_strand = ''.join(c_dna_strand)
            
    
    mRNA_strand_list = []  
    
    for base in complementary_dna_strand:
            
        if base == 'A':
            
            mRNA_strand_list.append('U')
            
        elif base == 'T':
            
            mRNA_strand_list.append('A')
            
        elif base == 'C':
            
            mRNA_strand_list.append('G')
            
        elif base == 'G':
            
            mRNA_strand_list.append('C')
                
    else:
        
        mRNA_strand = ''.join(mRNA_strand_list)
                     

    return complementary_dna_strand, dna_template_strand, mRNA_strand


# ---------------------------------------------------------------------------------------------------------------------------
def convert_dna_decorator_3_5(func): 
    
    """
       This convert_dna_decorator_5_3 decorator prints out the results: the complementary DNA strand, the
       base-pairing representation, and the mRNA strand that is synthesized from the template strand.
       In addition, the mRNA strand is copied to the clipboard if the user wants to utilize the convert_rna function.
       
    Args:
        func ([str]): The return value of convert_dna_3_5: a tuple consisting of the complementary_dna_strand
        the dna_template_strand, mRNA_strand.
        
    Returns:
          str: "Program Status: Done"; to specify that the results have finished printing.
    """
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        
        print("\n"+"Results".center(86, "-"))
        result = "5'-" + func(*args, **kwargs)[0] + "-'3"
        print("Complementary DNA Strand: " + "\n") 
        print(result + "\n")
        print("DNA Template and DNA Complementary Strand Base-Pairing Representation: " + "\n") 
        print("DNA Temp.: " + "3'-" + func(*args, **kwargs)[1] + "-'5" + "\n" + "DNA Comp.: " + "5'-" + func(*args, *kwargs)[0] + "-'5" + "\n")
        print("RNA Strand Synthesis Result: " + "\n")
        print("RNA Strand:"+"5'-" + func(*args, **kwargs)[2] + "-'3" + "\n")
        copy_rna_to_clipboard = pyperclip.copy(func(*args, **kwargs)[2])
        return "Program Status: Done"

    return wrapper

@convert_dna_decorator_3_5
def convert_dna_3_5(dna_template_strand):
    
    """
       The convert_dna_3_5 function takes in a input DNA strand that has a 3 to 5 directionality,
       and returns a complementary DNA strand that has a 5 to 3 directionality. Function also returns a RNA strand 
       that is synthesized from the template strand.
       
    Args:
        dna_template_strand (str): The template strand.
        
    Returns:
        complementary_dna_strand (str): The complementary strand.
        mRNA_strand (str): The mRNA strand synthesized from the 3-5 DNA strand. 
        
    """
    
    dna_characters = ['A', 'T', 'C', 'G']
    
    flag = True
    
    while flag == True:
        
        for letter in dna_template_strand:
            
            if letter not in dna_characters:
                raise Exception("DNA Strand Error: Your string contains a 5, 3, or unrecognized characters. Please re-run your code to avoid this problem") 
                sys.exit()
          
        else:
            flag = False
            break
                                   

    if ("5" or "3" or "U" not in dna_template_strand):
        
        c_dna_strand = []
        
        for base in dna_template_strand:
            
            if base == 'A':
                
                c_dna_strand.append('T')
                
            elif base == 'T':
                
                c_dna_strand.append('A')
                
            elif base == 'C':
                
                c_dna_strand.append('G')
                
            elif base == 'G':
                
                c_dna_strand.append('C')
                
        else:
            complementary_dna_strand = ''.join(c_dna_strand)
            

    mRNA_strand_list = []
    
    for base in dna_template_strand: 
        
        if base == 'A':
                
            mRNA_strand_list.append('U')
                
        elif base == 'T':
            
            mRNA_strand_list.append('A')
                
        elif base == 'C':
            
            mRNA_strand_list.append('G')
                
        elif base == 'G':
            
            mRNA_strand_list.append('C')
            
    else: 
        
        mRNA_strand = "".join(mRNA_strand_list)

    return complementary_dna_strand, dna_template_strand, mRNA_strand


#----------------------------------------------------------------------------------------------------------------------------

def convert_rna_decorator(func): 
    
    """
       This convert_rna_decorator function print out the results: the complementary tRNA strand, the base-pairing representation, 
       and the amino acid sequence data.
       
    Args:
        func ([str]): The return value of convert_rna: a tuple consisting of the the mRNA template strand, the complete tRNA sequence, 
        the modified complete tRNA sequence (to display with hyphens), and the amino acid sequence. 
        
    Returns:
        str: "Program Status: Done"; to specify that the results have finished printing.
    """
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        
        print("\n"+"Results".center(86, "-"))
        result = func(*args, **kwargs)[1] 
        print("tRNA sequence: " + "\n") 
        print(result + "\n\n")
        print("mRNA and tRNA base-pairing representation: \n")
        print("mRNA Temp.: " + "5'-" + func(*args, **kwargs)[0] + "-'3" + "\n" + "tRNA  Seq.: " + "   " + func(*args, *kwargs)[1] + "   " + "\n\n")
        print("Amino Acid Sequence Data: \n")
        print("tRNA Codon Sequence: " + func(*args, **kwargs)[2])
        print("Amino Acid Sequence: " + func(*args, **kwargs)[3] + "\n")
        return "Program Status: Done"

    return wrapper


@convert_rna_decorator
def convert_rna(mRNA_template_strand):
    
    """
       The convert_rna_5_3 function takes in a input mRNA strand that has a 5 to 3 directionality,
       and returns a complementary tRNA strand that has a 3 to 5 directionality. 
        
    Args:
        rna_template_strand (str): The single-stranded template RNA strand.
        
    Returns:
        complete_tRNA_strand: The resulting complementary tRNA strand.
        rna_template_strand: The template mRNA strand.
        formatted_amino_acid_sequence: The resulting amino acid sequence. 
    
    """
    
    rna_characters = ['A', 'U', 'C', 'G']
    
    flag = True
    
    while flag == True:
        
        for letter in mRNA_template_strand:
            
            if letter not in rna_characters:
                raise Exception("RNA Strand Error: Your string contains a 5, 3, or unrecognized characters. Please re-run your code to avoid this problem") 
                sys.exit()
                
        else:
            flag = False
            break

    if ("5" or "3" or "T" not in mRNA_template_strand):
        
        tRNA_strand = []
        
        for base in  mRNA_template_strand:
            
            if base == 'A':
                tRNA_strand.append('U')
            elif base == 'U':
                tRNA_strand.append('A')
            elif base == 'C':
                tRNA_strand.append('G')
            elif base == 'G':
                tRNA_strand.append('C')
                
        else:
            
            tRNA_strand_copy = tRNA_strand.copy()
            counter = 0
            
            for base_index in range(3, len(tRNA_strand_copy), 3):
                tRNA_strand_copy.insert(base_index + counter, '-')
                counter += 1
            
            modified_tRNA_sequence = ''.join(tRNA_strand_copy)   
            complete_tRNA_sequence = ''.join(tRNA_strand)
            
    tRNA_pattern = re.compile(r'(U[U|C|A|G][U|C|A|G])|(C[U|C|A|G][U|C|A|G]|A[U|C|A|G][U|C|A|G]|G[U|C|A|G][U|C|A|G])')

    match_obj = tRNA_pattern.finditer(complete_tRNA_sequence)

    match_list = (i.group(0) for i in match_obj)

    amino_acid_sequence = [] 
    
    for codon in match_list: 
    
        if (codon == 'AUG'):
        
            amino_acid_sequence.append('Met')
        
        elif (codon == 'CGU' or
              codon == 'CGC' or
              codon == 'CGA' or
              codon == 'CGG' or 
              codon == 'AGA' or
              codon == 'AGG' ):
            
            amino_acid_sequence.append('Arg')
        
        elif (codon == 'GGU' or
              codon == 'GGC' or
              codon == 'GGA' or 
              codon == 'GGG'):
            
            amino_acid_sequence.append('Gly')
            
        elif (codon == 'UAA' or
              codon == 'UAG' or
              codon == 'UGA'):
            
            amino_acid_sequence.append('TERM')
            
        elif (codon == 'UUA' or
              codon == 'UUG' or
              codon == 'CUU' or
              codon == 'CUC' or
              codon == 'CUA' or
              codon == 'CUG'): 
            
            amino_acid_sequence.append('Leu')
            
        elif (codon == 'AUU' or
              codon == 'AUC' or
              codon == 'AUA'):
            
            amino_acid_sequence.append('Ile')
            
        elif (codon == 'GUU' or
              codon == 'GUC' or
              codon == 'GUA' or
              codon == 'GUG'):
            
            amino_acid_sequence.append('Val')
        
        elif (codon == 'UCU' or
              codon == 'UCC' or  
              codon == 'UCA' or
              codon == 'UCG' or
              codon == 'AGU' or
              codon == 'AGC'):
            
            amino_acid_sequence.append('Ser')
            
        elif (codon == 'CCU' or
              codon == 'CCC' or
              codon == 'CCA' or
              codon == 'CCG'):
            
            amino_acid_sequence.append('Pro')
            
        elif (codon == 'ACU' or 
              codon == 'ACC' or
              codon == 'ACA' or 
              codon == 'ACG'):
            
            amino_acid_sequence.append('Thr')
            
        elif (codon == 'GCU' or 
              codon == 'GCC' or 
              codon == 'GCA' or 
              codon == 'GCG'):
            
            amino_acid_sequence.append('Ala')
            
        elif (codon == 'UUU' or codon == 'UUC'):
            
            amino_acid_sequence.append('Phe')
            
        elif (codon == 'UAU' or codon == 'UAC'):
            
            amino_acid_sequence.append('Tyr')
            
        elif (codon == 'CAU' or codon == 'CAC'): 
            
            amino_acid_sequence.append('His')
            
        elif (codon == 'CAA' or codon == 'CAG'):
            
            amino_acid_sequence.append('Gln')
            
        elif (codon == 'AAU' or codon == 'AAC'):
            
            amino_acid_sequence.append('Asn')
            
        elif (codon == 'AAA' or codon == 'AAG'):
            
            amino_acid_sequence.append('Lys')       
            
        elif (codon == 'GAU' or codon == 'GAC'):
            
            amino_acid_sequence.append('Asx')
            
        elif (codon == 'GAA' or codon == 'GAG'):
            
            amino_acid_sequence.append('Glx')
            
        elif (codon == 'UGU' or codon == 'UGC'): 
            
            amino_acid_sequence.append('Cys')
                
        elif (codon == 'UGG'):
            
            amino_acid_sequence.append('Trp')
        
        else: 
            raise Exception('tRNA Input Error: The inputted tRNA strand is unrecognizable, please restart the program.')

    else:
        formatted_amino_acid_seq  = "-".join(amino_acid_sequence)

    return  mRNA_template_strand, complete_tRNA_sequence, modified_tRNA_sequence, formatted_amino_acid_seq


#-------END OF CODE---------------------- END OF CODE--------------------------END OF CODE-------------------------
