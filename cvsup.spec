Summary:	A CVS-aware network file distribution system
Summary(pl):	Sieciowy system dystrybucji plików zwi±zany z CVS
Name:		cvsup
Version:	16.0
Release:	1
Group:		Development/Version Control
License:	BSD
Source0:	ftp://ftp.FreeBSD.org/pub/FreeBSD/CVSup/%{name}-%{version}.tar.gz
URL:		http://www.polstra.com/projects/freeware/CVSup/
Requires:	Modula-3
BuildRequires:	pm3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CVSup is a next-generation replacement for sup. It is a leap forward,
in terms of capability, speed, and server efficiency.

CVSup offers the following advantages:
- Capabilities. Clients can maintain local CVS branches without
  interference from CVSup.
- Speed. CVSup works directly from the CVS repository on the server.
  It can parse and edit RCS files, and it understands how they are
  typically changed under CVS. It uses a streaming protocol for updates
  and sends compressed diffs and reverse diffs of changes to minimize
  bandwidth.

%description -l pl
CVSup jest nastêpc± dla sup. CVSup jest szybkim, zgodnych z
poprzednikami serwerem.

CVSup oferuje:
- Mo¿liwo¶ci. Klienci mog± zarz±dzaæ lokalnymi drzewami.
- Szybko¶æ. CVSup dzia³a bezpo¶rednio z repozytorium CVS na serwerze.
  Mo¿e on analizowaæ i edytowaæ pliku CVS. CVSup u¿ywa strumieniowego
  protoko³u do aktualizowania (przesy³a skompesowane pliki by
  zminimalizowaæ zajmowane pasmo).

%package client
Summary:	Client-side CVSup package
Summary(pl):	CVSup - klient
Group:		Development/Version Control

%description client
CVSup is a next-generation replacement for sup. It is a leap forward,
in terms of capability, speed, and server efficiency.

CVSup offers the following advantages:
- Capabilities. Clients can maintain local CVS branches without
  interference from CVSup.
- Speed. CVSup works directly from the CVS repository on the server.
  It can parse and edit RCS files, and it understands how they are
  typically changed under CVS. It uses a streaming protocol for updates
  and sends compressed diffs and reverse diffs of changes to minimize
  bandwidth.

The client package allows a developer to maintain a local copy of a
full CVS repository. CVSup can also maintain local copies of other
kinds of directory trees.

%description client -l pl
CVSup jest nastêpc± dla sup. CVSup jest szybkim, zgodnych z
poprzednikami serwerem.

CVSup oferuje:
- Mo¿liwo¶ci. Klienci mog± zarz±dzaæ lokalnymi drzewami.
- Szybko¶æ. CVSup dzia³a bezpo¶rednio z repozytorium CVS na serwerze.
  Mo¿e on analizowaæ i edytowaæ pliku CVS. CVSup u¿ywa strumieniowego
  protoko³u do aktualizowania (przesy³a skompesowane pliki by
  zminimalizowaæ zajmowane pasmo).

Pakiet kliencki pozwala developerom zarz±dzaæ pe³n± lokaln± kopi±
repozytorium CVS. CVSup mo¿e równie¿ zarz±dzaæ innymi lokalnymi
kopiami drzew katalogowych.

%package server
Summary:	Server-side CVSup package
Summary(pl):	CVSup - serwer
Group:		Development/Version Control

%description server
CVSup is a next-generation replacement for sup. It is a leap forward,
in terms of capability, speed, and server efficiency.

CVSup offers the following advantages:
- Capabilities. Clients can maintain local CVS branches without
  interference from CVSup.
- Speed. CVSup works directly from the CVS repository on the server.
  It can parse and edit RCS files, and it understands how they are
  typically changed under CVS. It uses a streaming protocol for updates
  and sends compressed diffs and reverse diffs of changes to minimize
  bandwidth.

The server package allows a developer to publish a full or partial CVS
repository. CVSup can also publish other kinds of directory trees.

%description server -l pl
CVSup jest nastêpc± dla sup. CVSup jest szybkim, zgodnych z
poprzednikami serwerem.

CVSup oferuje:
- Mo¿liwo¶ci. Klienci mog± zarz±dzaæ lokalnymi drzewami.
- Szybko¶æ. CVSup dzia³a bezpo¶rednio z repozytorium CVS na serwerze.
  Mo¿e on analizowaæ i edytowaæ pliku CVS. CVSup u¿ywa strumieniowego
  protoko³u do aktualizowania (przesy³a skompesowane pliki by
  zminimalizowaæ zajmowane pasmo).

Pakiet serwera pozwala developerom na publikowanie czê¶ciowo lub w
ca³o¶ci repozytorium CVS. CVSup mo¿e tak¿e publikowaæ innego rodzaju
drzewa katalogowe.

%prep
%setup -q

%build
%{__make} M3TARGET=LINUXELF CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	M3TARGET=LINUXELF

gzip -9nf Acknowledgments Announce Blurb ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files client
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/cvsup
%{_mandir}/man1/cvsup.1*

%files server
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/cvsupd
%{_mandir}/man8/cvsupd.8*
