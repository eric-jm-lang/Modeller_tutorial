from modeller import *
from modeller.scripts import complete_pdb

log.verbose()    # request verbose output
env = environ()
env.libs.topology.read(file='$(LIB)/top_heav.lib') # read topology
env.libs.parameters.read(file='$(LIB)/par.lib') # read parameters

# Here you need to modify the name of the pdb file to match yours 
mdl = complete_pdb(env, '1qg8_fill.BL00060001.pdb')

# Assess all atoms with DOPE:
s = selection(mdl)
s.assess_dope(output='ENERGY_PROFILE NO_REPORT', 
              file='model6.profile', # You need to modify this to give the name you'd like for your profile
              normalize_profile=True, smoothing_window=15)
