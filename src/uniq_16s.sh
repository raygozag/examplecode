set -e

F="${1}merged.fastq.gz"
if [ -f ${F} ]; then
	exit 1
fi

sh ~/src/download_sra ${1}
fastq-dump --split-files ${1}.sra
rm ${1}.sra
kneaddata -i ${1}_1.fastq -i ${1}_2.fastq -db ~/humannomito -o clean
mv clean/${1}_1_kneaddata_paired_1.fastq ${1}clean_R1.fastq
mv clean/${1}_1_kneaddata_paired_2.fastq ${1}clean_R2.fastq
rm -rf clean
rm  ${1}_1.fastq ${1}_2.fastq
usearch -fastq_mergepairs ${1}clean_R1.fastq -fastq_minmergelen 100 -fastq_maxmergelen 470 -relabel @ -report /tmp/merge_nofilter.log -fastqout ${1}merged.fastq -tabbedout ${1}detail.log
rm ${1}clean_R1.fastq ${1}clean_R2.fastq
pigz ${1}merged.fastq
pigz ${1}detail.log