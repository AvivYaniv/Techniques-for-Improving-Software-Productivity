void assert (_Bool b) { if (!b) exit(); }
int nondet_int() { int x; return x; }
void assume (_Bool e) { while (!e) ; }

int gcd(int x, int y) 
{
  int i, gcd;
  // Fixed division by zero
  // changed from:	for(i=0; i < x && i < y; ++i)
  // changed to:	for(i=1; i < x && i < y; ++i)
  for(i=1; i < x && i < y; ++i)
  {
	  if(x%i==0 && y%i==0)
          gcd = i;	  
  }

  return gcd;

}
