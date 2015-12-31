int
is_palindrome (const char * s) {
    char * p = s;
    char * q = p+strlen(p) - 1;

    for (; p < q; ++p, --q) {
        if (*p != *q) {
            return -1;
        }
    }
    return 0;
}

int
main (int argc, char ** argv) {
    int res = is_palindrome(argv[1]);
    return res;
}
