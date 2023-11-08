// gcc gethosybyname.c -o gethostbyname
#include <stdio.h>
#include <netdb.h>
#include <string.h>
#include <sys/socket.h> 
#include <netinet/in.h> 
#include <arpa/inet.h>

int main(int argc, char *argv[])
{
int i;
struct in_addr myaddr;
struct hostent *myhostent;
char hostname[50];
if (argc == 1) {fprintf(stdout," inserire un hostname \n"); return(1);}
strcpy(hostname,argv[1]);
myhostent=gethostbyname(hostname);
if(myhostent==0) { fprintf(stdout,"%s: host sconosciuto\n",hostname); 
return(2);}

printf("h_name: %s\n", myhostent->h_name);

for (i=0; (myhostent->h_aliases[i]); i++)
printf("h_aliases: %s\n",myhostent->h_aliases[i]);

printf("h_addrtype: %d\n",myhostent->h_addrtype);

printf("h_hlength: %d\n",myhostent->h_length);

printf("h_addr: %s\n",inet_ntoa( *(struct in_addr *)myhostent->h_addr));


return (0) ;
}

