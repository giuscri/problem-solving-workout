#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

struct node { int data; struct node * next; };
struct list { int len; struct node * head; };

struct list *
insert (struct list * l, int data) {
    assert(l != 0);
    struct node * n = malloc(1 * sizeof(struct node));
    memset(n, 0, 1 * sizeof(struct node));
    n->data = data;
    n->next = l->head;
    l->head = n;
    l->len += 1;
    return l;
}

void
print_list (const struct list * l) {
    assert(l != 0);
    struct node * p = l->head;
    for (; p != 0; p = p->next) {
        printf("%d ", p->data);
    }
    puts("");
}

int
is_member (const struct list * l, int x) {
    assert(l != 0);
    struct node * p = l->head;

    for (; p != 0; p = p->next) {
        if (p->data == x) {
            return 1;
        }
    }
    return 0;
}

void
destroy_list (struct list * l) {
    assert(l != 0);
    if (l->len == 0) {
        return;
    }
    struct node * p = 0;
    struct node * q = 0;

    p = l->head;
    q = p->next;

    for (; q != 0;) {
        free(p);
        p = q;
        q = p->next;
    }

    free(p);
    free(l);
}

struct list *
delete_member (struct list * l, int x) {
    assert(l != 0);
    if (l->len == 0) {
        return l;
    }
    if (!is_member(l, x)) {
        return l;
    }
    if (l->head->data == x) {
        struct node * hk = l->head;
        l->head = l->head->next;
        l->len -= 1;
        free(hk);
        return l;
    }
    struct node * prev = l->head;
    struct node * cur = l->head->next;
    for (; cur->next != 0;) {
        if (cur->data == x) {
            prev->next = cur->next;
            l->len -= 1;
            free(cur);
            return l;
        }
        prev = cur;
        cur = cur->next;
    }
    prev->next = 0;
    free(cur);
    l->len -= 1;
    return l;
}

void
print_reversed (const struct list * l) {
    assert(l != 0);
    void _f (struct node * p) {
        if (p->next == 0) {
            printf("%d ", p->data);
            return;
        }
        _f(p->next);
        printf("%d ", p->data);
    }
    _f(l->head);
    puts("");
}

int
count_members (const struct list * l) {
    assert(l != 0);
    return l->len;
}

int
main () {
    int op = 0;
    struct list * l = 0;
    while (scanf(" %c", &op) > 0) {
        if (op == 'c') {
            printf("%d members\n", count_members(l));
        }
        else if (op == 'p') {
            print_list(l);
        }
        else if (op == 'o') {
            print_reversed(l);
        }
        else if (op == 'd') {
            destroy_list(l);
            l = 0;
        }
        else if (op == 'f') {
            break;
        }
        else if (op == '+') {
            int x = 0;
            scanf(" %d", &x);
            if (!l) {
                l = malloc(sizeof(struct list));
                memset(l, 0, sizeof(struct list));
            }
            if (is_member(l, x)) {
                continue;
            }
            insert(l, x);
        }
        else if (op == '-') {
            int x = 0;
            scanf(" %d", &x);
            if (!l) {
                l = malloc(sizeof(struct list));
                memset(l, 0, sizeof(struct list));
            }
            if (is_member(l, x)) {
                continue;
            }
            delete_member(l, x);
        }
        else if (op == '?') {
            int x = 0;
            scanf(" %d", &x);
            if (!l) {
                l = malloc(sizeof(struct list));
                memset(l, 0, sizeof(struct list));
            }
            if (is_member(l, x)) {
                puts("Yes");
            }
            else {
                puts("No");
            }
        }
    }
    if (l) { destroy_list(l); }
    return 0;
}
