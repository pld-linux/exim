#
# Conditional build:
%bcond_without	pgsql	# without PostgreSQL support
%bcond_without	mysql	# without MySQL support
%bcond_without	sqlite	# without sqlite
%bcond_without	whoson	# without whoson support
%bcond_without	sasl	# without SASL
%bcond_without	ldap	# without LDAP support
%bcond_without	spf	# without spf support
%bcond_without	srs	# without srs support
%bcond_without	dynamic # dynamic modules
%bcond_without	hiredis # without redis
%bcond_without	ocsp	# without experimental OCSP
%bcond_with	dsn	# DSN

Summary:	University of Cambridge Mail Transfer Agent
Summary(pl.UTF-8):	Agent Transferu Poczty Uniwersytetu w Cambridge
Summary(pt_BR.UTF-8):	Servidor de correio eletrônico exim
Name:		exim
Version:	4.82
Release:	3
Epoch:		2
License:	GPL
Group:		Networking/Daemons/SMTP
Source0:	ftp://ftp.exim.org/pub/exim/exim4/%{name}-%{version}.tar.bz2
# Source0-md5:	feb933baa4db773c2ef76b794c60b647
Source1:	ftp://ftp.exim.org/pub/exim/exim4/%{name}-html-%{version}.tar.bz2
# Source1-md5:	072326f172ddbda684ba5cc8bc85e0aa
Source2:	%{name}.init
Source3:	%{name}.cron.db
Source4:	%{name}4.conf
Source5:	analyse-log-errors
Source6:	%{name}on.desktop
# 20021016: http://www.logic.univie.ac.at/~ametzler/debian/exim4manpages/
Source7:	%{name}4-man-021016.tar.bz2
# Source7-md5:	b552704ebf853a401946038a2b7e8e98
Source9:	%{name}.aliases
Source10:	newaliases
Source11:	%{name}.logrotate
Source12:	%{name}.sysconfig

Source14:	ftp://ftp.exim.org/pub/exim/exim4/old/config.samples.tar.bz2
# Source14-md5:	4b93321938a800caa6127c48ad60a42b
Source15:	%{name}4-smtp.pamd
Source16:	%{name}on.png
Patch0:		%{name}4-EDITME.patch
Patch1:		%{name}4-monitor-EDITME.patch
Patch2:		%{name}4-cflags.patch
Patch3:		exim-defs.patch
Patch4:		%{name}4-Makefile-Default.patch
# http://marc.merlins.org/linux/exim/files/sa-exim-cvs/localscan_dlopen_exim_4.20_or_better.patch
Patch5:		localscan_dlopen_%{name}_4.20_or_better.patch

# http://sourceforge.net/projects/eximdsn/
Patch7:		%{name}_463_dsn_1_3.patch
Patch8:		%{name}-spam-timeout.patch
Patch9:		exim-bug-659.patch
Patch10:	%{name}-force-sigalrm.patch
URL:		http://www.exim.org/
%{?with_sasl:BuildRequires:	cyrus-sasl-devel >= 2.1.0}
BuildRequires:	db-devel
%{?with_hiredis:BuildRequires:	hiredis-devel}
%{?with_spf:BuildRequires:	libspf2-devel >= 1.2.5-2}
%{?with_srs:BuildRequires:	libsrs_alt-devel >= 1.0}
%{?with_mysql:BuildRequires:	mysql-devel}
%{?with_ldap:BuildRequires:	openldap-devel >= 2.3.0}
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pam-devel
BuildRequires:	pcre-devel
BuildRequires:	perl-devel >= 1:5.6.0
%{?with_pgsql:BuildRequires:	postgresql-devel}
BuildRequires:	readline-devel
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpmbuild(macros) >= 1.268
%{?with_sqlite:BuildRequires:	sqlite3-devel}
%{?with_whoson:BuildRequires:	whoson-devel}
%if "%{pld_release}" != "ac"
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXaw-devel
%else
BuildRequires:	XFree86-devel
%endif
Requires(post):	/bin/hostname
Requires(post):	fileutils
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires:	findutils
Requires:	pam >= 0.79.0
Requires:	rc-scripts
Requires:	which
Provides:	group(exim)
Provides:	smtpdaemon
Provides:	user(exim)
Obsoletes:	smtpdaemon
Conflicts:	logrotate < 3.8.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Smail like Mail Transfer Agent with single configuration file.
Features: flexible retry algorithms, header & envelope rewriting,
multiple deliveries down single connection or multiple deliveries in
parallel, regular expressions in configuration parameters, file
lookups, supports sender and/or reciever verification, selective
relaying, supports virtual domains, built-in mail filtering and can be
configured to drop root privilleges when possible.

%description -l pl.UTF-8
Agent transferu poczty (MTA) z pojedynczym plikiem konfiguracyjnym.
Jego zalety: świetne algorytmy, możliwość przepisywania nagłówków &
koperty, wielokrotne dostarczanie poczty podczas jednego połączenia
lub równoległe dostarczanie poczty, wyrażenia regularne w parametrach
konfiguracyjnych, weryfikacja nadawcy i/lub odbiorcy, selektywne
relayowanie, wsparcie dla wirtualnych domen, wbudowany system filtrów,
możliwość odrzucania praw roota kiedy jest to możliwe.

%description -l pt_BR.UTF-8
O exim é um agente de transporte de correio eletrônico (MTA),
desenvolvido na Universidade de Cambridge para uso em sistemas Unix
conectados a Internet. Similar em estilo ao smail 3, suas facilidades
são mais extensivas e em particular ele tem opções para verificação do
remetente e destinatário, para recusar mensagens de máquinas, redes ou
remetentes específicos.

%package X11
Summary:	X11 based Exim administration tool
Summary(pl.UTF-8):	Narzędzia administracyjne exima dla X11
Summary(pt_BR.UTF-8):	Monitor X11 para o exim
Group:		X11/Applications

%description X11
X11 based monitor & administration utility for the Exim Mail Transfer
Agent.

%description X11 -l pl.UTF-8
Bazujące na X11 narzędzia dla Exima - monitor i program
administracyjny.

%description X11 -l pt_BR.UTF-8
O monitor exim é um suplemento opcional ao pacote exim. Ele mostra
informações sobre o processamento do exim em uma janela X11. O
administrador pode executar uma série de ações de controle a partir
desta interface.

%package devel
Summary:	Header files for Exim
Summary(pl.UTF-8):	Pliki nagłówkowe dla Exima
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for Exim.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla Exima.

%global	dynamic_type	yes
%{?with_dynamic:%global dynamic_type 2}

%prep
%setup -q -a1 -a7
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%{?with_dsn:%patch7 -p1}
%patch8 -p1
%patch9 -p2
%patch10 -p1

install %{SOURCE14} doc/config.samples.tar.bz2

install -d Local
cat << 'EOF' >> Local/Makefile-Linux
CC=%{__cc}
CUSTOM_CFLAGS=%{rpmcppflags} %{rpmcflags}
CFLAGS_DYNAMIC=-shared -rdynamic -fPIC %{rpmldflags}
LOOKUP_CDB=yes
XLFLAGS=-L%{_prefix}/X11R6/%{_lib}
X11_LD_LIB=%{_prefix}/X11R6/%{_lib}
%{?with_dynamic:LOOKUP_MODULE_DIR=%{_libdir}/%{name}/modules}
SUPPORT_DSN=yes
EXPERIMENTAL_DCC=yes
EXPERIMENTAL_PRDR=yes
EXPERIMENTAL_TPDA=yes
%{?with_ocsp:EXPERIMENTAL_OCSP=yes}
%if %{with spf}
EXPERIMENTAL_SPF=yes
LOOKUP_LIBS+=-lspf2
%endif
%if %{with srs}
EXPERIMENTAL_SRS=yes
LOOKUP_LIBS+=-lsrs_alt
%endif
%if %{with hiredis}
EXPERIMENTAL_REDIS=yes
LOOKUP_LIBS+=-lhiredis
%endif
%if %{with mysql}
LOOKUP_MYSQL=%{dynamic_type}
# for dynamic
LOOKUP_MYSQL_INCLUDE=-I%{_includedir}/mysql
LOOKUP_MYSQL_LIBS=-lmysqlclient
# for static
LOOKUP_INCLUDE+=-I%{_includedir}/mysql
LOOKUP_LIBS+=-lmysqlclient
%endif
%if %{with pgsql}
LOOKUP_PGSQL=%{dynamic_type}
# for dynamic
LOOKUP_PGSQL_INCLUDE=-I%{_includedir}/pgsql
LOOKUP_PGSQL_LIBS=-lpq
# for static
LOOKUP_INCLUDE+=-I%{_includedir}/pgsql
LOOKUP_LIBS+=-lpq
%endif
%if %{with sqlite}
LOOKUP_SQLITE=%{dynamic_type}
# for dynamic
LOOKUP_SQLITE_LIBS=-lsqlite3
# for static
LOOKUP_LIBS+=-lsqlite3
%endif
%if %{with whoson}
LOOKUP_WHOSON=%{dynamic_type}
# for dynamic
LOOKUP_WHOSON_LIBS=-lwhoson
# for static
LOOKUP_LIBS+=-lwhoson
%endif
%if %{with sasl}
AUTH_CYRUS_SASL=yes
LOOKUP_LIBS+=-lsasl2
%endif
%if %{with ldap}
LOOKUP_LDAP=%{dynamic_type}
LDAP_LIB_TYPE=OPENLDAP2
# for dynamic
LOOKUP_LDAP_LIBS=-lldap -llber
# for static
LOOKUP_LIBS+=-lldap -llber
%endif
EOF

# have to be after Local/Makefile-Linux creation
cp -f src/EDITME Local/Makefile
cp -f exim_monitor/EDITME Local/eximon.conf

%build
%{__make} -e -j1 \
	FULLECHO=''

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/mail
install -d $RPM_BUILD_ROOT/etc/{cron.daily,logrotate.d,rc.d/init.d,sysconfig,pam.d,security}
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/man8,/usr/lib}
install -d $RPM_BUILD_ROOT%{_var}/{spool/exim/{db,input,msglog},log/{archive,}/exim,mail}
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}
install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/modules

install build-Linux-*/exim{,_fixdb,_tidydb,_dbmbuild,on.bin,_dumpdb,_lock} \
	build-Linux-*/exi{cyclog,next,what} %{SOURCE10} \
	build-Linux-*/{exigrep,exiqgrep,exipick,eximstats,exiqsumm,convert4r4} \
	util/unknownuser.sh \
	$RPM_BUILD_ROOT%{_bindir}
