#include <stdio.h>
#include <unistd.h>

unsigned long keygen()
{
  FILE *fp = fopen("/dev/urandom", "rb");
  unsigned long key;

  fread(&key, sizeof(unsigned long), 1, fp);
  fclose(fp);
  return key;
}

void saferm(char *filepath)
{
  FILE *fp = fopen(filepath, "rb+");
  unsigned long buf, key;
  size_t readBytes;
  
  if (fp == NULL) {
    perror(filepath);
    return;
  }

  key = keygen();
  
  while(1) {
    readBytes = fread((void*)&buf, 1, sizeof(unsigned long), fp);
    if (readBytes != sizeof(unsigned long)) break;

    buf ^= key;
    
    fseek(fp, -sizeof(unsigned long), SEEK_CUR);
    fwrite((void*)&buf, sizeof(unsigned long), 1, fp);
  }

  fclose(fp);

  if (unlink(filepath)) {
    perror(filepath);
    return;
  }
}

int main(int argc, char **argv)
{
  if (argc < 2) {
    puts("Usage: saferm [file]");
    return 1;
  }

  saferm(argv[1]);
  
  return 0;
}
