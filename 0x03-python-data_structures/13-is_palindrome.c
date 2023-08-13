#include "lists.h"
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: head of linked list
 * Return: 0 if not palindrome 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *scnd;

	temp = *head;
	scnd = NULL;
	while (temp)
	{
		add_nodeint(&scnd, temp->n);
		temp = temp->next;
	}
	
	if (equal(&scnd, head))
		return (1);
	return (0);
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

/**
 * equal - checks if two linked lists are equal
 * @first: first list
 * @second: second list
 * Return: 1 if equal 0 if not
 */
int equal(listint_t **first, listint_t **second)
{
	listint_t *t1, *t2;
	int same = 1;

	t1 = *first, t2 = *second;

	while(same && t1 && t2)
	{
		if (t1->n != t2->n)
			same = 0;

		t1 = t1->next;
		t2 = t2->next;
	}
	free_listint(first);
	return (same);
}
