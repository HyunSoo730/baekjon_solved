#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main()
{
	int num, i, a, b;
	scanf("%d\n", &num);
	for (i = 0; i < num; i++)
	{
		scanf("%d %d", &a, &b);
		printf("%d\n", a + b);
	}
	return 0;
}