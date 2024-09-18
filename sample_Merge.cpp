#include<iostream>
using namespace std;


void merge(int arr[],int l,int m,int r)
{
int n1=m-l+1;
int n2=r-m;
int L[n1],R[n2];

for(int i=0;i<n1;i++)
    L[i]=arr[i+l];
for(int j=0;j<n2;j++)
    R[j]=arr[m+1+j];
int i=0,j=0,k=l;
while(i<n1 && j<n2)
{
    if(L[i]<=R[j])
    {
    arr[k]=L[i];
    i++;
    }
    else{
        arr[k]=R[j];
        j++;
    }
    k++;
}

while(i<n1)
{
arr[k]=L[i];
i++;
k++;
}
while(j<n2)
{
arr[k]=R[j];
j++;
k++;
}
}
void mergeSort(int arr[],int l,int r)
{
    if(l<r)
    {
    int m=l+(r-l)/2;
    mergeSort(arr,l,m);
    cout<<"\n first call ";
    for (int i = l; i < m; i++)
        cout << arr[i] << " ";
    mergeSort(arr,m+1,r);
    cout<<"\n Second call ";
    for (int i = m; i < r; i++)
        cout << arr[i] << " ";
    merge(arr,l,m,r);
    cout<<"\n Third call ";
    for (int i = l; i < r; i++)
        cout << arr[i] << " ";
    }
}
int main() {
    int arr[] = {12, 11, 13, 5, 6, 7};
    int n = sizeof(arr) / sizeof(arr[0]);

    mergeSort(arr, 0, n - 1);

    cout << "Sorted array: ";
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    return 0;
}



// o/p:
// first call 
//  Second call 12
//  Third call 11
//  first call 11
//  Second call 12
//  Third call 11 12
//  first call 11 12
//  first call
//  Second call 5
//  Third call 5
//  first call 5
//  Second call 6 
//  Third call 5 6
//  Second call 13 5 6
//  Third call 5 6 7 11 12 Sorted array: 5 6 7 11 12 13 