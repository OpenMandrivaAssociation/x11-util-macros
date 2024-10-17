Name:		x11-util-macros
Summary:	Macro used for X.org development
Version:	1.20.1
Release:	1
Group:		Development/X11
License:	MIT
URL:		https://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/util/util-macros-%{version}.tar.xz
Source1:	x11-util-macros.rpmlintrc
BuildArch:	noarch

%description
Macros used for X.org development.

%prep
%autosetup -n util-macros-%{version} -p1

%build
%configure
%make_build

%install
%make_install

%files
%{_datadir}/util-macros/INSTALL
%{_datadir}/aclocal/xorg-macros.m4
%{_datadir}/pkgconfig/xorg-macros.pc
