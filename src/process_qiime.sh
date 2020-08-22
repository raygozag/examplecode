

qiime tools import --input-path manifest --type SampleData[PairedEndSequencesWithQuality] --output-path demux.qza --input-format PairedEndFastqManifestPhred33

#qiime demux summarize --i-data demux.qza --o-visualization demux.qzv

#qiime quality-filter q-score --i-demux demux.qza --o-filtered-sequences demux-filtered.qza --o-filter-stats demux-filter-stats.qza

 qiime dada2 denoise-paired  --i-demultiplexed-seqs demux.qza --p-trim-left-f 0 --p-trunc-len-f 200 --p-trim-left-r 0 --p-trunc-len-r 200 --o-representative-sequences rep-demux.qza --p-n-threads 0 --o-table table1.qza --o-denoising-stats ^Cda-stats.qza

 


#qiime feature-table summarize --i-table table1.qza --o-visualization table.qzv --m-sample-metadata-file meta.txt 



#qiime feature-table tabulate-seqs --i-data demux.qza --o-visualization rep-seqs.qzv

qiime feature-classifier classify-sklearn --i-classifier ~/classifiers/silva/silvaNBSRA.qza  --i-reads rep-demux.qza --o-classification taxonomy.qz


qiime taxa barplot --i-table table1.qza --i-taxonomy taxonomy.qz.qza --m-metadata-file meta.txt --o-visualization taxa-bar-plots.qzv
