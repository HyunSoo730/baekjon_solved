#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//백준에서 스택 관련 문제들 풀기 !!!
typedef struct node {
	int data;
	struct node* next;
}Node;
typedef struct Stack {
	Node* top;
	int count;
}Stack;
void InitStack(Stack* stack)
{
	stack->top = NULL;
	stack->count = 0;
}
Node* NewNode(int data)
{
	Node* now = (Node*)malloc(sizeof(Node));
	now->data = data;
	now->next = NULL;
	return now;
}
int isEmpty(Stack* stack)
{
	if (stack->count == 0)
		return 1;
	else
		return 0;
}
void push(Stack* stack, int data)
{
	Node* now = NewNode(data);
	now->next = stack->top;
	stack->top = now;
	stack->count++;
}
int pop(Stack* stack)
{
	if (isEmpty(stack) == 1)
	{
		return 0;
	}
	Node* now = stack->top;
	stack->top = stack->top->next;
	int temp = now->data;
	free(now);
	stack->count--;
	return temp;
}

int main()
{
	Stack stack;
	InitStack(&stack);
	int N, i, result;
	char oper[10];
	int data = 0;
	scanf("%d", &N);
	for (i = 0; i < N; i++)
	{
		scanf("%s", oper);
		getchar();
		if (strcmp(oper, "push") == 0)
		{
			scanf("%d", &data);
			getchar();
			push(&stack, data);
		}
		if (strcmp(oper, "pop") == 0)
		{
			if (isEmpty(&stack) == 1)
				printf("%d\n", -1);
			else
				printf("%d\n", pop(&stack));
		}
		if (strcmp(oper, "size") == 0)
		{
			printf("%d\n", stack.count);
		}
		if (strcmp(oper, "empty") == 0)
		{
			printf("%d\n", isEmpty(&stack));
		}
		if (strcmp(oper, "top") == 0)
		{
			if (isEmpty(&stack) == 1)
				printf("%d\n", -1);
			else
				printf("%d\n", stack.top->data);
		}
	}
}