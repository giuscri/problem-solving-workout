int
_main () {
    int n = 0;
    scanf("%d", &n);

    int * v = malloc(n * sizeof(int));

    int i = 0;
    for (i = 0; i < n; ++i) {
        int x = 0;
        scanf("%d", &x);
        v[i] = x;
    }

    for (i = n - 1; i >= 0; --i) {
        printf("%d ", v[i]);
    }
    puts("");
}

int main () {
    int * v = malloc(2 * sizeof(int));
    int len_v = 2;

    int x = 0;
    int i = 0;
    while (scanf("%d", &x) > 0) {
        if (x == 0) {
            break;
        }
        if (i == len_v) {
            /*
            v = realloc(v, len_v * 2 * sizeof(int));
            len_v *= 2;
            */
            v = realloc(v, (len_v +10) * sizeof(int));
            len_v += 10;
        }
        v[i] = x;
        i += 1;
    }

    for (i = i - 1; i >= 0; --i) {
        printf("%d ", v[i]);
    }
    puts("");
}
