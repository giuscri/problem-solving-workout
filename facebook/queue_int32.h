# ifndef _QUEUE_INT32_H
# define _QUEUE_INT32_H
# include <stdint.h>
# include <stdbool.h>

struct node_int32 {
    int32_t data;
    struct node_int32 * next;
};

struct queue_int32 {
    struct node_int32 * head;
    struct node_int32 * tail;
    size_t len;
};

struct queue_int32 * new_queue_int32 ();
struct queue_int32 * append_queue_int32 (struct queue_int32 * q, int32_t data);
int32_t pop0_queue_int32 (struct queue_int32 * q);
bool in_queue_int32 (struct queue_int32 * q, int32_t data);
void print_queue_int32 (struct queue_int32 * q);
void del_queue_int32 (struct queue_int32 * q);
# endif
