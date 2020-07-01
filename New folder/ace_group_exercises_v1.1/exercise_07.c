// ACE Group Example Code Snippet
// Find the bug and explain it to us!
// This code will not compile as-is; you only have source to spot the issue!

long validate_input(char *n, TYPE *m, char *sv) {
    int i; // iterator
    int j; // array length var
    char c, *s, *t, *v; // arg buffer pointers / temp vars

    // arg buffers
    #define TMPLEN 1024
    char tmp[TMPLEN], arg[TMPLEN];

    /* lines removed for clarity */

    if (t-v) { // parse string?
        strncpy(t=tmp, v, j); // copy to temp buffer
        tmp[j] = '\0';
        /* lines removed for clarity */

        if (*t == '"') { // check for quoted string
            for (v=arg, i=0, ++t; (c = *t++) != '"';) {
                if (c=='\\')
                    c = *t++;
                arg[i++] = c;
            }
        }
        /* lines removed for clarity */
    }
    /* lines removed for clarity */
}
