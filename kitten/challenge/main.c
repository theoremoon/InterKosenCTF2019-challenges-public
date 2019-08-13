#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#define MAX 10
#define NAME_LEN 128

int count = 0;
char __attribute__((section(".name"))) name[NAME_LEN];
char* __attribute__((section(".kittens"))) kittens[MAX];

int readline(char *ptr, int size)
{
  int readSize = read(0, ptr, size);
  if (readSize == 0) exit(1);
  if (ptr[readSize - 1] == '\n') ptr[readSize - 1] = '\x00';
  return readSize;
}

int readint(void)
{
  char s[8];
  readline(s, 7);
  return atoi(s);
}

int menu(void)
{
  puts("================================");
  puts("1. Find a feral kitten");
  puts("2. Feed a kitten");
  puts("3. Look for foster parents");
  puts("4. Release them into the wild");
  puts("================================");
  printf("> ");
  return readint();
}

void setup(void)
{
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);
}

void list_kittens(void)
{
  int i;

  puts("+-------------------------------+");
  for(i = 0; i < count; i++) {
    printf(" %d - %s\n", i, kittens[i]);
  }
  puts("+-------------------------------+");
}

void find_kitten(void)
{
  int len;
  
  if (count < MAX) {
    
    puts("You found a kitten!");
    printf("Name: ");
    len = readline(name, NAME_LEN - 1);
    kittens[count] = (char*)malloc(len);
    strcpy(kittens[count], name);
    count++;
    
  } else {
    
    puts("You have too many kittens to take care of.");
    
  }
}

void feed_kitten(void)
{
  int index;

  puts("Which one?");
  list_kittens();
  printf("> ");
  index = readint();

  if (index < count) {

    printf("%s: Meow!\n", kittens[index]);
    
  } else {

    puts("There's no such kitten...");
    
  }
}

void foster(void)
{
  int index;
  
  puts("Which one?");
  list_kittens();
  printf("> ");
  index = readint();

  if (index < count) {

    count--;
    printf("%s: Meow!\n", kittens[index]);
    free(kittens[index]);
    kittens[index] = kittens[count];
    
  } else {
    
    puts("There's no such kitten...");
    
  }
}

int main(void)
{
  int choice;
  
  setup();
  while(1) {
    choice = menu();
    switch(choice) {
    case 1:
      find_kitten();
      break;
    case 2:
      feed_kitten();
      break;
    case 3:
      foster();
      break;
    case 4:
      puts("Bye bye!");
      exit(1);
    }
  }
  
  return 0;
}
