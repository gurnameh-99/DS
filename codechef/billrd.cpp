#include <iostream>
#include <algorithm>
#define lli long long int
using namespace std;

int main() {
    int t = 0;
    cin>>t;
    while (t--)
    {
        lli N=0, K=0, x=0, y=0;
        cin>>N>>K>>x>>y;
        lli resx=0, resy=0;
        K = K%4;
        if(x==y){
            resx=N;
            resy=N;
        }
        else if (x>y)
        {
            if (K==1)
            {
                resx=N;
                resy=y+N-x;
            }
            else if (K==2)
            {
                resx=y+N-x;
                resy=N;
            }
            else if (K==3)
            {
                resx = 0;
                resy = x-y;
            }
            else{
                resx=x-y;
                resy=0;
            }
            
            
        }
        else
        {
            if (K==1)
            {
                resx=x+N-y;
                resy=N;
            }
            else if (K==2)
            {
                resx=N;
                resy=x+N-y;
            }
            else if (K==3)
            {
                resx = y-x;
                resy = 0;
            }
            else{
                resx=0;
                resy=y-x;
            }

        }
        cout<<resx<<" "<<resy<<endl;
    }
    return 0;
}