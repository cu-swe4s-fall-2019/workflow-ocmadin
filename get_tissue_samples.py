import argparse

def parse_args():
    
    parser=argparse.ArgumentParser(description='Get Gene counts input parsing')
    
    parser.add_argument('--data_file_name',
                    type=str,
                    help='File name with tissue data',
                    required=True)
    parser.add_argument('--tissue_type',
                    type=str,
                    help='Tissue type to get gene expression for',
                    required=True)
    parser.add_argument('--output_filename',
                        type=str,
                        help='file to output data for')
    args = parser.parse_args()
    return args.data_file_name, args.tissue_type, args.output_filename

def write_data_to_output(data_file_name,tissue_type,output_filename):
    o = open(output_filename, 'w')

    header = None
    sampid_col = -1
    smts_col = -1
    
    
    f = open(data_file_name)
    for l in f:
        A = l.rstrip().split('\t')
        if header is None:
            header = A
            sampid_col = A.index('SAMPID')
            smts_col = A.index('SMTS')
            continue
    
        if A[smts_col] == tissue_type:
            o.write(A[sampid_col] + '\n')
    f.close()
    o.close()
    
def main():
    data_file_name, tissue_type, output_filename = parse_args()
    print('Writing sample data to '+output_filename)
    write_data_to_output(data_file_name, tissue_type, output_filename)
    

if __name__ == '__main__':
    main()
