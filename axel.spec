%define name 	axel
%define version 1.0b
%define release %mkrel 1

Name: 		%name
Summary: 	A light Linux download accelerator - Console version
Version: 	%version
Release: 	%release
Source:         http://wilmer.gaast.net/downloads/%name-%version.tar.bz2
Url: 		http://wilmer.gaast.net/main.php/axel.html
Group:		Networking/File transfer
License: GPL

%description
Axel tries to accelerate the downloading process by using multiple
connections for one file. Starting from version 0.97, the program can use
different URL's for one download as well. The program tries to be as light
as possible (25-30k in binary form), so it might be useful as a wget clone
on byte-critical systems.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build
./configure --prefix=%{_prefix} --libdir=%_libdir --etcdir=%{_sysconfdir} --i18n=1

%make

%install

%makeinstall DESTDIR=$RPM_BUILD_ROOT

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%{_bindir}/axel
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/axelrc
%{_mandir}/man1/axel.1*
%doc CREDITS CHANGES README axelrc.example
