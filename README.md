# Basic Unpack Toolkit (Actually Just One Tool)
## What Does It Do?
  It enables you to unpack iterators without the usage of asterisk.
## How To Use? 
  ```python
  from unpack import *
  #this imports <class> unpack and <function> func_handler.

  def foo(x, y, z, t): #a dummy function
      return x+y+z+t

  def bar(a, b, c, d) #again, a dummy function
      return a*b*c*d

  globals().update(  func_handler(foo, bar)  ) #you are also able to use this with `locals()`
  result_foo = foo(  unpack( [1,2] ), 3, 4  ) #equals to 10
  result_bar = bar(  1, unpack( [2,3] ), 4  ) #equals to 24
  print(f"result_foo equals to {result_foo}.")
  print(f"result_bar equals to {result_bar}.")
  ```
