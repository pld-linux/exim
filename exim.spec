# Conditional build:
%bcond_without	pgsql	# without PostgreSQL support
%bcond_without	mysql	# without MySQL support
%bcond_without	whoson	# without whoson support
%bcond_without	ldap	# without LDAP support
%bcond_without	exiscan	# without exiscan support
%bcond_without	spf	# without spf support
%bcond_without	srs	# without srs support
%bcond_with	saexim	# with sa-exim support
#
%define		exiscan_version	4.41-24
%define		saexim_version 3.1
Summary:	University of Cambridge Mail Transfer Agent
Summary(pl):	Agent Transferu Poczty Uniwersytetu w Cambridge
Summary(pt_BR):	Servidor de correio eletrônico exim
Name:		exim
Version:	4.41
Release:	4
Epoch:		2
License:	GPL
Group:		Networking/Daemons
Source0:	ftp://ftp.csx.cam.ac.uk/pub/software/email/exim/exim4/%{name}-%{version}.tar.bz2
# Source0-md5:	769c8b03cdefcc98c9707dde965c96f1
Source1:	ftp://ftp.csx.cam.ac.uk/pub/software/email/exim/exim4/%{name}-texinfo-4.40.tar.bz2
# Source1-md5:	cc91bd804ee0f7fd70991e2e6b529033
Source2:	%{name}.init
Source3:	%{name}.cron.db
Source4:	%{name}4.conf
Source5:	analyse-log-errors
Source6:	%{name}on.desktop
# 20021016: http://www.logic.univie.ac.at/~ametzler/debian/exim4manpages/
Source7:	%{name}4-man-021016.tar.bz2
# Source7-md5:	b552704ebf853a401946038a2b7e8e98
Source8:	http://duncanthrax.net/exiscan-acl/exiscan-acl-%{exiscan_version}.patch.bz2
# Source8-md5:	13eaeb6c5def7cdf4c9cea6d82f85bd8
Source9:	%{name}.aliases
Source10:	newaliases
Source11:	%{name}.logrotate
Source12:	%{name}.sysconfig
Source13:	ftp://ftp.csx.cam.ac.uk/pub/software/email/exim/exim4/FAQ.txt.bz2
# Source13-md5:	8e188230dc95a0117cafd1fd804d2dd8
Source14:	ftp://ftp.csx.cam.ac.uk/pub/software/email/exim/exim4/config.samples.tar.bz2
# Source14-md5:	e760e86c8b23a07d10a91a3d2eaed7de
Source15:	%{name}4-smtp.pamd
Source16:	%{name}on.png
Source17:	http://marc.merlins.org/linux/exim/files/sa-exim-%{saexim_version}.tar.gz
# Source17-md5:	34892f195384c127f7c40c461a9ef421
Patch0:		%{name}4-EDITME.patch
Patch1:		%{name}4-monitor-EDITME.patch
Patch2:		%{name}4-texinfo.patch
Patch3:		%{name}4-use_system_pcre.patch
Patch4:		%{name}4-Makefile-Default.patch
Patch5:		%{name}4-exiscan-pld.patch
Patch6:		%{name}4-spf2.patch
URL:		http://www.exim.org/
%{?with_ldap:BuildRequires:	openldap-devel >= 2.0.0}
%{?with_spf:BuildRequires:	libspf2-devel}
%{?with_srs:BuildRequires:	libsrs_alt-devel}
%{?with_mysql:BuildRequires:	mysql-devel}
%{?with_pgsql:BuildRequires:	postgresql-devel}
%{?with_whoson:BuildRequires:	whoson-devel}
BuildRequires:	XFree86-devel
BuildRequires:	db-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pam-devel
BuildRequires:	pcre-devel
BuildRequires:	perl-devel >= 1:5.6.0
BuildRequires:	texinfo
PreReq:		rc-scripts
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(post):	fileutils
Requires(post,preun):	/sbin/chkconfig
Requires:	pam >= 0.77.3
Provides:	smtpdaemon
Obsoletes:	courier
Obsoletes:	masqmail
Obsoletes:	nullmailer
Obsoletes:	omta
Obsoletes:	postfix
Obsoletes:	qmail
Obsoletes:	qmail-client
Obsoletes:	sendmail
Obsoletes:	sendmail-cf
Obsoletes:	sendmail-doc
Obsoletes:	smail
Obsoletes:	smtpdaemon
Obsoletes:	ssmtp
Obsoletes:	zmailer
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

