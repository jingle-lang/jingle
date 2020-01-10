#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>

// Jingle prototype C virtual machine
// Version 0.0.0.1

// Type definitions
typedef struct ITEM_t {
  u_int8_t type;

  union {
    u_int8_t  u8;
    int8_t    i8;
    u_int32_t u32;
    int32_t   i32;
    void      *ptr;
  } ;

} ITEM;

typedef struct STACK_t {
  int top;
  int size;
  ITEM *stack;

} STACK;

typedef u_int8_t* (*instruction)(u_int8_t *, STACK *);

// Stack Creation
STACK stack_new(int size) {
  STACK s;
  s.top = 0;
  s.size = size;
  s.stack = (ITEM *)malloc(sizeof(ITEM) * size);

  return s;

}

int stack_push(STACK *s, ITEM o) {
  s->stack[s->top++] = o;
  return s->top;
} 

ITEM stack_pop(STACK *s) {
  return s->stack[--(s->top)];
}

ITEM stack_peek(STACK *s) {
  return s->stack[s->top - 1];
}

// Error Messages
void usageMessage() {
  puts("usage: vm <file>");
  exit(1);
}

// File loading
u_int8_t *load_file(char *filename) {
  FILE *f;
  int size;
  u_int8_t *code = NULL;
  struct stat st;

  if((f = fopen(filename, "r"))) {
    fstat(fileno(f), &st);
    code = (u_int8_t *)malloc(st.st_size);
    fread((void *)code, 1, st.st_size, f);
  } else {
    printf("ERROR: cannot open file %s\n", filename);
    usageMessage();
  }
  return code;
}

u_int8_t *op_nop(u_int8_t *ip, STACK *s) {
  return ip++;
}

u_int8_t *op_push_char(u_int8_t *ip, STACK *s) {
  ITEM o;
  o.type = 'c';
  o.u8 = *(ip++) ;
  stack_push(s, o);
  return ip + 2;
}

u_int8_t *op_emit(u_int8_t *ip, STACK *s) {
  ITEM o = stack_pop(s);
  putchar(o.u8);
  return ip++;
  
}

// Init
int main(int argc, char **argv) {
  u_int8_t *code;
  u_int8_t *ip;
  STACK data;
  instruction ops[256];

  if(argc != 2) {
    usageMessage();
  }

  for (int i = 0; i < 256; i++) {
    ops[i] = op_nop;
  }

  ops['c'] = op_push_char;

  code = load_file(argv[1]);
  data = stack_new(2048);
  ip = code;

  while( *ip != 'h') {
    ip = ops[*ip](ip, &data);

  }

  puts("VM started.");
  return 0;
}
