from modeller import *
from modeller.automodel import * 

# This part was within the script loop_modelling_2
# Here is is in a separate file for loop_modelling_3 so the script can be run in parallel

class MyLoop(dopehr_loopmodel):
    def select_atoms(self):
	    # Here only the second loop atoms are allowed to move so we do not mess with the first loop we have previously refined
        return selection(self.residue_range('218:', '231:'))
    def select_loop_atoms(self):
        return selection(self.residue_range('218:', '231:'))
