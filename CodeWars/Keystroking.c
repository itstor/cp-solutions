#include <string.h>
int num_key_strokes(const char *text)
{
    int total = 0;
    for (int i = 0; i < (int)strlen(text); i++)
    {
        if (text[i] == 32 || text[i] == 39 || text[i] == 61 || text[i] == 59 || (text[i] >= 44 && text[i] <= 57) || (text[i] >= 96 && text[i] <= 122) || (text[i] >= 91 && text[i] <= 93))
            total += 1;
        else
            total += 2;
    }
    return total;
}