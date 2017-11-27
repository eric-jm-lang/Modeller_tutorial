from modeller import *
from modeller.automodel import * 
from modeller.parallel import * # This enable to work with multiple processor cores
from MyLoop import MyLoop # The MyLoop class is in a different file and thus needs to be imported from MyLoop.py
# MyLoop.py needs to be in the same directory as this script

# This script enables to run the loop optimization process in parrallel
# Here we will refine the second loop of 1qg8

j = job()
# The following specify the number of processor cores to use, do not specify more core than you have available on your machine
j.append(local_slave())
j.append(local_slave())
j.append(local_slave())
j.append(local_slave())
j.append(local_slave())
j.append(local_slave())

log.verbose()
env = environ()
env.io.atom_files_directory = ['.', '../atom_files']

# no need to refer to an alignment anymore there since the missing atoms are already there
# We just want to optimize the second loop starting with the best model form the previous step
# you will need to change this with your pdb name
a = MyLoop(env, inimodel='model9.pdb',   # Best model form previous step
           sequence='model9',  # code (same name but without '.pdb'
           loop_assess_methods=assess.DOPE) # assess loops with DOPE  
              

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

# Specify that the run should be in parrallel
a.use_parallel_job(j)
 
a.make()
