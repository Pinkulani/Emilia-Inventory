// Emilia @ 14.7.2023

#include <iostream>
#include <fstream>
using namespace std;

int main () {
  ofstream TestFile ("Test.txt");
  if (TestFile.is_open())
  {
    TestFile << "Hello. \n";
    TestFile << "OwO. \n";
    TestFile.close();
  } else cout << "Unable to open file";
  
  return 0;
}