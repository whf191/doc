#!/bin/bash
iptables -F
iptables -X
iptables -Z
iptables -t nat -F
iptables -t nat -X
iptables -t nat -Z

iptables -A OUTPUT -p udp --dport 53 -m state --state NEW -j ACCEPT
iptables -A OUTPUT -p tcp -d 192.168.1.31/32 -j ACCEPT 
iptables -A OUTPUT -p all   -m state --state NEW -j LOG --log-leve 5 --log-prefix "output state new"


#rsyslog.conf add -->  kern.=notice /var/log/iptables.log