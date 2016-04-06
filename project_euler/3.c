// cc -lm -m32 -g -O0 3.c -o 3

# include <stdint.h>
# include <math.h>
# include <stdio.h>
# include <stdint.h>

int
main() {
    uint64_t n = 362081674054L; // 2 * 1009 * 179426003
    uint64_t r = 2L;
    while (n % 2 == 0) { n = n / 2; }

    uint64_t p = 3;
    while (n > 1) {
        if (n % p == 0) {
            r = p;
            if (p > sqrt(n)) { break; }
        }

        while (n % p == 0) {
            n = n / p;
        }

        r = p;
        p += 2;
    }

    printf("*** Computed %u\n", r);
}
