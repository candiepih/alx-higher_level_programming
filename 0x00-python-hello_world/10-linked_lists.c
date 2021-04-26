#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */

size_t print_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int n; /* number of nodes */

	current = h;
	n = 0;
	while (current != NULL)
	{
		printf("%i\n", current->n);
		current = current->next;
		n++;
	}

	return (n);
}

/**
 * add_nodeint - adds a new node at the beginning of a listint_t list
 * @head: pointer to a pointer of the start of the list
 * @n: integer to be included in node
 * Return: address of the new element or NULL if it fails
 */

listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = *head;
	*head = new;

	return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */

void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}

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
