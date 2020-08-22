#include <fstream>
#include <string>
#include <iostream>

using namespace std;

int main (int argc, char const *argv[])
{

  ifstream is(argv[1],ios::in);
  ofstream os(argv[2],ios::out);

  string line;

  string suffix = argv[3];
  while(getline(is,line)){

    int l=line.find(" ");
    os << line.substr(0,l)+"/"+suffix << endl;
    getline(is,line) ;
    os << line << endl;
    getline(is,line) ;
    os << "+" << endl;
    getline(is,line) ;
    os << line << endl;
  }

 os.close();
  is.close();

  return 0;
  }