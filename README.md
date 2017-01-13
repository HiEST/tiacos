Vagrant Box fot TIACOS Labs
==================================

##Steps:
1. run `vagrant up`
2. run `vagrant ssh` to log into the machine
3. run `vagrant halt` to stop the VM
4. run `vagrant destroy` to delete the VM and its associated image


##Reprovision:
If something changes in the vagrant configuration and you need to reprovision, 
 run `vagrant up provision`


##Running vagrant ssh in Windows:

An SSH client is generally not distributed with Windows by default. Because of this, if you are on Windows you have two options to ssh into the virtual machines:

**Option 1**

You can follow this recommendations:

https://docs-v1.vagrantup.com/v1/docs/getting-started/ssh.html

**Option 2**

If you have Windows 10 release 1607 or above (see https://technet.microsoft.com/en-gb/windows/release-info):

Install Canonical Bash for Windows (instructions: https://msdn.microsoft.com/en-us/commandline/wsl/about)
and then in a windows command shel (cmd.exe) run:

`doskey ssh=bash -c "ssh $1"`
