Name:		x11-util-macros
Summary:	Macro used for X.org development
Version:	1.19.2
Release:	1
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/util/util-macros-%{version}.tar.bz2
Source1:	x11-util-macros.rpmlintrc
BuildArch:	noarch

%description
Macros used for X.org development.

%prep
%setup -q -n util-macros-%{version}

%build
%configure
%make

%install
%makeinstall_std

%files
%{_datadir}/util-macros/INSTALL
%{_datadir}/aclocal/xorg-macros.m4
%{_datadir}/pkgconfig/xorg-macros.pc
