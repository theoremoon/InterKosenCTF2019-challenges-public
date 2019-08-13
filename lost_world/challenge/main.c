#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("ptr-yudai");
MODULE_DESCRIPTION("InterKosenCTF 2019");
MODULE_VERSION("1.0");

char f[] = "\x3c\x19\x06\x11\x1d\x31\x25\x36\x04\x0b\x22\x1f\x4f\x14\x26\x0a\x54\x15\x56\x10\x3c\x10\x51\x50\x1b\x31\x1d\x58\x18\x19\x1e\x58\x25\x32\x0a\x65\x3d\x0d\x07\x1d\x22\x00";

static void __decode(void)
{
  int i;
  for(i = 0; i < sizeof(f); i++) {
    f[i] ^= 0x77 ^ i;
  }
  f[i - 1] = 0;
}

static int __init lkm_example_init(void) {
  __decode();
  printk(KERN_WARNING "%s\n", f);
  return 0;
}

static void __exit lkm_example_exit(void) {
  printk(KERN_WARNING "Bye!");
}

module_init(lkm_example_init);
module_exit(lkm_example_exit);
