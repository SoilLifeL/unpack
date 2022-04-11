class unpack:
	def __init__(self,iterator):
		self.iterator = iterator
		
def func_handler(*funcs):
	redefined_funcs = []
	for func in (*funcs,):
		def new_func(*args, func = func):
			all = []
			for i in (*args,):
				if type(i) == type( unpack([]) ): all.extend([a for a in i.iterator])
				else: all.append(i)
			return func(*all)
		redefined_funcs.append(new_func)
	return redefined_funcs if len(redefined_funcs)>1 else redefined_funcs[0]
	
##EXAMPLE:
def foo(x,y,z,t,w):
	return x+y+z+t+w
def bar(a,b,c):
	return a*b*c
_foo, _bar = func_handler(foo, bar)
print(   _foo(  unpack( [1,2] ), 3, unpack( [4,5] )  )   )
print(   _bar(  10, unpack( [3,5] )  )   )
print(   _foo( unpack([10,10,10,10,10]) )   )

#or, you can use a "tricky" way to save functions' original names:
#_foo, _bar = foo, bar
#foo, bar = func_handler(_foo, _bar)