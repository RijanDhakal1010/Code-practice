import argparse # this will help create CLI elements

import pickle

import os

# this is the name of the parser object that will parse the commandline
parser = argparse.ArgumentParser(description=" This script takes an orthogroup with peptide sequences and generates a corresponding orthogroup with cds sequences. Two things are absoultely necessary, first a dict to identify the species in the sequence header using the most common subscript and dictified cds fastas with similar headers.")

# the arguments will be coded in the following format
# parser.add_argument('--insert_name_here',nargs='?', const='bar',default=False, help='') - If the default flag is false then there is no default.

parser.add_argument('--pickle',nargs='?', const='bar',default='Default', help= "This should be the location of the the pickled file with the species identification codes.")

# TODO : see if you can use * instead of extensions

parser.add_argument('--cds',nargs='?', const='bar',default=False, help='This should be the location of the cds fasta dicts in pickle format.')

parser.add_argument('--orthos',nargs='?', const='bar',default=False, help='The location of the orthos in Unix format.')

parser.add_argument('--output',nargs='?', const='bar',default=False, help='The location of the output files. Location should be in Unix format.')

# unsure about the function of this one
args = parser.parse_args()

def main():

    try:
        with open(args.pickle,'rb') as species:
            species_codes = pickle.load(species)
    except:
        print("Please make sure you supplied the correct location for the pickle")

    try:
        os.chdir(args.orthos)
    except:
        print("Is the path to the directory with orthos right?")
    
    for ortho_pep in os.listdir():
        with open(ortho_pep,'r') as current_ortho_pep:
            current_ortho_pep_headers = current_ortho_pep.readlines()
        
        ortho_pep_base = ortho_pep.split('.')[0]
        cds_base = f'{args.output}/{ortho_pep_base}.cds'
        ortho_pep_base = {}
        
        for pep_header in current_ortho_pep_headers:    
            if pep_header.startswith('>'):  
                for code_name in species_codes: 
                    if code_name in pep_header: 
                        species_name = species_codes.get(code_name) 
            
            species_pickle = f'{args.cds}/{species_name}.pickle'    
        
            try:    
                with open(species_pickle,'rb') as cds_handle:   
                    cds_pickle = pickle.load(cds_handle)    
            except: 
                print("Are you sure that ",species_pickle," exists?")   
        
            sequence_cds = cds_pickle.get(pep_header.rstrip(),"None") # what are in peps may not be in cds. So, if it is in pep but not in cds then we do not want to send NoneType to the dict 
            ortho_pep_base[pep_header] = sequence_cds   
            
        for l in ortho_pep_base:    
            line = l + '\n' +  ortho_pep_base   
            with open(cds_base,'a') as cds_handle:  
                cds_handle.write(line)  

main()