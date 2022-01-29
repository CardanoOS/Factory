#
# spec file for package trezord-go
#
# Copyright (c) 2022 PERLUR Group
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://github.com/CardanoOS/Factory
#

%global device_name trezor
%global pkg_name %{device_name}d
%define project github.com/%{device_name}/%{pkg_name}-go

Name:           %{pkg_name}
Version:        2.0.31
Release:        0
Summary:	    TREZOR Communication Daemon
License:        LGPL-3.0
Group:          Productivity/Security
URL:            https://github.com/trezor/trezord-go
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Requires:       %{device_name}-udev-rules
Requires(pre):  shadow
BuildRequires:  golang-packaging
BuildRequires:  go >= 1.12

%description
TREZOR Communication Daemon aka TREZOR Bridge (written in Go). This is used for
communication between your browser and your TREZOR, for the purposes of sites
like <https://wallet.trezor.io>. It has a very simple REST interface that is
bound to localhost which allows for device operations.

%package -n %{device_name}-udev-rules
Summary:        Udev rules for accessing TREZOR devices
Group:          Hardware/Other
Requires:       udev

%description -n %{device_name}-udev-rules
This package contains the udev rules for allowing TREZOR devices to be accessed
by the running trezord. It is required in order for trezord to be run with
reduced privileges.

%prep
%setup -q
%setup -q -D -T -a 1

%build
%goprep %{project}
%gobuild --mod=vendor "" ...

%install
%goinstall
mv %{buildroot}%{_bindir}/%{name}-go %{buildroot}%{_bindir}/%{name}
install -D -m0644 release/linux/trezor.rules %{buildroot}%{_udevrulesdir}/51-%{device_name}.rules
install -D -m0644 release/linux/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
mkdir -p %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

%pre
%service_add_pre %{name}.service
# Set up the trezord user.
getent group trezord >/dev/null || groupadd -r trezord
getent group plugdev >/dev/null || groupadd -r plugdev
getent passwd trezord >/dev/null || useradd -r -g trezord -d "%{_localstatedir}" -s /bin/false -c "TREZOR Bridge" trezord
usermod -a -G plugdev trezord

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%post -n %{device_name}-udev-rules
%{?udev_rules_update:%{udev_rules_update}}

%files
%defattr(-,root,root)
%doc CHANGELOG.md README.md
%if 0%{?suse_version} >= 1500
%license COPYING
%else
%doc COPYING
%endif
%{_bindir}/%{name}
%{_sbindir}/rc%{name}
%{_unitdir}/%{name}.service

%files -n %{device_name}-udev-rules
%{_udevrulesdir}/51-%{device_name}.rules

%changelog
