class CustomException(Exception):       #exceptions are objects and you need to instanciate them. 
  def __init__(self, value):            
    self.value = value
  
  def __str__(self):
    return self.value

def i_call_a_function_with_errors():            #call this method from the command line
  try:
    print "Calling a function...."              #this will print
    #function_with_generic_error()
    #function_with_custom_error()
    function_with_unknown_error(1)
    print "Tada!"
    
  except CustomException as inst: #inst can be anything. you have on exception handler 
    print "Custom Error Caught! Error({0})".format(inst.value) #insert the first element that i pass into format here
  except:
    print "Default Error Caught!"
  else:
    print "No error raised."
  finally:
    print "Goodbye!"
  
def function_with_generic_error():      #break, something bad happen so raise the exception foo
  raise Exception, "Foo!"
  
def function_with_custom_error():
  raise CustomException, "Foo Bar!"
  
def function_with_unknown_error(foo):
  foo.bar()

  # an exception will either get caught or be uncaught. UNCAUGHT ERRORS are when it crashes 
  # name error is a subclass of exception it didn't know what to do so it classes (when we typrd foo.bar()  into the terminal) 
  # in python you set up a block of code that you think errors will occur in by setting inside of a TRY command 
  # default command that says if anything from exception is raised do what except says. 
  # as soon as something is caught in yout tryblock it stops and gives you the exception 
  # number of different ways to use exceptions. You can specify which ones you want to catch. 
  # else commands means that if nothing broke then do this other thing 
  # import traceback <- this will print out the stack trace so that you know where the exception is being raised 
