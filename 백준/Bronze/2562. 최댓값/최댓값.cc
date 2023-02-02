#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
int main()
{
	int max, number = 0, i;
	int index = 0;
	int num[9] = { 0 };
	for (i = 0; i < 9; i++)
	{
		scanf("%d", &num[i]);
	}
	max = num[0];
	for (i = 0; i < 9; i++)
	{
		if (num[i] > max)
		{
			max = num[i];
			index = i;
		}
	}
	printf("%d\n%d", max, index+1);
	return 0;
}