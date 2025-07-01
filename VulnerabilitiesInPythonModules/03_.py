# import os
# try:
#     eval("__import__('os').system('clear')",{})
#     print("module os loaded by eval")
# except Exception as e:
#     print(repr(e))
#print(eval('dir()'))
# eval("os.system('clear')",{})  #----->error
#eval("__import__('os').system('clear')",{}) -->works
#eval("__import__('os').system('clear')",{'__builtins__':{}) #doesnt work its secured now

