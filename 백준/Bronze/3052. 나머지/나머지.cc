#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main()
{
	int num, i, j, remain[10] = { 0 };
	int count = 0, check = 0;
	for (i = 0; i < 10; i++)
	{
		scanf("%d", &num);
		remain[i] = num % 42;
	}
	for (i = 0; i < 10; i++)
	{
		check = 0;
		for (j = i + 1; j < 10; j++)
		{
			if (remain[i] == remain[j])
			{
				check = 1;
			}
		}
		if (check == 0)
			count++;
	}
	printf("%d", count);
	return 0;
}