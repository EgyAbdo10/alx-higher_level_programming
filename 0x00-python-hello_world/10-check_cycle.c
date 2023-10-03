#include "lists.h"

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
