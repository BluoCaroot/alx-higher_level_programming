#include "lists.h"
#include<stdio.h>
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: head of linked list
 * Return: 0 if not palindrome 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *scnd, *tmp;
	int i, cnt = 0, f = 1;

	temp = *head;
	scnd = NULL;
	while (temp)
	{
		cnt++;
		temp = temp->next;
	}
	temp = *head;
	for (i = 0; i < cnt / 2; ++i)
	{
		add_nodeint(&scnd, temp->n);
		temp = temp->next;
	}
	if (cnt % 2)
		temp = temp->next;


	tmp = scnd;
	for (i = 0; f && temp && tmp; ++i)
	{
		if (tmp->n != temp->n)
			f = 0;
		tmp = tmp->next;
		temp = temp->next;
	}

	free_listint(scnd);
	return (f);
}

/**
 * add_nodeint - adds a new node at the beginning of list
 * @head: pointer to head of list
 * @n: integer to add to list
 * Return: NULL if fail - address of new element
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);

	new->next = *head;
	new->n = n;
	*head = new;

	return (new);
}
