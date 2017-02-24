Vagrant Box fot TIACOS Labs
==================================

##Software Required:
- Vagrant: https://www.vagrantup.com/
- VirtualBox: https://www.virtualbox.org
- Git to clone this repository and keep up to date

##Steps to prepare the environment:
1. Download and install the latest version of VirtualBox
2. Download and install the latest version of Vagrant
3. Clone this repository: `git clone git@github.com:HiEST/tiacos.git`
4. Run the box

##Steps to run the Box:
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
