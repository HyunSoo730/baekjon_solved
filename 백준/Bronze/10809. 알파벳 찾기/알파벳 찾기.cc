#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
int main()
{
	char s[100] = "";
	int k[26];
	int index = 0, i, j;
	int length = 0, count = 0;
	for (i = 0; i < 26; i++)
		k[i] = -1;
	scanf("%s", s);
	length = strlen(s);   //문자열 길이
	for (i = 0; i < length; i++)
	{
		for (j = 0; j < 26; j++)
		{
			if (s[i] == 'a' + j && k[j] == -1)//k[j] == -1을 걸어준 이유는 중복 관리
			{
				k[j] = i;
				break;
			}
		}
	}
	for (i = 0; i < 26; i++)
	{
		printf("%d ", k[i]);
	}
	return 0;
}