Name: x11-util-macros
BuildArch: noarch
Summary: Macro used for X.org development
Version: 1.17
Release: 1
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/util/util-macros-%{version}.tar.bz2

%description
Macros used for X.org development

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


%changelog
* Wed Mar 14 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.17-1
+ Revision: 784985
- version update 1.17

* Tue Mar 06 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.16.2-1
+ Revision: 782309
- 1.16.2

  + Alexander Khrukin <akhrukin@mandriva.org>
    - version update 1.16.1

* Sun Dec 11 2011 Alexander Khrukin <akhrukin@mandriva.org> 1.16.0-1
+ Revision: 740295
- version update 1.16.0

* Sat Sep 10 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.15.0-1
+ Revision: 699290
- update to new version 1.15.0

* Mon Apr 11 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.13.0-1
+ Revision: 652713
- new version 1.13.0

* Mon Feb 28 2011 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.12.0-1
+ Revision: 640975
- New version: 1.12.0
- Remove useless "echo"
- Use configure2_5x
- Use makeinstall_std

* Sat Oct 30 2010 Thierry Vignaud <tv@mandriva.org> 1.11.0-1mdv2011.0
+ Revision: 590412
- new release

* Fri Sep 24 2010 Thierry Vignaud <tv@mandriva.org> 1.10.1-1mdv2011.0
+ Revision: 580845
- new release

* Wed Jul 21 2010 Thierry Vignaud <tv@mandriva.org> 1.10.0-1mdv2011.0
+ Revision: 556419
- new release

* Mon Apr 05 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.7.0-1mdv2010.1
+ Revision: 531620
- New version: 1.7.0

* Fri Mar 12 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.6.1-1mdv2010.1
+ Revision: 518393
- New version: 1.6.1

* Fri Feb 05 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.6.0-1mdv2010.1
+ Revision: 501250
- New version: 1.6.0

* Mon Jan 18 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.5.0-1mdv2010.1
+ Revision: 493193
- New version: 1.5.0

* Mon Jan 18 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.4.2-1mdv2010.1
+ Revision: 493080
- New version: 1.4.2

* Tue Dec 15 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.4.1-1mdv2010.1
+ Revision: 478932
- New version: 1.4.1

* Mon Nov 09 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.3.0-1mdv2010.1
+ Revision: 463695
- New version: 1.3.0

* Fri Jun 19 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 1.2.2-1mdv2010.0
+ Revision: 387309
- update to version 1.2.2

* Tue Dec 30 2008 Colin Guthrie <cguthrie@mandriva.org> 1.2.1-1mdv2009.1
+ Revision: 321322
- New version: 1.2.1

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.1.6-2mdv2009.0
+ Revision: 266066
- rebuild early 2009.0 package (before pixel changes)

* Mon Apr 14 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.6-1mdv2009.0
+ Revision: 192829
- Update to version 1.1.6.

* Wed Feb 13 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.5-5mdv2008.1
+ Revision: 167173
- Revert to use upstream tarball, build requires and remove non mandatory patches.

* Wed Dec 26 2007 Paulo Andrade <pcpa@mandriva.com.br> 1.1.5-4mdv2008.1
+ Revision: 137948
- Properly use tag util-macros-1.1.5 to generate tarball, and update to
  generate patches from that point.
- Fix documentation comment in spec file.
- Update x11-util-macros, required/used by all modules

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 15 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.1.5-3mdv2008.1
+ Revision: 98601
- spec cleanup (fix description and packager tags)

