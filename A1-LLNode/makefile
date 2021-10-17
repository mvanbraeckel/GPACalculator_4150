
CFLAGS		= -g -Wall

OBJS		= LLNode.o main.o


.SUFFIXES:	.md .dvi .ps .pdf .tex

listtest : $(OBJS)
	$(CC) $(CFLAGS) -o listtest $(OBJS)

clean :
	- rm -f $(OBJS)
	- rm -f listtest
	- rm -f tags

tags : dummy
	ctags *.c

dummy:
