# include <stdint.h>
# include <stdlib.h>

# include "linkedlist_friendship.h"
struct node_friendship *
new_node_friendship (size_t id, int32_t year_of_start) {
    struct node_friendship * nd = calloc(1, sizeof(struct node_friendship));
    nd->year_of_start = year_of_start;
    nd->id = id;
    return nd;
}

struct linkedlist_friendship *
new_linkedlist_friendship () {
    return calloc(1, sizeof(struct linkedlist_friendship));
}

struct linkedlist_friendship *
prepend_linkedlist_friendship (struct linkedlist_friendship * lst, \
                                    int32_t year_of_start, size_t id)
{
    struct node_friendship * nd = calloc(1, sizeof(struct node_friendship));
    nd->year_of_start = year_of_start;
    nd->id = id;
    nd->next = lst->head;
    lst->head = nd;
    lst->len += 1;
    return lst;
}

void
del_linkedlist_friendship (struct linkedlist_friendship * lst) {
    if (lst->len == 0) { return; }
    struct node_friendship * p = NULL;
    struct node_friendship * q = NULL;
    for (p = lst->head->next, q = lst->head; p != NULL; /* See below */) {
        free(q);
        q = p;
        p = p->next;
    }
    free(q);
    lst->len = 0;
    free(lst);
}
