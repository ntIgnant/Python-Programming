#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main() {
    int size;
    scanf("%d", &size);
    if (size < 0) {
        return 0;
    }

    int *array = malloc(sizeof(int[size]));
    int pos = 0;
    while (true) {
        if (pos < size) {
            scanf("%d", array + pos);
            pos += 1;
            if (pos == size)
                break;
        }
    }

    int largest = 0;
    for (int i = 0; i < size; i++) {
        if (array[i] > largest) {
            largest = array[i];
            pos = i;
        }
    }

    printf("%d", array[pos]);
}


