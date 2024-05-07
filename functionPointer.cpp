#include<iostream>
using namespace std;

void print()
{
	cout<<"This is demo of function pointer\n";
}

int main()
{
	void (*p)();
	p=print;
	p();
	return 0;
}
