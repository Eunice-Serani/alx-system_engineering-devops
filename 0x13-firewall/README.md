0x13. Firewall

DevOps
SysAdmin
Security

0. Block all incoming traffic but
mandatory
Let’s install the ufw firewall and setup a few rules on web-01.

Requirements:

The requirements below must be applied to web-01 (feel free to do it on lb-01 and web-02, but it won’t be checked)
Configure ufw so that it blocks all incoming traffic, except the following TCP ports:
22 (SSH)
443 (HTTPS SSL)
80 (HTTP)

1. Port forwarding
#advanced
Firewalls can not only filter requests, they can also forward them.

Requirements:

Configure web-01 so that its firewall redirects port 8080/TCP to port 80/TCP
