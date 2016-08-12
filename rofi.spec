%global glib2_version 2.40
%global xkbcommon_version 0.5.0

Name:          rofi
Version:       1.2.0
Release:       1%{?dist}
Summary:       A window switcher, run dialog and dmenu replacement

License:       MIT
URL:           https://davedavenport.github.io/rofi/
Source0:       https://github.com/DaveDavenport/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires: i3
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires: pkgconfig(libstartup-notification-1.0)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-ewmh)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-util)
BuildRequires: pkgconfig(xkbcommon) >= %{xkbcommon_version}
BuildRequires: pkgconfig(xkbcommon-x11)

%description
A popup window switcher roughly based on superswitcher.
                                                              
%prep
%autosetup

%build
%configure
%make_build V=1

%install
%make_install

%files
%doc AUTHORS Changelog README.md Examples
%license COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}-sensible-terminal
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/%{name}-sensible-terminal.1.*

%changelog
* Fri Aug 12 2016 Maxim Orlov <murmansksity@gmail.com> - 1.2.0-1.R
- Update to 1.2.0

* Tue Jun 14 2016 Maxim Orlov <murmansksity@gmail.com> - 1.1.0-1.R
- Update to 1.1.0

* Mon May 02 2016 Maxim Orlov <murmansksity@gmail.com> - 1.0.1-1.R
- Update to 1.0.1

* Sun Apr 17 2016 Maxim Orlov <murmansksity@gmail.com> - 1.0.0-1.R
- Update to 1.0.0
- Add xkbcommon dep version

* Sun Apr 03 2016 Maxim Orlov <murmansksity@gmail.com> - 1.0.0-0.1.rc1.R
- Update to 1.0.0rc1
- Add more BR's
- Use %%autosetup macro
- Remove tests
- Remove --enable-timings

* Sun Dec 27 2015 Maxim Orlov <murmansksity@gmail.com> - 0.15.12-1.R
- Update to 0.15.12

* Sun Nov 08 2015 Maxim Orlov <murmansksity@gmail.com> - 0.15.11-1.R
- Update to 0.15.11

* Sun Oct 25 2015 Maxim Orlov <murmansksity@gmail.com> - 0.15.10-1.R
- Update to 0.15.10

* Sun Sep 06 2015 Maxim Orlov <murmansksity@gmail.com> - 0.15.8-1.R
- Update to 0.15.8

* Fri Jul 24 2015 Maxim Orlov <murmansksity@gmail.com> - 0.15.7-1.R
- Update to 0.15.7

* Sun Apr 20 2014 Dmitry Melnichenko 0-1.gitd64345c
- Initial import based on commit d64345ccbef1a6ef61a3e693084b6f73480fb176
