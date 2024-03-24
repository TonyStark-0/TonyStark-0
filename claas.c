#include<stdio.h>

int main()

{
    int n;

    float sum = 0;
    
    printf("enter the value of n ");

    scanf("%d",&n);

    for(int i = 0; i<=n; i++)
    {
        sum += 1.0 / i;
    }
    printf("\n the result is %f",sum );


}