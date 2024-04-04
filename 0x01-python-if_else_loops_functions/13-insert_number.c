#include "lists.h"
#include <stdio.h>
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = NULL;
	listint_t *temp = NULL;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	temp = *head; 
	while (number < temp->next->n)
	{
		temp = temp->next;
	}

	node->next = temp->next;
	temp->next = node;
}
