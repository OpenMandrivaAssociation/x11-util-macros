Name: x11-util-macros
BuildArch: noarch
Summary: Macro used for X.org development
Version: 1.1.5
Release: %mkrel 5
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/util/util-macros-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

Patch1: 0001-Cannot-use-AC_CHECK_FILE-when-cross-compiling-assum.patch

%description
Macros used for X.org development

%prep
echo %{buildroot}
%setup -q -n util-macros-%{version}

%patch1 -p1

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/aclocal/xorg-macros.m4
%{_datadir}/aclocal/xorgversion.m4
