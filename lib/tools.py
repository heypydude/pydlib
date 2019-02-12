'''
Created on 12-Feb-2019

@author: mpk
'''

import os,sys
import subprocess

class Common(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.response = ''
    
    def info(self, *parts):
        if type(parts) == type(""):
            msg = parts
        else:
            msg = parts[0] if len(parts) else parts
            if len(msg)>1:
                for each in parts[1:]:
                    msg += ' - ' + each
        print (msg)
        
    def pathJoin(self, *parts):
        ret = '/'.join(parts)
        ret = ret.strip()
        ret = ret.replace('\\','/')
        return ret
    
    def wrapQuote(self, txt):
        return '"' + txt + '"'
    
    def execute2(self, cmdLst):
        '''!
        For python 3.7
        '''
        try:
            #input = 'command1\ncommand2\n'.encode('utf-8')
            response = subprocess.run(cmdLst, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            #response = subprocess.run(cmdLst, stdout=subprocess.PIPE, input=input)
            return str(response.stdout.decode('utf-8'))
        except Exception as e:
            print(e)
            return None
        
    def execute(self, cmdList):
        '''!
        For python 2.7
        '''
        try:
            cmd = ' '.join(cmdList).strip()
            self.info('Executing',cmd)
            p = subprocess.Popen(cmdList, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            while(True):
                # returns None while subprocess is running
                retcode = p.poll() 
                line = p.stdout.readline()
                if line:
                    line = line.decode('utf-8').strip()
                    yield line
                    if retcode is not None:
                        self.response = p.stdout.readlines() 
                        self.repsonseError = p.stderr.readlines()
                        break        
        except Exception as e:
            self.info(e.args)
            return None
