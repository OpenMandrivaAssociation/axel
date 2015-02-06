Summary:	A light Linux download accelerator - Console version
Name:		axel
Version:	2.4
Release:	4
License:	GPLv2+
Group:		Networking/File transfer
Url:		http://axel.alioth.debian.org/
Source0:	http://alioth.debian.org/frs/download.php/2287/%name-%version.tar.bz2

%description
Axel tries to accelerate the downloading process by using multiple
connections for one file. Starting from version 0.97, the program can use
different URL's for one download as well. The program tries to be as light
as possible (25-30k in binary form), so it might be useful as a wget clone
on byte-critical systems.

%files -f %{name}.lang
%{_bindir}/axel
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/axelrc
%{_mandir}/man1/axel.1*
%lang(zh_C) %{_mandir}/zh_CN/man1/*
%doc CREDITS CHANGES README axelrc.example

#----------------------------------------------------------------------------

%prep
%setup -q

%build
./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--etcdir=%{_sysconfdir} \
	--i18n=1 \
	--strip=0
echo 'CFLAGS=%{optflags}' >> Makefile.settings
%make

%install
%makeinstall_std

%find_lang %{name}

