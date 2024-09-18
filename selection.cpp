#include<iostream>
using namespace std;

int main()
{
    int temp=0;
    int a[]={23,1,10,5,2};
    int size=sizeof(a)/sizeof(a[0]);
    
    for(int i=0;i<size-1;i++)
    {
        int min=i;
        for(int j=i+1;j<size;j++)
        {
            if(a[min]>a[j])
            {
                min=j;
            }
        }
        int tem=a[min];
        a[min]=a[i];
        a[i]=tem;
    }  
    for (int i = 0; i < size; i++)
       cout << a[i] << " ";
       
       cout<<"\n";
   
    
}