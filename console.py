#!/usr/bin/python3
"""This module provides the entry point of the command interpreter"""
import cmd



class HBNBCommand(cmd.Cmd):
    """This class shows the basic console"""
    prompt = "(hbnb)"

    def do_EOF(self, line):
        """Handles End Of File character.
        """
        print()
        return True

    def do_quit(self, line):
        """Exits the program.
        """
        return True

    def emptyline(self):
        """Doesn't do anything on ENTER.
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
