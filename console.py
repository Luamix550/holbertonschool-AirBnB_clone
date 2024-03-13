#!/usr/bin/python3
"""This module provides the entry point of the command interpreter"""
import cmd
import sys



class HBNBCommand(cmd.Cmd):
    """This class shows the basic console"""
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """This method quit the console"""
        sys.exit()

    def do_EOF(self, arg):
        """This method shows EOF on the console """
        sys.exit()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
