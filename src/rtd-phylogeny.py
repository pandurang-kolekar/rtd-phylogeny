#!/usr/bin/env python

import argparse
from Bio import SeqIO
import re
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import squareform, pdist
import pandas
import dendropy
from ete3 import Tree


class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawDescriptionHelpFormatter):
    pass


def getRTD(sequence, kmer):
    """Compute return times of kmer in given sequence and return mean and standard deviation for RTD vector  """
    modSeq = re.sub(kmer, "*", sequence)
    rt = modSeq.split("*")
    rtvector = list(map(len, rt))
    if len(rtvector) > 1:
        del rtvector[0]
        del rtvector[-1]
    else:
        rtvector = []
    msd = getMeanSD(rtvector)
    return msd


def getMeanSD(vector):
    """Compute mean and standard deviation of RTD vector"""
    if len(vector) > 0:
        mean = np.mean(vector)
        sd = np.std(vector)
    else:
        mean = 0
        sd = 0
    ms = [mean, sd]
    return ms


def getKmers(k, bases):
    """Generate k-mers of size k"""
    import itertools
    kmers = [''.join(p) for p in itertools.product(bases, repeat=k)]
    return kmers


def list_to_npArray(vector1, vector2):
    """convert the list to numpy array"""
    if type(vector1) == list:
        vector1 = np.array(vector1)
    if type(vector2) == list:
        vector2 = np.array(vector2)
    return vector1, vector2


def euclidean(vector1, vector2):
    """ use matplotlib.mlab to calculate the euclidean distance. """
    vector1, vector2 = list_to_npArray(vector1, vector2)
    dist = plt.mlab.dist(vector1, vector2)
    return dist


def main(args):
    """Main function to process the inputs and perform computations"""

    fvector = args.fastaFile + ".RTD_vector.k_" + str(args.kmerSize) + ".tsv"
    fdist = args.fastaFile + ".RTD_distance_matrix.k_" + str(args.kmerSize) + ".tsv"
    fnewick = args.fastaFile + ".RTD_newick.k_" + str(args.kmerSize) + ".nwk"
    fpng = args.fastaFile + ".RTD_newick.k_" + str(args.kmerSize) + ".png"

    if args.seqType == 'N':
        bases = ['A', 'C', 'G', 'T']
    else:
        bases = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

    fasta_sequences = SeqIO.parse(open(args.fastaFile), 'fasta')

    kmers = getKmers(args.kmerSize, bases)
    fout = open(fvector, "w")
    fout.write("OTU\t")
    for kmer in kmers:
        kmean = kmer + '_mean'
        ksd = kmer + '_sd'
        fout.write(kmean + "\t" + ksd + "\t")
    fout.write("\n")

    for seq in fasta_sequences:
        fout.write(seq.id + "\t")
        for kmer in kmers:
            rtd = getRTD(str(seq.seq), kmer)
            fout.write("{}\t{}\t".format(rtd[0], rtd[1]))
        fout.write("\n")
    fout.close()

    df = pandas.read_csv(fvector, delimiter="\t")
    del df[list(df.columns)[-1]]
    dm = pandas.DataFrame(squareform(pdist(df.iloc[:, 1:])), columns=df.OTU.unique(), index=df.OTU.unique())
    dm.to_csv(fdist, sep='\t')

    pdm = dendropy.PhylogeneticDistanceMatrix.from_csv(src=open(fdist), delimiter="\t")
    nj_tree = pdm.nj_tree()
    sn = str(nj_tree) + ";"
    ftree = open(fnewick, "w")

    ftree.write(sn)
    ftree.close()

    t = Tree(sn)
    t.render(fpng)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Return Time Distribution based Alignment-free Phylogeny Analysis",
                                     epilog="Citation Information:\n\nKolekar P., Kale M., Kulkarni-Kale U., "
                                            "Alignment-free distance measure based on return time distribution for sequence"
                                            " analysis: Applications to clustering, molecular phylogeny and subtyping, "
                                            "Molecular Phylogenetics and Evolution, (2012) 65(2): 510-522. "
                                            "\n[PMID: 22820020]\n \n",
                                     formatter_class=CustomFormatter)
    parser.add_argument("--fastaFile", default=None, help="File with sequences in FASTA format", required=True)
    parser.add_argument("--seqType", default='N', help="Type of input sequences, either Nucleotide (N) or Protein (P)",
                        choices=['N', 'P'])
    parser.add_argument("--kmerSize", default=1, help="Size of k-mer to compute return time distributions (RTDs)",
                        type=int,
                        required=True, choices=[1, 2, 3, 4, 5, 6, 7])
    parser.add_argument('--version', action='version', version='RTD v0.0.1')

    args = parser.parse_args()
    main(args)
