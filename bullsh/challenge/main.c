#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define CMD_SIZE 64

void bullexec(char *cmd)
{
  char *p;

  for(p = cmd; *p != 0; ++p) {
    if (*p == '\n' || *p == ' ') {
      *p = 0;
      break;
    }
  }
  
  if (strcmp(cmd, "ls") == 0) {
    system(cmd);
  } else if (strcmp(cmd, "exit") == 0) {
    exit(0);
  } else {
    printf(cmd);
    puts(": No such command");
  }
}

void bullsh(void)
{
  char buf[CMD_SIZE];
  while(1) {
    printf("$ ");
    fgets(buf, CMD_SIZE - 1, stdin);
    bullexec(buf);
  }
}

int main(void)
{
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);
  
  bullsh();
  return 0;
}
