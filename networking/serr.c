#include <arpa/inet.h>
#include <netinet/in.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <sys/socket.h>
#define B_SIZE 16

int run = 1;
void cpyfrom(char *string, int start, int finish, char *dest) {
  int i = 0;
  while (start < finish) {
    dest[i++] = string[start++];
  }
  dest[4] = '\0';
}

void separate(char str[B_SIZE], int val[4]) {
  int i = 0;
  while (str[i] != '\0') {
    char sub_str[4];
    cpyfrom(str, i, i + 4, sub_str);
    val[i / 4] = atoi(sub_str);
    i += 4;
  }
}

void *handle(void *arg) {
  int a = 1;
  char ch;

  while (a) {
    printf("h:");
    scanf("%c", &ch);

    if (ch == 'a') {
      run = 0;
      a = 0;
    }
  }
  return NULL;
}

int main() {
  int sfd = socket(AF_INET, SOCK_DGRAM, 0);
  char buffer[B_SIZE];
  int cord[4];
  pthread_t event_thread;
  pthread_create(&event_thread, NULL, handle, NULL);

  struct sockaddr_in severaddr;
  bzero(&severaddr, sizeof(severaddr));
  severaddr.sin_family = AF_INET;
  severaddr.sin_addr.s_addr = htonl(INADDR_ANY);
  severaddr.sin_port = htons(5050);

  int a = bind(sfd, (struct sockaddr *)&severaddr, sizeof(severaddr));

  while (run) {
    ssize_t bytes_rev = recvfrom(sfd, buffer, 64, 0, NULL, 0);

    buffer[bytes_rev] = '\0';

    separate(buffer, cord);

    for (int i = 0; i < 4; i++) {
      cord[i] /= 1000;
      printf("%d ", cord[i]);
    }
    printf("\n");
  }

  pthread_join(event_thread, NULL);

  return 0;
}
