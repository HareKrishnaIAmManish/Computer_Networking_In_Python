import os
# for root,directories,files in os.walk(".",topdown=False):
#     print(type(root))
#     print(type(directories))
#     print(type(files))
#     print(root)
#     for file_entry in files:
#         print('[+] ',os.path.join(root,file_entry))
#     print("hello")    
#     for name in directories:
#         print('[++] ',name)   
# print("bye")
# for currentdir, dirnames, filenames in os.walk("."):
#   print(currentdir)
file_count = 0
for currentdir, dirnames, filenames in os.walk("."):
 file_count += len(filenames)
print(file_count)
