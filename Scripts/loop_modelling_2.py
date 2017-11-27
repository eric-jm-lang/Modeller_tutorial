from modeller import *
from modeller.automodel import * 

log.verbose()
env = environ()
env.io.atom_files_directory = ['.', '../atom_files']

# Create a new class based on 'dopehrloopmodel' (more accurate than 'loopmodel' so that we can redefine
# select_loop_atoms
class MyLoop(dopehr_loopmodel):
    # This routine picks the residues to be refined by loop modeling
    def select_atoms(self):
        # One loop from residue 134 to 136 inclusive
        return selection(self.residue_range('134:', '136:'), self.residue_range('218:', '231:'))
    def select_loop_atoms(self):
        # One loop from residue 134 to 136 inclusive
        return selection(self.residue_range('134:', '136:'))

a = MyLoop(env, alnfile = 'alignment.ali',
              knowns = '1qg8', sequence = '1qg8_fill',
              loop_assess_methods=assess.DOPE) # assess loops with DOPE  
              
# First a single model with the missing residue is created
a.starting_model= 1
a.ending_model  = 1

# Then the specified loop is refined and 25 models created
a.loop.starting_model = 1
a.loop.ending_model   = 25

# Very thorough optimization:
a.loop.library_schedule = autosched.slow
a.loop.max_var_iterations = 300
# Thorough MD optimization:
a.loop.md_level = refine.slow
# Repeat the whole optimization cycle 2 times
a.loop.repeat_optimization = 2

a.make()
