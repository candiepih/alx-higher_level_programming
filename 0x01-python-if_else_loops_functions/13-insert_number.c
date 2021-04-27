#include "lists.h"

/**
 * insert_node - inserts new node at a particullar position of
 * the sorted linked list
 * @head: start of linstint_t linked list
 * @number: member integer value of our listint_t linked list
 * Return: address of new node or (NULL)on failure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *our_head;
	listint_t *tmp;
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	our_head = *head;

	if (*head == NULL || (our_head->n > number))
	{
		new_node->next = *head;
		*head = new_node;
		return (*head);
	}

	while (our_head != NULL)
	{
		if (our_head->next == NULL)
		{
			free(new_node);
			return (add_nodeint_end(head, number));
		}
		else if (our_head->next->n >= number)
		{
			tmp = our_head->next;
			new_node->next = tmp;
			our_head->next = new_node;
			return (new_node);
		}
		our_head = our_head->next;
	}

	free(new_node);
	return (NULL);
}
