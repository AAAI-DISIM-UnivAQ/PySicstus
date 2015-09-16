
friend(pippo,pluto).
friend(pluto,papero).

friend(X,Y):- friend(X,Z),friend(Z,Y).

branch_then :- write('OK'),nl.
branch_else :- fail.

testGoal :- if(friend(pippo,papero),
			branch_then,
			branch_else).
			
