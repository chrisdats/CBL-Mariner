Summary:        Library that Implements a typesafe callback system for standard C++.
Name:           libsigc++20
Version:        2.10.0
Release:        7%{?dist}
License:        LGPLv2+
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          Applications/System
URL:            https://github.com/libsigcplusplus/libsigcplusplus
#Source0:        https://github.com/libsigcplusplus/libsigcplusplus/releases/download/%{version}/libsigcplusplus-%{version}.tar.xz
Source0:        libsigc++-%{version}.tar.xz

%description
It allows to define signals and to connect those signals to any callback function, either global or a member function, regardless of whether it is static or virtual. It also contains adaptor classes for connection of dissimilar callbacks and has an ease of use unmatched by other C++ callback libraries.

%package devel
Summary:        Documentation for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Static libraries and headers for %{name}

%package doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}

%description doc
Documentation for %{name}

%prep
%setup -q -n libsigc++-%{version}

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%check
make %{?_smp_mflags} check

%post -p /sbin/ldconfig
%postun    -p /sbin/ldconfig

%files
%license COPYING
%{_libdir}/libsigc-2.0.so.0*

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/sigc++-2.0/
%{_libdir}/*.so

%files doc
%{_datadir}/*

%changelog
* Mon Mar 29 2021 Thomas Crain <thcrain@microsoft.com> - 2.10.0-7
- Create devel/doc subpackages
- Lint to Mariner standards

* Sat May 09 2020 Nick Samson <nisamson@microsoft.com> - 2.10.0-6
- Added %%license line automatically

* Wed Apr 29 2020 Emre Girgin <mrgirgin@microsoft.com> 2.10.0-5
- Renaming libsigc++ to libsigc++20

* Thu Apr 09 2020 Joe Schmitt <joschmit@microsoft.com> 2.10.0-4
- Fix Source0 comment.

* Tue Apr 07 2020 Joe Schmitt <joschmit@microsoft.com> 2.10.0-3
- Update Source0 with valid URL.
- Update URL.
- Remove sha1 macro.
- License verified.

* Tue Sep 03 2019 Mateusz Malisz <mamalisz@microsoft.com> 2.10.0-2
- Initial CBL-Mariner import from Photon (license: Apache2).

* Thu May 25 2017 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.10.0-1
- Revert back to the stable version 2.10.0-1

* Wed Apr 12 2017 Danut Moraru <dmoraru@vmware.com> 2.99.8-1
- Updated to version 2.99.8

* Tue Apr 04 2017 Kumar Kaushik <kaushikk@vmware.com> 2.10.0-1
- Updated to version 2.10.0

* Tue Sep 06 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.8.0-1
- Updated to version 2.8.0-1

* Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 2.6.2-2
- GA - Bump release of all rpms

* Mon Feb 22 2016 XIaolin Li <xiaolinl@vmware.com> 2.6.2-1
- Updated to version 2.6.2

* Wed Nov 12 2014 Mahmoud Bassiouny <mbassiouny@vmware.com> 2.4.0-1
- Initial version
