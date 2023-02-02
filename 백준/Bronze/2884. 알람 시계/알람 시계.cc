#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main()
{
	int a, b, c; // 시 분  각각 범위 설정 
	scanf("%d %d", &a, &b);
	if (b < 45)
	{
		if (a != 0)
		{
			a = a - 1;
			b = b + 15;
		}
		else
		{
			a = 23;
			b = b + 15;
		}
	}
	else
	{
		b = b - 45;
	}
	printf("%d %d", a, b);


	return 0;
}