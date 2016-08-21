//first challenge, reversing a string. I will use recursion and code in c++

#include <string>
#include <iostream>

using namespace std;

string reverse (string str) {
  //base case, empty string will be returned
  if (str == "") return str;
  
  //if not, return the last character of the string + the reverse method again, with the last character chopped off.
  return str[str.size()-1] + reverse(str.substr(0,str.size()-1));
}


int main(int argc, char* argv[]) {
	string original = argv[1];
	string reversed = reverse(original);
	cout << reversed << endl;
	return 0;
}
