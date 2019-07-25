# PythonDynIP
This is a small cgi-bin script I use to get IP adresses from IOT devices that sit in a DHCP environment.

## Installation

* Enable cgi-bin in your favorite webserver
* change the placeholders to sensible values
* place the script in the cgi-bin directory

## Usage

* The script mimics the behavior of existing Dynamic DNS servers, so if your iot device has a client for dynamic dns, you can point it to this script. This works with ip cameras, routers, OpenWRT devices etc.
* if you don't have a pre-installed client, you can probably install one, there are many versions available for various OS environments and in various programming languages
* you can also just call the URL from your own code, it is : `https://<your-server-name>/cgi-bin/dyndns?ip=<ipaddr>&user=<username>&pass=<pass>&host=<domain>`
