#include <stdio.h>


unsigned long f(unsigned char bParm1,unsigned int uParm2,unsigned short uParm3)
{
  return (unsigned long)(unsigned short)(((unsigned short)(bParm1 >> 4) | (unsigned short)(((unsigned long)bParm1 & 0xf) << 4)) + 1 ^
                         ((unsigned short)(uParm2 >> 4) | (unsigned short)(~uParm2 << 4)) & 0xff |
                        (uParm3 >> 4) << 8 ^
                        (unsigned short)(((unsigned int)(uParm3 >> 0xc) | (unsigned int)uParm3 << 4) << 8));
}

unsigned hoge[] = {
  0x62d5,
  0x7b27,
  0xc5d4,
  0x11c4,
  0x5d67,
  0xa356,
  0x5f84,
  0xbd67,
  0xad04,
  0x9a64,
  0xefa6,
  0x94d6,
  0x2434,
  0x0178
};

int main() {
  int N = 14;
  unsigned long p = 0x1234;
  for (int i = 0; i < N; i++) {
    for (int c = 0; c < 256; c++) {
      unsigned long r = f(c, i, p);
      if (r == hoge[i]) {
        printf("%c", c);
        p = r;
        break;
      }
    }
  }
  printf("\n");
}
