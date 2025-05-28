import paramiko
ssh_client=paramiko.SSHClient()
ssh_client.connect('host',username='username',password='password')
        #not sufficient if the host_key is not saved in your system
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #with this paramiko automatically adds the remote server fingerprint to the host file of the os
#ssh_client.load_System_host_keys()
