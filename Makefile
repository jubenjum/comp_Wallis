
all:
	gcc -O3 -shared -std=c99 -lm -o wallis.so -fPIC wallis.c
	gcc -O3 wallis_c.c -o wallis_c

clean:
	@rm -rf *.so *.o *.pyc
