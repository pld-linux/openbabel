# TODO:
# - wxWidgets (cmake needs hacking to use wx-gtk2-unicode-config instead of wx-config)
# - install+package ruby, java, csharp bindings
Summary:	A cross-platform chemistry program and library designed to convert file formats
Summary(pl.UTF-8):	Międzyplatformowy program chemiczny i biblioteka do konwersji formatów plików
Name:		openbabel
Version:	2.3.0
Release:	0.1
License:	GPL v2
Group:		Libraries
Source0:	http://downloads.sourceforge.net/openbabel/%{name}-%{version}.tar.gz
# Source0-md5:	effda01ed4a31d18d8e3d08191799608
Patch0:		%{name}-ruby.patch
Patch1:		%{name}-python.patch
Patch2:		%{name}-prefix.patch
Patch3:		%{name}-perl.patch
URL:		http://openbabel.sourceforge.net/
BuildRequires:	cmake >= 2.6.0
BuildRequires:	eigen >= 2
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel >= 2.6.5
BuildRequires:	perl-devel
BuildRequires:	rpm-perlprov
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.577
#BuildRequires:	wxGTK2-devel
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
Obsoletes:	openbabel-static

%description devel
Header files for OpenBabel.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla OpenBabel.

%package -n perl-Chemistry-OpenBabel
Summary:	Perl binding for OpenBabel
Summary(pl.UTF-8):	Wiązanie Perla do biblioteki OpenBabel
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description -n perl-Chemistry-OpenBabel
Perl binding for OpenBabel.

%description -n perl-Chemistry-OpenBabel -l pl.UTF-8
Wiązanie Perla do biblioteki OpenBabel.

%package -n python-openbabel
Summary:	Python binding for OpenBabel
Summary(pl.UTF-8):	Wiązanie Pythona do biblioteki OpenBabel
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-openbabel
Python binding for OpenBabel.

%description -n python-openbabel -l pl.UTF-8
Wiązanie Pythona do biblioteki OpenBabel.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%cmake . \
	-DALL_BINDINGS=ON \
	-DCMAKE_C_FLAGS_RELEASE="-DNDEBUG" \
	-DCMAKE_CXX_FLAGS_RELEASE="-DNDEBUG" \
	-DwxWIDGETS_CONFIG_EXECUTABLE=%{_bindir}/wx-gtk2-unicode-config
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README THANKS doc/*.html
%attr(755,root,root) %{_bindir}/babel
%attr(755,root,root) %{_bindir}/obabel
%attr(755,root,root) %{_bindir}/obchiral
%attr(755,root,root) %{_bindir}/obconformer
%attr(755,root,root) %{_bindir}/obenergy
%attr(755,root,root) %{_bindir}/obfit
%attr(755,root,root) %{_bindir}/obgen
%attr(755,root,root) %{_bindir}/obgrep
%attr(755,root,root) %{_bindir}/obminimize
%attr(755,root,root) %{_bindir}/obprobe
%attr(755,root,root) %{_bindir}/obprop
%attr(755,root,root) %{_bindir}/obrotamer
%attr(755,root,root) %{_bindir}/obrotate
%attr(755,root,root) %{_bindir}/obspectrophore
%attr(755,root,root) %{_bindir}/roundtrip
%attr(755,root,root) %{_libdir}/libinchi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libinchi.so.0
%attr(755,root,root) %{_libdir}/libopenbabel.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopenbabel.so.4
%dir %{_libdir}/openbabel
%dir %{_libdir}/openbabel/%{version}
%attr(755,root,root) %{_libdir}/openbabel/%{version}/*.so
%{_datadir}/openbabel
%{_mandir}/man1/babel.1*
%{_mandir}/man1/obchiral.1*
%{_mandir}/man1/obconformer.1*
%{_mandir}/man1/obenergy.1*
%{_mandir}/man1/obfit.1*
%{_mandir}/man1/obgen.1*
%{_mandir}/man1/obgrep.1*
%{_mandir}/man1/obminimize.1*
%{_mandir}/man1/obprobe.1*
%{_mandir}/man1/obprop.1*
%{_mandir}/man1/obrotamer.1*
%{_mandir}/man1/obrotate.1*
%{_mandir}/man1/roundtrip.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libinchi.so
%attr(755,root,root) %{_libdir}/libopenbabel.so
%{_libdir}/openbabel/OpenBabel2*.cmake
%{_includedir}/inchi
%{_includedir}/openbabel-2.0
%{_pkgconfigdir}/openbabel-2.0.pc

%files -n perl-Chemistry-OpenBabel
%defattr(644,root,root,755)
%{perl_vendorarch}/Chemistry/OpenBabel.pm
%dir %{perl_vendorarch}/auto/Chemistry/OpenBabel
%{perl_vendorarch}/auto/Chemistry/OpenBabel/OpenBabel.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Chemistry/OpenBabel/OpenBabel.so

%files -n python-openbabel
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_openbabel.so
%{py_sitedir}/openbabel.py[co]
%{py_sitedir}/pybel.py[co]
%{py_sitedir}/openbabel-1.6-py*.egg-info
