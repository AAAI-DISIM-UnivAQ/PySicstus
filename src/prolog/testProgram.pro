<<<<<<< HEAD

friend(pippo,pluto).
friend(pluto,papero).

friend(X,Y):- friend(X,Z),friend(Z,Y).

branch_then :- write('OK'),nl.
branch_else :- fail.

testGoal :- if(friend(pippo,papero),
			branch_then,
			branch_else).
=======
% a test prolog program for PySictus Python class 

amico(pippo,pluto).
amico(pluto,papero).

amico(X,Y):- amico(X,Z),amico(Z,Y).

ramo_then.
ramo_else :- fail.

test :- if(amico(pippo,papero),
			ramo_then,
			ramo_else).
>>>>>>> origin/master
			
