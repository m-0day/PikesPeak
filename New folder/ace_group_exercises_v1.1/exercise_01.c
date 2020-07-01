#include <stdio.h>
#include <unistd.h>
#include <string.h>

void sayHello(char *uname) {  
    char  uname_buf[20];
    strcpy(uname_buf, uname);
    printf("Welcome, %s!\n", uname_buf);
}  

int main(int argc, char *argv[]) {  
    char uname[50];
    memset((char *)&uname, 0, sizeof(uname));
    printf("Who are you? ");
    fflush(stdout);
    read(0, &uname, sizeof(uname)-1);
    char *pos;
    if ((pos=strchr(uname, '\n')) != NULL) {
        *pos = '\0';
    } 
    sayHello((char *)&uname);
    return 0;
}
