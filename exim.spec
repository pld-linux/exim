Summary:	University of Cambridge Mail Transfer Agent 
Summary(pl):	Agent Transferu Poczty Uniwersytetu w Cambridge
Name:		exim
Version:	3.16
Release:	1
License:	GPL
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
URL:		http://www.exim.org/
Source0:	ftp://ftp.cus.cam.ac.uk/pub/software/programs/exim/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.cus.cam.ac.uk/pub/software/programs/exim/%{name}-texinfo-3.10.tar.gz
Source2:	exim.init
Source3:	exim.cron.db
Source4:	exim.8
Source5:	analyse-log-errors
Source6:	eximon.desktop
Source8:	Makefile-Linux
Source9:	exim.aliases
Source10:	exim.conf
Source11:	newaliases
Source12:	exim.logrotate
Source13:	exim.sysconfig
#Source14:	ftp://ftp.cus.cam.ac.uk/pub/software/programs/exim/FAQ.txt.gz
Source14:	exim-FAQ.txt.gz
#Source15:	ftp://ftp.cus.cam.ac.uk/pub/software/programs/exim/config.samples.tar.gz
Source15:	exim-config.samples.tar.gz
Patch0:		exim-EDITME.patch
Patch1:		exim-monitor-EDITME.patch
Patch2:		exim-texinfo.patch
Patch3:		exim-use_system_pcre.patch
Provides:	smtpdaemon
Obsoletes:	smtpdaemon
Obsoletes:	sendmail
Obsoletes:	postfix
Obsoletes:	zmailer
Obsoletes:	smail
Obsoletes:	qmail
Prereq:		/usr/sbin/useradd
Prereq:		/usr/sbin/groupadd
Prereq:		/bin/awk
BuildRequires:	openldap-devel
BuildRequires:	texinfo
BuildRequires:	perl
BuildRequires:	pam-devel
BuildRequires:	pcre-devel
Requires:	openldap
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Smail like Mail Transfer Agent with single configuration file.
Features: flexible retry algorithms, header & envelope rewriting,
multiple deliveries down single connection or multiple deliveries in
parallel, regular expressions in configuration parameters, file
lookups, supports sender and/or reciever verification, selective
relaying, supports virtual domains, built-in mail filtering and can be
configured to drop root privilleges when possible.

%description -l pl
Agent transferu poczty (MTA) z pojedynczym plikiem konfiguracyjnym.
Jego zalety: ¶wietne algorytmy, mo¿liwo¶æ przepisywania nag³ówków &
koperty, wielokrotne dostarczanie poczty podczas jednego po³±czenia
lub równoleg³e dostarczanie poczty, wyra¿enia regularne w parametrach
konfiguracyjnych, weryfikacja nadawcy i/lub odbiorcy, selektywne
relayowanie, wsparcie dla wirtualnych domen, wbudowany system filtrów,
mo¿liwo¶æ odrzucania praw roota kiedy jest to mo¿liwe.

%package X11
Summary:	X Window based Exim administration tool
Summary(pl):	Narzêdzia administracyjne exima dla X Window
Group:		X11/Utilities
Group(pl):	X11/Narzêdzia
Requires:	applnk

%description X11
X Window based monitor & administration utility for the Exim Mail
Transfer Agent.

%description -l pl X11
Bazuj±ce na X Window narzêdzia dla Exima - monitor i program
administracyjny.

%prep
%setup -q -T -b 0
%setup -q -T -D -a 1
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1

install %{SOURCE14} doc/FAQ.txt.gz
install %{SOURCE15} doc/config.samples.tar.gz

install -d Local
cp src/EDITME Local/Makefile
cp exim_monitor/EDITME Local/eximon.conf

%build
%{__make} "CFLAGS=$RPM_OPT_FLAGS"

makeinfo --no-split exim-texinfo-*/doc/oview.texinfo
makeinfo --no-split exim-texinfo-*/doc/spec.texinfo
makeinfo --no-split exim-texinfo-*/doc/filter.texinfo

