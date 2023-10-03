#include "lists.h"
/**
 * check_cycle - check if there is a cycle in a linked list
 * @list: the head pointer ot the linked list
 * Return: (1) if there is a cycle
 * (0) if there is not
*/
int check_cycle(listint_t *list)
{
listint_t *temp;
while (list != NULL)
{
temp = list->next;
while (temp != NULL)
{
if (temp == list)
return (1);
temp = temp->next;
}
list = list->next;
}
return (0);
}
