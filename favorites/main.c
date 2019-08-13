#include <stdio.h>
#include <string.h>

#define N 14

const char * first = "62d57b27c5d411c45d67a3565f84bd67ad049a64efa694d624340178";
const char * second = "62b64d65828570c33b25e1e54065524571a54d7583556d76b1767c759036";
const char * third = "62c64af7db4839d7eeb3d5363e85bb35e826ec56abd5e7d523956bb5";

unsigned short f(unsigned char x, unsigned int i, unsigned short p) {
  unsigned short a = ((p >> 4) & 0xFF) << 8;
  unsigned short b = (((p >> 12)|(p << 4)) & 0xFF) << 8;
  unsigned short c = (((x << 4) & 0xFF) | (x >> 4)) + 1;
  unsigned short d = ( ((~i) << 4) | (i >> 4) ) & 0xFF;

  return (a^b) | (c^d);
}

int main() {
  unsigned char code[N+1];
  unsigned short result[N];
  unsigned short p = 0x1234;

  printf("Do you know\n");
  printf(" --- the FLAG of this challenge?\n");
  printf(" --- my favorite anime?\n");
  printf(" --- my favorite character?\n");
  printf("\n");

  printf("Input your guess: ");
  scanf("%s", code);
  code[N] = '\0';

  for (int i = 0; i < N; i++) {
    p = f(code[i], i, p);
    result[i] = p;
  }


  char buf[N*4 + 1] = {0};
  for (int i = 0; i < N; i++) {
    sprintf(&buf[i*4], "%04x", result[i]);
  }

  if (strcmp(buf, first) == 0) {
    printf("Congrats! The flag is KosenCTF{%s}!\n", code);
  }
  else if (strcmp(buf, second) == 0) {
    printf("Wow! Let's see it together now!\n");
  }
  else if (strcmp(buf, third) == 0) {
    printf("Yes! Do you like too this?\n");
  }
  else {
    printf("No! You are not interested in me, are you?\n");
  }
}
