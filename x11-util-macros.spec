Name: x11-util-macros
BuildArch: noarch
Summary: Macro used for X.org development
Version: 1.1.6
Release: %mkrel 2
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/util/util-macros-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

%description
Macros used for X.org development

%prep
echo %{buildroot}
%setup -q -n util-macros-%{version}

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
