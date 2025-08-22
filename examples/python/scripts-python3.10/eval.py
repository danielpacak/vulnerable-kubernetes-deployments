#!/usr/bin/env python


def function_with_infinite_loop():
    while True:
        print(abs(-89))
        print(eval("7**8"))


def top_level_function():
    function_with_infinite_loop()


top_level_function()
