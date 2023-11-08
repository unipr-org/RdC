// gcc inaddr.c -o inaddr
//
#include <stdio.h>
#include <sys/socket.h> //inet_aton
#include <netinet/in.h> //inet_aton
#include <arpa/inet.h>  //inet_aton

void main()
{
char IPstring[]="192.135.11.37";
struct in_addr myinaddr;
printf("IPstring: %s \n", IPstring);
inet_aton(IPstring, &myinaddr);

char * ptr;
int i;
ptr = (char *) &myinaddr;
printf("Network order \n");
for (i=0; i<sizeof(int); i++) printf("val[%d]=%2hhu\n", i, ptr[i]);

printf("inet_ntoa: %s \n",inet_ntoa(myinaddr));

}

