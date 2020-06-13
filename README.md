# smart-home

> sudo apt-get update
> sudo apt-get upgrade

## Install Python pip 3

> sudo apt install python3-pip


### Make sure you are using Python 3 and pip 3

> sudo nano ~/.bashrc

Add the following items in a new line
	alias python=python3
	alias pip=pip3

> sudo source ~/.bashrc


## Database configuration

### Install MariaDB (SQL Database Server)

> sudo apt install mariadb-server

#### Define a root password and update security configurations

> sudo mysql_secure_installation

The default root password is empty. Press ENTER to go ahead
Define the new root password
Type Y for all the other items

#### First login into database

> mysql -u root -p

If you see ERROR 1698 (28000): Access denied for user 'root'@'localhost' try the following

> sudo mysql -u root
> UPDATE user SET plugin='mysql_native_password' WHERE User='root';
> FLUSH PRIVILEGES;
> sudo service mysql restart
try again using the define password

### Install MySQL/MariaDB Connector for Python

> sudo python3 -m pip install mysql-connector 
> pip install mysql-connector-python
> pip install pymysql

## YeeLight Python Module Installation

> pip install yeelight

More API details and usage examples in https://yeelight.readthedocs.io/en/latest/

## If you use SSH to control your Raspberry, this should be interesting for you!

### Keygen to avoid password retyping everytime

Consider that you want to send files from A to B A -> B
In A do:
> ssh-keygen -t rsa
Press ENTER in each step.
At the end the id_rsa file will be created on the home/<username>/.ssh/
> cd /home/<username>
Now it's time to create the corresponding folder in B

Use SSH to access B and create a .ssh folder
> ssh <usernameB>@<ip_address> mkdir -p .ssh
Use the password

Copy the id_rsa file in the B's folder
> cat .ssh/id_rsa.pub | ssh <usernameB>@<ip_address> 'cat >> .ssh/authorized_keys'

Now you are able to use SSH without passwords everytime!
If you have problems, try this: http://www.linuxproblem.org/art_9.html