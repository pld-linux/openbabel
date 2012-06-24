Summary:	A cross-platform chemistry program and library designed to convert file formats
Summary(pl):	Mi�dzyplatformowy program chemiczny i biblioteka do konwersji format�w plik�w
Name:		openbabel
Version:	1.99
Release:	3
License:	GPL v2
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	f6746bf54d7ef67e0335a125e04b01b2
Patch0:		%{name}-DESTDIR.patch
URL:		http://openbabel.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Open Babel is a project designed to pick up where Babel left off, as a
cross-platform program and library designed to interconvert between
many file formats used in molecular modeling and computational
chemistry.

%description -l pl
Open Babel to projekt maj�cy pozbiera� to, co zosta�o po zaniechaniu
projektu Babel, jako mi�dzyplatformowy program i biblioteka s�u��ce do
konwersji mi�dzy wielona formatami u�ywanymi w modelowaniu cz�steczek
i chemii obliczeniowej.

%package devel
Summary:	Header files for OpenBabel
Summary(pl):	Pliki nag��wkowe dla OpenBabel
Group:		X11/Development/Libraries
# static only library, so no R necessary
#Requires:	%{name} = %{version}

%description devel
Header files for OpenBabel.

%description devel -l pl
Pliki nag��wkowe dla OpenBabel.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.* .
%{__autoconf}
%configure

%{__make}
#%%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/openbabel}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install src/libopenbabel.a $RPM_BUILD_ROOT%{_libdir}
install src/*.h $RPM_BUILD_ROOT%{_includedir}/openbabel

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README THANKS doc/{FAQ,Migration,*.html}
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/openbabel
%attr(755,root,root) %{_datadir}/openbabel/*.txt
%{_mandir}/man1/*.1*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libopenbabel.a
%dir %{_includedir}/openbabel
%{_includedir}/openbabel/*.h
