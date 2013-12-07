Name:		x11-util-macros
Summary:	Macro used for X.org development
Version:	1.17.1
Release:	4
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/util/util-macros-%{version}.tar.bz2
BuildArch:	noarch

%description
Macros used for X.org development.

%prep
%setup -q -n util-macros-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_datadir}/util-macros/INSTALL
%{_datadir}/aclocal/xorg-macros.m4
%{_datadir}/pkgconfig/xorg-macros.pc

