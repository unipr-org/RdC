#include <stdio.h>
#include <stdlib.h>
#include <netdb.h>
#include <netinet/in.h>
#include <sys/socket.h>
  
int main(void)
{
    struct addrinfo *result;
    struct addrinfo *res;
 
    getaddrinfo("www.example.com", NULL, NULL, &result);    /* resolve the domain name into a list of addresses */
//    getaddrinfo("2606:2800:220:1:248:1893:25c8:1946", NULL, NULL, &result);    /* resolve the domain name into a list of addresses */
 
    /* loop over all returned results and do inverse lookup */
    for (res = result; res != NULL; res = res->ai_next)
    {   
        char hostname[1024] = "";
 
        getnameinfo(res->ai_addr, res->ai_addrlen, hostname, 1024, NULL, 0, 0); 

        printf("hostname: %s\n", hostname);
    }   
 
    freeaddrinfo(result);
    return 0;
}
