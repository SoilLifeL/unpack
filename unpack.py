class unpack:
    def __init__(self,iterator):
        self.iterator = iterator

def func_handler(*funcs):
    globs = {}
    for func in (*funcs,):
        if func.__name__.startswith("_raw_"):
            continue
        globs["_raw_" + func.__name__]  =  func
        def new_func(*args, func = func):
            all = []
            for i in (*args,):
                if type(i) == type( unpack([]) ): all.extend([a for a in i.iterator])
                else: all.append(i)
            return  globs["_raw_" + func.__name__](*all)
        globs[func.__name__] = new_func
    return globs

