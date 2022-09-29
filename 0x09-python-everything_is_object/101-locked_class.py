#!/usr/bin/python3
"""
This is a module that contains a class that avoids
dynamically created attributes
"""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ['first_name']
