int solution(int number)
{
    int sum = 0;

    for (int a = 0; a <= number; a += 3)
    {
        if (a < number && a % 5 != 0)
        {
            sum += a;
        }
    }
    for (int a = 0; a <= number; a += 5)
    {
        if (a < number)
        {
            sum += a;
        }
    }
    return sum;
}