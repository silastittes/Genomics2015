#first positional argument is reference, second is the prefix for paired-end fastq files to align to the reference. Modify bwa and samtools flags at your own risk. NOTE FILES MUST END IN *_1.fastq and *_2.fastq
ref=$1
gn=$2

#index the reference
bwa index $ref
#generate samfile
bwa mem $ref ${gn}_1.fastq ${gn}_2.fastq > $gn.sam
#convert to bam
samtools view -b -o $gn.bam -S ${gn}.sam
#sort the bam file
samtools sort ${gn}.bam ${gn}.sorted
#index the sorted bam file
samtools index ${gn}.sorted.bam
#index the reference
samtools faidx $ref
#call snps and indels
samtools mpileup -uf $ref ${gn}.sorted.bam | bcftools view -vcg - >  ${gn}.vcf
#command for new samtools
#samtools mpileup -uf $ref ${gn}.sorted.bam | bcftools call -mv >  ${gn}.vcf
