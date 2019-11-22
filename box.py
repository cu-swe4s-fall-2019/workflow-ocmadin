import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import argparse
import numpy as np

def parse_args():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--tissue_types',
                        required=True,
                        help = 'Types of tissue to create plots for',
                        nargs = '+',
                        type=str)

    parser.add_argument('--genes',
                        required=True,
                        help = 'Genes to create plots for',
                        nargs = '+',
                        type=str)
    
    parser.add_argument('--output_filename',
                        required=True,
                        help = 'Name to output figure to',
                        type=str)

    args = parser.parse_args()
        
    return args.tissue_types,args.genes,args.output_filename 

def get_counts(tissue_type,genes):
    
    counts = []
    for i in range(len(genes)):
    
        gene = genes[i]
        tissue = tissue_type
    
        sample_to_count_map = {}
    
        f = open(gene + '.txt')
        for l in f:
            A = l.rstrip().split()
            sample_to_count_map[A[0]] = int(A[1])
    
        f.close()
    
        count = []
    
        f = open(tissue + '.txt')
        for l in f:
            sample = l.rstrip()
            if sample in sample_to_count_map:
                count.append(sample_to_count_map[sample])
        f.close()
    
        counts.append(count)
        return counts
    
    
def plot_boxes(tissue_types,genes,output_filename):
    
    width=len(tissue_types) * 3
    height=width
    fig,ax = plt.subplots(ncols=1,nrows=len(tissue_types),figsize=(width,height),dpi=300)
    
    
    for i in range(len(tissue_types)):
        meta_counts = []
        for j in range(len(genes)):
            meta_counts.append(get_counts(tissue_types[i],genes))
        ax[i].boxplot(np.asarray(meta_counts))
        ax[i].set_xticklabels(genes)
        ax[i].spines['top'].set_visible(False)
        ax[i].spines['right'].set_visible(False)
        ax[i].set_title(tissue_types[i])
        ax[i].set_ylabel("Count")
    
    plt.savefig(output_filename,bbox_inches='tight')


def main():
    tissue_types,genes,output_filename = parse_args()
    plot_boxes(tissue_types,genes,output_filename)
    

if __name__ == '__main__':
    main()

    