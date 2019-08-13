#include <stdio.h>
#include <string.h>


int main(int argc, char**argv) {
    if (argc <= 1) {
        printf("<usage> %s: <flag>\n", argv[0]);
        return 0;
    }
    int values[] = {180, 247, 57, 89, 234, 57, 75, 107, 191, 128, 61, 209, 66, 16, 228, 66, 261, 88, 21, 264, 171, 24, 232, 205, 27, 235, 81, 30, 273, 68, 81, 134, 83, 72, 89, 54, 266, 155, 253};

    int x = 0;
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        x |= ( ((argv[1][i] << 4) & 0xFF) | (argv[1][i] >> 4) ) + i - values[i];
    }


    if (x == 0) {
        printf("Yes. This is the your flag :)\n");
    } else {
        printf("Try harder!");
    }
    return 0;
}
