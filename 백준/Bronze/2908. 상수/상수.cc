#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
int main()
{
	int a, b;   //세 자리 두 수 비교 위해
	int num1, num2;   //뒤집은 수 넣기 위해
	scanf("%d %d", &a, &b);
	num1 = (a % 10)*100 + ((a / 10) % 10)*10 + a / 100;
	num2 = (b % 10)*100 + ((b / 10) % 10)*10 + b / 100;
	if (num1 > num2)
		printf("%d", num1);
	else
		printf("%d", num2);
	return 0;
}