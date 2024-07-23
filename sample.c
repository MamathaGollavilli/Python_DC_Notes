#include <stdio.h>
void display()
{
printf("hello world\n");
}
void display1()
{
printf("hello python\n");
}
int add(int a,int b)
{
return (a+b);
}
void main()
{ 
display();
display1();
int c = add(20,30);
printf("c = %d\n",c);
}