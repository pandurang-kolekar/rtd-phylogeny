import rtd_phylogeny as rtd

letters = ['A', 'C', 'G', 'T']
kmerSize = 2
expectedKmers = ['AA', 'AC', 'AG', 'AT', 'CA', 'CC', 'CG', 'CT', 'GA', 'GC', 'GG', 'GT', 'TA', 'TC', 'TG', 'TT']


def test_getKmers():
    assert rtd.getKmers(kmerSize, letters) == expectedKmers

