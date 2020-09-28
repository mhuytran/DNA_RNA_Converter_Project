# Nucleic Acids Project
 
**Before reading the README.md document, please view these resources if you do not remember base-pairing.**

 
## Resources 
  
[DNA Base-Pairing Explanation](https://www.genome.gov/genetics-glossary/Base-Pair)

[DNA and RNA Base Pairing Rules PDF](https://www.peekskillcsd.org/cms/lib/NY01913880/Centricity/Domain/827/DNA%20RNA%20Base%20Pairing%20Rules.pdf)

[DNA and RNA Base Pairing Video](https://www.youtube.com/watch?v=QN2YFxu4swM)


## Purpose & Introduction

  Parsing through a DNA template strand or a mRNA strand can be extremely tedious and exhausting. However, a python program can alleviate this task. This project is designed for individuals that want to efficiently obtain the following: a DNA complementary strand, mRNA strand, tRNA strand, or amino acid sequence. 
  
  While the functionality of this project can be found in efficient modules, such as BioPython, all of the project files are written originally and completely by the author (mhuytran). The functions that are utilized in this project are in the **nucleicfunctions.py** file, and these function initiate the parsing of DNA and mRNA strands. To see the documentation of the functions, open the **nucleicfunctions.py** file in this repository to view the documentation strings. Moreover, please continue reading the README file for the **Normal_Example.py** and **Searchbar_Example.py** results sections to view the example outputs. 
  
  Lastly, I would like to state the sources of inspiration for this project. I was inspired by my AP Biology homework because it was very annoying when the question asked to write out a DNA complementary strand, mRNA strand, tRNA sequence, or amino acid sequence by hand. Additionally, I was inspired by molecular dynamics/modeling, and I wanted to create a python program that is related to biological processes. Nonetheless, I feel proud of this achievement, and I hope that this project will benefit you, the reader, in scientific analysis of DNA and RNA.
   
  
##  Download and Setup 
  
 1. Press the 'Code' button to either clone or download as zip.
 2. Open the files your code editor of choice, and put the nucleicfunctions.py in any directory. 
 3. Create a python file and code the following below:
           
 ```python
 import sys 
           
 #this will connect the nucleicfunctions.py file to your PATH so you can access it as a module!
           
 sys.append("C:\path\to\file\nucleicfunctions.py")
           
 ```
4. Run both the Example files, **Normal_Example.py** and **Searchbar_Example.py**.:

5. Happy Coding! Feel free to use the functions in the nucleicfunctions script, and view the results below to make sure you did everything correctly :). 

## **Normal_Example.py** Results:
```
---------------------------------------Results----------------------------------------
Complementary DNA Strand: 

3'-TGACTAGTAGCTAGCTACGTACGATGCATCGATCGATCGCTAGCAGCATCGATCGATCGATCG-'5


DNA Template and DNA Complementary Strand Base-Pairing Representation:

DNA Temp.: 5'-ACTGATCATCGATCGATGCATGCTACGTAGCTAGCTAGCGATCGTCGTAGCTAGCTAGCTAGC-'3
DNA Comp.: 3'-TGACTAGTAGCTAGCTACGTACGATGCATCGATCGATCGCTAGCAGCATCGATCGATCGATCG-'5


mRNA Strand Synthesis Result:

mRNA Strand:5'-ACUGAUCAUCGAUCGAUGCAUGCUACGUAGCUAGCUAGCGAUCGUCGUAGCUAGCUAGCUAGC-'3

Program Status: Done


Enter a mRNA strand: ACUGAUCAUCGAUCGAUGCAUGCUACGUAGCUAGCUAGCGAUCGUCGUAGCUAGCUAGCUAGC

---------------------------------------Results----------------------------------------
tRNA sequence: 

UGACUAGUAGCUAGCUACGUACGAUGCAUCGAUCGAUCGCUAGCAGCAUCGAUCGAUCGAUCG


mRNA and tRNA base-pairing representation: 

mRNA Temp.: 5'-ACUGAUCAUCGAUCGAUGCAUGCUACGUAGCUAGCUAGCGAUCGUCGUAGCUAGCUAGCUAGC-'3
tRNA  Seq.:    UGACUAGUAGCUAGCUACGUACGAUGCAUCGAUCGAUCGCUAGCAGCAUCGAUCGAUCGAUCG   


Amino Acid Sequence Data: 

tRNA Codon Sequence: UGA-CUA-GUA-GCU-AGC-UAC-GUA-CGA-UGC-AUC-GAU-CGA-UCG-CUA-GCA-GCA-UCG-AUC-GAU-CGA-UCG 
Amino Acid Sequence: TERM-Leu-Val-Ala-Ser-Tyr-Val-Arg-Cys-Ile-Asx-Arg-Ser-Leu-Ala-Ala-Ser-Ile-Asx-Arg-Ser

Program Status: Done


```

## **Searchbar_Example.py** Results:

Inputting DNA template strand with a 5-3 directionality:
```
----------------------------------------Prompt----------------------------------------
Please enter DNA or mRNA into the search bar:

DNA

Please enter 5-3 or 3-5 for the directionality of your DNA template strand. If mRNA strand, enter 5-3.

5-3

Confirmation: dna, 5-3

Now, please type in your 'DNA' template strand:

ATGCATCGTAGCTACTAGCTAGCTGATCGATGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTACGTG

---------------------------------------Results----------------------------------------
Complementary DNA Strand:

3'-TACGTAGCATCGATGATCGATCGACTAGCTACGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATGCAC-'5


DNA Template and DNA Complementary Strand Base-Pairing Representation:

DNA Temp.: 5'-ATGCATCGTAGCTACTAGCTAGCTGATCGATGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTACGTG-'3
DNA Comp.: 3'-TACGTAGCATCGATGATCGATCGACTAGCTACGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATGCAC-'5


mRNA Strand Synthesis Result:

mRNA Strand:5'-AUGCAUCGUAGCUACUAGCUAGCUGAUCGAUGCUAGCUAGCUAGCUAGCUAGCUAGCUAGCUAGCUAGCUAGCUAGCUAGCUAGCUAGCUACGUG-'3

Program Status: Done
```
Inputting DNA template strand with a 3-5 directionality: 
```
----------------------------------------Prompt----------------------------------------
Please enter DNA or mRNA into the search bar:

DNA

Please enter 5-3 or 3-5 for the directionality of your DNA template strand. If mRNA strand, enter 5-3. 

3-5

Confirmation: dna, 3-5

Now, please type in your 'DNA' template strand: 

ATCGATCGATCGTAGCTAGCTATCATCGTAGGGGGAAATCGTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTGATCG

---------------------------------------Results----------------------------------------
Complementary DNA Strand: 

5'-TAGCTAGCTAGCATCGATCGATAGTAGCATCCCCCTTTAGCATCGATCGATCGATCGATCGATCGATCGATCGACTAGC-'3

DNA Template and DNA Complementary Strand Base-Pairing Representation: 

DNA Temp.: 3'-ATCGATCGATCGTAGCTAGCTATCATCGTAGGGGGAAATCGTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTGATCG-'5
DNA Comp.: 5'-TAGCTAGCTAGCATCGATCGATAGTAGCATCCCCCTTTAGCATCGATCGATCGATCGATCGATCGATCGATCGACTAGC-'5

mRNA Strand Synthesis Result: 

mRNA Strand:5'-UAGCUAGCUAGCAUCGAUCGAUAGUAGCAUCCCCCUUUAGCAUCGAUCGAUCGAUCGAUCGAUCGAUCGAUCGACUAGC-'3

Program Status: Done
```

Inputting mRNA as template strand: 
```
----------------------------------------Prompt----------------------------------------
Please enter DNA or mRNA into the search bar:

mRNA

Please enter 5-3 or 3-5 for the directionality of your DNA template strand. If mRNA strand, enter 5-3. 

5-3 

Confirmation: mrna, 5-3

Now, please type in your 'mRNA' template strand: 

GACCUCGUCCGGGAUGAAACGUCUCAAUGAGGAAGGUGGACAUAUGCU

---------------------------------------Results----------------------------------------
tRNA sequence: 

CUGGAGCAGGCCCUACUUUGCAGAGUUACUCCUUCCACCUGUAUACGA


mRNA and tRNA base-pairing representation: 

mRNA Temp.: 5'-GACCUCGUCCGGGAUGAAACGUCUCAAUGAGGAAGGUGGACAUAUGCU-'3
tRNA  Seq.:    CUGGAGCAGGCCCUACUUUGCAGAGUUACUCCUUCCACCUGUAUACGA   


Amino Acid Sequence Data: 

tRNA Codon Sequence: CUG-GAG-CAG-GCC-CUA-CUU-UGC-AGA-GUU-ACU-CCU-UCC-ACC-UGU-AUA-CGA  
Amino Acid Sequence: Leu-Glx-Gln-Ala-Leu-Leu-Cys-Arg-Val-Thr-Pro-Ser-Thr-Cys-Ile-Arg  

Program Status: Done
```

## Modules Used In This Project

1. [functools](https://docs.python.org/3/library/functools.html?highlight=functools#module-functools)
2. [sys](https://docs.python.org/3/library/sys.html)
3. [re](https://docs.python.org/3/library/re.html?highlight=re#module-re)
4. [pyperclip](https://pypi.org/project/pyperclip/)
 

## Conclusion & Final Thoughts

Though this project has been finished, I will eventually model the central dogma in the nucleic functions script, which is not included in this project at the moment. I hope that you, the reader, have been satisfied with my project. Thank you!
  

