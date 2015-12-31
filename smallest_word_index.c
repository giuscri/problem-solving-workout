#include <stdio.h>
#include <string.h>

int
cmp_lexicographical(char * s, char * t) {
    // 0 if s==t, 1 if s>t, -1 if s<t
    int len = 0;
    len = strlen(s) < strlen(t) ? strlen(s) : strlen(t);

    int i = 0;
    for (i = 0; i < len; ++i) {
        if (s[i] < t[i]) {
            return -1;
        }
        else if (s[i] > t[i]) {
            return 1;
        }
    }

    if (strlen(s) == strlen(t)) {
        return 0;
    }
    else if (strlen(s) < strlen(t)) {
        return -1;
    }
    else {
        return 1;
    }
}

void
smallest_largest (char * d[], int len_d, char ** smallest, char ** largest) {
    *smallest = 0;
    *largest = 0;

    int i = 0;
    for (i = 0; i < len_d; ++i) {
        if (!*smallest && !*largest) {
            *smallest = *largest = d[0];
            continue;
        }
        if (strcmp(*smallest, d[i]) > 0) {
            *smallest = d[i];
        }
        if (strcmp(d[i], *largest) > 0) {
            *largest = d[i];
        }
    }
}

int
smallest_word_index (char * d[], int n) {
    int min_index = -1;

    int i = 0;
    for (i = 0; i < n; ++i) {
        if (min_index < 0) {
            min_index = i;
        }
        else if (cmp_lexicographical(d[min_index], d[i]) > 0) {
            min_index = i;
        }
    }
    return min_index;
}

int
main () {
    char * dict[] = {
        "ciao",
        "mondo",
        "come",
        "funziona",
        "bene",
        "questo",
        "programma",
        "zak!"
    };
    int len = sizeof(dict)/sizeof(char *);
    int res = smallest_word_index(dict, len);
    printf("Lowest string found is \"%s\"\n", dict[res]);

    char * smallest = 0;
    char * largest = 0;
    smallest_largest(dict, len, &smallest, &largest);

    printf("smallest,largest: %s,%s\n", smallest, largest);
}
