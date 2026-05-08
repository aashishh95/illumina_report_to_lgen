#usage: python illumina_report_to_lgen.py genotype_top_strand_matrix.csv output.lgen
import sys
from collections import OrderedDict

file_path = sys.argv[1]
out_prefix = sys.argv[2]

header = True
sample_dict = OrderedDict()
marker_list = []
with open(file_path) as source:
    for line in source:
        line = line.rstrip().split(",")
        if header:
            for sample in line[1:]:
                sample_dict[sample]=[]
            header = False
        else:
            marker_list.append(line[0])
            for i,v in enumerate(list(sample_dict.keys())):
                sample_dict[v].append(line[i+1])

with open(out_prefix,"w") as dest:
    for sample in sample_dict:
        lst_geno = sample_dict[sample]
        lst_geno = ["00" if x == "--" else x for x in lst_geno]
        for i,v in enumerate(lst_geno):
            dest.write(f"{sample}\t{marker_list[i]}\t{v[0]}\t{v[1]}\n")

