#include "lists.h"

/**
 * is_palindrome_util - uses recursion to and use function call stack to
 * determine value at head and value at last node
 * @left: pointer to the begining of the linked list
 * @right: the last most node in the linked list
 * Return: (1) on success (0) on failure
 */

int is_palindrome_util(listint_t **left, listint_t *right)
{
	int isp, isp1;

	if (!right)
		return (1);

	isp = is_palindrome_util(left, right->next);

	if (isp == 0)
        	return (0);

	isp1 = (right->n == (*left)->n);
	*left = (*left)->next;

	return (isp1);
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
	return (is_palindrome_util(head, *head));
}
