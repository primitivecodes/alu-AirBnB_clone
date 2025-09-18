#!/usr/bin/python3
"""
Entry point for the command interpreter.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB clone."""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF (Ctrl+D) is typed."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_create(self, arg):
        """Create a new instance of a class (placeholder)."""
        if not arg:
            print("** class name missing **")
        else:
            print(f"New instance of {arg} created (placeholder)")

    def do_show(self, arg):
        """Show an instance based on class name and id (placeholder)."""
        if not arg:
            print("** class name missing **")
        else:
            print(f"Showing instance: {arg} (placeholder)")

    def do_destroy(self, arg):
        """Destroy an instance based on class name and id (placeholder)."""
        if not arg:
            print("** class name missing **")
        else:
            print(f"Destroyed instance: {arg} (placeholder)")

    def do_all(self, arg):
        """Show all instances of a class (placeholder)."""
        if not arg:
            print("Showing all instances (placeholder)")
        else:
            print(f"Showing all instances of {arg} (placeholder)")

    def do_update(self, arg):
        """Update an instance with new attribute (placeholder)."""
        if not arg:
            print("** class name missing **")
        else:
            print(f"Updated instance: {arg} (placeholder)")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
from models.base_model import BaseModel
import models

def do_create(self, arg):
    """Create a new instance of BaseModel and save it."""
    if not arg:
        print("** class name missing **")
    elif arg != "BaseModel":
        print("** class doesn't exist **")
    else:
        obj = BaseModel()
        obj.save()
        print(obj.id)

