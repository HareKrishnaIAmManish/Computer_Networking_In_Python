import os
if not os.path.exists("/home/kali/Desktop/Desktop/ComputerNetworks/ch2/underatanding_file_system/temp_directory"):
    try:
        os.makedirs("/home/kali/Desktop/Desktop/ComputerNetworks/ch2/underatanding_file_system/temp_directory")
    except OSError as error:
        print(error)
    else:
        print("created a directory")
    finally:
        print("bye bye")
            

