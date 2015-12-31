#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char *
tokenize (char * s, char ** res) {
    int len_res = strlen(s)+strlen(s)-1 + 1;
    *res = malloc(len_res*sizeof(char));
    memset(*res, 0, len_res*sizeof(char));

    *res[0] = s[0];

    char * p = s + 1;
    char * q = *res + 1;

    for (; p < s+strlen(s); ++p) {
        if (*(p-1) > *p) {
            *q = '-';
            *(q+1) = *p;
            q += 2;
        }
        else {
            *q = *p;
            q += 1;
        }
    }
    *q = 0;
    return *res;
}

int
main () {
    void * hk = 0;
    char * res = 0;
    hk = tokenize("amore", &res);
    printf("%s\n", res);
    free(hk);
    hk = tokenize("scafroglia", &res);
    printf("%s\n", res);
    free(hk);
    return 0;
}
