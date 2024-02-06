# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-pyopenssl
Epoch: 100
Version: 24.1.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Python wrapper module around the OpenSSL library
License: Apache-2.0
URL: https://github.com/pyca/pyopenssl/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-cryptography >= 41.0.5
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
High-level wrapper around a subset of the OpenSSL library.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500 || 0%{?rhel} == 7
%package -n python%{python3_version_nodots}-pyOpenSSL
Summary: Python wrapper module around the OpenSSL library
Requires: python3
Requires: python3-cryptography >= 41.0.5
Provides: python3-pyOpenSSL = %{epoch}:%{version}-%{release}
Provides: python3dist(pyOpenSSL) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pyOpenSSL = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pyOpenSSL) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pyOpenSSL = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pyOpenSSL) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-pyOpenSSL
High-level wrapper around a subset of the OpenSSL library.

%files -n python%{python3_version_nodots}-pyOpenSSL
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?rhel} == 7)
%package -n python3-pyOpenSSL
Summary: Python wrapper module around the OpenSSL library
Requires: python3
Requires: python3-cryptography >= 41.0.5
Provides: python3-pyOpenSSL = %{epoch}:%{version}-%{release}
Provides: python3dist(pyOpenSSL) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pyOpenSSL = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pyOpenSSL) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pyOpenSSL = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pyOpenSSL) = %{epoch}:%{version}-%{release}

%description -n python3-pyOpenSSL
High-level wrapper around a subset of the OpenSSL library.

%files -n python3-pyOpenSSL
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
