#!/usr/bin/env python
#
# WebSploit Framework CloudFlare Resolver module
# Created By 0x0ptim0us (Fardin Allahverdinazhand)
# Email : 0x0ptim0us@Gmail.Com
import os
import socket
from core import wcolors
from colorama import init, Fore, Back, Style
from core import help
from time import sleep

options = ["google.com"]
def cloudflare_resolver():
    try:
        line_1 = wcolors.color.UNDERL + wcolors.color.BLUE + "wsf" + wcolors.color.ENDC
        line_1 += ":"
        line_1 += wcolors.color.UNDERL + wcolors.color.BLUE + "CloudFlare Resolver" + wcolors.color.ENDC
        line_1 += " > "
        com = raw_input(line_1)
        com = com.lower()
        if com[0:10] =="set target":
            options[0]=com[11:]
            print "TARGET => ", options[0]
            cloudflare_resolver()
        elif com[0:12] =='show options':
            print ""
            print "Options\t\t Value\t\t\t RQ\t Description"
            print "---------\t--------------\t\t----\t--------------"
            print "Target\t\t"+options[0]+"\t\tyes\tTarget Address"
            cloudflare_resolver()
        elif com[0:2] =='os':
            os.system(com[3:])
            cloudflare_resolver()
        elif com[0:4] =='help':
            help.help()
            cloudflare_resolver()
        elif com[0:4] =='back':
            pass
        elif com[0:3] =='run':
            sub = (
                    'mail', 'webmail', 'email', 'owa',
                    'direct-connect-mail', 'direct', 'direct-connect', 'direct-web', 'direct-secure', 'direct-ssh',
                    'cpanel', 'whm',
                    'firewall', 'waf', 'ids',
                    'ftp',
                    'forum',
                    'blog',
                    'm',
                    'dev', 'staging', 'devstaging', 'development', 'production', 'prod', 'live', 'demo', 'test', 'testing',
                    'record',
                    'ssl', 'secure-ssl', 'ssl-secure', 'sslsecure', 'securessl', 'syssecure', 'sys-secure',
                    'help',
                    'dns', 'http', 'proxy', 'sftp', 'rftp', 'rssh',
                    'web','web-secure','web-remote','web-ssh','wwweb','wwwadmin', 'www-admin',
                    'ns', 'ns1', 'ns2', 'ns3', 'ns4',
                    'irc', 'aim', 'chat', 'japper', 'sip', 'wifi', 'phone', 'phones', 'voip',
                    'server',
                    'shop', 'clientarea', 'client', 'clients',
                    'intranet', 'extranet', 'internet',
                    'bugs', 'tickets', 'helpdesk',
                    'status',
                    'portal', 'webportal', 'web-portal',
                    'doc', 'docs', 'documents',
                    'beta', 'alpha', 'charlie',
                    'admin', 'adm', 'webadmin',
                    'imap','smtp', 'pop', 'pop3', 'pops', 'imaps', 'smtps',
                    'w1', 'ww1', 'www1', 'ww2', 'www2', 'w-w-w',
                    'sql', 'mysql', 'mssql', 'oracle', 'db2', 'sap', 'postgres',
                    'api',
                    'support',
                    'backup',
                    'corporate', 'corp',
                    'online', 'online-banking', 'onlinebanking', 'onlinebank', 'online-bank', 'online-secure', 'onlinesecure',
                    'remote', 'remote-ssh', 'remote-web', 'remote-connect',
                    'locations', 'loc',
                    'win', 'windows', 'linux', 'unix',
                    'global', 'world', 'worldwide', 'worldwideweb', 
                    'exe',
                    'ir',
                    'vps',
                    'sas',
                    'nas',
                    'z',
                    'secure',
                    'telnet', 'term', 
                    'git', 'cvs', 'svn', 'repo',
                    'backup', 'backups',
                    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                    'wordpress', 'piwik', 'wiki', 'stats', 'flatpress', 'multipress', 'cms', 'jms', 'crm', 'sugar', 'salesforce', 'sf',
                    'asterisk', 'vpn', 'system', 'sys',
                    'www-origin', 'origin-www', 'origin', 'production-origin', 'www.origin', 'origin.www', 'origin-web', 'web-origin', 'origin.web', 'web.origin',
                    )
            try:
                orgip = socket.gethostbyname(options[0])
                print "[-------------------------]"
                print "[+] Default IP Address : %s"%orgip
                print "[-------------------------]"
            except(socket.gaierror):
                print "[-] Error : Host is Down !"
            for i in sub:
                host = i+'.'+options[0]
                try:
                    ip = socket.gethostbyname(host)
                    if ip == orgip:
                        print "%s%s[+] %s : %s%s" % (Style.BRIGHT, Fore.CYAN, host, ip, Style.RESET_ALL)
                    else:
                        print "%s%s[+] %s : %s%s" % (Style.BRIGHT, Fore.GREEN, host, ip, Style.RESET_ALL)
                except(socket.gaierror):
                    print "%s%s[-] %s : N/A%s" % (Style.BRIGHT, Fore.BLUE, host, Style.RESET_ALL)
            cloudflare_resolver()
        else:
            print "Wrong Command =>" + com
    except(KeyboardInterrupt):
        print "\n[!] Operation Stoped By User."
