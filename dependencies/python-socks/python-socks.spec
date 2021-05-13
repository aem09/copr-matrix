%global undername python_socks

%global _description %{expand:
The python-socks package provides a core proxy client functionality for Python.
Supports SOCKS4(a), SOCKS5, HTTP (tunneling) proxy and provides sync and async
(asyncio, trio, curio) APIs. It is used internally by aiohttp-socks and
httpx-socks packages.
}

Name:           python-socks
Version:        1.2.4
Release:        1%{?dist}
Summary:        Core proxy (SOCKS4, SOCKS5, HTTP tunneling) functionality for Python

License:        ASL 2.0
URL:            https://github.com/romis2012/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-socks
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# For tests
# https://github.com/romis2012/python-socks/blob/master/requirements-dev.txt
BuildRequires:  %{py3_dist async-timeout}
BuildRequires:  %{py3_dist curio}
BuildRequires:  %{py3_dist flask}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-asyncio}
BuildRequires:  %{py3_dist pytest-trio}
BuildRequires:  %{py3_dist trio}
BuildRequires:  %{py3_dist yarl}

%description -n python3-socks %_description

# extras: asyncio, curio, trio
%{?python_extras_subpkg:%python_extras_subpkg -n python3-socks -i %{python3_sitelib}/*.egg-info asyncio curio trio}

%prep
%autosetup

%build
%py3_build

%install
%py3_install

%check
# https://github.com/romis2012/python-socks/blob/master/.travis.yml
%pytest tests/

%files -n python3-socks
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/%{undername}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{undername}

%changelog
* Tue May 11 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.2.4-1
- Use py3_dist marcos everywhere
- Remove unneeded egg info removal command

* Mon May 10 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.2.4-1
- use single line extras macro invocation

* Mon May 10 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.2.4-1
- do not use modname as a variable

* Mon May 10 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.2.4-1
- Use github tar
- Enable all tests and remove conditional
- Provide meta packages for extras
- Remove unneeded comments
- Remove weak deps: included by the automatic dep generator in extra sub-packages

* Mon May 10 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.2.4-1
- Initial package