%description -l pt_BR
O exim é um agente de transporte de correio eletrônico (MTA),
desenvolvido na Universidade de Cambridge para uso em sistemas Unix
conectados a Internet. Similar em estilo ao smail 3, suas facilidades
são mais extensivas e em particular ele tem opções para verificação do
remetente e destinatário, para recusar mensagens de máquinas, redes ou
remetentes específicos.

%package X11
Summary:	X11 based Exim administration tool
Summary(pl):	Narzêdzia administracyjne exima dla X11
Summary(pt_BR):	Monitor X11 para o exim
Group:		X11/Applications

%description X11
X11 based monitor & administration utility for the Exim Mail Transfer
Agent.

%description X11 -l pl
Bazuj±ce na X11 narzêdzia dla Exima - monitor i program
administracyjny.

%description X11 -l pt_BR
O monitor exim é um suplemento opcional ao pacote exim. Ele mostra
informações sobre o processamento do exim em uma janela X11. O
administrador pode executar uma série de ações de controle a partir
desta interface.

%prep
%setup -q -a1 -a7
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1
%patch4 -p1
%patch5 -p0

%{?with_exiscan:test -f %{SOURCE8} || exit 1; bzip2 -d -c %{SOURCE8} | patch -p1 || exit 1}
%{?with_saexim:test -f %{SOURCE17} || exit 1; gzip -d -c %{SOURCE17} | tar -x || exit 1}

%patch6 -p0

install %{SOURCE13} doc/FAQ.txt.bz2
install %{SOURCE14} doc/config.samples.tar.bz2

install -d Local
cp -f src/EDITME Local/Makefile
cp -f exim_monitor/EDITME Local/eximon.conf

%build

%if %{with saexim}
    cd sa-exim-%{saexim_version}
    %{__make} -j1 sa-exim.h
    echo '#define SPAMASSASSIN_CONF "%{_sysconfdir}/mail/spamassassin/local.cf"' >> sa-exim.h
    cat sa-exim.c > ../src/local_scan.c
    cat sa-exim.h > ../src/sa-exim.h
    cd ..
%endif

%{__make} -j1 \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{?with_spf:-DSPF} %{?with_srs:-DSRS}" \
	LOOKUP_CDB=yes \
XLFLAGS=-L%{_prefix}/X11R6/%{_lib} \
X11_LD_LIB=%{_prefix}/X11R6/%{_lib} \
	%{?with_mysql:LOOKUP_MYSQL=yes} \
	%{?with_pgsql:LOOKUP_PGSQL=yes} \
	%{?with_whoson:LOOKUP_WHOSON=yes} \
	%{?with_ldap:LOOKUP_LDAP=yes LDAP_LIB_TYPE=OPENLDAP2} \
	LOOKUP_LIBS="%{?with_ldap:-lldap -llber} %{?with_mysql:-lmysqlclient} %{?with_pgsql:-lpq} %{?with_whoson:-lwhoson} %{?with_spf:-lspf2} %{?with_srs:-lsrs_alt}" \
	LOOKUP_INCLUDE="%{?with_mysql:-I%{_includedir}/mysql} %{?with_pgsql:-I%{_includedir}/pgsql}"

makeinfo --force exim-texinfo-*/doc/*.texinfo

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/mail
install -d $RPM_BUILD_ROOT/etc/{cron.{daily,weekly},logrotate.d,rc.d/init.d,sysconfig,pam.d}
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/man8,/usr/lib}
install -d $RPM_BUILD_ROOT%{_var}/{spool/exim/{db,input,msglog},log/{archiv,}/exim,mail}
install -d $RPM_BUILD_ROOT{%{_infodir},%{_prefix}/X11R6/bin,%{_desktopdir},%{_pixmapsdir}}

install build-Linux-*/exim{,_fixdb,_tidydb,_dbmbuild,on.bin,_dumpdb,_lock} \
	build-Linux-*/exi{cyclog,next,what} %{SOURCE10} \
	build-Linux-*/{exigrep,eximstats,exiqsumm,convert4r4} \
	util/unknownuser.sh \
	$RPM_BUILD_ROOT%{_bindir}
install build-Linux-*/eximon.bin $RPM_BUILD_ROOT%{_prefix}/X11R6/bin
install build-Linux-*/eximon $RPM_BUILD_ROOT%{_prefix}/X11R6/bin

install %{SOURCE5} .
install %{SOURCE3} $RPM_BUILD_ROOT/etc/cron.weekly/
install %{SOURCE12} $RPM_BUILD_ROOT/etc/sysconfig/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install	%{SOURCE11} $RPM_BUILD_ROOT/etc/logrotate.d/%{name}
install %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/mail/exim.conf
install {doc,man}/*.8 $RPM_BUILD_ROOT%{_mandir}/man8/
install %{SOURCE9} $RPM_BUILD_ROOT%{_sysconfdir}/mail/aliases
install	*.info* $RPM_BUILD_ROOT%{_infodir}/
install %{SOURCE15} $RPM_BUILD_ROOT/etc/pam.d/smtp

%{?with_saexim:install sa-exim-%{saexim_version}/sa-exim.conf $RPM_BUILD_ROOT/%{_sysconfdir}/mail/sa-exim.conf}

ln -sf %{_bindir}/exim $RPM_BUILD_ROOT%{_sbindir}/sendmail
ln -sf %{_bindir}/exim $RPM_BUILD_ROOT/usr/lib/sendmail
ln -sf %{_bindir}/exim $RPM_BUILD_ROOT%{_sbindir}/mailq
ln -sf %{_bindir}/exim $RPM_BUILD_ROOT%{_sbindir}/rsmtp
ln -sf %{_bindir}/exim $RPM_BUILD_ROOT%{_sbindir}/rmail
ln -sf %{_bindir}/exim $RPM_BUILD_ROOT%{_sbindir}/runq

install %{SOURCE6} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE16} $RPM_BUILD_ROOT%{_pixmapsdir}

touch $RPM_BUILD_ROOT%{_var}/log/exim/{main,reject,panic,process}.log

%clean
rm -rf $RPM_BUILD_ROOT

%pre
if [ -n "`/usr/bin/getgid exim`" ]; then
	if [ "`getgid exim`" != "79" ]; then
		echo "Warning: group exim haven't gid=79. Correct this before installing exim" 1>&2
		exit 1
	fi
else
	/usr/sbin/groupadd -g 79 -r -f exim
fi

if [ -n "`/bin/id -u exim 2>/dev/null`" ]; then
	if [ "`id -u exim`" != "79" ]; then
		echo "Warning: user exim doesn't have uid=79. Correct this before installing Exim" 1>&2
		exit 1
	fi
else
	/usr/sbin/useradd -u 79 -r -d /var/spool/exim -s /bin/false -c "Exim pseudo user" -g exim exim 1>&2
fi

%post
umask 022
/sbin/chkconfig --add %{name}
if [ -f /var/lock/subsys/exim ]; then
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

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/exim ]; then
		/etc/rc.d/init.d/exim stop >&2
	fi
	/sbin/chkconfig --del %{name}
fi

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
if [ "$1" = "0" ]; then
	/usr/sbin/userdel exim
	/usr/sbin/groupdel exim
fi

%triggerpostun -- exim  < 3.90
if [ -f /etc/mail/exim.conf ]; then
	umask 022
	mv /etc/mail/exim.conf /etc/mail/exim.conf.3
	/usr/bin/convert4r4 < /etc/mail/exim.conf.3 > /etc/mail/exim.conf
fi

%files
%defattr(644,root,root,755)
%doc README* NOTICE LICENCE analyse-log-errors doc/{ChangeLog,NewStuff,dbm.discuss.txt,filter.txt,spec.txt,Exim*.upgrade,OptionLists.txt%{?with_exiscan:,exiscan-*.txt}} build-Linux-*/transport-filter.pl
%attr( 644,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/mail/exim.conf
%{?with_saexim:%attr( 644,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/mail/sa-exim.conf}
%attr( 644,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/mail/aliases
%attr( 644,root,root) %config(noreplace) %verify(not size mtime md5) /etc/sysconfig/exim
%attr( 644,root,root) %config(noreplace) %verify(not size mtime md5) /etc/logrotate.d/exim
%attr( 754,root,root) /etc/rc.d/init.d/exim
%attr(4755,root,root) %{_bindir}/exim
%attr( 770,root,exim) %dir %{_var}/spool/exim
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
%attr( 755,root,root) %{_bindir}/newaliases
%attr( 755,root,root) %{_bindir}/convert4r4
%attr( 755,root,root) %{_sbindir}/*
%attr( 755,root,root) /usr/lib/sendmail
%attr( 754,root,root) /etc/cron.weekly/exim.cron.db
%attr( 750,exim,root) %dir %{_var}/log/exim
%attr( 750,exim,root) %dir %{_var}/log/archiv/exim
%attr( 640,exim,root) %ghost %{_var}/log/exim/*
%attr( 640,root,root) /etc/pam.d/smtp
%{_infodir}/*
%{_mandir}/man8/*

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/X11R6/bin/*
%{_desktopdir}/%{name}on.desktop
%{_pixmapsdir}/%{name}on.png
