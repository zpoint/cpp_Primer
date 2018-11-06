#include "../../lib/unp.h"
#include <time.h>

int main(int argc, char **argv)
{
		int listenfd, connfd;
		socklen_t len;
		char buff[MAXLINE];
		time_t ticks;
		struct sockaddr_storage cliaddr;

		if (argc == 2)
				listenfd = Tcp_listen(NULL, argv[1], &len);
		else if (argc == 3)
				listenfd = Tcp_listen(argv[1], argv[2], &len);
		else
				err_quit("usage: daytimetcpsrvIndependent [ <host> ] <service or port>");

		for ( ; ; )
		{
				len = sizeof(cliaddr);
				connfd = Accept(listenfd, (SA *) &cliaddr, &len);
				printf("connection from %s\n", Sock_ntop((SA *) &cliaddr, len));

				ticks = time(NULL);
				snprintf(buff, sizeof(buff), "%.24s\r\n", ctime(&ticks));
				Write(connfd, buff, strlen(buff));

				Close(connfd);
		}
}