%install
rm -rf $RPM_BUILD_ROOT
install -d	$RPM_BUILD_ROOT%{_sysconfdir}/{cron.{daily,weekly},logrotate.d,rc.d/init.d,sysconfig,mail}
install -d	$RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/man8,%{_libdir}}
install -d	$RPM_BUILD_ROOT%{_var}/{spool/exim/{db,input,msglog},log/exim,mail}
install -d	$RPM_BUILD_ROOT%{_infodir}
install -d	$RPM_BUILD_ROOT{/usr/X11R6/bin,%{_applnkdir}/System}

install	build-Linux-pld/exim		$RPM_BUILD_ROOT%{_bindir}
install build-Linux-pld/exim_fixdb	$RPM_BUILD_ROOT%{_bindir}
install build-Linux-pld/exim_tidydb	$RPM_BUILD_ROOT%{_bindir}
install build-Linux-pld/exim_dbmbuild	$RPM_BUILD_ROOT%{_bindir}
install build-Linux-pld/eximon.bin	$RPM_BUILD_ROOT/usr/X11R6/bin
install build-Linux-pld/eximon		$RPM_BUILD_ROOT/usr/X11R6/bin
install build-Linux-pld/exim_dumpdb	$RPM_BUILD_ROOT%{_bindir}
install build-Linux-pld/exicyclog	$RPM_BUILD_ROOT%{_bindir}
install build-Linux-pld/exim_lock	$RPM_BUILD_ROOT%{_bindir}
install build-Linux-pld/exinext		$RPM_BUILD_ROOT%{_bindir}
install build-Linux-pld/exiwhat		$RPM_BUILD_ROOT%{_bindir}
install util/exigrep			$RPM_BUILD_ROOT%{_bindir}
install util/eximstats			$RPM_BUILD_ROOT%{_bindir}
install util/exiqsumm			$RPM_BUILD_ROOT%{_bindir} 
install util/unknownuser.sh		$RPM_BUILD_ROOT%{_bindir}
install util/transport-filter.pl	$RPM_BUILD_ROOT%{_bindir}
install %{SOURCE5}			.
install %{SOURCE11}			$RPM_BUILD_ROOT%{_bindir}
install %{SOURCE3}			$RPM_BUILD_ROOT/etc/cron.daily/
install %{SOURCE13}			$RPM_BUILD_ROOT/etc/sysconfig/%{name}
install %{SOURCE2}			$RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install	%{SOURCE12}			$RPM_BUILD_ROOT/etc/logrotate.d/%{name}
install %{SOURCE10}			$RPM_BUILD_ROOT%{_sysconfdir}/mail/
install %{SOURCE4}			$RPM_BUILD_ROOT%{_mandir}/man8/
install %{SOURCE9}			$RPM_BUILD_ROOT%{_sysconfdir}/mail/aliases
install	*.info				$RPM_BUILD_ROOT%{_infodir}/

ln -s %{_bindir}/exim $RPM_BUILD_ROOT%{_sbindir}/sendmail
ln -s %{_bindir}/exim $RPM_BUILD_ROOT%{_libdir}/sendmail
ln -s %{_bindir}/exim $RPM_BUILD_ROOT%{_sbindir}/mailq
ln -s %{_bindir}/exim $RPM_BUILD_ROOT%{_sbindir}/rsmtp
ln -s %{_bindir}/exim $RPM_BUILD_ROOT%{_sbindir}/rmail
ln -s %{_bindir}/exim $RPM_BUILD_ROOT%{_sbindir}/runq

install %{SOURCE6} $RPM_BUILD_ROOT%{_applnkdir}/System

