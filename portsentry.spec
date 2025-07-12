Name:		portsentry
Version:	2.0.2
Release:	1
Source0:	https://github.com/portsentry/portsentry/archive/v%{version}/%{name}-%{version}.tar.gz
# PATCH to fix  cmake issue where files are installed to /usr/etc instead of /etc
Patch0:		portsentry-2.0.2.patch0
Summary:	Portsentry monitors network traffic in order to detect port scans in real-time. 
URL:		https://github.com/portsentry/portsentry
License:	GPL
Group:		Networking/Other
BuildRequires:	cmake
BuildRequires:	pkgconfig(libpcap)
BuildSystem:	cmake

%description
Portsentry monitors network traffic in order to detect port scans in real-time.
It can identify several types of scans, including TCP, SYN, FIN, XMAS, and NULL
scans and UDP probing.

%prep
echo %doc
%autosetup -p1

%files
%{_bindir}/%{name}


%{_sysconfdir}/logrotate.d/%{name}
%{_sysconfdir}/%{name}/%{name}.*
%{_unitdir}/%{name}.service
%{_docdir}/%{name}/*
%{_mandir}/man8/%{name}*.8.zst
