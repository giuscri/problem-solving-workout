# ifndef _GRAPH_H
# define _GRAPH_H
# include <stdint.h>
# include <stdlib.h>

# include "linkedlist_friendship.h"
struct user {
    int32_t id;
    char * first_name;
    char * last_name;
    struct linkedlist_friendship * friendships;
};

struct user * new_user (size_t id, char * first_name, char * last_name);
void print_user (struct user * u);
void del_user (struct user * u);

struct graph {
    struct user ** users;
    size_t nusers;
};

struct graph * new_graph (size_t nusers);
void del_graph (struct graph * G);
struct queue_int32 * bfs (struct graph * G, int32_t id);
struct queue_queues_int32 * connected_components (struct graph * G);
# endif
