# ifndef _LINKEDLIST_FRIENDSHIP_H
# define _LINKEDLIST_FRIENDSHIP_H
# include <stdint.h>
# include <stdlib.h>
struct node_friendship {
    int32_t year_of_start;
    int32_t id;
    struct node_friendship * next;
};

struct node_friendship * new_node_friendship (size_t id, int32_t year_of_start);

struct linkedlist_friendship {
    struct node_friendship * head;
    size_t len;
};

struct linkedlist_friendship * new_linkedlist_friendship ();
struct linkedlist_friendship * prepend_linkedlist_friendship ( \
    struct linkedlist_friendship * lst, int32_t year_of_start, size_t id
);
void del_linkedlist_friendship (struct linkedlist_friendship * lst);
# endif
