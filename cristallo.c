// THIS ONE IS IN ITALIAN, SORRY ABOUT THAT.

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int
latoCristallo (int t) {
    if (t == 0) { return 1; }
    return 1 + 2 * latoCristallo(t - 1);
}

char **
creaMatrice (int n) {
    char ** ret = malloc(n * sizeof(char *));
    int i = 0;
    for (i = 0; i < n; ++i) {
        ret[i] = malloc(n * sizeof(char));
        memset(ret[i], '.', n * sizeof(char));
    }
    return ret;
}

void
stampaMatrice (char ** m, int n) {
    int i = 0;
    int j = 0;
    for (i = 0; i < n; ++i) {
        for (j = 0; j < n; ++j) {
            printf("%c ", m[i][j]);
        }
        puts("");
    }
}

void
crist (char ** m, int r0, int c0, int l) {
    if (l==1) { m[r0 + l/2][c0 + l/2] = '*'; return; }
    crist(m, r0, c0, l/2);
    crist(m, r0, c0+l/2 + 1, l/2);
    crist(m, r0+l/2 + 1, c0, l/2);
    crist(m, r0+l/2 + 1, c0+l/2 + 1, l/2);
    m[r0 + l/2][c0 + l/2] = '*';
}

void
cristallo (char ** m, int l) {
    crist(m, 0, 0, l);
}

int
main () {
    char ** matrix ;
    int t , lato ;
    printf("Type an instant `t' (e.g. 2): ");
    scanf ( "%d" , &t );
    if( t >= 0 ){
        lato = latoCristallo ( t );
        matrix = creaMatrice ( lato );
        cristallo ( matrix , lato );
        stampaMatrice ( matrix , lato );
    }
}
