#include "lists.h"
/**
 * check_cycle - checks if there's a cycle in the list
 * @list: list to check
 * Return: 1 if loops 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *x, *y;

	x = list;
	y = x;
	while (x && y && y->next)
	{
		x = x->next;
		y = y->next->next;
		if (x == y)
			return (1);
	}
	return (0);
}
