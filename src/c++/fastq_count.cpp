#include <seqan/seq_io.h>
#include <string>
#include <iostream>

using namespace std;
using namespace seqan;

int main(int argc, char const *argv[])
{
	SeqFileIn sq(argv[1]);
	string id;
	string seq;
	int k=0;
	while(!atEnd(sq)){
		readRecord(id,seq,sq);
		k++;
	}
	cout << argv[1] << "\t" << k << endl;
	return 0;
}