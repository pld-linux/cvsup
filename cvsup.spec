#
# Spec file for cvsup utility
# Thomas Lockhart 1999-01-22
#
Summary: A CVS-aware network file distribution system
Name: cvsup
Version: 15.5
Release: 1
Copyright: BSD
Group: Development/Version Control
Source: ftp://ftp.FreeBSD.org/pub/FreeBSD/CVSup/cvsup-15.5.tar.gz
URL: http://www.polstra.com/projects/freeware/CVSup/
Distribution: PostgreSQL Linux
Vendor: PostgreSQL
Packager: Thomas Lockhart <lockhart@alumni.caltech.edu>
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
Summary: Client-side CVSup package
Group: Development/Version Control
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
Summary: Server-side CVSup package
Group: Development/Version Control
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
%setup


%build
make M3TARGET=LINUXELF M3FLAGS="-DNOGUI -DSTATIC"


%install
make M3TARGET=LINUXELF M3FLAGS="-DNOGUI" install


%files client
%doc Acknowledgments Announce Blurb ChangeLog Install
/usr/local/bin/cvsup
/usr/local/man/man1/cvsup.1


%files server
%doc Acknowledgments Announce Blurb ChangeLog Install
/usr/local/sbin/cvsupd
/usr/local/man/man8/cvsupd.8


%clean
# put ancillary cleanup of files outside the build tree here...
