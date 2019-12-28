int putd(double x, double y) { }

// Fixed to accept pointer and not by value
// changed from: void swap(double *x, double *y) 
// changed to: void swap(double x, double y) 
void swap(double *x, double *y) 
{
  *x = *x - *y;
  *y = *x + *y;
  *x = *y - *x;

  putd(x, y);
}
