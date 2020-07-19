![alt text](data/RTD_Phylogeny.jpeg "RTD logo (c) Pandurang Kolekar 2017")

# RTD Phylogeny
Molecular phylogeny analysis using Return time distribution (RTD) based alignment-free sequence analysis method



### Author
Pandurang Kolekar, PhD Bioinformatics

![alt text](https://orcid.org/sites/default/files/images/orcid_16x16(1).gif "Logo ORCID") http://orcid.org/0000-0003-0044-0076

E-mail: pandurang.kolekar@gmail.com

Website: [http://biosakshat.wixsite.com/pandurang-kolekar](http://biosakshat.wixsite.com/pandurang-kolekar)
___

## Introduction

Return time distribution (RTD) is a method for alignment-free phylogenetic analysis using nucleotide / protein sequences. The method first computes the RTDs of k-mers and summarize them using the parameters of RTDs viz. mean and standard deviation for each of the sequences. Thus, each sequence is converted into a numeric vector of the size _2*4<sup>k</sup>_. The pair wise distance between numeric vectors of sequences is calculated using Euclidean distance function. The pairwise distance matrix, thus obtained is given as an input to Neighbor-joining clustering algorithm to reconstruct phyogenetic tree. 

The statistical details of the method are described in [Kolekar et al. 2012](https://www.ncbi.nlm.nih.gov/pubmed/22820020)

## Requirements

Tested on Python 3.7
Please refer to requirements.txt file

## Quick Start
```shell
python src/rtd_phylogeny.py --help
python src/rtd_phylogeny.py --version
python src/rtd_phylogeny.py --fastaFile <input_file> --seqType N --kmerSize 3
```

## Web Server

The web server for RTD-based phylogeny is available from [http://bioinfo.net.in/RTD/home.html](http://196.1.114.46:1800/RTD/home.html).

## Perl Executables

The standalone Perl executables for RTD Phylogeny program are available from [http://bioinfo.net.in/RTD/download.html](http://196.1.114.46:1800/RTD/download.html).

## Citation Information

If you find this program useful please cite it as following,

Kolekar P., Kale M., Kulkarni-Kale U., Alignment-free distance measure based on return time 
distribution for sequence analysis: Applications to clustering, molecular phylogeny and subtyping, 
Molecular Phylogenetics and Evolution, (2012) 65(2): 510-522

PubMed ID: [22820020](https://www.ncbi.nlm.nih.gov/pubmed/22820020)

## Feedback

Please do feel free to give your comments / suggestions about this package by any of the following mode.

* Report an issue on this GitHub repository [here](https://github.com/pandurang-kolekar/rtd-phylogeny/issues)

* E-mail us at rtd.phylogeny@gmail.com

* Fill the feedback form for the RTD Phylogeny server: Available [here](https://docs.google.com/forms/d/e/1FAIpQLSel8RYKGQ3IIUxwjo0HgrDUyNv0ClNNwQETvguLUA2VYt0Odw/viewform)

Your feedback is highly valuable! 
