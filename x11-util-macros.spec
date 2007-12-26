Name: x11-util-macros
BuildArch: noarch
Summary: Macro used for X.org development
Version: 1.1.5
Release: %mkrel 4
Group: Development/X11
URL: http://xorg.freedesktop.org
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/util/macros xorg/util/macros
# cd xorg/util/macros
# git-archive --format=tar --prefix=util-macros-1.1.5/ util-macros-1.1.5 | bzip2 -9 > util-macros-1.1.5.tar.bz2
########################################################################
Source0: util-macros-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch util-macros-1.1.5..origin/mandriva+gpl
Patch1: 0001-Cannot-use-AC_CHECK_FILE-when-cross-compiling-assum.patch
Patch2: 0002-Add-a-common-set-of-macros-to-be-used-by-modules.patch
########################################################################

%description
Macros used for X.org development

%prep
echo %{buildroot}
%setup -q -n util-macros-%{version}

%patch1 -p1
%patch2 -p1

%build
autoreconf -ifs
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
