#include<iostream>
using namespace std;

int main()
{
    int temp=0;
    int a[]={23,1,10,5,2};
    int size=sizeof(a)/sizeof(a[0]);
    for(int i=0;i<size;i++)
    {
       int key=a[i+1];
       int j=i;

       while(j>=0 && a[j]>key)
       {
        cout<<"while\n";
        a[j+1]=a[j];
        j=j-1;
         for (int i = 0; i < size; i++)
       cout<<a[i] << " ";
       cout<<"\n";
       }
       a[j+1]=key;
       for (int i = 0; i < size; i++)
       cout << a[i] << " ";
       
       cout<<"\n";
   
    
    }  
    
}