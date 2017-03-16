all:kseq.h kseq_test.c
		$(CC) -g -O2 kseq_test.c -o kseq_test  -lz
		$(CC) -g -O2 kseq_test.c -o kseq_test_static -static  -lz

clean:
		rm -f *.o kseq_test
