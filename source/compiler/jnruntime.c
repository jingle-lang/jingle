/* jnruntime.c

   This file contains runtime support functions for Jingle
   as well as boot-strapping code related to getting the main program
   to run.
*/

#include <stdio.h>

// __declspec(dllexport)      // Uncomment on Windows
void _print_int(int x) {
  printf("%i\n", x);
}

// __declspec(dllexport)     // Uncomment on Windows
void _print_float(double x) {
  printf("%f\n", x);
}

// __declspec(dllexport)    // Uncomment on Windows
void _print_byte(char c) {
  printf("%c", c);
  fflush(stdout);
}

/*
__declspec(dllexport)    // Uncomment on Windows
void _print_string(char c) {
  printf("%c\n", c);
  printf("%d", c);
  fflush(stdout);
}
*/

/* Bootstrapping code for a stand-alone executable */

#ifdef NEED_MAIN
extern void __jn_init(void);
extern int __jn_main(void);

int main() {
  __jn_init();
  return __jn_main();
}
#endif
