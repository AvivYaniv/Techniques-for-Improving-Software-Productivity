int gcd(int x, int y) 
{
  int gcd;
  
  // ADDED SECTION [START]
  if ((0 == x) && (0 == y))
  {
	  return 1;
  }
  if (0 == x)
  {
	  return y;
  
  }
  if (0 == y)
  {
	  return x;
  }
  // ADDED SECTION [END]
  
  while(x!=y)
  {
    if(x > y)
      x -= y;
    else
      y -= x;
  }
  
  gcd = x;

  return gcd;

}
