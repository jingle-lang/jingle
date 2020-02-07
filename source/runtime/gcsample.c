#include <stdio.h>

#include <gc.h>

static void*

my_malloc(long size) {

    return GC_malloc(size);

}

static void 

finalizer(void* obj, void* client_data) 

{

    static int count = 0;

    printf("freed%d\n", count++);

}

int 

main(int argc, char* argv[]) 

{

    GC_init();

    int i = 0;

    for (i = 0; i < 100; i++) {

        void* p = my_malloc(128);

        GC_register_finalizer(p, finalizer, NULL, NULL, NULL);

    }

    GC_gcollect();

    return 0;

}
