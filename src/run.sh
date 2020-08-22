#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=80
#SBATCH --time=11:50:00
#SBATCH --job-name=tst[run]
#SBATCH --mail-type=ALL
#SBATCH --output=/scratch/c/croitoru/raygozag/diab/out.txt


cd $SLURM_SUBMIT_DIR

mkdir [run]
cd [run]

module load java
set -e

download_sra [run]
fastq-dump --split-files [run].sra
rm -rf [run].sra
conda activate knead
kneaddata -i [run]_1.fastq -i [run]_2.fastq  -db ${scrt}/humannomito -o clean --bowtie2-options "--very-sensitive -p 20" --trimmomatic '/home/c/croitoru/raygozag/bin/Trimmomatic-0.38'
conda deactivate 
mv clean/[run]_1_kneaddata_paired_1.fastq m1.fastq
mv clean/[run]_1_kneaddata_paired_2.fastq m2.fastq
rm -rf [run]_1.fastq
rm -rf [run]_2.fastq
rm -rf clean
/scratch/c/croitoru/raygozag/a5_miseq_linux_20160825/bin/a5_pipeline.pl m1.fastq  m2.fastq tst --metagenome --threads 20
rm -rf tst.s*
rm -rf tst.libr*
rm -rf tst.preproc*
rm -rf tst.ec.*
rm -rf tst.tmp*
rm -rf *.fastq

conda activate prokka_env
prokka --outdir annot --prefix npc  tst.contigs.fasta 
conda deactivate
pigz *.fasta
conda activate hmmer
cd annot
hmmsearch -E 0.0001 --tblout hits.txt ${scrt}/hmms/NLPC_P60.hmm npc.faa
cat hits.txt | grep -v "\#" |awk '{print $1}' > ids.txt
conda deactivate 
pigz *

#
