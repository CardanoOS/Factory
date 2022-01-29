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

%global device_name ledger
%global pkg_name %{device_name}-udev-rules

Name:           %{pkg_name}
Version:        1631263597.2776324
Release:        0
Summary:        Ledger udev rules list
License:        Apache-2.0
Group:          Productivity/Security
URL:            https://github.com/LedgerHQ/udev-rules
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(systemd)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Udev rules to connect a Ledher hardware wallet to your Linux box

%prep
%setup -q

%build
rm add_udev_rules.sh
mv 20-hw1.rules 20-ledger.rules

%install
install -D -m 0644 -t %{buildroot}%{_udevrulesdir} 20-ledger.rules

%post
%udev_rules_update

%postun
%udev_rules_update

%files
%license LICENSE
%doc README.md
%{_udevrulesdir}/20-ledger.rules

%changelog
