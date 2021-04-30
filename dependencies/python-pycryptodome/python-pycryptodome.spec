# Created by pyp2rpm-3.3.5
%global pypi_name pycryptodome

Name:           python-%{pypi_name}
Version:        3.0
Release:        1%{?dist}
Summary:        Cryptographic library for Python

License:        Public Domain
URL:            http://www.pycryptodome.org
Source0:        %{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
PyCryptodome PyCryptodome is a self-contained Python package of low-level
cryptographic primitives. It is a fork of PyCrypto.It supports Python 2.4 or
newer, all Python 3 versions and PyPy.For more information, see the
homepage_... _homepage:

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
%{?python_provide:%python_provide python3-crypto}

Provides:   python3dist(pycrypto)

Conflicts:  python-crypto
Conflicts:  python3-crypto

BuildRequires: gcc
BuildRequires: gmp

%description -n python3-%{pypi_name}
PyCryptodome PyCryptodome is a self-contained Python package of low-level
cryptographic primitives. It is a fork of PyCrypto.It supports Python 2.4 or
newer, all Python 3 versions and PyPy.For more information, see the
homepage_... _homepage:

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE.rst Doc/LEGAL/copy/LICENSE.orig Doc/LEGAL/copy/LICENSE.libtom Doc/LEGAL/copy/LICENSE.python-2.2 Doc/src/license.rst
%doc README.rst
%{python3_sitearch}/Crypto
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Sat Mar 13 2021 Alex Manning <git@alex-m.co.uk> - 3.0-1
- Initial package.
