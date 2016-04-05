// cc -m32 -g -O0 1.c -o 1

# include <stdint.h>
# include <stdio.h>

uint32_t
fn(uint32_t n, uint32_t k) {
    uint32_t m = n / k;
    return m * (m + 1) / 2;
}

uint32_t
main() {
    uint32_t n = 1000000000;
    printf("*** Computed %u\n", fn(n, 3) + fn(n, 5) - fn(n, 15));
    return 0;
}
