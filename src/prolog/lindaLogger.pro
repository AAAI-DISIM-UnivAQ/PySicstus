:-use_module('myLindaClient.pl').
:-use_module(library('system')).
:-linda_client(localhost:3010).

lindaLogger.

logLinda(X) :- 	out(agente_attivo(lindaLogger,localhost:3010)),
				repeat,
					rd_noblock(X),write('tuple: '),write(X),nl,
					sleep(1),
					X==debugStop,
				!,in(debugStop).

% :- linda_trace(on).
%:- logLinda(X).


					