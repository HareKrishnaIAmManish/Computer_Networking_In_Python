import asyncssh
import asyncio
import getpass
async def execute_command(host,command,username,password):
    async with asyncssh.connect(host,username=username,password=password) as connection:
        result=await connection.run(command)
        return result.stdout
if  __name__=='__main__':
    hostname=input("enter the hostname: ")
    command=input("enter command: ")
    username=input("enter username: ")
    password=getpass.getpass(prompt="Enter the password: ")
    loop=asyncio.get_event_loop()
    output_command=loop.run_until_complete(execute_command(hostname,command,username,password))
    print(output_command)
