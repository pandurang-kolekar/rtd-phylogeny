# RTD Phylogeny
Molecular phylogeny analysis using Return time distribution (RTD) based alignment-free sequence analysis method

![alt text][logo]

[logo]: http://196.1.114.46:1800/RTD/images/RTD_.jpg "RTD logo (c) Pandurang Kolekar 2017"
___

## Introduction

Return time distribution (RTD) is a method for alignment-free phylogenetic analysis using nucleotide / protein sequences. The method first computes the RTDs of k-mers and summarize them using the parameters of RTDs viz. mean (\mu) and standard deviation (\sigma) for each of the sequences. Thus, each sequence is converted into a numeric vector of the size _2*4<sup>k<sup>_. The pair wise distance between numeric vectors of sequences is calculated using Euclidean distance function. The pairwise distance matrix, thus obtained is given as an input to Neighbor-joining clustering algorithm to reconstruct phyogenetic tree. 

The statistical details of the method are described in [Kolekar et al. 2012](https://www.ncbi.nlm.nih.gov/pubmed/22820020)

## Requirements

* Python 2.7+
* BioPython
* Pandas
* NumPy
* SciPy
* matplotlib
* DendroPy
* ete3

## Quick Start
```shell
python RTD.py --help
python RTD.py --version
python RTD.py --fastaFile <input_file> --seqType N --kmerSize 3
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

* Create an issue ticket on this GitHub repository

* E-mail us at rtd.phylogeny@gmail.com

* Fill the feedback form for the RTD Phylogeny server: Available [here](https://docs.google.com/forms/d/e/1FAIpQLSel8RYKGQ3IIUxwjo0HgrDUyNv0ClNNwQETvguLUA2VYt0Odw/viewform)