#include <math.h>
#include <stdio.h>

float wallis(int n) {
    float pi = 2.0, tmp_;
    for (int i=1; i<=n; i++) {
        tmp_ = 4.0*powf((float)i, 2.0);
        pi *= tmp_/(tmp_-1);
    }

   return pi;
}

int main(int argv, char **argc) {
    int n = 1000000;
    fprintf(stderr, "%d -> %f\n", n, wallis(n));

    return 1;

}
