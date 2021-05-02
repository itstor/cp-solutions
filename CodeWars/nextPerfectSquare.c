#include <math.h>
unsigned long long next_perfect_square(long long n)
{
    return n >= 0 ? (floor(sqrt(n) + 1)) * floor((sqrt(n) + 1)) : 0;
}