## Downloads an sra file with given run accession and uses edgepro to measure fpkm for a bacterial genome.


set -e

if [ -f rpkms/${1}.rpkm_0 ]; then
    exit
fi

mkdir -p ${1}

wget -O ${1}.sra $(esearch -db sra -query ${1}| efetch -format runinfo| tail -n 2| head -n 1| awk -F, '{print $10}')

cp ${1}.sra ${1}

cd ${1}

fastq-dump ${1}.sra

rm -rf ${1}.sra

fastp -i ${1}.fastq -o ${1}T.fastq -w 8 --cut_right -w 24


rm -rf ${1}.fastq


mkdir -p  edge

cd edge


edge.pl -g ../../ref/U00096.fna -p ../../ref/U00096.ptt -r ../../ref/U00096.rnt -u ../${1}T.fastq -t 24 -o ${1}


mv ${1}.rpkm_0 ../../rpkms
cd ../..

rm -rf ${1}




