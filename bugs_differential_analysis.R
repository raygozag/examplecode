#######################
## This script performs differential abundance for metaphlan results with a small sample size per group.
#######################


library(doBy)
library(foreach)
library(parallel)
library(doParallel)
cl<-makeCluster(detectCores())
registerDoParallel(cl)

meta<-read.table("mapping.tsv",sep="\t",stringsAsFactors = F,header = T)


bugs<-read.table('bugs/uc_bugs.tsv',sep="\t",header = T,stringsAsFactors = F)

bugs<-bugs[which(bugs$sample_id%in%meta$id),]

meta<-meta[which(meta$id%in%bugs$sample_id),]

meta<-meta[match(bugs$sample_id,meta$id),]



bugs<-bugs[match(meta$id,bugs$sample_id),]

table(meta$id==bugs$sample_id)

bugs$sample_id<-NULL

bugs<-cbind(meta,bugs)


taxa<-colnames(bugs[,3:ncol(bugs)])





data<-matrix(nrow=0,ncol=8)
colnames(data)<-c("variable","zero_proportion","Hc","Post-uc","Pre-uc ","kw_pre_post.p","kw_pre_hc.p","kw_post_hc.p")

dec=3
data<-foreach(i=taxa,.combine = "rbind")%dopar%{
  zeroProp<-zero_prop(bugs,i)

  form<-as.formula(paste0(i," ~ category"))

  means<-mean_groups(bugs,form)

  kw_pre_post<-kruskal_pvalue(bugs,c("Pre-uc","Post-uc"),form)


  kw_pre_hc<-kruskal_pvalue(bugs,c("Pre-uc","Hc"),form)

  kw_post_hc<-kruskal_pvalue(bugs,c("Post-uc","Hc"),form)

  row<-c(i,round(zeroProp,dec),means,round(kw_pre_post,dec),round(kw_pre_hc,dec),round(kw_post_hc,dec))
  names(row)<-c("variable","zero_proportion","mean_Hc","mean_Post-uc","mean_Pre-uc ","kw_pre_post.p","kw_pre_hc.p","kw_post_hc.p")
  row
}

#Multiple testing correction

write.table(data,'bugs_comparison.tsv',sep="\t",col.names = T, row.names = F,quote = F)


stopCluster(cl)