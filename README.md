# DNA & mRNA Converter Project
 
Before reading the README.md document, **please** view these resources if you do not remember base-pairing.

 
## Resources 
  
[DNA Base-Pairing Explanation](https://www.genome.gov/genetics-glossary/Base-Pair)

[DNA and RNA Base Pairing Rules PDF](https://www.peekskillcsd.org/cms/lib/NY01913880/Centricity/Domain/827/DNA%20RNA%20Base%20Pairing%20Rules.pdf)

[DNA and RNA Base Pairing Video](https://www.youtube.com/watch?v=QN2YFxu4swM)


## Purpose & Introduction

  Parsing through a DNA template strand or mRNA strand can be exhausting; however, a python script can alleviate this problem instantly. This project I wrote is designed for individuals that want to obtain a complementary strand, either DNA or tRNA instantly with python code. Additionally, if the inputted template strandis mRNA, then the tRNA template strand and its amino acid sequence is returned. 
  
  While the functionality of this project can be found in very-efficient modules, such as BioPython, all of the project files are written originally and completely by the author (Minh-Huy Tran). The functions that are utilized in this project are in the **converterFunctions.py** file, and these functions initiate the parsing of DNA and mRNA strands into their respective template strands. To see the effects of these functions, I have also included the **DNA_Normal_Example.py** and **DNA_Searchbar_Example.py** files to help you, the reader, better visualize how these functions work. 
  
  Lastly, I would like to include in this paragraph a fun fact about this project. This project was the accumulation of 7 months of learning python programming through youtube videos and readings. Honestly, I feel proud of this achievement, and I hope that this project will benefit you, the reader, in scientific analysis of DNA and RNA template strand analysis.
  
##  Download and Setup 
  
 1. Press the 'Code' button to either clone or download as zip 
 2. Open the files in a code editor 
 3. Create a python file and code the following below
           
 ```
 import sys 
           
 #this will connect the converterFunctions.py file to your PATH so you can access it as a module!
           
 sys.append("C:\path\to\file\converterFunctions.py")
           
 ```
4. Run both the Example files, **DNA_Normal_Example.py** and **DNA_Searchbar_Example.py** to understand functionality
5. Happy Coding! Feel Free to use the functions
 
 ##
           
  
  
