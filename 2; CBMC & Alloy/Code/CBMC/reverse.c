int reverse(int x) 
{
	int reversedNumber = 0, remainder;

	while(x != 0)
	{
		remainder = x%10;
		reversedNumber = reversedNumber*10 + remainder;
		x /= 10;
	}

	return reversedNumber;

}
