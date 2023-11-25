/* urlencode - v. RFC 1738 per i dettagli */
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

int main()
{
	int c;
	char *h = "0123456789abcdef";

	while( (c = getchar()) != EOF ){
		if( 'a' <= c && c <= 'z'
		|| 'A' <= c && c <= 'Z'
		|| '0' <= c && c <= '9'
		|| c == '-' || c == '_' || c == '.' )
			putchar(c);
		else if( c == ' ' )
			putchar('+');
		else {
			putchar('%');
			putchar(h[c >> 4]);
			putchar(h[c & 0x0f]);
		}
	}
	exit(0);
}

