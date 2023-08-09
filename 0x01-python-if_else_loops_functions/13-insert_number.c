#include "lists.h"
/**
 * insert_node - inserts node in sorted list
 * @head: pointer to first node
 * @number: element to insert
 * Return: pointer to element inserted
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t)), *node = *head;

	if (!new)
		return (NULL);
	new->n = number;

	if (!node || node->next->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}
	while (node && node->next && node->next->n < number)
		node = node->next;
	new->next = node->next;
	node->next = new;
	return (new);
}
