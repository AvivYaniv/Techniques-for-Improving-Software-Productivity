void assert (_Bool b) { if (!b) exit(); }
int nondet_int() { int x; return x; }
void assume (_Bool e) { while (!e) ; }

int access(int x, int y) 
{

  int i, flag;
  int a[32];
  
  // ADDED SECTION [START]
  // If greater than bound
  if (32 <= y)
  {
	  y = 31;
  }
  // ADDED SECTION [END]

  while (x < y)
  {
    flag = 0;

    for(i = 2; i <= x/2; ++i)
    {
      if(x % i == 0)
      {
        flag = 1;
        break;
      }
    }

    if (flag == 0) 
      break;

    ++x;
  }
  
  assert(x > 0);
  assert(x < 32);

  return a[x];
}
