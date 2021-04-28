#include "lists.h"
/**
 * check_cycle - Function that check if is a loop inside linked list
 * @list: pointer to head of list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *detectc = list;

	if (!list || !list->next)
		return (0);
	while (detectc && list && detectc->next)
	{
		detectc = detectc->next->next;
		list = list->next;
		if (detectc == list)
			return (1);
	}
	return (0);
}
