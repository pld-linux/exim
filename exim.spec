Name: exim
Summary: University of Cambridge Mail Transfer Agent 
Version: 2.12
Release: 9
Copyright: GPL
Group: Daemons
Provides: smtpdaemon
Source0: ftp://ftp.cus.cam.ac.uk/pub/software/programs/exim/exim-2.12.tar.gz
Source1: ftp://ftp.cus.cam.ac.uk/pub/software/programs/exim/exim-texinfo-2.10.tar.gz
Source2: ftp://ftp.cus.cam.ac.uk/pub/software/programs/exim/exim-postscript-2.10.tar.gz
Source3: ftp://ftp.cus.cam.ac.uk/pub/software/programs/exim/exim-pdf-2.10.tar.gz
Source4: ftp://ftp.cus.cam.ac.uk/pub/software/programs/exim/exim-html-2.10.tar.gz
Source5: exim
Source6: exim.cron.db
Source8: exim.8
Source9: analyse-log-errors
Source10: one-line-queuelist
Source11: EDITME
Source12: Makefile-Linux
Source13: eximon.conf
Source14: aliases
Source15: exim.conf
Source16: newaliases
Source17: exim.lr

BuildRoot: /tmp/exim-root
Packager:  Florian Wallner <wallner@speed-link.de>

%changelog

* Thu Mar 4 1999 Florian Wallner <wallner@speed-link.de>

 - Build package of version 2.12
 - uses logrotate now, though exicyclog still gets installed.
 - all binaries and scripts reside in /usr/bin
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

%description
Smail like Mail Transfer Agent with single configuration file. Features:
flexible retry algorithms, header & envelope rewriting, multiple deliveries
down single connection or multiple deliveries in parallel, regular expressions
in configuration parameters, file lookups, supports sender and/or reciever
verification, selective relaying, supports virtual domains, built-in mail
filtering and can be configured to drop root privilleges when possible.

%package X11
Summary: X windows based Exim administration tool
Group: X11/Utilities
 
%description X11
X windows based monitor & administration utility for the Exim Mail Transfer
Agent.

%package doc
Summary: Documentation for Exim Mail Transfer Agent
Group: Documentation
 
%description doc
Documentation for the Exim Mail Transfer Agent

%prep
%setup -T -b 0
%setup -T -D -a 1
%setup -T -D -a 2
%setup -T -D -a 3
%setup -T -D -a 4
mkdir -p Local
cp $RPM_SOURCE_DIR/EDITME Local/Makefile
cp $RPM_SOURCE_DIR/Makefile-Linux Local/
cp $RPM_SOURCE_DIR/eximon.conf Local/

%build
rm -fr $RPM_BUILD_ROOT

make "CFLAGS=$RPM_OPT_FLAGS"

%install
umask 022
mkdir -p $RPM_BUILD_ROOT/etc
mkdir -p $RPM_BUILD_ROOT/usr
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/etc/sysconfig
mkdir -p $RPM_BUILD_ROOT/etc/logrotate.d

