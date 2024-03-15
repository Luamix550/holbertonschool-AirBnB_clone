#!/usr/bin/python3

"""This module provides the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """This class shows the basic console"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Handles End Of File character."""
        print()
        return True

    def do_quit(self, line):
        """Exits the program."""
        return True

    def emptyline(self):
        """Doesn't do anything on ENTER."""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        if not line:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(line)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance"""
        if not line:
            print("** class name missing **")
        else:
            try:
                class_name, instance_id = line.split()
                if class_name not in storage.all():
                    print("** class doesn't exist **")
                else:
                    key = class_name + "." + instance_id
                    if key not in storage.all()[class_name]:
                        print("** no instance found **")
                    else:
                        print(storage.all()[class_name][key])
            except ValueError:
                print("** instance id missing **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id """
        if not line:
            print("** class name missing **")
        else:
            try:
                class_name, instance_id = line.split()
                if class_name not in storage.all():
                    print("** class doesn't exist **")
                else:
                    key = class_name + "." + instance_id
                    if key not in storage.all()[class_name]:
                        print("** no instance found **")
                    else:
                        del storage.all()[class_name][key]
                        storage.save()
            except ValueError:
                if len(line.split()) == 1:
                    print("** instance id missing **")

    def do_all(self, line):
        instance_list = []
        if not line:
            for key, value in storage.all().items():
                instance_list.append(str(value))
            print(instance_list)
        else:
            name_class = line.split()[0]
            if name_class not in storage.all():
                print("** class doesn't exist **")
            else:
                for key, value in storage.all()[name_class].items():
                    instance_list.append(str(value))
            print(instance_list)

    def do_update(self, line):
        
        
        
        
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
