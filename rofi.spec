%global commit d64345ccbef1a6ef61a3e693084b6f73480fb176
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           rofi
Version:        0
Release:        1.git%{shortcommit}%{?dist}
Summary:        A popup window switcher and launcher

License:        MIT/X11
URL:            https://github.com/DaveDavenport/rofi
Source0:        https://github.com/DaveDavenport/rofi/archive/%{commit}/rofi-%{commit}.tar.gz

BuildRequires:  autoconf
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(libxdg-basedir)
BuildRequires:  i3

%description
A popup window switcher and launcher, requiring only xlib and xft.

%prep
%setup -qn %{name}-%{commit}
autoreconf --install

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%doc COPYING README.md
%{_bindir}/rofi
%{_mandir}/man1/rofi.1.*

%changelog
* Sun Apr 20 2014 Dmitry Melnichenko 0-1.gitd64345c
- Initial import based on commit d64345ccbef1a6ef61a3e693084b6f73480fb176
