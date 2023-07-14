// Emilia @ 14.7.2023

#include <iostream>
#include <fstream>
using namespace std;

ofstream ReadMe ("ReadMe.txt");
ofstream TestFile ("Test.txt");
ofstream WriteTest ("WriteTest.txt");

void Test() {
  if (ReadMe.is_open())
  {
    ReadMe << "Version: 0.01";
    ReadMe.close();
  } else cout << "Unable to open file";
}

void Write() {
  string Input;
  int Counter = 0;
  WriteTest.is_open();
  while (Counter < 10) {
   cout << "Type something: ";
   cin >> Input; 
   WriteTest << Input << endl;
   Counter++;
  }
  WriteTest.close();
}

int main () {
  cout << "|- Emilia's Inventory -|" << endl;
  if (TestFile.is_open())
  {
    TestFile << "Hello. \n";
    TestFile << "OwO. \n";
    TestFile.close();
  } else cout << "Unable to open file";
  
  Test();
  Write();
  return 0;
}
