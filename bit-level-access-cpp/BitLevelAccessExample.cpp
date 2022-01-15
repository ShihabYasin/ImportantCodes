#include <stdio.h>
#include <iostream>
using namespace std;

void printingBits( int i)
{
	unsigned int ind = 1;
	for (int j = 31; j > -1 ; j--)
	{		
		//printf("%d ", ((ind << j)&i) ? 1 : 0);
	}
	//printf("\n");
}
int readBit(int i, int position)
{
	return ((1 << position)&i)?1:0;
}
void setBit(int* i, int position)
{
	unsigned int ind = 1;
	*i = (*i) | (ind << position);
	printingBits(*i);
}
void resetBit(int* i, int position)
{
	unsigned int ind = 1;
	*i = (*i & ind << position) ? (*i) ^ (ind << position) :*i ;
	printingBits(*i);
}
void cpyBit(int from, int* to, int position)
{
	((1 << position) & from) ? setBit(to,position) : resetBit(to,position) ;
}
void SetDate(int date, int month, int year, int* result)
{
	for (int i = 0; i <= 4; i++)
	{
		cpyBit(date, result, i);
	}
	for (int i = 5; i <= 8 ; i++)
	{
		readBit(month, i - 5) ? setBit(result, i ) : resetBit(result, i);
	}
	for (int i = 9; i <= 15; i++)
	{
		readBit(year, i - 9) ? setBit(result, i) : resetBit(result, i);
	}
}
void printDate(int result)
{
	int _date=0, _month=0, _year = 0;
	for (int i = 0; i <= 4; i++)
	{
		cpyBit(result, &_date, i);
	}
	for (int i = 5; i <= 8; i++)
	{
		readBit(result, i) ? setBit(&_month, i - 5) : resetBit(&_month, i - 5);
	}
	for (int i = 9; i <= 15; i++)
	{
		readBit(result, i) ? setBit(&_year, i - 9) : resetBit(&_year, i - 9);
	}
	printf("\n Date: %d  Month: %d  Year:  %d\n",_date,_month,_year);
}
int main()
{
	int res = 0x00000000;
	SetDate(31,1,99,&res);
	printDate(res);
	SetDate(13, 10, 59, &res);
	printDate(res);
	//printf("\n\n\n");
	return 0;
}
