#include "lists.h"
#include<stdio.h>
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: head of linked list
 * Return: 0 if not palindrome 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *tmp;
	int i, cnt = 0, f = 1;

	temp = *head;
	while (temp)
	{
		cnt++;
		temp = temp->next;
	}
	temp = *head;
	for (i = 0; i < cnt / 2; ++i)
	{
		temp = temp->next;
	}
	if (cnt % 2)
		temp = temp->next;
	revlist(&temp);

	tmp = *head;
	for (i = 0; f && temp; ++i)
	{
		if (tmp->n != temp->n)
			f = 0;
		tmp = tmp->next;
		temp = temp->next;
	}

	return (f);
}
/**
 * reverse_listint - Reverses a list
 * @head: start of section to reverse
 * Return: A pointer to the head of the reversed list.
 */
listint_t *revlist(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}

