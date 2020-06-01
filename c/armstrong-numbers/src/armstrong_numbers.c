#include <stdio.h>
#include <string.h>
#include <math.h>
#include "armstrong_numbers.h"

int is_armstrong_number(int num) {
    char str[10];
    sprintf(str, "%d", num);
    int power = strlen(str);
    int sum = 0;
    for (int i = 0; i < power; i++) {
        int digit = (int)str[i] - '0';
        sum += pow(digit, power);
    }
    return sum == num;
}
