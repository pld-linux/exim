Summary:	University of Cambridge Mail Transfer Agent 
Summary(pl):    Agent Transferu Poczty Uniwersytetu w Cambridge
Name:		exim
Version:	3.02
Release:	1
Copyright:	GPL
Group:		Daemons
Group(pl):	Serwery
URL:		http://www.exim.org/
Source0:	ftp://ftp.cus.cam.ac.uk/pub/software/programs/exim/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.cus.cam.ac.uk/pub/software/programs/exim/%{name}-texinfo-3.00.tar.gz
Source2:	exim.init
Source3:	exim.cron.db
Source4:	exim.8
Source5:	analyse-log-errors
Source6:	one-line-queuelist
Source6:	EDITME
Source7:	Makefile-Linux
Source8:	eximon.conf
Source9:	exim.aliases
Source10:	exim.conf
Source11:	newaliases
Source12:	exim.logrotate
Source13:	exim.sysconfig
Provides:	smtpdaemon
Conflicts:	smtpdaemon
BuildRequires:	openldap-devel
BuildRequires:	texinfo
BuildRequires:	perl
Requires:	openldap
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Smail like Mail Transfer Agent with single configuration file. Features:
flexible retry algorithms, header & envelope rewriting, multiple deliveries
down single connection or multiple deliveries in parallel, regular
expressions in configuration parameters, file lookups, supports sender
and/or reciever verification, selective relaying, supports virtual domains,
built-in mail filtering and can be configured to drop root privilleges when
possible.

%description -l pl
Agent transferu poczty (MTA) z pojedynczym plikiem konfiguracyjnym.
Jego zalety to: �wietne algorytmy, mo�liwo�� przepisywania nag��wk�w & koperty,
wielokrotne dostarczanie poczty poprzez podczas jednego po��czenia lub r�wnoleg�e
dostarczanie poczty, regularne wyra�enia w parametrach konfiguracyjnych, weryfikacja
nadawcy i/lub odbiorcy, selektywne relayowanie, wsparcie dla wirtualnych domen,
wbudowany system filtr�w, mo�liwo�� odrzucania praw roota kiedy jest to mo�liwe.

%package X11
Summary:	X windows based Exim administration tool
Group:		X11/Utilities

%description X11
X windows based monitor & administration utility for the Exim Mail Transfer
Agent.

%description -l pl X11
Bazuj�ce na X Windows narz�dzia dla Exima - monitor && narz�dzie administracyjne.

%prep
%setup -q -T -b 0
%setup -q -T -D -a 1
install -d	Local
install		%{SOURCE6}	Local/Makefile
install		%{SOURCE7}	Local/
install		%{SOURCE8}	Local/

%build
makeinfo	--no-split --output exim_overview.info	exim-texinfo-*/doc/oview.texinfo
makeinfo	--no-split --output exim.info		exim-texinfo-*/doc/spec.texinfo
makeinfo	--no-split --output exim_filter.info	exim-texinfo-*/doc/filter.texinfo
make            "CFLAGS=$RPM_OPT_FLAGS"

%install
rm -rf		$RPM_BUILD_ROOT
install -d	$RPM_BUILD_ROOT/etc/{cron.{daily,weekly},logrotate.d,rc.d/init.d,sysconfig,mail}
install -d	$RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/man8,%{_libdir}}
install -d	$RPM_BUILD_ROOT%{_var}/{spool/exim/{db,input,msglog},log/exim,mail}
install -d	$RPM_BUILD_ROOT%{_infodir}

install	build-Linux-i386/exim				$RPM_BUILD_ROOT%{_bindir}
install build-Linux-i386/exim_fixdb			$RPM_BUILD_ROOT%{_bindir}
install build-Linux-i386/exim_tidydb			$RPM_BUILD_ROOT%{_bindir}
install build-Linux-i386/exim_dbmbuild			$RPM_BUILD_ROOT%{_bindir}
install build-Linux-i386/eximon.bin			$RPM_BUILD_ROOT%{_bindir}
install build-Linux-i386/eximon				$RPM_BUILD_ROOT%{_bindir}
install build-Linux-i386/exim_dumpdb			$RPM_BUILD_ROOT%{_bindir}
install build-Linux-i386/exicyclog			$RPM_BUILD_ROOT%{_bindir}
install build-Linux-i386/exim_lock			$RPM_BUILD_ROOT%{_bindir}
install build-Linux-i386/exinext			$RPM_BUILD_ROOT%{_bindir}
install build-Linux-i386/exiwhat			$RPM_BUILD_ROOT%{_bindir}
install util/exigrep					$RPM_BUILD_ROOT%{_bindir}
install util/eximstats					$RPM_BUILD_ROOT%{_bindir}
install util/exiqsumm					$RPM_BUILD_ROOT%{_bindir} 
install util/unknownuser.sh				$RPM_BUILD_ROOT%{_bindir}
install util/transport-filter.pl			$RPM_BUILD_ROOT%{_bindir}
install %{SOURCE5}					.
install %{SOURCE6}					$RPM_BUILD_ROOT%{_bindir}
install %{SOURCE11}					$RPM_BUILD_ROOT%{_bindir}
install %{SOURCE3}					$RPM_BUILD_ROOT/etc/cron.daily/
install %{SOURCE13}					$RPM_BUILD_ROOT/etc/sysconfig/%{name}
install %{SOURCE2}                                      $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install	%{SOURCE12}					$RPM_BUILD_ROOT/etc/logrotate.d/%{name}
install %{SOURCE10}					$RPM_BUILD_ROOT/etc/mail/
install %{SOURCE4}                                      $RPM_BUILD_ROOT%{_mandir}/man8/
install %{SOURCE9}					$RPM_BUILD_ROOT/etc/mail/aliases
install	*.info						$RPM_BUILD_ROOT%{_infodir}/

