#include "lists.h"

/**
 * check_cycle - finds a cycle in a linked list
 * @list: linked list of listint_t
 * Description: finds cycle in a linked list using floyd's cycle
 * finding algorithm
 *
 * Return: (0) if no cycle found (1) if cycle found
 */

int check_cycle(listint_t *list)
{
	listint_t *hare;
	listint_t *tortoise;

	if (!list)
		return (0);

	tortoise = list;
	hare = list;

	while (tortoise)
	{
		tortoise = tortoise->next;
		if (hare && hare->next)
		{
			hare = hare->next->next;
			if (hare == tortoise)
				return (1);
		}
	}

	return (0);
}
