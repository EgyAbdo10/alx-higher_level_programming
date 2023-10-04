#include "lists.h"
/**
 * insert_node - insert a node in its right order
 * @head: a ponter to the head pointer
 * @number: the number to be put in the node
 * Return: a pointer to the new node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *ptr, *new = *head;
if (new->n > number || new == NULL)
{
ptr = malloc(sizeof(listint_t));
if (ptr == NULL)
return (NULL);
ptr->n = number;
ptr->next = new;
new = ptr;
return (new);
}
while (new->next != NULL)
{
if (new->next->n < number)
new = new->next;
else
break;
}
ptr = malloc(sizeof(listint_t));
if (ptr == NULL)
return (NULL);
ptr->next = new->next;
ptr->n = number;
new->next = ptr;
return (ptr);
}
