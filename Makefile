
all:
	gcc -O3 -shared -std=c99 -lm -o wallis.so -fPIC wallis.c
	gcc -O3 wallis_c.c -o wallis_c
	gfortran -O3 wallis.f90 -o wallis_f

clean:
	@rm -rf *.so *.o *.pyc
	@rm a.* wallis_f wallis_c
