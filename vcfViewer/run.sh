mvn clean compile package
mvn dependency:copy-dependencies
cp target/dependencies/* target/
java -jar target/vcfViewer-0.1.jar