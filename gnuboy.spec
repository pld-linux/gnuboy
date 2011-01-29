Summary:	gnuboy - a Nintendo GameBoy Color emulator
Summary(pl.UTF-8):	gnuboy - emulator platformy Nintendo GameBoy Color
Name:		gnuboy
Version:	1.0.3
Release:	3
License:	GPL v2+
Group:		Applications/Emulators
Source0:	http://gnuboy.unix-fu.org/src/%{name}-%{version}.tar.gz
# Source0-md5:	9947162a208ebfe699a1bfe98c437ac3
Patch0:		%{name}-gcc.patch
URL:		http://gnuboy.unix-fu.org/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	xorg-lib-libXext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnuboy is a portable program for emulating the Nintendo GameBoy Color
software platform.

%description -l pl.UTF-8
gnuboy jest przenośnym emulatorem platformy programowej Nintendo
GameBoy Color.

%prep
%setup -q

%patch0 -p1

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
%{__make} install \
	bindir=$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc docs/* INSTALL README
