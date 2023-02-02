#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
int main()
{
	int N, count = 0;
	int temp; // while문 반복할 때 값 저장위해
	int a, b , c; // a는 10의 자리 b는 일의 자리
	int check = 0;
	scanf("%d", &N);
	a = N / 10;
	b = N % 10;
	
	while (1)
	{
		count++;
		c = (a + b) % 10;
		temp = b * 10 + c;  // 비교되는 값 temp
		if (N == temp)
			break;
		a = temp / 10;
		b = temp % 10;

	}
	printf("%d", count);


	return 0;
}
