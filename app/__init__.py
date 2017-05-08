#!/usr/bin/env python
# -*- coding: utf8 -*-


def data_type_validator(func):
    ano = func.__annotations__
    def wrapper(*args):
        import inspect
        func_sig = inspect.signature(func)
        params = {k: v for k, v in zip(func_sig.parameters, args)}
        for k in func_sig.parameters.keys():
            if not isinstance(params[k], ano[k]):
                raise Exception('Invalid Argument DataType')
        return func(*args)
    return wrapper
