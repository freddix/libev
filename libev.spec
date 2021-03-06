Summary:	Event notification library
Name:		libev
Version:	4.19
Release:	1
License:	BSD or GPL v2+
Group:		Libraries
Source0:	http://dist.schmorp.de/libev/%{name}-%{version}.tar.gz
# Source0-md5:	01d1c672697f649b4f94abd0b70584ff
URL:		http://software.schmorp.de/pkg/libev.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libev API provides a mechanism to execute a callback function when
a specific event occurs on a file descriptor or after a timeout has
been reached. It is meant to replace the asynchronous event loop found
in event-driven network servers.

%package devel
Summary:	Header files for libev library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libev library.

%prep
%setup -q

# insert empty line after AM_INIT_AUTOMAKE to unbreak autoreconfig
%{__sed} '/AM_INIT_AUTOMAKE.*/{G;}' -i configure.ac

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

# conflict with libevent
%{__rm} $RPM_BUILD_ROOT%{_includedir}/event.h

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Changes LICENSE README
%attr(755,root,root) %ghost %{_libdir}/libev.so.?
%attr(755,root,root) %{_libdir}/libev.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libev.so
%{_includedir}/ev.h
%{_includedir}/ev++.h
%{_mandir}/man3/ev.3*

