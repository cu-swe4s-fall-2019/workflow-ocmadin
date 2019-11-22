#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:27:51 2019

@author: owenmadin
"""

import argparse
import gzip

def parse_args():
    
    parser=argparse.ArgumentParser(description='Get Gene counts input parsing')
    
    parser.add_argument('--gene_name',
                    type=str,
                    help='Name of the gene to count',
                    required=True)
    parser.add_argument('--gene_count_file',
                    type=str,
                    help='file that contains the gene counts',
                    required=True)
    parser.add_argument('--output_filename',
                        type=str,
                        help='file to output sample IDs and counts to')
    args = parser.parse_args()
    return args.gene_name,args.gene_count_file,args.output_filename


def write_gene_counts(gene_count_file, output_filename, gene_name):
    
    o = open(output_filename, 'w')
    
    version = None
    dim = None
    header = None
    
    
    f = gzip.open(gene_count_file, 'rt')
    for l in f:
        A = l.rstrip().split('\t')
        if version is None:
            version = A
            continue
        if dim is None:
            dim = A
            continue
        if header is None:
            header = A
            continue
        if A[1] == gene_name:
            for i in range(2, len(header)):
                o.write(header[i] + ' ' + A[i] + '\n')
    f.close()
    o.close()

def main():
    gene_name, gene_count_file, output_filename = parse_args()
    print('Writing gene counts to '+output_filename)
    write_gene_counts(gene_count_file,output_filename,gene_name)
    

if __name__ == '__main__':
    main()
