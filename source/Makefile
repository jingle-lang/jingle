# Makefile for creating a shared-library version of the Jingle runtime.
# This is used if you're going to run Jingle programs as a JIT. 
# See the file jingle/run.py

osx::
	gcc -bundle -undefined dynamic_lookup jnruntime.c -o jnruntime.so

linux::
	gcc -shared -fPIC jnruntime.c -o jnruntime.so

# Prerequisite: cl.exe on path configured for x64, run "vcvarsall.bat x64".

win::
	cl /LD jnruntime.c /link /out:jnruntime.dll
