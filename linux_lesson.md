## Change password
	`$ passwd`

## Configure RaspberryPi
	`$ raspi-config `
		change hostname
		change locale
			en_US.UTF-8
		expand partitions to full sd card
	reboot

## Install packages
	example htop
	`$ sudo apt-get install htop`
	show demo of htop
		`$ htop`
			q to quit


## Talk about root/sudo
	Example: write custom motd message
		`$ nano /etc/motd`
			Will open file but cannot write out
		`$ sudo nano /etc/motd`
			Write a new message 
			ctl-o to write file
			ctl-x to exit
	Elevate to root permissions
	`$ sudo su`
		`$ nano /etc/motd`

## Moving around
	pwd - Print Working Directory
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
