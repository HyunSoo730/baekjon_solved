#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
int main()
{
	int N, M, i, min, max;
	min = 1000000;
	max = -1000000;
	scanf("%d", &N);
	for (i = 0; i < N; i++)
	{
		scanf("%d", &M);
		if (M >= max)
			max = M;
		if (M <= min)
			min = M;
	}
	printf("%d %d", min, max);
	return 0;
}