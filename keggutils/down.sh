
java -cp target/keggutils-0.0.1.jar org.raygoza.kegg.GenePathwaysRetriever $1 $1.xml && growlnotify -m "$1.xml done"