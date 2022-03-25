# Central Authentication service script (ldapscript.py)

The script install LDAP Server. It should be executed as the last
process after creating a fileserver using the procedures specified
in the fileserver creation documention. 

An LDAP server provides the following benefits:
    - It authenticate all users of RaspberryPI client in your network
    - Store files that are in /etc
    - Store contact details

The main aim of this service is to have one central point of authentication.

## Scope
This script will
    - Install OpenLDAP server 
    - Configure OpenLDAP server
    - Load LDAP database with user account and password
    - Run OpenLDAP server test

## Pre-requisites

RaspberryPi running Raspbian OS

## Reference

Most commands are from the following link: https://help.ubuntu.com/12.04/serverguide/openldap-server.html

## Manual Installation

The following are procedures that you can use to manually install the server instead of using the script

- Open terminal emulator in RaspberryPi
- Configure the domain name of the RaspberryPi

    $sudo echo "schoolname.pef.local" > /etc/hostname
    
- Replace schoolname "schoolname.pef.local" with the particular school name accordigly
- Reboot the Pi
- Install slapd and ldap-utils

    $ sudo apt update && sudo apt install slapd ldap-utils -y

- Enter the admin password of the user database "pef.org" when prompted
- Test the database "pef.local" that was created.

    $ ldapsearch -x -LLL -H ldap:/// -b dc=pef,dc=local dn

- OpenLDAP (if working correctly) will reply the following to indicate a database  is created

    dn:dc=pef, dc=local
    dn: cn=admin, dc=pef, dc=local

- By using the provided add_content.ldif file, modify it accordingly (or not)  and add the contents to the database.

Note: This script is creating a user with uid=john and password=johnldap.

    $ ldapadd -x -D cn=admin,dc=pef,dc=local -W -f add_content.ldif

- OpenLDAP will display the following:

    $ Enter password: 
        "ou=People,dc=pef,dc=local"
        adding new entry "ou=Groups,dc=pef,dc=local"
        adding new entry "cn=miners,ou=Groups,dc=pef,dc=local"
        adding new entry "uid=john,ou=People,dc=pef,dc=local"

- Check the data above is actually in the database "pef.local"

    $ ldapsearch -x -LLL -b dc=example,dc=com 'uid=john' cn gidNumber

- OpenLDAP will display: 
  
    dn: uid=john,ou=People,dc=example,dc=com
    cn: John Doe
    gidNumber: 500
