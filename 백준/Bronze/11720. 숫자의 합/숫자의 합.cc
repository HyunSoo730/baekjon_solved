#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
int main()
{
	int N, sum = 0, i;
	char num[100] = "";
	scanf("%d", &N);
	scanf("%s", num);//문자열 입력
	for (i = 0; i < N; i++)
	{
		sum = sum + num[i] - '0';
	}
	printf("%d", sum);
	return 0;
}