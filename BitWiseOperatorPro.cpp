/* GetBit,Setbit,Clearbit and UpdateBit using bitwiseoperator*/
#include <iostream>
using namespace std;
int Getbit(int n, int pos)
{
    return ((n&(1<<pos))!=0);
}

int Setbit(int n, int pos)
{
    return ((n|(1<<pos))!=0);
}

int Clearbit(int n, int pos)
{
    return ((~n&(1<<pos))!=0);
}

int UpdateBit(int n, int pos)
{
    return ((~n |(1<<pos))!=0);
}
int main()
{
    std::cout<<Getbit(5,2)<<endl;
    std::cout<<Setbit(5,2)<<endl;
    cout<<Clearbit(5,2)<<endl;
    cout<<UpdateBit(5,2)<<endl;
    return 0;
}
