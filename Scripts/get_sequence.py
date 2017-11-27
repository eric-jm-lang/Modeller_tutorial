from modeller import *
code = '1qg8' # only this need to be modified to match your PDB filename
e = environ()
m = model(e, file=code)
aln = alignment(e)
aln.append_model(m, align_codes=code)
aln.write(file=code+'.seq')
