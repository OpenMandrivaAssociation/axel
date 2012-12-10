%define name 	axel
%define version 2.4
%define release %mkrel 2

Name: 		%name
Summary: 	A light Linux download accelerator - Console version
Version: 	%version
Release: 	%release
Source:         http://alioth.debian.org/frs/download.php/2287/%name-%version.tar.bz2
Url: 		http://axel.alioth.debian.org/
Group:		Networking/File transfer
BuildRoot: 	%{_tmppath}/%{name}-buildroot
License: GPLv2+

%description
Axel tries to accelerate the downloading process by using multiple
connections for one file. Starting from version 0.97, the program can use
different URL's for one download as well. The program tries to be as light
as possible (25-30k in binary form), so it might be useful as a wget clone
on byte-critical systems.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --libdir=%_libdir --etcdir=%{_sysconfdir} --i18n=1
echo 'CFLAGS=%optflags' >> Makefile.settings
%make

%install
rm -fr %buildroot
%makeinstall_std
%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%{_bindir}/axel
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/axelrc
%{_mandir}/man1/axel.1*
%lang(zh_C) %{_mandir}/zh_CN/man1/*
%doc CREDITS CHANGES README axelrc.example


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.4-2mdv2011.0
+ Revision: 610014
- rebuild

* Sun Dec 20 2009 J√©r√¥me Brenier <incubusss@mandriva.org> 2.4-1mdv2010.1
+ Revision: 480266
- new version 2.4

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 2.3-2mdv2010.0
+ Revision: 436735
- rebuild

* Thu Feb 05 2009 Funda Wang <fwang@mandriva.org> 2.3-1mdv2009.1
+ Revision: 337718
- New version 2.3

* Mon Nov 17 2008 Funda Wang <fwang@mandriva.org> 2.2-1mdv2009.1
+ Revision: 303890
- New version 2.2

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.1-3mdv2009.0
+ Revision: 243123
- rebuild

* Mon Jan 28 2008 Funda Wang <fwang@mandriva.org> 1.0b-1mdv2008.1
+ Revision: 159082
- New version 1.1

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 15 2007 Pascal Terjan <pterjan@mandriva.org> 1.0b-1mdv2008.0
+ Revision: 63754
- Import axel



* Wed Jul 20 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 1.0b-1mdk
- New release 1.0b
- Fix Source
- mkrel

* Sun Mar 13 2005 Nicolas LÈcureuil <neoclust@mandrake.org> 1.0a-4mdk
- Fix URL

* Mon Feb 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.0a-3mdk
- rebuild

* Thu Jan 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.0a-2mdk
- rebuild

* Tue May 21 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.0a-1mdk
- fix files permissions
- Matthias Debus  <psic4t@netbands.de> :
	- Rewritten most parts of the spec file to fit Mandrake rpm specifications
	- GUI is not included as Mandrake does not provide Kaptain

* Sun Dec 16 2001 Wilmer van der Gaast <lintux@debian.org>
- Made the package a bit more rpmlint clean

* Fri Nov 09 2001 Wilmer van der Gaast <lintux@lintux.cx>
- Added axel-kapt binary package

* Wed Aug 15 2001 Wilmer van der Gaast <lintux@lintux.cx>
- Removed line which removed all other builds from rpm directory, don't really
  know why it was there
- New description

* Wed Jun 26 2001 Wilmer van der Gaast <lintux@lintux.cx>
- Version changes will not be logged anymore
- spec file is part of the default source tarball now
- Small spec file changes

* Tue May 22 2001 Wilmer van der Gaast <lintux@lintux.cx>
- Upgraded to version 0.93

* Fri May 11 2001 Wilmer van der Gaast <lintux@lintux.cx>
- Upgraded to version 0.92

* Sat May 05 2001 Ralph Slooten <axllent@axllent.cjb.net>
- Rpm created