touch $RPM_BUILD_ROOT%{_var}/log/exim/{main,reject,panic,process}.log
strip $RPM_BUILD_ROOT%{_bindir}/* 2> /dev/null|| :

gzip -9nf $RPM_BUILD_ROOT{%{_mandir}/man*/*,%{_infodir}/*} \
	README* NOTICE LICENCE analyse-log-errors \
	doc/{ChangeLog,NewStuff,dbm.discuss.txt,filter.txt,oview.txt,spec.txt}

%pre
/usr/sbin/groupadd -g 79 -r -f exim
if [ -n "`id -u exim 2>/dev/null`" ]; then
	if [ "`id -u exim`" != "79" ]; then
		echo "Warning: user exim doesn't have uid=79. Corect this before installing Exim" 1>&2
		exit 1
	fi
else
	/usr/sbin/useradd -u 79 -r -d /var/spool/exim -s /bin/false -c "Exim pseudo user" -g exim exim 1>&2
	if [ -f /var/db/passwd.db ]; then
		/usr/bin/update-db 1>&2
	fi
fi
%post
umask 022
/sbin/chkconfig --add %{name}
if [ -r /var/run/exim*.pid ]; then
	/etc/rc.d/init.d/%{name} restart >&2
else
	echo "Run \"/etc/rc.d/init.d/%{name} start\" to start exim daemon."
fi

if [ ! -f /etc/mail/mailname ]; then
	rm -f /etc/mail/mailname && hostname -f > /etc/mail/mailname
	chmod 644 /etc/mail/mailname
fi
newaliases
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

# Add/modify MAIL variable via pam_env.
mv -f %{_sysconfdir}/security/pam_env.conf{,.tmp}
awk '$1 != "MAIL" { print $0; }; END { print "MAIL\t\tDEFAULT=${HOME}/Mail/Mailbox"; }' \
	< %{_sysconfdir}/security/pam_env.conf.tmp \
	> %{_sysconfdir}/security/pam_env.conf
rm -f %{_sysconfdir}/security/pam_env.conf.tmp

%preun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del %{name}
	/etc/rc.d/init.d/%{name} stop >&2
fi

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
if [ "$1" = "0" ]; then
	/usr/sbin/userdel exim
	/usr/sbin/groupdel exim
	
	mv -f %{_sysconfdir}/security/pam_env.conf{,.tmp}
	awk '$1 != "MAIL" { print $0; }' \
		< %{_sysconfdir}/security/pam_env.conf.tmp \
		> %{_sysconfdir}/security/pam_env.conf
	rm -f %{_sysconfdir}/security/pam_env.conf.tmp
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* NOTICE* LICENCE* analyse-log-errors*
%doc doc/{ChangeLog,NewStuff,dbm.discuss.txt,filter.txt,oview.txt,spec.txt}.gz
%doc doc/{FAQ.txt,config.samples.tar}.gz
%attr( 644,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/mail/exim.conf
%attr( 644,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/mail/aliases
%attr( 644,root,root) %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/exim
%attr( 644,root,root) /etc/logrotate.d/exim
%attr( 754,root,root) /etc/rc.d/init.d/exim
%attr(4755,root,root) %{_bindir}/exim
%attr( 775,root,mail) %dir %{_var}/mail
%attr( 700,exim,root) %dir %{_var}/spool/exim
%attr( 750,exim,exim) %dir %{_var}/spool/exim/db
%attr( 700,exim,root) %dir %{_var}/spool/exim/input
%attr( 750,exim,root) %dir %{_var}/spool/exim/msglog
%attr( 755,root,root) %{_bindir}/exim_*
%attr( 755,root,root) %{_bindir}/exinext
%attr( 755,root,root) %{_bindir}/exiwhat
%attr( 755,root,root) %{_bindir}/exicyclog
%attr( 755,root,root) %{_bindir}/exigrep
%attr( 755,root,root) %{_bindir}/eximstats
%attr( 755,root,root) %{_bindir}/exiqsumm
%attr( 755,root,root) %{_bindir}/unknownuser.sh
%attr( 755,root,root) %{_bindir}/transport-filter.pl
%attr( 755,root,root) %{_bindir}/newaliases
%attr( 755,root,root) %{_sbindir}/*
%attr( 755,root,root) %{_libdir}/*
%attr( 754,root,root) /etc/cron.daily/exim.cron.db
%attr( 750,exim,root) %dir %{_var}/log/exim
%attr( 640,exim,root) %ghost %{_var}/log/exim/*
%{_infodir}/*
%{_mandir}/man8/*

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/*
%{_applnkdir}/System/*
