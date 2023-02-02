#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main()
{
	int A, B, C; // 세 개의 주어진 수
	int count[10] = { 0 };  //0~9까지 몇 번 나왔는지 확인하기 위해
	int length = 0, i;
	int num, num2, temp;
	scanf("%d %d %d", &A, &B, &C);
	num = A * B * C;
	num2 = num;
	while (num != 0)
	{
		num = num / 10;
		length++;
	}//자릿수 확보
	for (i = 0; i < length; i++)
	{
		temp = num2% 10;//한 자릿수씩 비교하기 위해 temp에 저장해둠
		count[temp]++;//temp가 나온 수 즉 0~9중 count배열에 증가시켜둠
		num2 = num2 / 10;
	}
	for (i = 0; i < 10; i++)
	{
		printf("%d\n", count[i]);
	}
	return 0;
}