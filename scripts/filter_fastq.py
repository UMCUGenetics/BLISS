#!/usr/bin/env python

"""
script to filter SRA header fastqs

"""

import re
import sys, os
import argparse
from Bio.Seq import Seq


        
def filterBLISSfasta(input_fastq_file):
    try:
        f = open(input_fastq_file, 'r')
    except IOError:
        sys.exit('Error: Cannot open fasta file: {0}'.format(input_fastq_file))
    else:
        with f:
            for line in f:
                line = line.strip('\n')
                if line.startswith('@'):
                    ####@NS500414:682:H3HM3AFX2:1:11101:21345:1017 2:N:0:ATCACG###
                    #print line
                    my_header = line.split(' ')
                    my_header_2 = my_header[0].split('.')
                    #print my_header,my_header_2
                    
                    print '{A}:{B}:H3HM3AFX2:1:11101:{C}:{D} {E}:N:0:NNNNNNNN'.format(
                         A=my_header_2[0],
                         B=my_header_2[1],
                         C=my_header_2[2],
                         D=my_header[1],
                         E=my_header_2[3]
                    )
                elif line.startswith('+'):
                    ####@NS500414:682:H3HM3AFX2:1:11101:21345:1017 2:N:0:ATCACG###
                    #print line
                    my_header = line.split(' ')
                    my_header_2 = my_header[0].split('.')
                    #print my_header,my_header_2
                    
                    print '{A}:{B}:H3HM3AFX2:1:11101:{C}:{D} {E}:N:0:NNNNNNNN'.format(
                         A=my_header_2[0],
                         B=my_header_2[1],
                         C=my_header_2[2],
                         D=my_header[1],
                         E=my_header_2[3]
                    )
                else:
                    print line

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=100, width=200))

    #parser.add_argument('--remove_filtered', action='store_true', help='Skip variants with a filter flag other than PASS.')

    required_named = parser.add_argument_group('required named arguments')
    required_named.add_argument('-i', '--input_fastq_file', help='path/to/input_fastq_file', required=True)
    #required_named.add_argument('-b', '--sample_barcode', help='sample_barcode', required=True)

    args = parser.parse_args()
    filterBLISSfasta(args.input_fastq_file)