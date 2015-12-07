# getfeatures
Extract annotated sequence features in a genbank file from a fasta file.
Designed for extracting features from organellar genomes. functional on genbank format as of December 7th, 2015. For *nix machines only.

Usage:
```
python getfeatures.py --fasta <A_thaliana_cp.fasta> --genbank <A_thaliana_cp.gb>
```

Output is written to screen. Redirect to file with the ">" operator.

Arabidopsis thaliana chloroplast files are provided here for example (A_thal*) 
