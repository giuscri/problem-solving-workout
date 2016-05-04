# include <stdint.h>
# include <stdlib.h>
# include <stdbool.h>
# include <assert.h>
# include <stdio.h>

# include "queue_int32.h"

struct queue_int32 *
new_queue_int32 () {
    return calloc(1, sizeof(struct queue_int32));
}

struct queue_int32 *
append_queue_int32 (struct queue_int32 * q, int32_t data) {
    struct node_int32 * nd = calloc(1, sizeof(struct node_int32));
    nd->data = data;
    if (q->len == 0) {
        q->head = q->tail = nd;
    }
    else {
        q->tail->next = nd;
        q->tail = nd;
    }
    q->len += 1;
    return q;
}

int32_t
pop0_queue_int32 (struct queue_int32 * q) {
    assert(q->len > 0);
    int32_t ret = q->head->data;
    struct node_int32 * next = q->head->next;
    free(q->head);
    q->head = next;
    q->len -= 1;
    return ret;
}

bool
in_queue_int32 (struct queue_int32 * q, int32_t data) {
    struct node_int32 * nd = q->head;
    for (; nd != NULL; nd = nd->next) {
        if (nd->data == data) {
            return true;
        }
    }
    return false;
}

void
print_queue_int32 (struct queue_int32 * q) {
    struct node_int32 * p = q->head;
    printf("[ ");
    for (; p != NULL; p = p->next) {
        printf("%d ", p->data);
    }
    puts("]");
}

void
del_queue_int32 (struct queue_int32 * q) {
    if (q->len > 0) {
        do {
            pop0_queue_int32(q);
        } while (q->len > 0);
    }
    free(q);
}
