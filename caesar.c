#include <stdio.h>

int
encrypt_character(int c, int e_key) {
    return (c-'a'+e_key)%26 + 'a';
}

int
main (int argc, char ** argv) {
    int e_key = 0;

    printf("Type the encryption key: ");
    fflush(stdout);

    scanf("%d", &e_key);

    printf("Type your message: ");

    int c = 0;

    // Consume all the characters in stdin,
    // then stop at the first non separator
    scanf(" %c", &c);

    do {
        if (c == '\n') { break; }
        if (c != ' ') {
            c = encrypt_character(c, e_key);
        }
        printf("%c", c);
        fflush(stdout);
    } while (scanf("%c", &c) > 0);

    puts("");
}
