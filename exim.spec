Summary:	University of Cambridge Mail Transfer Agent 
Name:		exim
Version:	2.12
Release:	10
Copyright:	GPL
Group:		Daemons
Source0:	ftp://ftp.cus.cam.ac.uk/pub/software/programs/exim/%{name}-%version}.tar.gz
Source1:	ftp://ftp.cus.cam.ac.uk/pub/software/programs/exim/exim-texinfo-2.10.tar.gz
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
Source12:	exim.lorrotate
Provides:	smtpdaemon
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Smail like Mail Transfer Agent with single configuration file. Features:
flexible retry algorithms, header & envelope rewriting, multiple deliveries
down single connection or multiple deliveries in parallel, regular
expressions in configuration parameters, file lookups, supports sender
and/or reciever verification, selective relaying, supports virtual domains,
built-in mail filtering and can be configured to drop root privilleges when
possible.

%package X11
Summary:	X windows based Exim administration tool
Group:		X11/Utilities

%description X11
X windows based monitor & administration utility for the Exim Mail Transfer
Agent.

%prep
%setup -T -b 0
%setup -T -D -a 1
mkdir -p Local
cp $RPM_SOURCE_DIR/EDITME Local/Makefile
cp $RPM_SOURCE_DIR/Makefile-Linux Local/
cp $RPM_SOURCE_DIR/eximon.conf Local/

%build
make "CFLAGS=$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{cron.{daily,weekly},logrotate.d,rc.d/init.d,sysconfig} \
	$RPM_BUILD_ROOT/usr/{bin,lib,man/man8,sbin}

install -m4755 -g root -o root build-Linux-i386/exim $RPM_BUILD_ROOT%{_bindir}
install build-Linux-i386/exim_fixdb $RPM_BUILD_ROOT%{_bindir}
install build-Linux-i386/exim_tidydb $RPM_BUILD_ROOT%{_bindir}
install build-Linux-i386/exim_dbmbuild $RPM_BUILD_ROOT%{_bindir}
install build-Linux-i386/eximon.bin $RPM_BUILD_ROOT%{_bindir}
install build-Linux-i386/eximon $RPM_BUILD_ROOT%{_bindir}
install build-Linux-i386/exim_dumpdb $RPM_BUILD_ROOT%{_bindir}
install build-Linux-i386/exicyclog $RPM_BUILD_ROOT%{_bindir}
install build-Linux-i386/exim_lock $RPM_BUILD_ROOT%{_bindir}
install build-Linux-i386/exinext $RPM_BUILD_ROOT%{_bindir}
install build-Linux-i386/exiwhat $RPM_BUILD_ROOT%{_bindir}
install util/exigrep $RPM_BUILD_ROOT%{_bindir}
install util/eximstats $RPM_BUILD_ROOT%{_bindir}
install util/exiqsumm $RPM_BUILD_ROOT%{_bindir} 
install util/unknownuser.sh $RPM_BUILD_ROOT%{_bindir}
install util/transport-filter.pl $RPM_BUILD_ROOT%{_bindir}
install $RPM_SOURCE_DIR/analyse-log-errors $RPM_BUILD_ROOT%{_bindir}
install $RPM_SOURCE_DIR/one-line-queuelist $RPM_BUILD_ROOT%{_bindir}
install $RPM_SOURCE_DIR/newaliases $RPM_BUILD_ROOT%{_bindir}
cp -f $RPM_SOURCE_DIR/exim.sc $RPM_BUILD_ROOT/etc/sysconfig/exim
cp -f $RPM_SOURCE_DIR/exim.lr $RPM_BUILD_ROOT/etc/logrotate.d/exim
install $RPM_SOURCE_DIR/exim.conf $RPM_BUILD_ROOT/etc

ln -s %{_bindir}/exim $RPM_BUILD_ROOT%{_sbindir}/sendmail
ln -s %{_bindir}/exim $RPM_BUILD_ROOT%{_libdir}/sendmail
ln -s %{_bindir}/exim $RPM_BUILD_ROOT%{_sbindir}/mailq
ln -s %{_bindir}/exim $RPM_BUILD_ROOT%{_sbindir}/rsmtp
ln -s %{_bindir}/exim $RPM_BUILD_ROOT%{_sbindir}/rmail
ln -s %{_bindir}/exim $RPM_BUILD_ROOT%{_sbindir}/runq

install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/exim
install  $RPM_BUILD_ROOT/etc/cron.daily
cp -a $RPM_SOURCE_DIR/exim.cron.log $RPM_BUILD_ROOT/etc/cron.weekly

