##
## EPITECH PROJECT, 2020
## Makefile
## File description:
## Makefile of 105torus
##

NAME	=	107transfer

all:
	chmod +x $(NAME)

$(NAME): all

clean:
	rm -f *~
	rm -f *#
	rm -r -f __pycache__

fclean: clean

re:	fclean all
