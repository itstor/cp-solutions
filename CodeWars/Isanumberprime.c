#include <stdbool.h>

bool is_prime(int num)
{
    bool prime = true;
    for (int i = 2; i * i <= num + 1; i++)
    {
        if (num % i == 0 && num != i)
        {
            prime = false;
            break;
        }
    }
    return num > 1 ? prime : 0;
}