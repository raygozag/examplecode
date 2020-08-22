invisible(library(RMySQL))

conn<-dbConnect(MySQL(), user="root", password="hermosillo", host='localhost')

dbs<-dbGetQuery(conn,'show databases')

exclude=c("mysql","sys","performance_schema","information_schema")

dbs<-setdiff(dbs[,1],exclude)

paste0(dbs,collapse=" ")

dbDisconnect(conn)