install build-Linux-*/eximon.bin $RPM_BUILD_ROOT%{_bindir}
install build-Linux-*/eximon $RPM_BUILD_ROOT%{_bindir}
%{?with_dynamic:install build-Linux-*/*/*.so $RPM_BUILD_ROOT%{_libdir}/%{name}/modules}

install %{SOURCE5} .
install %{SOURCE3} $RPM_BUILD_ROOT/etc/cron.daily
install %{SOURCE12} $RPM_BUILD_ROOT/etc/sysconfig/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install	%{SOURCE11} $RPM_BUILD_ROOT/etc/logrotate.d/%{name}
install %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/mail/exim.conf
install {doc,man}/*.8 $RPM_BUILD_ROOT%{_mandir}/man8
install %{SOURCE9} $RPM_BUILD_ROOT%{_sysconfdir}/mail/aliases
install %{SOURCE15} $RPM_BUILD_ROOT/etc/pam.d/smtp

ln -sf %{_bindir}/exim $RPM_BUILD_ROOT%{_sbindir}/sendmail
ln -sf %{_bindir}/exim $RPM_BUILD_ROOT/usr/lib/sendmail
ln -sf %{_bindir}/exim $RPM_BUILD_ROOT%{_sbindir}/mailq
ln -sf %{_bindir}/exim $RPM_BUILD_ROOT%{_sbindir}/rsmtp
ln -sf %{_bindir}/exim $RPM_BUILD_ROOT%{_sbindir}/rmail
ln -sf %{_bindir}/exim $RPM_BUILD_ROOT%{_sbindir}/runq

install %{SOURCE6} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE16} $RPM_BUILD_ROOT%{_pixmapsdir}

install -d $RPM_BUILD_ROOT%{_includedir}/%{name}
install src/{local_scan,store,mytypes}.h $RPM_BUILD_ROOT%{_includedir}/%{name}
install build-Linux-*/config.h $RPM_BUILD_ROOT%{_includedir}/%{name}

touch $RPM_BUILD_ROOT%{_var}/log/exim/{main,reject,panic,process}.log

touch $RPM_BUILD_ROOT/etc/security/blacklist.smtp

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 79 exim
%useradd -u 79 -d /var/spool/exim -s /bin/false -c "Exim pseudo user" -g exim exim

%post
umask 022
/sbin/chkconfig --add %{name}
%service %{name} restart "exim daemon"

if [ ! -f /etc/mail/mailname ]; then
	rm -f /etc/mail/mailname && hostname -f > /etc/mail/mailname
fi
newaliases

%preun
if [ "$1" = "0" ]; then
	%service exim stop
	/sbin/chkconfig --del %{name}
fi

%postun
if [ "$1" = "0" ]; then
	%userremove exim
	%groupremove exim
fi

%files
%defattr(644,root,root,755)
%doc README* NOTICE LICENCE analyse-log-errors doc/{ChangeLog,NewStuff,dbm.discuss.txt,filter.txt,spec.txt,Exim*.upgrade,OptionLists.txt,experimental-spec.txt} build-Linux-*/transport-filter.pl
%doc exim-html-*/doc/html
%dir %{_sysconfdir}/mail
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mail/exim.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mail/aliases
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/exim
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/exim
%attr(754,root,root) /etc/rc.d/init.d/exim
%attr(4755,root,root) %{_bindir}/exim
%attr(770,root,exim) %dir %{_var}/spool/exim
%attr(750,exim,exim) %dir %{_var}/spool/exim/db
%attr(700,exim,root) %dir %{_var}/spool/exim/input
%attr(750,exim,root) %dir %{_var}/spool/exim/msglog
%attr(755,root,root) %{_bindir}/exim_*
%attr(755,root,root) %{_bindir}/exinext
%attr(755,root,root) %{_bindir}/exiwhat
%attr(755,root,root) %{_bindir}/exicyclog
%attr(755,root,root) %{_bindir}/exigrep
%attr(755,root,root) %{_bindir}/exipick
%attr(755,root,root) %{_bindir}/exiqgrep
%attr(755,root,root) %{_bindir}/eximstats
%attr(755,root,root) %{_bindir}/exiqsumm
%attr(755,root,root) %{_bindir}/unknownuser.sh
%attr(755,root,root) %{_bindir}/newaliases
%attr(755,root,root) %{_bindir}/convert4r4
%attr(755,root,root) %{_sbindir}/mailq
%attr(755,root,root) %{_sbindir}/rmail
%attr(755,root,root) %{_sbindir}/rsmtp
%attr(755,root,root) %{_sbindir}/runq
%attr(755,root,root) %{_sbindir}/sendmail
%attr(755,root,root) /usr/lib/sendmail
%attr(754,root,root) /etc/cron.daily/exim.cron.db
%attr(750,exim,root) %dir %{_var}/log/exim
%attr(750,exim,root) %dir %{_var}/log/archive/exim
%attr(640,exim,root) %ghost %{_var}/log/exim/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/smtp
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.smtp
%if %{with dynamic}
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/modules
%{?with_mysql:%attr(755,root,root) %{_libdir}/%{name}/modules/mysql.so}
%{?with_pgsql:%attr(755,root,root) %{_libdir}/%{name}/modules/pgsql.so}
%{?with_sqlite:%attr(755,root,root) %{_libdir}/%{name}/modules/sqlite.so}
%{?with_whoson:%attr(755,root,root) %{_libdir}/%{name}/modules/whoson.so}
%endif
%{_mandir}/man8/*

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/eximon
%attr(755,root,root) %{_bindir}/eximon.bin
%{_desktopdir}/eximon.desktop
%{_pixmapsdir}/eximon.png

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
