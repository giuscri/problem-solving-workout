# include <stdint.h>
# include <stdlib.h>
# include <stdio.h>

# include "queue_queues_int32.h"
struct queue_queues_int32 *
new_queue_queues_int32 () {
    return calloc(1, sizeof(struct queue_queues_int32));
}

struct queue_queues_int32 *
append_queue_queues_int32 (struct queue_queues_int32 * qq, struct queue_int32 * q) {
    struct node_queue_int32 * nd = calloc(1, sizeof(struct node_queue_int32));
    nd->q = q;
    if (qq->len == 0) {
        qq->head = qq->tail = nd;
    }
    else {
        qq->tail->next = nd;
        qq->tail = nd;
    }
    qq->len += 1;
    return qq;
}

void
del_queue_queues_int32 (struct queue_queues_int32 * qq) {
    if (qq->len == 0) { return; }
    struct node_queue_int32 * p = NULL;
    struct node_queue_int32 * q = NULL;
    for (p = qq->head->next, q = qq->head; p != NULL; /* See below */) {
        del_queue_int32(q->q);
        free(q);
        q = p;
        p = p->next;
    }
    del_queue_int32(q->q);
    free(q);
    qq->len = 0;
    free(qq);
}

void
print_queue_queues_int32 (struct queue_queues_int32 * qq) {
    struct node_queue_int32 * p = qq->head;
    puts("[");
    for (; p != NULL; p = p->next) {
        printf("\t");
        print_queue_int32(p->q);
    }
    puts("]");
}
