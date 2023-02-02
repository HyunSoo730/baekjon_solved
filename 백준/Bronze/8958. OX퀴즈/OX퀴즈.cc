#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
int main()
{
	int N, i, j;
	char ch[81] = "";
	int length = 0, score = 0, count = 0;
	scanf("%d", &N);
	for (i = 0; i < N; i++)
	{
		scanf("%s", ch);
		score = 0;
		count = 1;   //연속으로 맞는 횟수
		length = strlen(ch);
		for (j = 0; j < length; j++)
		{
			if (ch[j] == 'O')
			{
				score = score + count;
				count++;
			}
			else   //틀린 경우
				count = 1;
		}
		printf("%d\n", score);
	}
	return 0;
}