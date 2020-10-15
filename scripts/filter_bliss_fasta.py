#!/usr/bin/env python

"""
script to filter bliss reads

"""

import re
import sys, os
import argparse
#import numpy as np
#from Bio.Seq import Seq
from Bio.Seq import Seq
#from Bio import pairwise2 
#from Bio.pairwise2 import format_alignment


def read2(f):
    for line in f:
        try:
            line2 = f.next()
        except StopIteration:
            line2 = ''

        yield line, line2
        
def check_header(line):
    if not line.startswith('>'):
         sys.exit('Error: line {0} does not start with >'.format(line))
         
def parse_sequence(line,sample_barcode,UMI_length):
    my_dna = Seq(line)
    
    
    my_dna_barcode = my_dna[int(UMI_length):int(UMI_length)+len(Seq(sample_barcode))+2]
    #print my_dna_barcode
    match = my_dna_barcode.find(Seq(sample_barcode))
    #print match
    if match == int(1):
       my_dna = my_dna[1:]
    elif match == int(0):
       my_dna = my_dna
    else: my_dna = Seq("")
    return my_dna
    
def chopsequence(line,sample_barcode,UMI_length):
    chopped_line = [str(line[0:int(UMI_length)]), str(line[int(UMI_length):int(UMI_length)+len(Seq(sample_barcode))]), str(line[int(UMI_length)+len(Seq(sample_barcode)):])]
    return chopped_line

#alignments = pairwise2.align.localxx(my_dna_barcode, Seq(sample_barcode))
#print alignments
#print(format_alignment(*alignments[0]))


        
def filterBLISSfasta(input_fasta_file, sample_barcode,UMI_length):
    try:
        f = open(input_fasta_file, 'r')
    except IOError:
        sys.exit('Error: Cannot open fasta file: {0}'.format(input_fasta_file))
    else:
        with f:
            for line1, line2 in read2(f):
                line1 = line1.strip('\n')
                check_header(line1)
                line1 = line1.split(' ')[0]
                line2 = line2.strip('\n')
                parse_sequence_line = parse_sequence(line2,sample_barcode,UMI_length)
                #print parse_sequence_line
                if parse_sequence_line:
                    length_seq = len(parse_sequence_line)
                    chopped_seq_line = chopsequence(parse_sequence_line,sample_barcode,UMI_length)
                    print '{lineheader}:[1,{sequencelengths}]'.format(
                        lineheader=line1,
                        sequencelengths=length_seq
                    )
                    print '{A} {B} {C}'.format(
                        A=chopped_seq_line[0],
                        B=chopped_seq_line[1],
                        C=chopped_seq_line[2]
                    )
if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=100, width=200))

    #parser.add_argument('--remove_filtered', action='store_true', help='Skip variants with a filter flag other than PASS.')

    required_named = parser.add_argument_group('required named arguments')
    required_named.add_argument('-i', '--input_fasta_file', help='path/to/input_fasta_file', required=True)
    required_named.add_argument('-b', '--sample_barcode', help='sample_barcode', required=True)
    required_named.add_argument('-u', '--UMI_length', help='sample_barcode', required=True)

    args = parser.parse_args()
    filterBLISSfasta(args.input_fasta_file, args.sample_barcode, args.UMI_length)