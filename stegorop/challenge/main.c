#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <unistd.h>

char lock = 0;

char table[][4] = {
  ">>", "><", ">+", ">-", ">.", ">,",
  "<>", "<<", "<+", "<-", "<.", "<,",
  "+>", "+<", "++", "+-", "+.", "+,",
  "->", "-<", "-+", "--", "-.", "-,",
  ".>", ".<", ".+", ".-", "..", ".,",
  ",>", ",<", ",+", ",-", ",.", ",,",
  "[-]"
};

void __abort(char *progname)
{
  printf("*** stegorop detected *** %s: double startup ***\n", progname);
  exit(0);
}

void stagernography(char *text)
{
  char *ptr;
  printf("Output: ");
  for(ptr = text; *ptr != 0; ++ptr) {
    char c = toupper(*ptr);
    if ('0' <= c && c <= '9') {
      printf("%s", table[c - 0x30]);
    } else if ('A' <= c && c <= 'Z') {
      printf("%s", table[c - 0x41 + 10]);
    } else if (c == ' ') {
      printf("%s", table[36]);
    }
  }
  printf("\n");
}

int main(int argc, char **argv)
{
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);
  if (lock != 0) __abort(argv[0]);
  //////////
  
  char text[100];
  puts("===== Online Steganography Tool =====");
  printf("Input: ");
  read(0, text, 0x100);
  stagernography(text);
  
  //////////
  if (lock != 0) __abort(argv[0]);
  lock = 1;
  return 0;
}
