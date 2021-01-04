#include <iostream>
#include <string.h>
#include <sstream>
#define lli long long int
using namespace std;

int main() {
    int t = 0;
    cin>>t;
    while (t--)
    {
        string problems, str;
        lli T = 0;
        lli n = 0, k = 0, d = 0;
        lli totalProb = 0;
        cin>>n>>k>>d;
        cin.ignore();
        getline(cin, problems);
        istringstream X(problems);
        while ( X >> T )
        {
            totalProb += T;
        }
        lli result = totalProb/k;
        if(result >= d){
            cout<<d;
        }
        else
        {
            cout<<result;
        }
    }
    
    return 0;
}