# include <stdint.h>
# include <stdio.h>
# include <math.h>

int32_t
main() {
    int32_t res = 0;

    int32_t a = 1;
    int32_t b = 1;

    int32_t c = 2;
    do {
        res += c;
        a = c + b;
        b = a + c;
        c = a + b;
    } while (c < 4 * pow(10, 6));

    printf("*** Computed %d\n", res);

    return 0;
}
