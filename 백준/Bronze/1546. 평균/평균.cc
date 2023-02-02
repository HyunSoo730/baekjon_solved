#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main()
{
	int N, i;
	double score[1000], max = 0.0, avg = 0.0;
	scanf("%d", &N);
	for (i = 0; i < N; i++)
	{
		scanf("%lf", &score[i]);
		if (score[i] >= max)
			max = score[i];
	}
	for (i = 0; i < N; i++)
	{
		score[i] = score[i] / max * 100;
		avg = avg + score[i];
	}
	printf("%.2lf", avg / N);
	return 0;
}