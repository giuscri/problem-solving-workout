# define _GNU_SOURCE

# include <stdlib.h>
# include <assert.h>
# include <string.h>
# include <stdio.h>

# include "queue_int32.h"
# include "queue_queues_int32.h"
# include "graph.h"

struct user *
new_user (size_t id, char * first_name, char * last_name) {
    struct user * u = calloc(1, sizeof(struct user));
    u->id = id;
    u->first_name = strndup(first_name, 32);
    u->last_name = strndup(last_name, 32);
    u->friendships = new_linkedlist_friendship();
    return u;
}

void
print_user (struct user * u) {
    printf("%s, %s (%d)\n", u->last_name, u->first_name, u->id);
}

void
del_user (struct user * u) {
    free(u->first_name);
    free(u->last_name);
    del_linkedlist_friendship(u->friendships);
    //free(u->friendships);
    free(u);
}

struct graph *
new_graph (size_t nusers) {
    struct graph * g = calloc(1, sizeof(struct graph));
    g->nusers = nusers;
    g->users = calloc(nusers, sizeof(struct user *));
    return g;
}

void
del_graph (struct graph * G) {
    for (size_t i = 0; i < G->nusers; ++i) {
        if (G->users[i] == NULL) { continue; }
        del_user(G->users[i]);
    }
    free(G->users);
    free(G);
}

struct queue_int32 *
bfs (struct graph * G, int32_t id) {
    assert(G->users[id] != NULL);
    struct queue_int32 * q = new_queue_int32();
    append_queue_int32(q, id);
    struct queue_int32 * visited = new_queue_int32();
    append_queue_int32(visited, id);

    while (q->len > 0) {
        int32_t ppd = pop0_queue_int32(q);
        struct node_friendship * ad = G->users[ppd]->friendships->head;
        for (; ad != NULL; ad = ad->next) {
            if (in_queue_int32(visited, ad->id)) {
                continue;
            }
            append_queue_int32(visited, ad->id);
            append_queue_int32(q, ad->id);
        }
    }

    del_queue_int32(q);
    return visited;
}

struct queue_queues_int32 *
connected_components (struct graph * G) {
    struct queue_queues_int32 * ret = new_queue_queues_int32();
    struct queue_int32 * visited = new_queue_int32();

    for (size_t i = 0; i < G->nusers; ++i) {
        if (G->users[i] == NULL) {
            continue;
        }

        if (in_queue_int32(visited, i)) {
            continue;
        }

        struct queue_int32 * cmpnt = bfs(G, i);

        struct node_int32 * nd = cmpnt->head;
        for (; nd != NULL; nd = nd->next) {
            append_queue_int32(visited, nd->data);
        }

        append_queue_queues_int32(ret, cmpnt);
    }

    del_queue_int32(visited);
    return ret;
}
