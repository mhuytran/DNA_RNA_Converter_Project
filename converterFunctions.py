import functools

#---------------------------------------------------------------------------------------------------------------------------
def convert_dna_decorator_5_3(func): 
    """
       This convert_dna_decorator_5_3 takes the two parameters from
       the original function, the DNA template strand with a 5 to 3 directionality
       and the DNA complementary strand with a 3 to 5 directionality.
       Consequently, the decorator implements its functionality to the original function, convert_dna_5_3,to 
       print out the results: the complementary DNA strand and the base-pairing representation.
        
       
    Args:
    
        func([str]): The return value of convert_dna_5_3: a tuple consisting of the complementary_dna_strand
        and the dna_template_strand.
        
    Returns:
        
        str: "Done"; to specify that the results have finished printing. 
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("\n"+"Results".center(86, "-"))
        print("Complementary DNA Strand: " + "\n") 
        result = "3'-" + func(*args, **kwargs)[0] + "-'5"
        print(result + "\n")
        print("DNA Template and DNA Complementary Strand Base-Pairing Representation: " + "\n") 
        print("DNA Temp.: "+"5'-" + func(*args, **kwargs)[1] + "-'3" + "\n" + "DNA Comp.: " + "3'-" + func(*args, *kwargs)[0] + "-'5" + "\n")
        return "Done"

    return wrapper

@convert_dna_decorator_5_3
def convert_dna_5_3(dna_template_strand):
    
    """The convert_dna function takes in a input DNA strand that has a 5 to 3 directionality,
       and returns a complementary DNA strand that has a 3 to 5 directionality. 
       
    Args:
        dna_template_strand (str): The template strand.

    Returns:
        complementary_dna_strand (str): The complementary strand.
    """
    flag = True
    
    while flag == True:
        
        for letter in dna_template_strand:
            
            if letter == '5' or letter == '3' or letter =='U':
                print("\n\n I'm sorry, please correctly type your DNA strand. DO NOT INCLUDE A U, 5'CAP, OR 3'CAP \n\n")
                dna_template_strand = input()
            
        else:
            flag = False
            break
                                   

    if "5" or "3" or "U" not in dna_template_strand:
        
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

    return complementary_dna_strand, dna_template_strand

# ---------------------------------------------------------------------------------------------------------------------------

def convert_dna_decorator_3_5(func): 
    """
       This convert_dna_decorator_3_5 takes the two parameters from
       the original function, the DNA template strand with a 3 to 5 directionality
       and the DNA complementary strand with a 5 to 3 directionality.
       Consequently, the decorator implements its functionality to the original function, convert_dna_5_3,
       to print out the results: the complementary DNA strand and the base-pairing representation.

    Args:
        func ([str]): The return value of convert_dna_3_5: a tuple consisting of the complementary_dna_strand
        and the dna_template_strand.

    Returns:
          str: "Done"; to specify that the results have finished printing.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("\n"+"Results".center(86, "-"))
        print("Complementary DNA Strand: " + "\n") 
        result = "5'-" + func(*args, **kwargs)[0] + "-'3"
        print(result + "\n")
        print("DNA Template and DNA Complementary Strand Base-Pairing Representation: " + "\n") 
        print("DNA Temp.: " + "3'-" + func(*args, **kwargs)[1] + "-'5" + "\n" + "DNA Comp.: " + "5'-" + func(*args, *kwargs)[0] + "-'5" + "\n")
        return "Done"

    return wrapper

@convert_dna_decorator_3_5
def convert_dna_3_5(dna_template_strand):
    
    """The convert_dna_3_5 function takes in a input DNA strand that has a 3 to 5 directionality,
       and returns a complementary DNA strand that has a 5 to 3 directionality. 

    Args:
        dna_template_strand (str): The template strand.

    Returns:
        complementary_dna_strand (str): The complementary strand.
    """
    flag = True
    
    while flag == True:
        
        for letter in dna_template_strand:
            
            if letter == '5' or letter == '3' or letter =='U':
                print("\n\n I'm sorry, please correctly type your DNA strand. DO NOT INCLUDE A U, 5'CAP, OR 3'CAP \n\n")
                dna_template_strand = input()
            
        else:
            flag = False
            break
                                   

    if "5" or "3" or "U" not in dna_template_strand:
        
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

    return complementary_dna_strand, dna_template_strand

