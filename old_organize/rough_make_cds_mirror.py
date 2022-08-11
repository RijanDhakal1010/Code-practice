import pickle

with open('/home/rijand/Desktop/Workspace/pal2nal_setup/OG0000000.hfa','r') as pepheads:
    pepheaders = pepheads.readlines()

with open('/home/rijand/Desktop/Workspace/pal2nal_setup/codes.pkl','rb') as handle:
	the_dict = pickle.load(handle)

cds_dict = {}

for i in pepheaders:
    for codeid in the_dict:
        if codeid in i:
            # maybe insert a break here.
            species_name = the_dict.get(codeid)
    
    species_pickle = f'/home/rijand/Desktop/Backup/pickles/{species_name}.pickle'

    with open(species_pickle,'rb') as cds_handle:
	    cds_pickle = pickle.load(cds_handle)

    sequence_cds = cds_pickle.get(i.rstrip(),"None") # what are in peps may not be in cds. So, if it is in pep but not in cds then we do not want to send NoneType to the dict
    #cds_dict[i] = sequence_cds
    cds_dict[i] = sequence_cds

for l in cds_dict:
    line = l + cds_dict.get(l) + '\n'
    with open('test.fa','a') as writer:
        writer.write(line)