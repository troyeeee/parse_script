import pysam

# bam = pysam.AlignmentFile('L1.L1.pos.fq.bam')
# s = bam.fetch("SVA_A", 0, 1)
# print(s)
depth = pysam.TabixFile('L1_depth.gz')
s = depth.fetch('chr22', 0, 2)
for i in s:

    print(i)