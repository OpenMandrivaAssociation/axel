%define _disable_rebuild_configure 1

Summary:	A light Linux download accelerator - Console version
Name:		axel
Version:	2.17.11
Release:	1
License:	GPLv2+
Group:		Networking/File transfer
Url:		https://github.com/axel-download-accelerator/axel
Source0:	https://github.com/axel-download-accelerator/axel/releases/download/v%{version}/axel-%{version}.tar.xz
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	gettext-devel
BuildRequires:	make
BuildRequires:	pkgconfig(libssl)

%description
Axel tries to accelerate the downloading process by using multiple
connections for one file. Starting from version 0.97, the program can use
different URL's for one download as well. The program tries to be as light
as possible (25-30k in binary form), so it might be useful as a wget clone
on byte-critical systems.

%files -f %{name}.lang
%{_bindir}/axel
%{_mandir}/man1/axel.1*

#----------------------------------------------------------------------------

%prep
%autosetup -p1
%configure

%build
%make_build

%install
%make_install

%find_lang %{name}
