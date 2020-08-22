set -e
mkdir -p tmp
bowtie2-build $1 tmp/idx
bowtie2 -x tmp/idx -1 ${2}_1.fastq -2 ${2}_2.fastq -S tmp/aln.sam -p 4
