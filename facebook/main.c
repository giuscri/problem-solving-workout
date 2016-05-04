# include <stdint.h>
# include <stdlib.h>
# include <stdbool.h>
# include <stdio.h>
# include <string.h>
# include <assert.h>

# include "queue_int32.h"
# include "queue_queues_int32.h"

# include "linkedlist_friendship.h"
# include "graph.h"

/*
    Data structures involved:
        + struct node_int32,
    
              struct node_int32 {
                  int32_t data;
                  struct node_int32 * next;
              };

        + struct queue_int32,

              struct queue_int32 {
                  struct node_int32 * head;
                  struct node_int32 * tail;
                  size_t len;
              };

        + struct node_friendship,

              struct node_friendship {
                  int32_t year_of_start;
                  int32_t id;
              };

        + struct linkedlist_friendship,

              struct linkedlist_friendship {
                  struct node_friendship * head;
                  size_t len;
              };

        + struct node_queue_int32,

              struct node_int32 {
                  int32_t data;
                  struct node_int32 * next;
              };

        + struct queue_queues_int32,

              struct queue_int32 {
                  struct node_int32 * head;
                  struct node_int32 * tail;
                  size_t len;
              };

        + struct user, an implementation
          of a user,

              struct user {
                  int32_t id;
                  char * first_name;
                  char * last_name;
                  struct linkedlist_friendship * friendships;
              };

        + struct graph, a graph implemented
          via adjacent lists:
          [
            [ user ] => <linkedlist_friendship>,
            [ user ] => <linkedlist_friendship>,
            [ user ] => <linkedlist_friendship>,
            ...
          ],

              struct graph {
                struct user ** users;
                size_t nusers;
              };
         
*/

void run_tests ();

int
main (int argc, char ** argv) {
    run_tests();

    if (argc < 2) {
        puts("Usage: main <max users allowed>");
        return -1;
    }

    size_t at_most = atoi(argv[1]);

    struct graph * G = new_graph(at_most);

    /*
        API:
            + add <first_name> <last_name> <id>
            + find <id>
            + mfriends <id0> <id1> <year_of_start>
            + extract_groups
    */

    char * cmd = calloc(32, sizeof(char));
    int res = 0;
    while ((res=scanf(" %s", cmd)) != 0 && res != EOF) {
        if (strncmp(cmd, "#", 1) == 0) {
            continue;
        }
        else if (strncmp(cmd, "add", 32) == 0) {
            char * first_name = calloc(32, sizeof(char));
            char * last_name = calloc(32, sizeof(char));
            int32_t id = 0;
            scanf(" %s %s %d", first_name, last_name, &id);
            G->users[id] = new_user(id, first_name, last_name);
            free(last_name);
            free(first_name);
        }
        else if (strncmp(cmd, "find", 32) == 0) {
            int32_t id = 0;
            scanf(" %d", &id);
            if (G->users[id] == NULL) {
                printf("#%d does not exist yet.", id);
                continue;
            }
            print_user(G->users[id]);
        }
        else if (strncmp(cmd, "mfriends", 32) == 0) {
            int32_t i = 0;
            int32_t j = 0;
            int32_t year_of_start = 0;
            scanf(" %d %d %d", &i, &j, &year_of_start);
            if (G->users[i] == NULL) {
                printf("#%d does not exist yet.", i);
                continue;
            }
            if (G->users[j] == NULL) {
                printf("#%d does not exist yet.", j);
                continue;
            }
            if (G->users[i]->friendships == NULL) {
                G->users[i]->friendships = new_linkedlist_friendship();
            }
            if (G->users[j]->friendships == NULL) {
                G->users[j]->friendships = new_linkedlist_friendship();
            }
            prepend_linkedlist_friendship(G->users[i]->friendships, \
                                             year_of_start, j);
            prepend_linkedlist_friendship(G->users[j]->friendships, \
                                             year_of_start, i);
        }
        else if (strncmp(cmd, "extract_groups", 32) == 0) {
            struct queue_queues_int32 * qq = \
               connected_components(G);
            size_t group_ix = 0;
            for (struct node_queue_int32 * it = qq->head; it != NULL; it = it->next) {
                printf("Group #%d:\n", group_ix);
                for (struct node_int32 * _it = it->q->head; _it != NULL; _it = _it->next) {
                    printf("\t");
                    print_user(G->users[_it->data]);
                }
                group_ix += 1;
            }
            del_queue_queues_int32(qq);
        }
    }
    free(cmd);
    del_graph(G);
    return 0;
}

void run_tests () {
    // Testing queue_int32
    struct queue_int32 * q = new_queue_int32();
    assert(q->len == 0);
    assert(q->head == 0);
    assert(q->tail == 0);
    for (size_t i = 0; i < 100; ++i) {
        append_queue_int32(q, i);
    }
    for (size_t i = 0; i < 50; ++i) {
        int32_t ppd = pop0_queue_int32(q);
        assert(ppd == i);
    }
    del_queue_int32(q);
    assert(q->len == 0);

    // Testing queue_queues_int32
    struct queue_int32 * qs[100] = { 0 };
    for (size_t i = 0; i < 100; ++i) {
        qs[i] = new_queue_int32();
    }
    for (size_t i = 0; i < 100; ++i) {
        for (size_t j = 0; j < 100; ++j) {
            append_queue_int32(qs[i], j);
        }
        assert(qs[i]->len == 100);
    }
    struct queue_queues_int32 * qq = new_queue_queues_int32();
    for (size_t i = 0; i < 100; ++i) {
        append_queue_queues_int32(qq, qs[i]);
    }
    assert(qq->len == 100);

    for (struct node_queue_int32 * it = qq->head; it != NULL; it = it->next) {
        assert(it->q->len == 100);
    }

    del_queue_queues_int32(qq);

    // Testing user
    struct user ** us = calloc(100, sizeof(struct user *));
    for (size_t i = 0; i < 100; ++i) {
        us[i] = new_user(i, "David", "Bowie");
    }
    for (size_t i = 0; i < 100; ++i) {
        assert(strcmp(us[i]->first_name, "David") == 0);
        assert(strcmp(us[i]->last_name, "Bowie") == 0);
    }
    for (size_t i = 0; i < 100; ++i) {
        del_user(us[i]);
    }
    free(us);

    // Testing linkedlist_friendship
    struct linkedlist_friendship * lfs = new_linkedlist_friendship();
    for (size_t i = 0; i < 100; ++i) {
        prepend_linkedlist_friendship(lfs, 1916 + i, i);
    }
    size_t ix = 0;
    for (struct node_friendship * it = lfs->head; it != NULL; it = it->next) {
        assert(it->year_of_start == 1916 + 99 - ix);
        assert(it->id == 99 - ix);
        ix += 1;
    }
    assert(lfs->len == 100);
    del_linkedlist_friendship(lfs);
    assert(lfs->len == 0);
}
