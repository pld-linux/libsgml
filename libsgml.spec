Summary:	Small, fast, state based SGML parser
Summary(pl):	Ma�y, szybki, oparty na stanach parser SGML-a
Name:		libsgml
Version:	1.1.4
Release:	1
License:	free (see License)
Group:		Libraries
Source0:	http://www.hick.org/code/skape/libsgml/%{name}-%{version}.tar.gz
# Source0-md5:	a3ba2f8c19faf1a53182d9c6fab22e58
Patch0:		%{name}-opt.patch
URL:		http://www.hick.org/code/skape/libsgml/docs/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libsgml is a small, fast, state based SGML parser. It supports:
 - HTML DOM parsing with tag escaping and text, comment, and element
   stripping,
 - XML DOM parsing,
 - Custom SGML parsing.

%description -l pl
libsgml to ma�y, szybki, oparty na stanach parser SGML-a. Obs�uguje:
 - analiz� HTML DOM z cytowaniem znacznik�w i usuwaniem tekstu,
   komentarzy i element�w,
 - analiz� XML DOM,
 - analiz� w�asnego SGML-a.

%package devel
Summary:	Header files for libsgml library
Summary(pl):	Pliki nag��wkowe biblioteki libsgml
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libsgml library.

%description devel -l pl
Pliki nag��wkowe biblioteki libsgml.

%package static
Summary:	Static libsgml library
Summary(pl):	Statyczna biblioteka libsgml
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libsgml library.

%description static -l pl
Statyczna biblioteka libsgml.

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
%configure
%{__make} \
	DEBUG="%{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/sgml}

install libsgml.so libsgml.a $RPM_BUILD_ROOT%{_libdir}
install include/*.h $RPM_BUILD_ROOT%{_includedir}/sgml

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Bugs ChangeLog License README TODO
%attr(755,root,root) %{_libdir}/libsgml.so

%files devel
%defattr(644,root,root,755)
%doc docs/html/*
%{_includedir}/sgml

%files static
%defattr(644,root,root,755)
%{_libdir}/libsgml.a
