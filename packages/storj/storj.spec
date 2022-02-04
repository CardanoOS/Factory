#
# spec file for package storj
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

%global pkg_name storj
%global provider_prefix %{pkg_name}.io
%global import_path     %{provider_prefix}


Name:           %{pkg_name}
Version:        1.47.3
Release:        0
Summary:	    Decentralized cloud storage, affordable, easy to use, private, and secure
License:        AGPL-3.0-only
Group:          Productivity/Networking/Other
URL:            https://storj.io/
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
BuildRequires:  golang-packaging
BuildRequires:  go >= 1.17

%description
Storj is an S3-compatible platform and suite of decentralized applications that
allows you to store data in a secure and decentralized manner. Your files are
encrypted, broken into little pieces and stored in a global decentralized
network of computers. Luckily, we also support allowing you (and only you) to
retrieve those files!

%package -n %{pkg_name}-identity
Summary:        Udev rules for accessing TREZOR devices

%description -n %{pkg_name}-identity
This package contains the udev rules for allowing TREZOR devices to be accessed
by the running trezord. It is required in order for trezord to be run with
reduced privileges.

%package -n %{pkg_name}-multinode
Summary:        Udev rules for accessing TREZOR devices

%description -n %{pkg_name}-multinode
This package contains the udev rules for allowing TREZOR devices to be accessed
by the running trezord. It is required in order for trezord to be run with
reduced privileges.

%package -n %{pkg_name}-storagenode-updater
Summary:        Udev rules for accessing TREZOR devices

%description -n %{pkg_name}-storagenode-updater
This package contains the udev rules for allowing TREZOR devices to be accessed
by the running trezord. It is required in order for trezord to be run with
reduced privileges.

%package -n %{pkg_name}-storagenode
Summary:        Udev rules for accessing TREZOR devices

%description -n %{pkg_name}-storagenode
This package contains the udev rules for allowing TREZOR devices to be accessed
by the running trezord. It is required in order for trezord to be run with
reduced privileges.

%package -n %{pkg_name}-uplinkng
Summary:        Udev rules for accessing TREZOR devices
License:        MIT

%description -n %{pkg_name}-uplinkng
This package contains the udev rules for allowing TREZOR devices to be accessed
by the running trezord. It is required in order for trezord to be run with
reduced privileges.

%package -n %{pkg_name}-uplink
Summary:        Udev rules for accessing TREZOR devices
License:        MIT


%description -n %{pkg_name}-uplink
This package contains the udev rules for allowing TREZOR devices to be accessed
by the running trezord. It is required in order for trezord to be run with
reduced privileges.

%prep
%setup -q
%setup -q -D -T -a 1

%build
%goprep %{provider_prefix}/%{pkg_name}/cmd/identity
%gobuild

%goprep %{provider_prefix}/%{pkg_name}/cmd/multinode
%gobuild

%goprep %{provider_prefix}/%{pkg_name}/cmd/storagenode-updater
%gobuild

%goprep %{provider_prefix}/%{pkg_name}/cmd/storagenode
%gobuild

%goprep %{provider_prefix}/%{pkg_name}/cmd/uplinkng
%gobuild

%goprep %{provider_prefix}/%{pkg_name}/cmd/uplink
%gobuild


%install
%goinstall
mv %{buildroot}/%{_bindir}/identity %{buildroot}/%{_bindir}/%{name}-identity
mv %{buildroot}/%{_bindir}/multinode %{buildroot}/%{_bindir}/%{name}-multinode
mv %{buildroot}/%{_bindir}/storagenode-updater %{buildroot}/%{_bindir}/%{name}-storagenode-updater
mv %{buildroot}/%{_bindir}/storagenode %{buildroot}/%{_bindir}/%{name}-storagenode
mv %{buildroot}/%{_bindir}/uplinkng %{buildroot}/%{_bindir}/%{name}-uplinkng
mv %{buildroot}/%{_bindir}/uplink %{buildroot}/%{_bindir}/%{name}-uplink

%files
%defattr(-,root,root)
%doc README.md
%if 0%{?suse_version} >= 1500
%license LICENSE
%else
%doc LICENSE
%endif

%files -n %{name}-identity
%{_bindir}/%{name}-identity

%files -n %{name}-multinode
%{_bindir}/%{name}-multinode

%files -n %{name}-storagenode-updater
%{_bindir}/%{name}-storagenode-updater

%files -n %{name}-storagenode
%{_bindir}/%{name}-storagenode-updater

%files -n %{name}-storagenode
%{_bindir}/%{name}-storagenode

%files -n %{name}-uplinkng
%{_bindir}/%{name}-uplinkng

%files -n %{name}-uplink
%{_bindir}/%{name}-uplink

%changelog
