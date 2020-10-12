#!/gnu/store/n1c9jiv2njnvdfz58v71fvzq0hkgivz1-bash-5.0.7/bin/sh

guixr load-profile /hpc/cuppen/projects/P0008_brca1/dsb_seq/analysis/Arne/BLISS/BLISS-guix-profile -- <<EOF
  echo "Running inside a BLISS-guix-profile environment"
  export BLISS_PATH="/hpc/cuppen/projects/P0008_brca1/dsb_seq/analysis/Arne/BLISS/blissNP/bin/"
  #bash /hpc/cuppen/projects/P0008_brca1/dsb_seq/analysis/Arne/BLISS/blissNP/bin//bliss.sh 0gray_H3HM3AFX2_S1 0gray_S1 human ./0gray_H3HM3AFX2_S1_0grayS1_ATCACG 60 /hpc/cuppen/projects/P0008_brca1/dsb_seq/analysis/fastq ATCACG 8
  bash /hpc/cuppen/projects/P0008_brca1/dsb_seq/analysis/Arne/BLISS/blissNP/bin//bliss.sh 10gray_H3HM3AFX2_S1 10gray_S1 human ./10gray_H3HM3AFX2_S1_10grayS1_TCGTTC 60 /hpc/cuppen/projects/P0008_brca1/dsb_seq/analysis/fastq TCGTTC 8

EOF
