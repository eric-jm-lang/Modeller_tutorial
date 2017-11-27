from modeller import *
from modeller.automodel import * 

# This script will not provide good models, and is here for illustrative purpose only

log.verbose()
env = environ()
env.io.atom_files_directory = ['.', '../atom_files']

# This is where you will need to modify the script to match your file names
a = loopmodel(env, alnfile = 'alignment.ali',
              knowns = '1qg8', sequence = '1qg8_fill')  
              
# First a single model with the missing residue is created
a.starting_model= 1
a.ending_model  = 1

# Then the shortest loop is refined and 2 models created
a.loop.starting_model = 1
a.loop.ending_model   = 2
a.loop.md_level       = refine.fast

a.make()
