#include <stdio.h>
#include <math.h>

double f(int x, double *coeff) {
  int i;
  double y = 0.0;
  for(i = 0; i < 8; i++) {
    y += coeff[i] * pow(x, i);
  }
  return y;
}

char f1(int x) {
  double coeff[] = {7.50000000e+01, -2.15730952e+02, 6.17336111e+02, -5.52511111e+02, 2.31798611e+02, -5.00319444e+01, 5.36527778e+00, -2.25992063e-01};
  return (char)round(f(x, coeff));
}

char f2(int x) {
  double coeff[] = {1.23000000e+02, -7.28500000e+02, 1.57130278e+03, -1.26677361e+03, 4.93069444e+02, -9.98194444e+01, 1.01277778e+01, -4.06944444e-01};
  return (char)round(f(x, coeff));
}

char f3(int x) {
  double coeff[] = {1.12000000e+02, -5.46942857e+02, 9.77608333e+02, -7.18198611e+02, 2.74833333e+02, -5.71027778e+01, 6.05833333e+00, -2.55753968e-01};
  return (char)round(f(x, coeff));
}

int main(int argc, char** argv)
{
  int i, l;
  char *ptr;
  
  if (argc < 2) goto NG;

  for(i = 0, ptr = argv[1]; *ptr != 0; ++ptr, ++i) {
    if (i < 0x08) {
      if (*ptr != f1(i)) goto NG;
    } else if (i < 0x10) {
      if (*ptr != f2(i - 0x08)) goto NG;
    } else {
      if (*ptr != f3(i - 0x10)) goto NG;
    }
  }
  if (i != 0x18) goto NG;

  puts("OK");
  return 0;

 NG:
  puts("NG");
  return 1;
}

