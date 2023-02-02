#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
int Getnumber(int N)  //각 자리가 등차수열인 수인 한수를 만족하는지 판별N은 1000보다 같작.
{
	int i, result, a, b, c;
	if (N < 100)
	{
		result = 1;   //100미만이면 무조건 등차수열을 만족하는 한수
		return result;
	}
	else//100~1000
	{
		a = N / 100;// 백의 자리
		b = (N / 10) % 10;//십의 자리
		c = N % 10;//일의 자리
		if (a == b && b == c)
			result = 1;
		else if ((b - a) == (c - b))
			result = 1;
		else result = 0;
		return result;
	}
}
int main()
{
	int N, i, count = 0, result;
	scanf("%d", &N);
	for (i = 1; i <=N; i++)
	{
		result = Getnumber(i);
		if (result == 1)
			count++;
	}
	printf("%d", count);
	return 0;
}