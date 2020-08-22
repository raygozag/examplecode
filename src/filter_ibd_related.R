
print(getwd())

args = commandArgs(trailingOnly=TRUE)
ibd<-read.table(paste0(args[1],'indp.genome.gz'),header=T,as.is = T)
png('identity-by-descent.png')
hist( ibd$PI_HAT, breaks = 100, ylim = c(0,1000) )
dev.off()
exclusions = ibd[ ibd$PI_HAT > 0.2, c('FID2','IID2')]
write.table( exclusions, file=paste0(args[1],"_related_samples.txt"), col.names = F, row.names = F, quote = F )