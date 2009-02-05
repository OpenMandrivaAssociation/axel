%define name 	axel
%define version 2.3
%define release %mkrel 1

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
