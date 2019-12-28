#include <stdio.h>
#include <stdlib.h> 
#include <assert.h>
#include <string.h>

#define TRUE	1
#define FALSE	0

#define DEBUG_PRINT				1

#define KLEE_RUN				0

#if KLEE_RUN
	// KLEE Annotation
	#include <klee/klee.h>
#endif

#define TEST_BUFFER_OVERRUNS	0
#define TEST_IS_SORTED			0
#define TEST_IS_PERMUTATION		0

// Counts the number of instances of the number x in the arr
int countX(int x, int *arr, int len)
{
	int count = 0;
	for (int i=0; i<len; i++){
		if (arr[i] == x)
			count++;
	}
	return count;
}

// Returns 1 if arr is sorted, 0 otherwise
int isSorted(int *arr, int len)
{	
	for (int i=0;i<len-1;i++){
		if (arr[i]>arr[i+1])
			return 0;
	}
	return 1;
}

// Returns 1 if arr is a permutation of origin, 0 otherwise
int isPerm(int *origin, int *arr, int len)
{	
	for (int i=0;i<len;i++){
		if (countX(origin[i],arr,len) != countX(origin[i],origin,len))
			return 0;
	}
	return 1;
}

int arePermutations(int a[], int b[], int n, int m) 
{ 
  
    int sum1 = 0, sum2 = 0, mul1 = 1, mul2 = 1; 
  
    // Calculating sum and multiply of first array 
    for (int i = 0; i < n; i++) { 
        sum1 += a[i]; 
        mul1 *= a[i]; 
    } 
  
    // Calculating sum and multiply of second array 
    for (int i = 0; i < m; i++) { 
        sum2 += b[i]; 
        mul2 *= b[i]; 
    } 
  
    // If sum and mul of both arrays are equal, 
    // return true, else return false. 
    return ((sum1 == sum2) && (mul1 == mul2)) ? 1 : 0; 
}

int findMax(int arr[], int n)
{
	int max = arr[0];
	for (int i=1; i<n; i++){
		if (arr[i]>max)
			max = arr[i];
	}
	return max;
}

//swapping 2 elements in array 
void swap(int *x, int *y) 
{ 
	int temp = *x; 
	*x = *y; 
	*y = temp; 
} 
	
void bubbleSort(int arr[], int len) 
{ 
	#if TEST_BUFFER_OVERRUNS
		len *= 2;
		arr[-1] = arr[len * 2];
	#endif	

	int i, j; 
	for (i = 0; i < len-1; i++)	 
		// Last i elements are already in place 
		for (j = 0; j < len-i-1; j++) 
			if (arr[j] >= arr[j+1]) 
			{
				swap(&arr[j], &arr[j+1]); 				
			}
							
		//printf("in bs,issorted\n");
		//swap(&arr[0],&arr[len-1]);
		
	#if TEST_IS_SORTED
		arr[0] = 3;
		arr[1] = 2;
	#endif
	
	#if TEST_IS_PERMUTATION
		arr[len-1]++;
	#endif
} 
	
int main()
{
	int n, i;

	#if KLEE_RUN		
		#if KLEE_RUN_DEBUG
			n = 6;
		#else
			klee_make_symbolic(&n, sizeof(n), "n");
		
			#if TEST_IS_SORTED
				klee_assume(2<n);
			#endif
		#endif
	#else
		printf("Please enter number of elements: ");
		scanf("%d", &n);
		//int* arr = (int*)malloc(n * sizeof(int)); //MAY
	#endif

	int* arr = (int*)malloc(n * sizeof(int));
	int* sorted = (int*) malloc(n * sizeof(int));
	
	#if KLEE_RUN		
		// KLEE Annotation - Instead of reading the input, let KLEE generate it
		klee_make_symbolic(arr, n * sizeof(int), "arr");			
	#else	
		/*printf("Please enter the number of elements - n \n");
		scanf("%d", &n);
		
		int* arr = (int*) malloc(n * sizeof(int));*/

		printf("Enter the numbers \n");
		for (i = 0; i < n; ++i){
			scanf("%d", &arr[i]);
			sorted[i] = arr[i];}
	#endif	
	
	#if DEBUG_PRINT
		#if TEST_BUFFER_OVERRUNS
		#else
			for(int k=0;k<n;k++)
			{
				printf("arr[%d]=%d\n",k,arr[k]);
			}	
		#endif
	#endif
	
	bubbleSort(sorted, n); 

	#if DEBUG_PRINT
		#if TEST_BUFFER_OVERRUNS
		#else
			for(int j=0;j<n;j++)
			{
				printf("sorted[%d]=%d\n",j,sorted[j]);
			}
		#endif
	#endif

	#if KLEE_RUN
		klee_assert(isSorted(sorted,n));	
		klee_assert(arePermutations(sorted,arr,n, n));	
	#else
		//assert(arePermutations(sorted,arr,n, n));
		assert(isPerm(sorted,arr,n));		
		assert(isSorted(sorted,n));
	#endif 
	
	for (int i = 0; i < n; i++)
		arr[i] = sorted[i];
		
	free(arr);
	free(sorted); 
	
	return 0;
}