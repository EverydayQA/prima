
Files here are experimental - looking at things like API issues.

SQLite ODBC
-----------

Download odbc driver from http://www.ch-werner.de/sqliteodbc/ and compile/install.

Then install (via OpenSuse Yast) the `iodbc` and `iodbc-admin` packages.  These
install a command called iodbcadm-gtk which you can run as a user.

Using `iodbcadm-gtk` add a driver (the sqlite driver installed above, with no config file).
Then add a "User DSN" that uses the driver.  This will create a file `~/.odbc.ini` with 
details like:

	[ODBC Data Sources]
	srm-test-sqlite = sqlite
	
	[srm-test-sqlite]
	Driver      = /usr/local/lib64/libsqlite3odbc.so
	Description = test connection for srm and sqlite

Running `iodbctest` appears to do some kind of minimal test.

Programming with ODBC
---------------------

There's some documentation at http://msdn.microsoft.com/en-us/library/hh829589.aspx

This seems more useful for working on Linux: 
http://www.easysoft.com/developer/languages/c/odbc_tutorial.html
