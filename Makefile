
all:
	gcc -O3 -shared -std=c99 -lm -o wallis.so -fPIC wallis.c

clean:
	@rm -rf *.so *.o *.pyc
