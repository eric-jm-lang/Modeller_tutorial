from modeller import *
from modeller.automodel import * 

# This script can be modified easily so you can use it for your own loop recosntruction

log.verbose()
env = environ()
env.io.atom_files_directory = ['.', '../atom_files']

# Create a new class based on 'dopehrloopmodel' (more accurate than 'loopmodel') 
# This class will enable to fix the positions of the residues that should not move
# It will also be used to define the residues composing the loop to refine (only one loop at a time)
# You need to change the residue_range to match your needs
class MyLoop(dopehr_loopmodel):
    # This routine picks the residues to be refined
    def select_atoms(self):
        return selection(self.residue_range('134:', '136:'), self.residue_range('218:', '231:'))
    def select_loop_atoms(self):
        # One loop from residue 134 to 136 inclusive
        return selection(self.residue_range('134:', '136:'))

		# You need to modify this part with your filenames and sequence names
a = MyLoop(env, alnfile = 'alignment.ali',
              knowns = '1qg8', sequence = '1qg8_fill',
              loop_assess_methods=assess.DOPE) # assess loop models with DOPE score (in addition to molpdf)
              
# First a single model with the missing residue is created
a.starting_model= 1
a.ending_model  = 1

# Then the specified loop is refined and 25 models created
a.loop.starting_model = 1
a.loop.ending_model   = 25 # More models can be generated. 100 is usually sufficient

# You don't need to modify the following
# Very thorough optimization:
a.loop.library_schedule = autosched.slow
a.loop.max_var_iterations = 300
# Thorough MD optimization:
a.loop.md_level = refine.slow
# Repeat the whole optimization cycle 2 times
a.loop.repeat_optimization = 2

a.make()
