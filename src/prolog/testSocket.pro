

            :- use_module(library(sockets)).

            sendcmd(IP,PORT,X) :- socket_client_open(IP:PORT, Stream, [type(text)]),
                          % write('sending '),write(X),nl,
                          write(Stream,X),nl(Stream),
                          close(Stream).


            writeTcp(X) :- sendcmd(localhost,3333,X).
