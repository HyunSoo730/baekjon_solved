#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
int main()
{
	int C, N, i, count, cnt = 0;
	int score[1000] = { 0 }, sum = 0;
	double avg = 0.0;
	scanf("%d", &C);
	for (count = 0; count < C; count++)
	{
		scanf("%d", &N);
		avg = 0.0;
		cnt = 0;
		sum = 0;
		for (i = 0; i < N; i++)
		{
			scanf("%d", &score[i]);
			sum = sum + score[i];
		}
		avg = (double)sum / N;  //평균
		for (i = 0; i< N; i++)
		{
			if (score[i] > avg)
			{
				cnt++;
			}
		}
		printf("%.3lf%%\n", (double)cnt * 100 / N);
	}

	return 0;
}