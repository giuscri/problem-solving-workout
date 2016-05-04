CC=gcc
CFLAGS=-g -O0 -m32 -std=c11

main: main.o queue_int32.o queue_queues_int32.o linkedlist_friendship.o graph.o
	$(CC) $(CFLAGS) $? --output $@

graph.o: graph.c
	$(CC) $(CFLAGS) -c $?

linkedlist_friendship.o: linkedlist_friendship.c
	$(CC) $(CFLAGS) -c $?

queue_queues_int32.o: queue_queues_int32.c
	$(CC) $(CFLAGS) -c $?

queue_int32.o: queue_int32.c
	$(CC) $(CFLAGS) -c $?

clean:
	rm -f *.o

# vim: set noet:
