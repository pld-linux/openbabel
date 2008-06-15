Summary:	A cross-platform chemistry program and library designed to convert file formats
Summary(pl.UTF-8):	Międzyplatformowy program chemiczny i biblioteka do konwersji formatów plików
Name:		openbabel
Version:	2.1.1
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/openbabel/%{name}-%{version}.tar.gz
# Source0-md5:	a2a002c6913d6fb94fdc7dede2166194
URL:		http://openbabel.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel >= 2.6.5
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Open Babel is a project designed to pick up where Babel left off, as a
cross-platform program and library designed to interconvert between
many file formats used in molecular modeling and computational
chemistry.

%description -l pl.UTF-8
Open Babel to projekt mający pozbierać to, co zostało po zaniechaniu
projektu Babel, jako międzyplatformowy program i biblioteka służące do
konwersji między wieloma formatami używanymi w modelowaniu cząsteczek
i chemii obliczeniowej.

%package devel
Summary:	Header files for OpenBabel
Summary(pl.UTF-8):	Pliki nagłówkowe dla OpenBabel
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	zlib-devel

%description devel
Header files for OpenBabel.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla OpenBabel.

%package static
Summary:	Static OpenBabel library
Summary(pl.UTF-8):	Statyczna biblioteka OpenBabel
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static OpenBabel library.

%description static -l pl.UTF-8
Statyczna biblioteka OpenBabel.

%prep
%setup -q

%build
# simulate there is no libinchi installed (if openbabel is already installed),
# so it will be build with openbabel
# inchi is available separately at http://www.iupac.org/inchi/, but requires
# registration to download
%configure \
	ac_cv_lib_inchi_GetINCHI=no \
	--enable-shared

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/openbabel/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README THANKS doc/*.html
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libinchi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libinchi.so.?
%attr(755,root,root) %{_libdir}/libopenbabel.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopenbabel.so.?
%dir %{_libdir}/openbabel
%attr(755,root,root) %{_libdir}/openbabel/*.so
%{_datadir}/openbabel
%{_mandir}/man1/*.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libinchi.so
%attr(755,root,root) %{_libdir}/libopenbabel.so
%{_libdir}/libinchi.la
%{_libdir}/libopenbabel.la
%{_includedir}/inchi
%{_includedir}/openbabel-2.0
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libinchi.a
%{_libdir}/libopenbabel.a
