#!/usr/bin/python3

"""This module provides the entry point of the command interpreter"""
import cmd
import models
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity

list_class = ["BaseModel", "User", "State", "City",
              "Amenity", "Place", "Review", "email",
              "password", "first_name", "last_name"]


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
            class_name = line.split()
            if class_name[0] not in list_class:
                print("** class doesn't exist **")
                return
            if len(class_name) == 1:
                print("** instance id missing **")
                return
            instance_id = class_name[1]
            key = class_name[0] + "." + instance_id
            if key not in storage.all().keys():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id """
        if not line:
            print("** class name missing **")
            return
        try:
            class_name, instance_id = line.split()
        except ValueError:
            print("** instance id missing **")
            return
        if class_name not in list_class:
            print("** class doesn't exist **")
            return
        cn_id = class_name + "." + instance_id
        if cn_id not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[cn_id]
        storage.save()

    def do_all(self, line):
        """Print all instances of a specific class or all classes."""
        instance_list = []
        if line in list_class:
            for key, value in storage.all().items():
                if value.to_dict()['__class__'] == line:
                    instance_list.append(value.__str__())
            print(instance_list)
        elif not line:
            for key, value in storage.all().items():
                instance_list.append(value.__str__())
            print(instance_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Update the attributes of a specific instance of a class. """
        if not line:
            print("** class name missing **")
        else:
            split_line = line.split()
            if len(split_line) <= 1:
                print("** instance id missing **")
                return
            elif len(split_line) <= 2:
                print("** attribute name missing **")
                return
            elif len(split_line) <= 3:
                print("** value missing **")
                return
            else:
                class_name = split_line[0]
                instance_id = split_line[1]
                attribute_name = split_line[2]
                value_attr = split_line[3]
                cn_id = class_name + "." + instance_id
                if class_name not in list_class:
                    print("** class doesn't exist **")
                    return
                if cn_id not in storage.all().keys():
                    print("** no instance found **")
                for key, value in storage.all().items():
                    if cn_id == key:
                        value.__dict__[attribute_name] = value_attr
                        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
