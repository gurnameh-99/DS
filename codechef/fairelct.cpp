#include <iostream>
#include <algorithm>
#define lli long long int
using namespace std;

int main() {
    int t = 0;
    cin>>t;
    while (t--)
    {
        lli sumA = 0, sumB = 0;
        lli n = 0, m = 0;
        cin>>n>>m;
        lli a[n], b[m];
        for (lli i = 0; i < n; i++)
        {
            cin >> a[i];
            sumA += a[i];
        }
        for (lli i = 0; i < m; i++)
        {
            cin >> b[i];
            sumB += b[i];
        }
        lli swap = 0, temp = 0, count = 0;
        sort(a, a+n);
        sort(b, b+m, greater<lli>());
        if (n <= m)
        {
            count = n;
        }
        else
        {
            count = m;
        }
        
        
        for (lli i = 0; i < count; i++)
        {
            if(sumA > sumB){
                break;
            }
            
            sumA = sumA - a[i] + b[i];
            sumB = sumB - b[i] + a[i];
            swap += 1;
        }

        if(sumA <= sumB){
            swap = -1;
        }

        cout<<swap<<endl;      
        
    }
    
    return 0;
}