"""
 PySictus module to encapsulate Sictus Prolog process management
 
 Licensed with Apache Public License
 by AAAI Research Group
 Department of Information Engineering and Computer Science and Mathematics
 University of L'Aquila, ITALY
 https://www.disim.univaq.it
"""

__author__ = 'giodegas'

import pexpect

def write2file(fname, txt):
    with open(fname,'w') as fout:
        fout.write(txt+'\n')

OPTIONS = '--nologo --noinfo'

class PrologSystem:

    def __init__(self, name, cmd='/usr/local/sicstus4.2.3/bin/sicstus', options=OPTIONS):
        self.name = name
        self.PrologCmd = cmd
        self.options = options
        self.PrologInt = None
        self.basedir = None


    def prepCmd(self, fname, goal):
        cmd = self.PrologCmd
        if len(fname)>0:
            cmd += ' '+' -l '+fname
        if len(self.options)>0:
            cmd += ' '+self.options
        if goal:
            cmd += " --goal " + goal + "."
        return cmd

    def consultFile(self, fname, goal=None, debug=False, blocking=True, waitString='yes|no'):
        print(  fname, goal )
        if self.PrologInt:
            self.PrologInt.sendline("consult('"+fname+"').\r")
            self.waitFor(waitString)
            if goal:
                if blocking:
                    print( 'asking: ',goal)
                    r = self.ask(goal)
                    if debug:
                        print( r )
                else:
                    self.PrologInt.sendline(goal+'.')
            if debug:
                print( self.PrologInt.before )
                print( self.PrologInt.after )
        else:
            cmd = self.prepCmd(fname, goal)
            print( 'Consulting a Prolog program: ',cmd )
            pexpect.run(cmd)

    def consult(self, program, goal=None):
        assert(type(program) == type(''))
        fname = 'prolog/'+self.name+'.pro'
        write2file(fname, program)
        self.consultFile(fname,goal)

    def spawn(self, fname='', goal=None):
        cmd = self.prepCmd(fname, goal)
        print( "Spawing Prolog system: ",cmd )
        logF = open('log/'+self.name+'.log','w')
        print( 'spawning:     ', cmd, self.basedir )
        self.PrologInt = pexpect.spawn(cmd, logfile=logF)

    def waitFor(self,msg, debug=False):
        if self.PrologInt:
            lst = msg.split('|')
            index = self.PrologInt.expect(lst)
            if debug:
                print( self.PrologInt.match.re.pattern )
            self.PrologInt.send('\r')
            return index

    def ask(self,question):
        if self.PrologInt:
            self.PrologInt.after = ''
            self.PrologInt.sendline("ensure_loaded('../interpreter/tcpout.pl').")
            idx = self.waitFor('yes|no|Existence error')
            self.PrologInt.sendline(question+'.')
            idx = self.waitFor('.{18}   Actived Agent [a-zA-Z0-9_]* .{19}')
            return (idx==0)

    def readAll(self):
        try:
            self.PrologInt.readline()
            self.PrologInt.readline()
            self.PrologInt.readline()
            self.PrologInt.readline()
            i = self.PrologInt.readline()
            return i
        except Exception as e:
            print(f"Exception: ", e)
            return "TIMEOUT"


    def runInteractive(self):
        self.options = ''
        cmd = self.prepCmd('', None)
        print( 'Launching Prolog shell...' )
        print( cmd )
        logF = open('log'+self.name+'.log','w')
        self.PrologInt = pexpect.spawn(cmd, logfile=logF)
        self.PrologInt.expect('| ?-')
        self.PrologInt.before
        self.PrologInt.after,
        self.PrologInt.interact()
        self.PrologInt.kill(1)

    def setBasedir(self, basedir):
        self.basedir = basedir

    def debugOut(self):
        if self.PrologInt:
            out = str(self.PrologInt.before) + '\n' + str(self.PrologInt.after)
        else:
            out = 'Prolog interpreter not running'
        return out

    def isAlive(self):
        if self.PrologInt:
            return self.PrologInt.isalive()
        else:
            return False

    def send(self,toStr,waitStr='',debug=False):
        if self.PrologInt:
            self.PrologInt.sendline(toStr)
            if len(waitStr)>0:
                index = self.PrologInt.expect(waitStr)
                # self.PrologInt.send('\r')
            if debug:
                print( self.PrologInt.before )
                print( self.PrologInt.after )

    def terminate(self):
        self.PrologInt.terminate(True)
        self.PrologInt.kill(1)

class SicstusProlog(PrologSystem):

    def somethingSpecial(self):
        pass
