# Log Analysis Project: Reporting Tool
By Abdulrahman Elsharqawi, This project is supervised by Udacity's **[Full Stack Web Developer Nanodegree](https://www.udacity.com/course/nd004)**

## About
The projects is consist of 3 parts: 
	1 . News DB, which is a 'PostgreSQL' database that has 3 tables : Authors, Articles, Log. With about 1.6 million rows.
	2 .'Logs Analysis.py', which is a python file to handle and print the results of 3 queries presented in the following questions: 
		* What are the most popular three articles of all time?
		* Who are the most popular article author of all time?
		* On which days did more than 1% of request lead to errors?

## Prerequisites
* Python 2
* [VirtualBox](virtualbox.org)
* [Vagrant](https://www.vagrantup.com/downloads.html)
* PowerShell or git Bash

## How to Run
  1. first, download and install vagrant from [here](https://www.vagrantup.com/downloads.html) **Make sure to allow network permissions for vagrant**.
  2. If Vagrant is successfully installed, you will be able to run `vagrant --version`
  in your terminal to see the version number.
  3. You can download and unzip this file: [FSND-Virtual-Machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) This will give you a directory called FSND-Virtual-Machine.
  4. Either way, you will end up with a new directory containing the VM files. Change to this directory in your terminal with 'cd'. Inside, you will find another directory called **vagrant**. Change directory to the **vagrant** directory.
  5. From your terminal, inside the vagrant subdirectory, run the command 'vagrant up'. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.
  6. When 'vagrant up' is finished running, you will get your shell prompt back. At this point, you can run 'vagrant ssh' to log in to your newly installed Linux VM!
  7. Next, [download the data here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called 'newsdata.sql'. Put this file into the **vagrant** directory, which is shared with your virtual machine.
  8. Move the file 'Logs Analysis.py' to the same **vagrant** directory.
  9. run these commands in your shell bash : 
  	*  psql - the PostgreSQL command line program
  	*  -d news — connect to the database named news which has been set up for you
  	*  -f newsdata.sql — run the SQL statements in the file newsdata.sql
  10. Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.
  11. To execute the program, run `python "logs analysis.py"` from the command line.