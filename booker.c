#include <stdlib.h>
#include <stdio.h>
#include <string.h>

struct b_t { char ** b; int nclients; };

struct b_t *
new_book (int nclients) {
    struct b_t * b = malloc(1 * sizeof(struct b_t));
    b->nclients = nclients;
    b->b = malloc(b->nclients * sizeof(char *));
    memset(b->b, 0, b->nclients * sizeof(char *));
    return b;
}

int
book (struct b_t * b, int k, const char * name) {
    if (b->b[k]) {
        return -1;
    }
    b->b[k] = strndup(name, 256);
    return 0;
}

int
cancel (struct b_t * b, int k) {
    if (!b->b[k]) {
        return -1;
    }
    free(b->b[k]);
    b->b[k] = 0;
    return 0;
} 

int
move (struct b_t * b, int f, int t) {
    if (!b->b[f]) {
        return -1;
    }
    if (b->b[t]) {
        return -1;
    }
    book(b, t, b->b[f]);
    cancel(b, f);
    return 0;
}

void
print_book (const struct b_t * b) {
    char * p = *(b->b);

    int i = 0;
    for (i = 0; i < b->nclients; ++i) {
        if (b->b[i]) {
            printf("#%d %s\n", i, b->b[i]);
        }
    }
}

int
main () {
    int command = 0;
    struct b_t * b = 0;
    while (scanf(" %c", &command) > 0) {
        if (command == 'b') {
            printf("Creating new book ...");
            fflush(stdout);
            int nclients = 0;
            scanf("%d", &nclients);
            b = new_book(nclients);
            puts("");
        }
        else if (command == '+') {
            int k = 0;
            char * name = malloc(256*sizeof(char));
            scanf("%d", &k);
            scanf(" %s", name);
            book(b, k, name);
        }
        else if (command == 'p') {
            print_book(b);
        }
        else if (command == 'f') {
            break;
        }
    }
}
