
amico(pippo,pluto).
amico(pluto,papero).

amico(X,Y):- amico(X,Z),amico(Z,Y).

test :- if(amico(pippo,pluto),
			write('test OK'),
			write('test fallito')),
			nl.
			
