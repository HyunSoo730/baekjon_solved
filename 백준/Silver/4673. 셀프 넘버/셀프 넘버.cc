#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
int sum(int N)
{
	int result = N;
	while (N)
	{
		result = result + N % 10;
		N = N / 10;
	}
	return result;   //합계 리턴
}
int main()
{
	int N, i, result;
	int index[10001] = { 0 };
	for (i = 1; i <= 10000; i++)
	{
		result = sum(i);
		if(result<=10000)
			index[result] = 1;   //생성자가 있는 수는 거르기 위해 1을 넣어둠
	}
	for (i = 1; i <= 10000; i++)
	{
		if (index[i] !=1)
		{
			printf("%d\n", i);
		}
	}
	return 0;
}