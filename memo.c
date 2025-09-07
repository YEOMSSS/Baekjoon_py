#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    char *string = malloc(101);
    fgets(string, 101, stdin);
    string[strcspn(string, "\n")] = '\0';

    int cnt = 0;
    for (size_t i = 0; i < strlen(string); i++)
    {
        putchar(string[i]);
        cnt++;
        if (cnt == 10)
        {
            putchar('\n');
            cnt = 0;
        }
    }
    free(string);
    return 0;
}