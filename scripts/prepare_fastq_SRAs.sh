#!/gnu/store/n1c9jiv2njnvdfz58v71fvzq0hkgivz1-bash-5.0.7/bin/sh



guixr load-profile /hpc/cuppen/projects/P0008_brca1/dsb_seq/analysis/Arne/BLISS/BLISS-guix-profile -- <<EOF
  zcat /hpc/cuppen/projects/P0008_brca1/dsb_seq/raw/SRA/SRR5241057.1_1.fastq.gz > /hpc/cuppen/projects/P0008_brca1/dsb_seq/raw/SRA/SRR5241057.1_1.fastq
  python /hpc/cuppen/projects/P0008_brca1/dsb_seq/analysis/Arne/BLISS/scripts/filter_fastq.py -i /hpc/cuppen/projects/P0008_brca1/dsb_seq/raw/SRA/SRR5241057.1_1.fastq > /hpc/cuppen/projects/P0008_brca1/dsb_seq/raw/SRA/SRR5241057.reformatted_1.fastq
  gzip -c /hpc/cuppen/projects/P0008_brca1/dsb_seq/raw/SRA/SRR5241057.reformatted_1.fastq > /hpc/cuppen/projects/P0008_brca1/dsb_seq/raw/SRA/SRR5241057.reformatted_1.fastq.gz

  zcat /hpc/cuppen/projects/P0008_brca1/dsb_seq/raw/SRA/SRR5241057.1_2.fastq.gz > /hpc/cuppen/projects/P0008_brca1/dsb_seq/raw/SRA/SRR5241057.1_2.fastq
  python /hpc/cuppen/projects/P0008_brca1/dsb_seq/analysis/Arne/BLISS/scripts/filter_fastq.py -i /hpc/cuppen/projects/P0008_brca1/dsb_seq/raw/SRA/SRR5241057.1_2.fastq > /hpc/cuppen/projects/P0008_brca1/dsb_seq/raw/SRA/SRR5241057.reformatted_2.fastq
  gzip -c /hpc/cuppen/projects/P0008_brca1/dsb_seq/raw/SRA/SRR5241057.reformatted_2.fastq > /hpc/cuppen/projects/P0008_brca1/dsb_seq/raw/SRA/SRR5241057.reformatted_2.fastq.gz
  
EOF