/* urldecode - v. RFC 1738 per i dettagli */
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

int main()
{
	char c, c1, c2;
	while( (c = getchar()) != EOF ){
		if( c == '%' ){
			c1 = getchar();
			c2 = getchar();
			if( c1 == EOF || c2 == EOF )  exit(0);
			c1 = tolower(c1);
			c2 = tolower(c2);
			if( ! isxdigit(c1) || ! isxdigit(c2) )  exit(0);
			if( c1 <= '9' )
				c1 = c1 - '0';
			else
				c1 = c1 - 'a' + 10;
			if( c2 <= '9' )
				c2 = c2 - '0';
			else
				c2 = c2 - 'a' + 10;
			putchar( 16 * c1 + c2 );
		} else if( c == '+' )
			putchar(' ');
		else
			putchar(c);
	}
	exit(0);
}

