Summary:	A cross-platform chemistry program and library designed to convert file formats
Summary(pl):	Miêdzyplatformowy program chemiczny i biblioteka do konwersji formatów plików
Name:		openbabel
Version:	1.99
Release:	1
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
install -d $RPM_BUILD_ROOT/%{_libdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install src/libopenbabel.a $RPM_BUILD_ROOT/%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README THANKS doc/{FAQ,Migration,*.html}
%attr(755,root,root) %{_bindir}/*
%{_libdir}/libopenbabel.a
%attr(755,root,root) %{_datadir}/openbabel/*.txt
%{_mandir}/man1/*.1*
