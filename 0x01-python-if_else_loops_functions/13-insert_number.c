#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = NULL;
	listint_t *temp = NULL;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	temp = *head;
	if (number < temp->n)
	{
		node->n = number;
		node->next = temp;
		temp->next = node;
	}
	while (number < temp->next->n)
	{
		temp = temp->next;
	}
	node->n = number;
	node->next = temp->next;
	temp->next = node;
	return (node);
}
