#include <iostream>
#include <string>
#include <vector>
#define lli long long int
using namespace std;

int main() {
    int t = 0;
    cin>>t;
    while (t--)
    {
        string str;
        cin.ignore();
        getline(cin, str);
        vector<int> T;
        for (int i = 0; str[i] != '\0'; i++)
        {
            T.push_back(str[i] - 48);
        }
        int j =0;
        while(j < T.size()){
            cout<<T[j]<<endl;
            j++;
        }
        

    }
    
    return 0;
}