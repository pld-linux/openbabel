Summary:	A cross-platform chemistry program and library designed to convert file formats
Summary(pl):	Miêdzyplatformowy program chemiczny i biblioteka do konwersji formatów plików
Name:		openbabel
Version:	1.99
Release:	2
License:	GPL v2
Group:		X11/Libraries
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://openbabel.sourceforge.net/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Open Babel is a project designed to pick up where Babel left off, as a
cross-platform program and library designed to interconvert between
many file formats used in molecular modeling and computational
chemistry.

%package devel
Summary:	Header files for OpenBabel
Summary(pl):	Pliki nag³ówkowe dla OpenBabel
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for OpenBabel.

%description devel -l pl
Pliki nag³ówkowe dla OpenBabel.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.* .
%{__autoconf}
%configure

%{__make}
#%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_libdir},%{_includedir}/openbabel}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install src/libopenbabel.a $RPM_BUILD_ROOT/%{_libdir}
install src/*.h $RPM_BUILD_ROOT/%{_includedir}/openbabel/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README THANKS doc/{FAQ,Migration,*.html}
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_datadir}/openbabel/*.txt
%{_mandir}/man1/*.1*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libopenbabel.a
%{_includedir}/openbabel/*.h
