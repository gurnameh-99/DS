#include <iostream>
#include <algorithm>

#define lli long long int
using namespace std;
int main()
{
    int t = 0;
    cin >> t;
    for(int i = 1; i<=t; i++){
        lli N = 0, B = 0;
        cin >> N >> B;
        lli A[N];
        for(lli i = 0; i<N; i++){
            cin >> A[i];
        }
        sort(A, A+N);
        lli res = 0, cost = 0;
        
        for(lli i = 0; i < N; i++){
            if(cost+A[i] <= B){
                cost += A[i];
                res++;
            }
            else{
                break;
            }
        }
        cout<<"Case #"<<i<<": "<<res;
    }
 
    return 0;
}