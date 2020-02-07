; LLVM 4.0.0.1 @64bit

; created by tattn

; my_malloc

define internal i8* @my_malloc(i64 %size) {

  %ret = call noalias i8* @GC_malloc(i64 %size)

  ret i8* %ret

}

; finalizer

@finalizer.str.freed = private unnamed_addr constant [10 x i8] c"freed %d\0A\00"

@finalizer.count = internal global i32 0, align 4

define internal void @finalizer(i8*, i8*) {

  %count = load i32, i32* @finalizer.count, align 4

  %count2 = add nsw i32 %count, 1

  store i32 %count2, i32* @finalizer.count, align 4

  call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([10 x i8], [10 x i8]* @finalizer.str.freed, i32 0, i32 0), i32 %count)

  ret void

}

; main

@main.str.format = private constant [5 x i8] c"%ld\0A\00" 

define i32 @main() {

  call void @GC_init()

  %i8_int64 = call i8* @my_malloc(i64 8)

  %int64 = bitcast i8* %i8_int64 to i64*

  store i64 1234567890, i64* %int64

  %int64v = load i64, i64* %int64

  call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @main.str.format, i32 0, i32 0), i64 %int64v)

  %i = alloca i32, align 4

  %p = alloca i8*, align 8

  store i32 0, i32* %i, align 4

  br label %for_start

for_start:

  %iv = load i32, i32* %i, align 4

  %for_cond = icmp slt i32 %iv, 100

  br i1 %for_cond, label %for_body, label %for_end

for_body:

  %pv = call i8* @my_malloc(i64 128)

  store i8* %pv, i8** %p, align 8

  call void @GC_register_finalizer(i8* %pv, void (i8*, i8*)* @finalizer, i8* null, void (i8*, i8*)** null, i8** null)

  br label %for_next

for_next:

  %iv2 = load i32, i32* %i, align 4

  %iv3 = add nsw i32 %iv2, 1

  store i32 %iv3, i32* %i, align 4

  br label %for_start

for_end:

  call void @GC_gcollect()

  ret i32 0

}

; decrlaration

declare i32 @printf(i8*, ...)

@GC_gc_no = external global i64, align 8

declare void @GC_init()

declare noalias i8* @GC_malloc(i64)

declare i32 @GC_calloc(...)

declare i8* @GC_realloc(i8*, i64)

declare void @GC_free(i8*)

declare void @GC_gcollect()

declare void @GC_register_finalizer(i8*, void (i8*, i8*)*, i8*, void (i8*, i8*)**, i8**)

declare void @GC_set_max_heap_size(i64)

declare i64 @GC_size(i8*)

declare i8* @GC_base(i8*)

declare noalias i8* @GC_malloc_uncollectable(i64)

declare i64 @GC_get_heap_size()

declare i64 @GC_get_free_bytes()

declare i64 @GC_get_bytes_since_gc()

declare i64 @GC_get_total_bytes() 
