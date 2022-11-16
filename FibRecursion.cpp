// Fibonacci Series using Recursion
#include <bits/stdc++.h>
using namespace std;

int fib(int n)
{
    if (n <= 1)
        return n;
    return fib(n - 1) + fib(n - 2);
}

int main()
{
    int x, i = 0;
    cout << "Enter the number of terms of series : ";
    cin >> x;
    cout << "Fibonnaci Series : ";
    while (i < x)
    {
        cout << " " << fib(i);
        i++;
    }
    return 0;
}
