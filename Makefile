#/
## EPITECH PROJECT, 2025
## my_octal_nbr
## File description:
## my_octal_nbr
#/

src	=	$(wildcard *.py)

files-test	=	$(wildcard file/*.py)

name  =		TicTacToe

BINTESTNAME	=	unit_tests

COV	=	-coverage -lcriterion -lgcov

cc	=	clang

all: $(name)

$(name):	$(src)
	    cp main.py $(name)
		chmod +x $(name)

clean:
	    rm -f $(name)

fclean: clean
	    rm -f $(BINTESTNAME)
		rm -f *.gcno *.gcda

re:		clean $(name)

unit_tests:
	        $(cc) $(files-test) $(CFLAGS)  $(COV) -o $(BINTESTNAME)

tests_run: $(BINTESTNAME)
	      ./$(BINTESTNAME)
