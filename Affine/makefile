OBJ = affine.o gcdeuc.o
EXEC = affine

$(EXEC) : $(OBJ)
	gcc -o $(EXEC) $(OBJ)

affine.o : affine.c affine.h
	gcc -c affine.c

gcdeuc.o : gcdeuc.c gcdeuc.h
	gcc -c gcdeuc.c

clean : 
	rm -f $(EXEC) $(OBJ)
