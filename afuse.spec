Summary:	An automounter implemented with FUSE
Name:		afuse
Version:	0.2
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/afuse/%{name}-%{version}.tar.gz
# Source0-md5:	97b58a768ecb30696fb6c33dd8435b83
URL:		http://afuse.sourceforge.net
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libfuse-devel >= 0:2.3
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An automounter implemented with FUSE.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/afuse
