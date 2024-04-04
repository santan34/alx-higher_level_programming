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
	node->n = number;
	node->next = NULL;
	if (temp == NULL)
	{
		temp = node;
		return (node);
	}
	if (number < temp->n)
	{
		node->next = temp;
		*head = node;
	}
	while (number > temp->next->n)
	{
		temp = temp->next;
	}
	node->next = temp->next;
	temp->next = node;
	return (node);
}