#----------------------------------------------------------------------------------------------------------------------------
def convert_rna_decorator_5_3(func): 
    """This convert_rna_decorator_5_3 takes the two parameters from
       the original function, the RNA template strand with a 5 to 3 directionality
       and the tRNA complementary strand with a 3 to 5 directionality.
       Consequently, the decorator implements its functionality to the original function,convert_rna_5_3,
       to print out the results: the complementary tRNA strand and the base-pairing representation.

    Args:
        func ([str]): The return value of convert_rna_5_3: a tuple consisting of the complementary_tRNA_strand
        and the rna_template_strand.

    Returns:
        str: "Done"; to specify that the results have finished printing.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("\n"+"Results".center(86, "-"))
        print("Complementary tRNA Strand: " + "\n") 
        result = "3'-" + func(*args, **kwargs)[0] + "-'5"
        print(result + "\n")
        print("RNA and tRNA base-pairing representation: \n")
        print("RNA  Temp.: " + "5'-" + func(*args, **kwargs)[1] + "-'3" + "\n" + "tRNA Comp.: " + "3'-" + func(*args, *kwargs)[0] + "-'5" + "\n")
        return "Done"

    return wrapper

@convert_rna_decorator_5_3
def convert_rna_5_3(rna_template_strand):
    """The convert_rna_5_3 function takes in a input RNA strand that has a 5 to 3 directionality,
       and returns a complementary tRNA strand that has a 3 to 5 directionality. 

    Args:
        rna_template_strand (str): The single-stranded template RNA strand.

    Returns:
        complete_tRNA_strand: The resulting complementary tRNA strand.
    """
    flag = True
    
    while flag == True:
        
        for letter in rna_template_strand:
            
            if letter == '5' or letter == '3' or letter == 'T':
                print("I'm sorry, please correctly type your RNA strand, and DO NOT INCLUDE A T, 5' CAP, OR 3' CAP ends")
                rna_template_strand = input()
                
        else:
            flag = False
            break

    if "5" or "3" or "T" not in  rna_template_strand:
        
        tRNA_strand = []
        
        for base in  rna_template_strand:
            
            if base == 'A':
                tRNA_strand.append('U')
            elif base == 'U':
                tRNA_strand.append('A')
            elif base == 'C':
                tRNA_strand.append('G')
            elif base == 'G':
                tRNA_strand.append('C')
                
        else:
            complete_tRNA_strand = ''.join(tRNA_strand)

    return complete_tRNA_strand, rna_template_strand


#-----------------------------------------------------------------------------------------------------------------------

def convert_rna_decorator_3_5(func): 
    """This convert_rna_decorator_3_5 takes the two parameters from
       the original function, the RNA template strand with a 3 to 5 directionality
       and the tRNA complementary strand with a 5 to 3 directionality.
       Consequently, the decorator implements its functionality to the original function, convert_rna_3_5,
       to print out the results: the complementary tRNA strand and the base-pairing representation.

    Args:
        func ([str]): The return value of convert_rna_3_5: a tuple consisting of the complementary_tRNA_strand
        and the rna_template_strand.

    Returns:
        str: "Done"; to specify that the results have finished printing.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("\n"+"Results".center(86, "-"))
        print("Complementary tRNA Strand: " + "\n") 
        result = "5'-" + func(*args, **kwargs)[0] + "-'3"
        print(result + "\n")
        print("RNA and tRNA base-pairing representation: \n")
        print("RNA  Temp.: " + "3'-" + func(*args, **kwargs)[1] + "-'5" + "\n" + "tRNA Comp.: " + "5'-" + func(*args, *kwargs)[0] + "-'3" + "\n")
        return "Done"

    return wrapper

@convert_rna_decorator_3_5
def convert_rna_3_5(rna_template_strand):
    """The convert_rna function takes in a input RNA strand and returns a complementary tRNA strand

    Args:
        rna_template_strand (str): The single-stranded template RNA strand

    Returns:
        complete_tRNA_strand: The resulting complementary tRNA strand
    """
    flag = True
    
    while flag == True:
        
        for letter in rna_template_strand:
            
            if letter == '5' or letter == '3' or letter == 'T':
                print("I'm sorry, please correctly type your RNA strand, and DO NOT INCLUDE A T, 5' CAP, OR 3' CAP ends")
                rna_template_strand = input()
                
        else:
            flag = False
            break

    if "5" or "3" or "T" not in  rna_template_strand:
        
        tRNA_strand = []
        
        for base in  rna_template_strand:
            
            if base == 'A':
                tRNA_strand.append('U')
            elif base == 'U':
                tRNA_strand.append('A')
            elif base == 'C':
                tRNA_strand.append('G')
            elif base == 'G':
                tRNA_strand.append('C')
                
        else:
            complete_tRNA_strand = ''.join(tRNA_strand)

    return complete_tRNA_strand, rna_template_strand
