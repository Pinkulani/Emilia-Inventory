// Emilia @ 14.7.2023

#include <iostream>
#include <fstream>
using namespace std;

ofstream TestFile ("Test.txt");

int main () {
  cout << "|- Emilia's Inventory -|" << endl << "Version: 0.01" << endl;
  if (TestFile.is_open())
  {
    TestFile << "Hello. \n";
    TestFile << "OwO. \n";
    TestFile.close();
  } else cout << "Unable to open file";
  
  return 0;
}