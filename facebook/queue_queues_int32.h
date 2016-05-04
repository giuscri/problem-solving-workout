# ifndef _QUEUE_QUEUES_INT32_H
# define _QUEUE_QUEUES_INT32_H

# include "queue_int32.h"

struct node_queue_int32 {
    struct queue_int32 * q;
    struct node_queue_int32 * next;
};

struct queue_queues_int32 {
    struct node_queue_int32 * head;
    struct node_queue_int32 * tail;
    size_t len;
};

struct queue_queues_int32 * new_queue_queues_int32 ();
struct queue_queues_int32 * append_queue_queues_int32 ( \
    struct queue_queues_int32 * qq, struct queue_int32 * q \
);
void del_queue_queues_int32 (struct queue_queues_int32 * qq);
void print_queue_queues_int32 (struct queue_queues_int32 * qq);
# endif
