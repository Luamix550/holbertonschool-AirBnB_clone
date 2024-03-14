#!/usr/bin/python3
"""This module provides the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """This class shows the basic console"""
    prompt = "(hbnb) "

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

    def do_create(self, line):
        if not line:
            print("** class name missing **")
        else:
            try:
                class_create = eval(line)()
                class_create.save()
                print(class_create.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self,line):
        if not line:
            print("** class name missing **")
        else:
            try:
                info = line.split()
                verify_class = eval(line[0])
                if len(info) > 2:
                    print("** instance id missing **")
                else:
                    Class_name = info[0] + "." + info[1]
                    if Class_name not in storage.all().keys():
                        print("** no instance found **")
                    else:
                        for key, value in storage.all().items():
                            if Class_name == key:
                                print(value)
            except NameError:
                print("** class doesn't exist **")

    def do_destroy(self,line):
        









"""        return
        try:
            Class_id = line.split()
            data = Class_id[0] + "." + Class_id[1]
            if not Class_id[1]:
                print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")
"""
if __name__ == '__main__':
    HBNBCommand().cmdloop()
