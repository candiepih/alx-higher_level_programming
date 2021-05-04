#include "lists.h"

/**
 * list_length - gets the total number of nodes in a linked list
 * @h: beginning of listint_t linked list
 * Return: total nodes in linked list
 */

int list_length(listint_t **h)
{
	listint_t *tmp = *h;
	int i = 0;

	while (tmp)
	{
		i++;
		tmp = tmp->next;
	}

	return (i);
}

/**
 * get_nodeint_at_index - finds the nth node of a listint_t linked list.
 * @head: head of a listint_t linked list.
 * @index: index of the node finding starting from 0
 * Return: found node
 */

listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	listint_t *tmp = head;
	listint_t *node_found = NULL;
	int i = 0;

	while (tmp)
	{
		if (i == ((int)index))
		{
			node_found = tmp;
			break;
		}
		tmp = tmp->next;
		i++;
	}

	if (!node_found)
		return (NULL);

	return (node_found);
}

/**
 * is_palindrome - determines if a linked list is a palindrome
 * @head: beginning of the listint_t linked list
 * Description: determines if the linked list reads same way forward and
 * backward
 *
 * Return: (1) if it's a palindrom (0) if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *p1, *p2, *tmp;
	int length;
	int track_index = 0;

	if (!*head || !head)
		return (0);

	length = list_length(head);
	if (length == 1)
		return (1);

	tmp = *head;
	while (tmp)
	{
		p1 = tmp;
		p2 = get_nodeint_at_index(*head, ((length - 1) - track_index));
		if (p1->n != p2->n)
			return (0);
		track_index++;
		tmp = tmp->next;
	}
	return (1);
}