ln -s	%{_bindir}/exim					$RPM_BUILD_ROOT%{_sbindir}/sendmail
ln -s	%{_bindir}/exim					$RPM_BUILD_ROOT%{_libdir}/sendmail
ln -s	%{_bindir}/exim					$RPM_BUILD_ROOT%{_sbindir}/mailq
ln -s	%{_bindir}/exim					$RPM_BUILD_ROOT%{_sbindir}/rsmtp
ln -s	%{_bindir}/exim					$RPM_BUILD_ROOT%{_sbindir}/rmail
ln -s	%{_bindir}/exim					$RPM_BUILD_ROOT%{_sbindir}/runq

touch		$RPM_BUILD_ROOT%{_var}/log/exim/{mainlog,rejectlog,paniclog,processlog}
strip		$RPM_BUILD_ROOT%{_bindir}/* 2> /dev/null|| :
gzip -9nf       $RPM_BUILD_ROOT%{_mandir}/man*/*	$RPM_BUILD_ROOT%{_infodir}/*

%pre
%{_sbindir}/groupadd -f -g 79 exim
%{_sbindir}/useradd -M -g exim -d /var/spool/exim/ -u 79 -s /bin/false exim 2> /dev/null

%postun
%{_sbindir}/userdel exim 2> /dev/null
%{_sbindir}/groupdel exim 2> /dev/null

%post
umask 022
/sbin/chkconfig --add %{name}
if [ -r /var/run/exim*.pid ]; then
	/etc/rc.d/init.d/%{name} stop >&2
	/etc/rc.d/init.d/%{name} start >&2
else
	echo "Run \"/etc/rc.d/init.d/%{name} start\" to start exim daemon."
fi

if [ ! -f /etc/mail/mailname ]; then
	rm -f /etc/mail/mailname && hostname -f > /etc/mail/mailname
	chmod 644 /etc/mail/mailname
fi
newaliases

/sbin/install-info --section="Exim" \
     --entry "* Overview: (exim_overview).   Overview of the Exim system" \
     %{_infodir}/exim_overview.info.gz /etc/info-dir
/sbin/install-info --section="Exim" \
     --entry "* User guide: (exim).          Exim manual" \
     %{_infodir}/exim.info.gz  /etc/info-dir
/sbin/install-info --section="Exim" \
     --entry "* Filtering: (exim_filter).    Filtering mail with Exim" \
     %{_infodir}/exim_filter.info.gz   /etc/info-dir

%preun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del %{name}
	/etc/rc.d/init.d/%{name} stop >&2
fi
/sbin/install-info --delete %{_infodir}/exim_overview.info	/etc/info-dir
/sbin/install-info --delete %{_infodir}/exim_filter.info	/etc/info-dir
/sbin/install-info --delete %{_infodir}/exim.info		/etc/info-dir



%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* NOTICE LICENCE analyse-log-errors exim-texinfo-*/doc/*
%attr( 644,root,root) %config(noreplace) %verify(not size mtime md5) /etc/mail/exim.conf
%attr( 644,root,root) %config(noreplace) %verify(not size mtime md5) /etc/mail/aliases
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
%attr( 644,root,root) %{_infodir}/*
%attr( 754,root,root) /etc/cron.daily/exim.cron.db
%attr( 750,exim,root) %dir %{_var}/log/exim
%attr( 644,exim,root) %ghost %{_var}/log/exim/mainlog
%attr( 644,exim,root) %ghost %{_var}/log/exim/rejectlog
%attr( 644,exim,root) %ghost %{_var}/log/exim/paniclog
%attr( 644,exim,root) %ghost %{_var}/log/exim/processlog
%{_mandir}/man8/*

%files X11
%attr( 755,root,root) %{_bindir}/eximon
%attr( 755,root,root) %{_bindir}/eximon.bin
