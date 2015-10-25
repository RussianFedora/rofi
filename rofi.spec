Name:          rofi
Version:       0.15.10
Release:       1%{?dist}
Summary:       A window switcher, run dialog and dmenu replacement

License:       MIT
URL:           https://davedavenport.github.io/rofi/
Source0:       https://github.com/DaveDavenport/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(libstartup-notification-1.0)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(cairo-xlib)
BuildRequires: i3

%description
A popup window switcher roughly based on superswitcher, requiring
only xlib and pango.
                                                              
%prep
%setup -q

%build
%configure --disable-silent-rules
%make_build

%install
%make_install

%check
make test

%files
%doc AUTHORS Changelog README.html README.md Examples
%license COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}-sensible-terminal
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/%{name}-sensible-terminal.1.*

%changelog
* Sun Oct 25 2015 Maxim Orlov <murmansksity@gmail.com> - 0.15.10-1.R
- Update to 0.15.10

* Sun Sep 06 2015 Maxim Orlov <murmansksity@gmail.com> - 0.15.8-1.R
- Update to 0.15.8

* Fri Jul 24 2015 Maxim Orlov <murmansksity@gmail.com> - 0.15.7-1.R
- Update to 0.15.7

* Sun Apr 20 2014 Dmitry Melnichenko 0-1.gitd64345c
- Initial import based on commit d64345ccbef1a6ef61a3e693084b6f73480fb176
