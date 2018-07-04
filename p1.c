#include<stdio.h>
main()
{
int i,j,k=0,l;
char a[10],b[10];
printf("enter the string:\n");
gets(a);
l=strlen(a);
//printf("string length:%d\n",l);

for(i=0;i<l;i++)
{
 for(j=l-1;j>0;j--)
 {
  if(a[i]==a[j])
  {
  
   b[k]=a[i];
   
  }
   
   else
   {
   j--;
   }
 }
}

printf("substrings:%c\n",b[k]);


}
