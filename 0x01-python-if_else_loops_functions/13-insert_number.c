#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @h: ptr the head of the linked list
 * @nbr: number to insert
 *
 * Return: If the function fails  NULL.
 *         Otherwise ptr to the new node.
 */
listint_t *insert_node(listint_t **h, int nbr) {
  listint_t *node = *h, *new;

  new = malloc(sizeof(listint_t));
  if (new == NULL)
    return (NULL);
  new->n = nbr;

  if (node == NULL || node->n >= nbr) {
    new->next = node;
    *h = new;
    return (new);
  }
  while (node && node->next && node->next->n < nbr)
    node = node->next;
  new->next = node->next;
  node->next = new;
  return (new);
}
