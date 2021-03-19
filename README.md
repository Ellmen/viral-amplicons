# Viral Amplicon Finder

This is a tool for finding low degeneracy amplicons that can amplify a variety of viral species. It is built on top of a Python3 compatible update to Primer Prospector (https://github.com/Ellmen/primerprospector3).


## Installing

Clone the repository and run

`pip install .`

This will install the Python library and the CLI.

## Usage example

Generate primer hits and amplicons:

```
cd test_data
amplicons find sars-cov-2.fasta aligned.fasta
```

Find lowest degeneracy primer pair:

```
amplicons ld
```
