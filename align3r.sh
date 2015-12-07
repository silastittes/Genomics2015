#first positional argument is reference, second is a fastq file of single-end reads to align to the reference
ref=$1
gn=$2

#index the reference
bwa index $ref
#generate samfile
bwa mem $ref $gn > $gn.sam
#convert to bam
samtools view -b -o $gn.bam -S $gn.sam
#sort the bam file
samtools sort $gn.bam $gn.sorted
#index the sorted bam file
samtools index $gn.sorted.bam
#index the reference
samtools faidx $ref
#call snps and indels
samtools mpileup -uf $ref $gn.sorted.bam | bcftools view -vcg - >  $gn.vcf
