# RTD Phylogeny
Molecular phylogeny analysis using Return time distribution (RTD) based alignment-free sequence analysis method

![alt text][logo]

[logo]: http://196.1.114.46:1800/RTD/images/RTD_.jpg "RTD logo (c) Pandurang Kolekar 2017"
___

## Introduction

Return time distribution (RTD) is a method for alignment-free phylogenetic analysis using nucleotide / protein sequences. The method first computes the RTDs of k-mers and summarize them using the parameters of RTDs viz. mean (\mu) and standard deviation (\sigma) for each of the sequences. Thus, each sequence is converted into a numeric vector of the size _2*4<sup>k<sup>_. The pair wise distance between numeric vectors of sequences is calculated using Euclidean distance function. The pairwise distance matrix, thus obtained is given as an input to Neighbor-joining clustering algorithm to reconstruct phyogenetic tree. The details of the method are described in [Kolekar et al. 2012](https://www.ncbi.nlm.nih.gov/pubmed/22820020)

## Requirements

## Quick Start

## 
