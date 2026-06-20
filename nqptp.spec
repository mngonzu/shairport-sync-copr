Name:           nqptp
Version:        1.2.8
Release:        1%{?dist}
Summary:        Not Quite PTP - A daemon that monitors timing data from PTP clocks

License:        GPL-2.0-only
URL:            https://github.com/mikebrady/nqptp
Source0:        https://github.com/mikebrady/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  systemd-rpm-macros

Requires:       systemd

%description
nqptp is a daemon that monitors timing data from PTP clocks it sees on ports 
319 and 320. It maintains records for one clock, identified by its Clock ID. 
It is a companion application to Shairport Sync and provides timing 
information for AirPlay 2 operation.

%prep
%autosetup

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

# Install systemd service files natively
install -D -m 0644 nqptp.service %{buildroot}%{_unitdir}/nqptp.service

%post
%systemd_post nqptp.service

%preun
%systemd_preun nqptp.service

%postun
%systemd_postun_with_restart nqptp.service

%files
%license LICENSE
%doc README.md
%{_bindir}/nqptp
%{_unitdir}/nqptp.service
%{_mandir}/man8/nqptp.8*

%changelog
* Sat Jun 20 2026 Your Name <youremail@example.com> - 1.2.4-1
- Initial build configuration for Fedora Copr tracking upstream 1.2.4
