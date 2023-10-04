#include "lists.h"
/**
 * add_node_beg - add a node to the beginning of a list
 * @head: a pointer to the head pointer
 * @number: teh number to be in the node
 * Return: a pointer to thh newly created node
 */
listint_t *add_node_beg(listint_t **head, int number)
{
listint_t *ptr;
ptr = malloc(sizeof(listint_t));
if (ptr == NULL)
return (NULL);
ptr->n = number;
ptr->next = *head;
*head = ptr;
return (ptr);
}
/**
 * insert_node - insert a node in its right order
 * @head: a ponter to the head pointer
 * @number: the number to be put in the node
 * Return: a pointer to the new node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *ptr, *new = *head;
if (new == NULL)
{
ptr = malloc(sizeof(listint_t));
if (ptr == NULL)
return (NULL);
ptr->n = number;
ptr->next = new;
return (ptr);
}
if (new->n > number)
retrun (add_node_beg(head, number));
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