install $RPM_SOURCE_DIR/exim.8 $RPM_BUILD_ROOT%{_mandir}/man8
install $RPM_SOURCE_DIR/aliases $RPM_BUILD_ROOT/etc/aliases

strip $RPM_BUILD_ROOT/usr/{bin,sbin}/*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/*

%post
/sbin/chkconfig --add exim
if test -r /var/run/exim.pid; then
	/etc/rc.d/init.d/exim stop >&2
	/etc/rc.d/init.d/exim start >&2
else
	echo "Run \"/etc/rc.d/init.d/exim start\" to start exim daemon."
fi

%preun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del exim
	/etc/rc.d/init.d/exim stop >&2
fi


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* NOTICE LICENCE 
%config /etc/exim.conf
%config /etc/aliases
%attr(640,root,root) %config(noreplace) /etc/sysconfig/exim
%config /etc/logrotate.d/exim
%attr(754,root,root) /etc/rc.d/init.d/exim
%{_bindir}/exim
%{_bindir}/exim_dumpdb
%{_bindir}/exim_fixdb
%{_bindir}/exim_tidydb
%{_bindir}/exinext
%{_bindir}/exiwhat
%{_bindir}/exim_dbmbuild
%{_bindir}/exicyclog
%{_bindir}/exigrep
%{_bindir}/eximstats
%{_bindir}/exiqsumm
%{_bindir}/unknownuser.sh
%{_bindir}/transport-filter.pl
%{_mandir}/man8/*

%{_sbindir}/sendmail
%{_sbindir}/mailq
%{_sbindir}/rsmtp
%{_sbindir}/runq
%{_sbindir}/rmail
/etc/cron.daily/exim.cron.db
/etc/cron.weekly/exim.cron.log
%{_bindir}/newaliases

%files X11
%{_bindir}/eximon
%{_bindir}/eximon.bin

%changelog
* Mon May  3 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.12-10]
- added %post{un} sections with automated restart/stop exim on
  upgrade/uninstall,
- removed %config from binaries,
- removed LICENCE from %doc (exim is GPL),
- added %clean section,
- removed ps, html and pdf documentation (can be generated from info).

* Thu Mar 4 1999 Florian Wallner <wallner@speed-link.de>
 - Build package of version 2.12
 - uses logrotate now, though exicyclog still gets installed.
 - all binaries and scripts reside in %{_bindir}
 - config file is now /etc/exim.conf
 - added Procmail Transport and Director to the sample exim.conf.
 - added 'newaliases' and modified the alias director to do a dbm lookup.
 - I did all this to seamlessly replace Sendmail on a RH installation. 

* Wed Dec 21 1998 Arkadi E. Shislov <arkadi@kvin.lv>
  - Build package with changes provided by Andrew Inggs <aminggs@leviathan.cs.sun.ac.za>

* Fri Nov 20 1998 Arkadi E. Shislov <arkadi@kvin.lv>
  - Build package based on 2.05 offical release (glibc).

* Fri Aug 21 1998 Arkadi E. Shislov <arkadi@kvin.lv>
  - Build package based on 2.02 offical release (glibc).

* Sat Apr 11 1998 Hans Grobler <grobh@sun.ac.za>
  - Build package based on 1.90 offical release (glibc).

* Sun Dec 22 1997 Hans Grobler <grobh@sun.ac.za>
  - Build package based on 1.82 offical release (glibc).

* Fri Dec 11 1997 Hans Grobler <grobh@sun.ac.za>
  - Build package based on 1.81 offical release (glibc).

* Sat Oct 11 1997 Hans Grobler <grobh@nolian.ee.sun.ac.za>
  - Added signal handler patch.
  - Build package based on 1.73 offical release (glibc).

* Wed Oct 7 1997 Hans Grobler <grobh@nolian.ee.sun.ac.za>
  - Build package based on 1.73 offical release.

* Tue Sep 15 1997 Hans Grobler <grobh@nolian.ee.sun.ac.za>
  - Build package based on 1.71 offical release.
  - Add latest documentation.

* Sun Aug 10 1997 Hans Grobler <grobh@nolian.ee.sun.ac.za>
  - Added new default configuration file.
  - Add smail compatible links (runq/rmail/rsmtp).
  - Intall the exiqsumm script.

* Sat Aug  2 1997 Hans Grobler <grobh@nolian.ee.sun.ac.za>
  - Build package based on 1.653 test release.
