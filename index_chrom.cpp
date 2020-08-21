//Generates an index for a text file containing SNP information for easy lookup.
//saves the byte position and the value for the first column of the first line of a block of lines in a file.

#include <string>
#include <fstream>
#include <iostream>
#include "Tokenizer.h"

using namespace std;


int main (int argc, char const *argv[])
{
	
	size_t sz;
	
	long chunk_size = stol(argv[1],&sz);
	long lines=0;
	
	string infile="chr"+string(argv[2])+".txt";
	string index_file="chr"+string(argv[2])+".idx";
	ifstream chr(infile.c_str(),ios::in);
	ofstream idx(index_file.c_str(),ofstream::binary);
	
	
	string line;
	
	long pos=chr.tellg();
	getline(chr,line);
	
	Tokenizer tk(line,"\t");
	
	vector<string> values = tk.split();
	
	unsigned long long chrpos= stol(values[1],&sz);
	
	
	idx.write((char*)&chrpos,sizeof(unsigned long long ));
	idx.write((char*)&pos,sizeof(unsigned long long));
	lines=1;
	
	while(getline(chr,line)){
		lines++;
		
		if(lines==chunk_size){
			Tokenizer tk(line,"\t");
	
			vector<string> values = tk.split();
	
			unsigned long long chrpos= stol(values[1],&sz);
	
			idx.write((char*)&chrpos,sizeof(unsigned long long ));
			idx.write((char*)&pos,sizeof(unsigned long long));
			idx.flush();
			lines=0;
			
		}
		
		
		
		pos = chr.tellg();
	}
	
	
	
	
	
	idx.close();
	return 0;
}