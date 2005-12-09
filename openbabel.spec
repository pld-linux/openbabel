Summary:	A cross-platform chemistry program and library designed to convert file formats
Summary(pl):	Mi�dzyplatformowy program chemiczny i biblioteka do konwersji format�w plik�w
Name:		openbabel
Version:	2.0.0
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/openbabel/%{name}-%{version}.tar.gz
# Source0-md5:	3bddfa9188042e2518eb53c064279b4e
URL:		http://openbabel.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Open Babel is a project designed to pick up where Babel left off, as a
cross-platform program and library designed to interconvert between
many file formats used in molecular modeling and computational
chemistry.

%description -l pl
Open Babel to projekt maj�cy pozbiera� to, co zosta�o po zaniechaniu
projektu Babel, jako mi�dzyplatformowy program i biblioteka s�u��ce do
konwersji mi�dzy wieloma formatami u�ywanymi w modelowaniu cz�steczek
i chemii obliczeniowej.

%package devel
Summary:	Header files for OpenBabel
Summary(pl):	Pliki nag��wkowe dla OpenBabel
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for OpenBabel.

%description devel -l pl
Pliki nag��wkowe dla OpenBabel.

%package static
Summary:	Static OpenBabel library
Summary(pl):	Statyczna biblioteka OpenBabel
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static OpenBabel library.

%description static -l pl
Statyczna biblioteka OpenBabel.

%prep
%setup -q

%build
%configure \
	--enable-shared

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/openbabel/math}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install src/math/{matrix3x3,vector3}.h \
	$RPM_BUILD_ROOT%{_includedir}/openbabel/math

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README THANKS doc/*.html
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libopenbabel.so.*.*.*
%attr(755,root,root) %{_libdir}/libinchi.so.*.*.*
%attr(755,root,root) %{_libdir}/openbabel/*.so
%dir %{_datadir}/openbabel
%attr(755,root,root) %{_datadir}/openbabel/%{version}/*.txt
%{_mandir}/man1/*.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopenbabel.so
%{_libdir}/libopenbabel.la
%{_libdir}/*.la
%{_libdir}/openbabel/*.la
%{_includedir}/openbabel
%{_includedir}/inchi
%{_includedir}/openbabel-2.0
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libopenbabel.a
%{_libdir}/libinchi.a
%{_libdir}/openbabel/*.a
