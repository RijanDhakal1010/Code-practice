import argparse # this will help create CLI elements

import os

# this is the name of the parser object that will parse the commandline
parser = argparse.ArgumentParser(description="")

# the arguments will be coded in the following format
# If the default flag is false then there is no default.
# nargs is the number of argument
# The first argument is the flag name
# parser.add_argument('--',nargs='?', const='bar',default=False, help='') 

parser.add_argument('--peps',nargs='?', const='bar',default='Default', help= "This is the path to the directory where the old peptide files with the superset of headers are. Make sure not to give a trailing slash at the end, python adds that on its own.")

parser.add_argument('--cds',nargs='?', const='bar',default=False, help='This is path to the folders with the None coded cds files are. Make sure not to supply the trailing slash at the end, python does that on its own.')

parser.add_argument('--ext',nargs='?', const='bar',default=".fa", help='The extension of the cds peptide files. Please supply one or .fa will be used by default. And if you do supply one do not forget the dot.')

parser.add_argument('--out',nargs='?', const='bar',default=False, help='This is the location where the output files will be delivered. Make sure not to supply the trailing slash at the end, python does that on its own.') 

# unsure about the function of this one
args = parser.parse_args()


def run():

    nuc_dict = {}

    pep_dict = {}


    for i in os.listdir(args.cds):

        l = i.rsplit('.')[0]

        k = f'{args.out}{l}{args.ext}'

        l = f'{args.peps}{l}{args.ext}'

        j = f'{args.cds}{i}'

        print(l)

        with open(j,'r') as nucleo:
            nucleo_lines = nucleo.readlines()
        
        with open(l,'r') as peptides:
            peptide_lines = peptides.readlines()

    
    for index,header in enumerate(nucleo_lines):
        if header.startswith('>'):
            sequence = nucleo_lines[index + 1]
            if sequence.rstrip() != "None":
                nuc_dict[header] = sequence
    
    for index1,header1 in enumerate(peptide_lines):
        if header1.startswith('>'):
            sequence1 = peptide_lines[index1 + 1]
            pep_dict[header1] = sequence1
    
    for header3 in nuc_dict:
        line = header3 + pep_dict.get(header3)
        with open(k,'a') as writer:
            writer.write(line)



def main():

    if os.path.isdir(args.peps) == False:
        print("Cannot access ", args.peps,", are you sure it is there?")
        quit()
    
    if os.path.isdir(args.out) == False:
        print("Cannot access ", args.out,", are you sure it is there?")
        quit()

    if os.path.isdir(args.cds) == False:
        print("Cannot access ", args.cds,", are you sure it is there?")
        quit()
    
    run()
    

main()