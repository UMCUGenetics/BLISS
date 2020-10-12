#!/bin/bash

cd /hpc/cuppen/projects/P0008_brca1/dsb_seq/analysis/Arne/BLISS/scripts/
logdir=/hpc/cuppen/projects/P0008_brca1/dsb_seq/analysis/Arne/BLISS/logs

#sbatch -o $logdir/0gray_H3HM3AFX2_S1_output.txt -e $logdir/0gray_H3HM3AFX2_S1_error.txt --mail-user=a.vanhoeck@umcutrecht.nl --time=24:00:00 --mem=40G --cpus-per-task=5 run_BLISS.sh
sbatch -o $logdir/10gray_H3HM3AFX2_S1_output.txt -e $logdir/10gray_H3HM3AFX2_S1_error.txt --mail-user=a.vanhoeck@umcutrecht.nl --time=24:00:00 --mem=40G --cpus-per-task=5 run_BLISS.sh
