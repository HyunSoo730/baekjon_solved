#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main()
{
	int x, y;
	int count;
	scanf("%d %d", &x, &y);
	if (x > 0 && y > 0)
		count = 1;
	else if (x > 0 && y < 0)
		count = 4;
	else if (x < 0 && y>0)
		count = 2;
	else
		count = 3;
	printf("%d", count);

	return 0;
}