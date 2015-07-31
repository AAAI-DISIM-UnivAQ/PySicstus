% a test prolog program for PySictus Python class 

amico(pippo,pluto).
amico(pluto,papero).

amico(X,Y):- amico(X,Z),amico(Z,Y).

ramo_then.
ramo_else :- fail.

test :- if(amico(pippo,papero),
			ramo_then,
			ramo_else).
			