install -m4755 -g root -o root build-Linux-i386/exim $RPM_BUILD_ROOT/usr/bin
install -m755 -g root -o root build-Linux-i386/exim_fixdb $RPM_BUILD_ROOT/usr/bin
install -m755 -g root -o root build-Linux-i386/exim_tidydb $RPM_BUILD_ROOT/usr/bin
install -m755 -g root -o root build-Linux-i386/exim_dbmbuild $RPM_BUILD_ROOT/usr/bin
install -m755 -g root -o root build-Linux-i386/eximon.bin $RPM_BUILD_ROOT/usr/bin
install -m755 -g root -o root build-Linux-i386/eximon $RPM_BUILD_ROOT/usr/bin
install -m755 -g root -o root build-Linux-i386/exim_dumpdb $RPM_BUILD_ROOT/usr/bin
install -m755 -g root -o root build-Linux-i386/exicyclog $RPM_BUILD_ROOT/usr/bin
install -m755 -g root -o root build-Linux-i386/exim_lock $RPM_BUILD_ROOT/usr/bin
install -m755 -g root -o root build-Linux-i386/exinext $RPM_BUILD_ROOT/usr/bin
install -m755 -g root -o root build-Linux-i386/exiwhat $RPM_BUILD_ROOT/usr/bin
install -m755 -g root -o root util/exigrep $RPM_BUILD_ROOT/usr/bin
install -m755 -g root -o root util/eximstats $RPM_BUILD_ROOT/usr/bin
install -m755 -g root -o root util/exiqsumm $RPM_BUILD_ROOT/usr/bin 
install -m755 -g root -o root util/unknownuser.sh $RPM_BUILD_ROOT/usr/bin
install -m755 -g root -o root util/transport-filter.pl $RPM_BUILD_ROOT/usr/bin
install -m755 -g root -o root $RPM_SOURCE_DIR/analyse-log-errors $RPM_BUILD_ROOT/usr/bin
install -m755 -g root -o root $RPM_SOURCE_DIR/one-line-queuelist $RPM_BUILD_ROOT/usr/bin
install -m755 -g root -o root $RPM_SOURCE_DIR/newaliases $RPM_BUILD_ROOT/usr/bin
cp -f $RPM_SOURCE_DIR/exim.sc $RPM_BUILD_ROOT/etc/sysconfig/exim
cp -f $RPM_SOURCE_DIR/exim.lr $RPM_BUILD_ROOT/etc/logrotate.d/exim
strip $RPM_BUILD_ROOT/usr/bin/exim 
strip $RPM_BUILD_ROOT/usr/bin/exim_fixdb
strip $RPM_BUILD_ROOT/usr/bin/exim_tidydb 
strip $RPM_BUILD_ROOT/usr/bin/exim_dbmbuild 
strip $RPM_BUILD_ROOT/usr/bin/eximon.bin 
strip $RPM_BUILD_ROOT/usr/bin/exim_dumpdb
install -m644 -g root -o root $RPM_SOURCE_DIR/exim.conf $RPM_BUILD_ROOT/etc
mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/usr/lib
ln -s /usr/bin/exim $RPM_BUILD_ROOT/usr/sbin/sendmail
ln -s /usr/bin/exim $RPM_BUILD_ROOT/usr/lib/sendmail
ln -s /usr/bin/exim $RPM_BUILD_ROOT/usr/sbin/mailq
ln -s /usr/bin/exim $RPM_BUILD_ROOT/usr/sbin/rsmtp
ln -s /usr/bin/exim $RPM_BUILD_ROOT/usr/sbin/rmail
ln -s /usr/bin/exim $RPM_BUILD_ROOT/usr/sbin/runq
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
install -m755 -g root -o root $RPM_SOURCE_DIR/exim $RPM_BUILD_ROOT/etc/rc.d/init.d
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/rc0.d
ln -sf ../init.d/exim $RPM_BUILD_ROOT/etc/rc.d/rc0.d/K30exim
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/rc1.d
ln -sf ../init.d/exim $RPM_BUILD_ROOT/etc/rc.d/rc1.d/K30exim
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/rc2.d
ln -sf ../init.d/exim $RPM_BUILD_ROOT/etc/rc.d/rc2.d/S80exim
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/rc3.d
ln -sf ../init.d/exim $RPM_BUILD_ROOT/etc/rc.d/rc3.d/S80exim
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/rc5.d
ln -sf ../init.d/exim $RPM_BUILD_ROOT/etc/rc.d/rc5.d/S80exim
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/rc6.d
ln -sf ../init.d/exim $RPM_BUILD_ROOT/etc/rc.d/rc6.d/K30exim
mkdir -p $RPM_BUILD_ROOT/etc/cron.daily
cp -a $RPM_SOURCE_DIR/exim.cron.db $RPM_BUILD_ROOT/etc/cron.daily
mkdir -p $RPM_BUILD_ROOT/etc/cron.weekly
cp -a $RPM_SOURCE_DIR/exim.cron.log $RPM_BUILD_ROOT/etc/cron.weekly
mkdir -p $RPM_BUILD_ROOT/usr/man/man8
install -m644 -g root -o root $RPM_SOURCE_DIR/exim.8 $RPM_BUILD_ROOT/usr/man/man8
install -m644 -g root -o root $RPM_SOURCE_DIR/aliases $RPM_BUILD_ROOT/etc/aliases

mv exim-postscript-2.10/doc/* doc/
mv exim-pdf-2.10/doc/* doc/
mv exim-html-2.10/doc/* doc/
mv exim-texinfo-2.10/doc/* doc/

%files
%doc README* NOTICE LICENCE 
%config /etc/exim.conf
%config /etc/aliases
/usr/bin/exim
/usr/bin/exim_dumpdb
/usr/bin/exim_fixdb
/usr/bin/exim_tidydb
/usr/bin/exinext
/usr/bin/exiwhat
/usr/bin/exim_dbmbuild
/usr/bin/exicyclog
/usr/bin/exigrep
/usr/bin/eximstats
/usr/bin/exiqsumm
/usr/bin/unknownuser.sh
/usr/bin/transport-filter.pl
%doc /usr/man/man8/exim.8

%config /usr/sbin/sendmail
%config /usr/lib/sendmail
%config /usr/sbin/mailq
%config /usr/sbin/rsmtp
%config /usr/sbin/runq
%config /usr/sbin/rmail
%config /etc/sysconfig/exim
%config /etc/logrotate.d/exim
%config /etc/rc.d/init.d/exim
%config /etc/rc.d/rc0.d/K30exim
%config /etc/rc.d/rc1.d/K30exim
%config /etc/rc.d/rc2.d/S80exim
%config /etc/rc.d/rc3.d/S80exim
%config /etc/rc.d/rc5.d/S80exim
%config /etc/rc.d/rc6.d/K30exim
%config /etc/cron.daily/exim.cron.db
%config /etc/cron.weekly/exim.cron.log
%config /usr/bin/newaliases

%files X11
/usr/bin/eximon
/usr/bin/eximon.bin

%files doc
%doc doc/*

%post
#echo "WARNING: The 'mail' user must exist before you can start the mail server."
#if ! grep "^mail:" /etc/passwd >/dev/null 2>&1 && \
#   ! cut -f3 -d: /etc/passwd | grep 20 >/dev/null 2>&1
#then
#	echo "Now creating 'exim' user."
#	useradd -d /var/spool/exim -g mail -n -r -u 8 exim -c "Exim User" -s ""
#	mkdir -p -m 0750 /var/spool/exim /var/spool/exim/log
#	chown mail /var/spool/exim /var/spool/exim/log
#	chgrp mail /var/spool/exim /var/spool/exim/log
#fi
