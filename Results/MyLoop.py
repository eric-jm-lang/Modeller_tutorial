from modeller import *
from modeller.automodel import * 

class MyLoop(dopehr_loopmodel):
    def select_atoms(self):
        return selection(self.residue_range('218:', '231:'))
    def select_loop_atoms(self):
        return selection(self.residue_range('218:', '231:'))
