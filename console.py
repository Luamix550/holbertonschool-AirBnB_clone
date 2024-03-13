#!/usr/bin/python3
import cmd
import sys

class HBNBCommand(cmd.Cmd):
    
    prompt = "(hbnb)"
    
    def do_quit(self, arg):
        sys.exit()
        
    def do_EOF(self,arg):
        sys.exit()
    
    do_EOF = do_quit

if __name__ == '__main__':
    HBNBCommand().cmdloop()