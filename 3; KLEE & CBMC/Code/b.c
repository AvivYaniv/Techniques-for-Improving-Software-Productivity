// http://feliam.wordpress.com/2010/10/07/the-symbolic-maze/ ‎
// twitter.com/feliam
/*
 * It's a maze!
 * Use a,s,d,w to move "through" it.
 */

#include<string.h>
#include<stdio.h>
#include<assert.h>
#include<stdlib.h>
#include<unistd.h>

// KLEE Annotation


#define MAGIC "010111101010111101"
//#define MAGIC "010"
#define KLEE_RUN				1
#define KLEE_RUN_DEBUG			1

#if KLEE_RUN
	 #include <klee/klee.h>
#endif
/**
 * The main function
 */
int main (int argc, char *argv[])
{
	#define ITERS 18
	  char program[ITERS];
	  char maze[ITERS];

	  //Initial position
	  int x = 1;
	  int i = 0, j = 0;
	  //int ox, oy, y;
	 
	 printf("it=%d\n",ITERS);
	  
	  // KLEE Annotation - Instead of reading the input, let KLEE generate it
	#if KLEE_RUN
	   klee_make_symbolic(program,ITERS,"program");
	#else
		 //Read the directions 'program' to execute...
	  read(0,program,ITERS);
	#endif

printf("before while\n");
	//Iterate and run 'program'
	while (i < ITERS)
	{
printf("i=%d\n",i);
		//Save old player position
		//ox = x;
		// oy = y;
		//Move player position depending on the actual command
		switch (program[i])
		{
		case '0':
			maze[i]='0';
			printf("case 0\n");
			//i++;
		  break;
		case '1':
			maze[i]='1';
			//i++;
		  break;
		default:
		  printf("Wrong command!(only w,s,a,d accepted!)\n");
		  printf("You lose illegal!\n");
		  exit(-1);
		}
		printf("%d\n",i);
		
		printf("i=%d, m=%d=%c, g=%d=%c \n", i, maze[i], maze[i], MAGIC[i], MAGIC[i]);
		int ret = maze[i] - MAGIC[i];
		printf("ret=%d \n", ret);
	   if(0 != ret) 
	   {
		   printf("You lose dont match\n");
			exit(-2);
	   }
	   else 
	   {
			printf("BI i=%d \n", i);
			if (i == (ITERS-1))
			{
				printf("Win!!!\n");
				// KLEE Annotation - will throw an error on successful run :-)
				#if KLEE_RUN
					
					   klee_assert(0);
				#else
					int a = 0;
					printf("%d\n",5/a);
				#endif


				printf ("Your solution <%42s>\n",program);
				exit (1);
			}
			printf("NE i=%d \n", i);
	   }
	   printf("Pass i=%d \n", i);
	  i++;
	}
}