Name: rofi
Version: 0.15.7
Release: 1%{?dist}
Summary: A window switcher, run dialog and dmenu replacement

License: MIT
URL: https://davedavenport.github.io/rofi/
Source0: https://github.com/DaveDavenport/rofi/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: automake 
BuildRequires: autoconf 
BuildRequires: pkgconfig(xft)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(libxdg-basedir)

%description
A popup window switcher roughly based on superswitcher,
requiring only xlib and pango.

%prep
%setup -q
autoreconf -i

%build
%configure
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%doc AUTHORS Changelog README.html README.md 
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/rofi.1.*

%changelog
* Fri Jul 24 2015 Maxim Orlov <murmansksity@gmail.com> - 0.15.7-1.R
- Update to 0.15.7

* Sun Apr 20 2014 Dmitry Melnichenko 0-1.gitd64345c
- Initial import based on commit d64345ccbef1a6ef61a3e693084b6f73480fb176
