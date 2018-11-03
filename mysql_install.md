Windows install link: https://dev.mysql.com/downloads/installer/
<br>
Config type: Development Computer<br>
TCP/IP<br>
Port: 3306<br>
X Protocol Port: 33060<br>
Open Windows Firewall ports for network access<br>
Strong Root Password<br>
Added user: admin | strong password<br>
Configure MySQL Server as a Windows Service<br>
Windows Service Name: MySQL 80<br>
Start the MySQL Server at System Startup<br>
Standard System Account<br>


CREATE TABLE `nest_log` (
  `Timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Mode` varchar(10) DEFAULT NULL,
  `State` varchar(20) DEFAULT NULL,
  `Temp` decimal(6,1) DEFAULT NULL,
  `Target` decimal(6,1) DEFAULT NULL,
  `Humidity` decimal(6,1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8
