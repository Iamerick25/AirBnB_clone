#!/usr/bin/python3
"""
Module for console
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand console class
    """
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """
        Quit command to quit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Handles End Of File character.
        """
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
