#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * main - check the code
 *
 * Return: Always 0.
 */
int main(void)
{
listint_t *head;
listint_t *current;
listint_t *temp;
int i;

head = NULL;
add_nodeint(&head, 0);
add_nodeint(&head, 1);
add_nodeint(&head, 2);
add_nodeint(&head, 3);
add_nodeint(&head, 4);
add_nodeint(&head, 98);
add_nodeint(&head, 402);
add_nodeint(&head, 1024);
print_listint(head);

if (check_cycle(head) == 0)
printf("Linked list has no cycle\n");
else if (check_cycle(head) == 1)

