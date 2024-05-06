from modeller import *

env = environ()
aln = alignment(env)
for (pdb, chain) in (('2hky', 'A'), ('4x09', 'A'), ('6mv6', 'A'),
                     ('6sso', 'A'), ('1k2a', 'A'),):
    m = model(env, file=pdb, model_segment=('FIRST:'+chain, 'LAST:'+chain))
    aln.append_model(m, atom_files=pdb, align_codes=pdb+chain)
aln.malign()
aln.malign3d()
aln.compare_structures()
aln.id_table(matrix_file='family.mat')
env.dendrogram(matrix_file='family.mat', cluster_cut=-1.0)
