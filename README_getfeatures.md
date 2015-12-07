# getfeatures
Extract annotated sequence features in a genbank file from a fasta file.
Designed for extracting features from organellar genomes. functional on genbank format as of December 7th, 2015. For *nix machines only.

This script is intended to be used in a downstream blast, to compare a fasta that you are annotating, to the features of an already annotated genome.

Usage:
```
python getfeatures.py --fasta A_thaliana_cp.fasta --genbank A_thaliana_cp.gb
```

Output is written to screen. Redirect to file with the ">" operator.

Arabidopsis thaliana chloroplast files are provided here for example (A_thal*)

NOTE: The headers are made to be as informative as possible for annotation, which includes if it is one of multiple exons, the strand it was found on (+/-), and the positions where the feature occures. 
email silas(dot)tittes(at)gmail(dot)com
with questions.
