Summary:	A CVS-aware network file distribution system
Name:		cvsup
Version:	16.0
Release:	1
Group:		Development/Version Control
Group(pl):	Programowanie/Zarz±dzanie wersjami
Copyright:	BSD
Source:		ftp://ftp.FreeBSD.org/pub/FreeBSD/CVSup/%{name}-%{version}.tar.gz
URL:		http://www.polstra.com/projects/freeware/CVSup/
Requires:	Modula-3
BuildRoot:	/tmp/%{name}-%{version}-root

%description
CVSup is a next-generation replacement for sup.  It is a leap
forward, in terms of capability, speed, and server efficiency.

CVSup offers the following advantages:
* Capabilities. Clients can maintain local CVS branches without
  interference from CVSup.
* Speed. CVSup works directly from the CVS repository on the
  server. It can parse and edit RCS files, and it understands
  how they are typically changed under CVS. It uses a streaming
  protocol for updates and sends compressed diffs and reverse
  diffs of changes to minimize bandwidth.


%package client
Summary:	Client-side CVSup package
Group:		Development/Version Control
Group(pl):	Programowanie/Zarz±dzanie wersjami

%description client
CVSup is a next-generation replacement for sup.  It is a leap
forward, in terms of capability, speed, and server efficiency.

CVSup offers the following advantages:
* Capabilities. Clients can maintain local CVS branches without
  interference from CVSup.
* Speed. CVSup works directly from the CVS repository on the
  server. It can parse and edit RCS files, and it understands
  how they are typically changed under CVS. It uses a streaming
  protocol for updates and sends compressed diffs and reverse
  diffs of changes to minimize bandwidth.

The client package allows a developer to maintain a local copy
of a full CVS repository. CVSup can also maintain local copies
of other kinds of directory trees.


%package server
Summary:	Server-side CVSup package
Group:		Development/Version Control
Group(pl):	Programowanie/Zarz±dzanie wersjami

%description server
CVSup is a next-generation replacement for sup.  It is a leap
forward, in terms of capability, speed, and server efficiency.

CVSup offers the following advantages:
* Capabilities. Clients can maintain local CVS branches without
  interference from CVSup.
* Speed. CVSup works directly from the CVS repository on the
  server. It can parse and edit RCS files, and it understands
  how they are typically changed under CVS. It uses a streaming
  protocol for updates and sends compressed diffs and reverse
  diffs of changes to minimize bandwidth.

The server package allows a developer to publish a full or
partial CVS repository. CVSup can also publish other kinds of
directory trees.

%prep
%setup -q

%build
make M3TARGET=LINUXELF

%install
rm -rf $RPM_BUILD_ROOT
make install \
	PREFIX=/usr \
	M3TARGET=LINUXELF 

strip $RPM_BUILD_ROOT/usr/{bin,sbin}/*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	Acknowledgments Announce Blurb ChangeLog Install

%clean
rm -rf $RPM_BUILD_ROOT

%files client
%doc *.gz
%{_bindir}/cvsup
%{_mandir}/man1/cvsup.1.gz

%files server
%doc *.gz
%{_sbindir}/cvsupd
%{_mandir}/man8/cvsupd.8.gz

%changelog
* Mon Apr 12 1999 Micha³ Kuratczyk <kura@pld.org.pl>
  [1.16-1]
- added %changelog
- added gzipping documentation and man pages
- added Group(pl)
- added 'rm -rf $RPM_BUILD_ROOT' to %clean
- added -q %setup parameter
- added BuildRoot (by PLD standard)
- added stripping binaries
