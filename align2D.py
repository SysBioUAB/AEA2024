from modeller import *

env = environ()
aln = alignment(env)
mdl = model(env, file='2hky', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='2hkyA', atom_files='2hky.pdb')
aln.append(file='target.fasta', align_codes='target', alignment_format='FASTA')
aln.align2d()
aln.write(file='aligned.fasta', alignment_format='FASTA')
aln.write(file='aligned.ali', alignment_format='PIR')
aln.write(file='aligned.pap', alignment_format='PAP')
