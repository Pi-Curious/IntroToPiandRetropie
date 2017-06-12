# Intro to Linux
The goal of this lesson is to learn the basics of the linux command line. A lot of the time, especally with hardware related projects, your RaspberryPi will be running in a headless mode. If your goal is to run a system like this it is critical to become comfortable with linux command line. This lesson will just begin to scratch the surface of what can be done with a linux shell.
 
## Configure RaspberryPi
 
First thing is first, we need to configure the pi. We do this with the command `$ sudo raspi-config` We need to change the following items
 
* Password
* Hostname
* Localisation
* Keyboard Layout
* Expand Filesystems 
 
#### Password
Select **1 Change User Password** and change it to something you will not forget because you can get locked out of your system
 
#### Hostname
The hostname is the name of the device on the network. Right now your raspberry pi is named `raspberrypi` to make each device easier to identify give it a unique name. Select **2 Hostname** and enter a new name for you pi.
 
#### Localisation
Your RaspberryPi thinks it is living in England. We must remind it that it is in America now. 
Select **4 Localisation Options** and then **I1 Change Locale**
 
#### Keyboard Layout
The English use a slightly different keyboard layout than ours. Let's go fix that
```
Select 104 key keyboard then proceed to the next screen
scroll and select other, find United States and select generic keyboard and move on
```
 
#### Expand Filesystems 
Rasbian does not take up the full sd card and only adds a small part of it to its partitions to fix that goto **7 Advanced Options** and select **A1 Expand Filesystems**
 
#### Wrapping up configuration
Exit the menu and reboot if it asks you. If it doesn't ask you `$ sudo reboot now` just to be safe
 
 
## Installing packages
Most tools and applications can be downloaded and installed through a package manager in Linux. Debian flavors of Linux such as Rasbian, Ubuntu and Linux mint use the package manager *apt-get*. You might have noticed we already used it a couple times when we did the initial setup of the Pis to do a full system update.
 
As an example we are going to install a useful program htop. Htop is a bit like task manager in windows but more text based. To install it we are going to run `$ sudo apt-get install htop`. Follow the prompts and when it completes we can open it with the `$ htop` command. To quit out of htop press the `f10` key
 
## Permission levels
When you are logged in as `pi` you are a normal user that can only write files in their own home directory. To be able to write in other directories we need to login as the `root` user. Root is a special user in linux systems that is the equivalent of an administrator account in windows. Because of the power of some linux commands, it is dangerous to work logged in as root. It is also a bad idea to give out your root password or let any user elevate to the root user. This is where `sudo` comes in. Sudo allows you to temporarily elevate to root permissions until the command or script you ran is done executing. 

As an example we are going to go change the default message you see everytime you login

`$ nano /etc/motd`

If you notice at the bottom of the screen it says *Read only file*. This is because we are trying to edit a file that you do not own or have permission to edit. To get around this problem we can run 

`$ sudo nano /etc/motd`

There is no longer a read only warning at the bottom of the window. Go ahead and change that message to anything you like. When you are done press `ctrl-o` to save and `ctl-w` to exit. 

Not every user has the right to use sudo. Only users that are assigned to the `wheel` or `sudo` group can use it. 

To change your user over to Root at any time you can `$ sudo su` if you `$ nano /etc/motd` once more you will notice that the warning is not at the bottom of the page. At this point exit out of root with `ctl-d`.

## Moving around in the shell
This section is inteneded to be run in order to get comfortable with moving around with these commands

First lets find out what directory we are in

`$ pwd` - **P**rint **W**orking **D**irectory

Now lets see what is in this directory.

`$ ls` - **L**i**s**t files



	pwd - 
		shows the current filepath
	ls - lists directories in pwd
		`$ ls --help`
			talk about help/man
		`$ ls -la`
			explain special files
			hidden files
				.filename
				.directory
	cd - change directory
		`$ cd directory`
			changes to that directory
		`$ cd . `
			your current directory
		`$ cd ..`
			the previous directory
		`$ cd or `$ cd ~`
			shortcut to your home directory
		`$ cd /`
			root directory
	mkdir - make directory
		`$ mkdir ~/test_dir`
			makes a directory called git in your home directory
	touch - create file
		`$ cd test_dir`
		`$ touch testFile`
	echo - echos back whatever you type after it
		`$ echo lol`
		Can also be used to write lines to a file
			```$ echo lol >> testFile
			$ echo this is a sentence >> testFile```
	cat - prints contents of files to console
		```$ cat testFile
		$ echo this will write over the whole file > testFile```
			be careful when using `>` and `>>`
			`>` will write over the whole file
			`>>` will append a newline to the file 
	less - prints contents of files to console but is more interactive
		`$ less testFile`
	mv - move
		```
		$ touch ~/testFile2
		$ mv ~/testFile2 testFile2
		```
	cp - copy
		`$ cp testFile2 testFile3`
	rm - remove
		```
		$ rm testFile
		$ rm testFile*
		```
			you can use wild cards this will delete testFile2 and testFile3
		```
		$ cd ..
		$ rm test_dir
		```
			will error out saying its a directory
		```$ rm -rf test_dir
		$ rm --help```
			-r removes directories and their files recursively
			-f force
				Be very careful when using this. You cannot get your files back if you delete them by mistake
 
## git
	```$ mkdir git
	$ cd git
	$ git clone https://github.com/Pi-Curious/IntroToPiandRetropie.git```
		This just downloaded our repos
 
## bash scripting
	```
	$ cd IntroToPiandRetropie/ExampleScripts
	$ chmod +x *.sh
	```
		We need execute permissions to run these scripts.
		chmod allows us to change premissions on files
		+x sets the execute flag on the file you select
		since these are all .sh files we can use a * (wildcard) as a shortcut
	`$ touch createFiles.sh`
	`$ ./createFiles.sh`
		creates 10 files as an example of a for loop
	`$ ls TestFiles`
	`$ touch editFiles.sh`
	`$ ./editFiles.sh`
		edits all the files in the directory
	`$ cat TestFiles/file_1`
	`$ touch replaceSomeText.sh`
	`$ ./replaceSomeText.sh`
		replaces text with replaced text to demonstrate sed
 
		sed - Stream EDitor
			A powerful tool to programatically edit files
			for more info try `$ man sed `
 
 
