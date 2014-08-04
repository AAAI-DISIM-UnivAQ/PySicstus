__author__ = 'giodegas'

from pysicstus import SicstusProlog, PrologSystem

# Example 1
# Spawing and consulting an existing prolog file
sp = SicstusProlog('test1')
sp.spawn('prolog/testProgram.pro','test') # non blocking
sp.waitFor('test OK')
ans = sp.ask('amico(pippo,pluto)')
print ans
if sp.ask('amico(pippo,pluto)'):
    print 'ho capito che pippo e pluto sono amici.'
else:
    print 'pippo non conosce pluto'
print "Is Prolog alive?", sp.isAlive()
print isinstance(sp, PrologSystem)

# Example 2
# Spawing and then consulting later a prolog file
sp2 = SicstusProlog('test2')
sp2.spawn()
sp2.consultFile('prolog/testProgram.pro','test',debug=True)
print sp2.ask('amico(pippo,pluto)')

# Example 3
# Spawing, then consulting a direct prolog program
sp3 = SicstusProlog('test3')
sp3.spawn()
prologProgram = '''
                x.
                y.
                couple(X,Y):- X,Y.
                '''
sp3.consult(prologProgram)
print sp3.ask('x')
print sp3.ask('couple(x,y)')
print sp3.ask('couple(x,z)')
print sp3.ask('alfa')

# Example 4
sp4 = SicstusProlog('tcpLogger')
sp4.spawn()
sp4.consultFile('prolog/testSocket.pro')
sp4.ask("writeTcp('test tcp 2')")
