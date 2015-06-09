# TODO:
# - install+package csharp bindings
#
# Conditional build:
%bcond_without	java	# Java/JNI bindings
%bcond_with	mono	# .NET/C# bindings
#
Summary:	A cross-platform chemistry program and library designed to convert file formats
Summary(pl.UTF-8):	Międzyplatformowy program chemiczny i biblioteka do konwersji formatów plików
Name:		openbabel
Version:	2.3.2
Release:	6
License:	GPL v2
Group:		Libraries
Source0:	http://downloads.sourceforge.net/openbabel/%{name}-%{version}.tar.gz
# Source0-md5:	9b0007560d9d838b40ab4ad06daf5610
Patch0:		%{name}-prefix.patch
Patch1:		ruby-gcc-no-option.patch
Patch2:		cmake-fix.patch
Patch3:		python-build.patch
Patch4:		perl-x32.patch
Patch5:		python-x32.patch
URL:		http://openbabel.sourceforge.net/
BuildRequires:	cairo-devel
BuildRequires:	cmake >= 2.6.0
BuildRequires:	eigen3 >= 3
BuildRequires:	inchi-devel >= 1.0.3
%{?with_java:BuildRequires:	jdk}
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel >= 2.6.5
%{?with_mono:BuildRequires:	mono-csharp}
BuildRequires:	perl-devel
BuildRequires:	rpm-perlprov
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.577
BuildRequires:	ruby-devel
BuildRequires:	swig >= 2.0
BuildRequires:	wxGTK2-unicode-devel
BuildRequires:	zlib-devel
Requires:	inchi-libs >= 1.0.3
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

%package gui
Summary:	OpenBabel GUI
Summary(pl.UTF-8):	Graficzny interfejs użytkownika OpenBabel
Group:		X11/Applications/Science
Requires:	%{name} = %{version}-%{release}

%description gui
Graphical User Interface for OpenBabel.

%description gui -l pl.UTF-8
Graficzny interfejs użytkownika OpenBabel.

%package -n java-openbabel
Summary:	Java binding for OpenBabel
Summary(pl.UTF-8):	Wiązanie Javy do biblioteki OpenBabel
Group:		Libraries/Java

%description -n java-openbabel
Java binding for OpenBabel.

%description -n java-openbabel -l pl.UTF-8
Wiązanie Javy do biblioteki OpenBabel.

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

%package -n ruby-openbabel
Summary:	Ruby binding for OpenBabel
Summary(pl.UTF-8):	Wiązanie języka Ruby do biblioteki OpenBabel
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description -n ruby-openbabel
Ruby binding for OpenBabel.

%description -n ruby-openbabel -l pl.UTF-8
Wiązanie języka Ruby do biblioteki OpenBabel.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p1
%patch5 -p1

%build
%cmake . \
	-DBIN_INSTALL_DIR=%{_bindir} \
	-DLIB_INSTALL_DIR=%{_lib} \
	%{?with_mono:-DCSHARP_BINDINGS=ON} \
	-DCSHARP_EXECUTABLE=/usr/bin/mcs \
	-DCMAKE_C_FLAGS_RELEASE="-DNDEBUG" \
	-DCMAKE_CXX_FLAGS_RELEASE="-DNDEBUG" \
	%{?with_java:-DJAVA_BINDINGS=ON} \
	-DOBPERL_INSTALLDIRS="vendor" \
	-DPERL_BINDINGS=ON \
	-DPYTHON_BINDINGS=ON \
	-DRUBY_BINDINGS=ON \
	-DOPENBABEL_USE_SYSTEM_INCHI=ON \
	-DwxWidgets_CONFIG_EXECUTABLE=%{_bindir}/wx-gtk2-unicode-config
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

%{__make} install \
	RUBYARCHDIR=$RPM_BUILD_ROOT%{ruby_vendorarchdir} \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_libdir}/*.py $RPM_BUILD_ROOT%{py_sitedir}

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%if %{with java}
install -d $RPM_BUILD_ROOT%{_javadir}
%{__mv} $RPM_BUILD_ROOT%{_libdir}/*.jar $RPM_BUILD_ROOT%{_javadir}
%endif

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
%attr(755,root,root) %{_bindir}/obrms
%attr(755,root,root) %{_bindir}/obrotamer
%attr(755,root,root) %{_bindir}/obrotate
%attr(755,root,root) %{_bindir}/obspectrophore
%attr(755,root,root) %{_bindir}/roundtrip
%attr(755,root,root) %{_libdir}/libopenbabel.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopenbabel.so.4
%dir %{_libdir}/openbabel
%dir %{_libdir}/openbabel/%{version}
%attr(755,root,root) %{_libdir}/openbabel/%{version}/*.so
%{_datadir}/openbabel
%{_mandir}/man1/babel.1*
%{_mandir}/man1/obabel.1*
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
%{_mandir}/man1/obspectrophore.1*
%{_mandir}/man1/roundtrip.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopenbabel.so
%{_includedir}/openbabel-2.0
%{_pkgconfigdir}/openbabel-2.0.pc
%{_libdir}/cmake/openbabel2

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/obgui
%{_mandir}/man1/obgui.1*

%if %{with java}
%files -n java-openbabel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopenbabel_java.so
%{_javadir}/openbabel.jar
%endif

%files -n perl-Chemistry-OpenBabel
%defattr(644,root,root,755)
%{perl_vendorarch}/Chemistry/OpenBabel.pm
%dir %{perl_vendorarch}/auto/Chemistry/OpenBabel
%attr(755,root,root) %{perl_vendorarch}/auto/Chemistry/OpenBabel/OpenBabel.so

%files -n python-openbabel
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/_openbabel.so
%{py_sitedir}/openbabel.py[co]
%{py_sitedir}/pybel.py[co]
%{py_sitedir}/openbabel-1.7-py*.egg-info

%files -n ruby-openbabel
%defattr(644,root,root,755)
%attr(755,root,root) %{ruby_vendorarchdir}/openbabel.so
