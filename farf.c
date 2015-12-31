#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int
is_vowel (char c) {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

int
count_vowels (const char * s) {
    int cnt = 0;
    int i = 0;
    for (i = 0; i < strlen(s); ++i) {
        if (is_vowel(s[i])) {
            cnt += 1;
        }
    }
    return cnt;
}

char *
translate_vowel (char vowel, char * res) {
    res[0] = res[2] = vowel;
    res[1] = 'f';
    return res;
}

char *
farfalize (const char * s, char ** res) {
    int n_vs = count_vowels(s);
    int n_cs = strlen(s) - n_vs;
    *res = malloc(sizeof(char) * (n_cs + n_vs*3) + 1);

    char * p = 0;
    char * q = 0;
    for (p=s, q=*res; p < s+strlen(s);) {
        if (!is_vowel(*p)) {
            *q = *p;
            q += 1;
            p += 1;
        }
        else {
            translate_vowel(*p, q);
            p += 1;
            q += 3;
        }
    }

    // q has now the address of the last byte of res
    *q = 0;
    return *res;
}

int
main (int argc, char ** argv) {
    // Useful for hooking allocated mem
    void * hk = 0;

    char ** p = argv + 1;
    for (; p < argv+argc; ++p) {
        char * res = 0;
        hk = farfalize(*p, &res);
        printf("%s ", res);
        free(hk);
    }
    puts("");

    return 0;
}
