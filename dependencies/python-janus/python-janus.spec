# Created by pyp2rpm-3.3.5
%global pypi_name janus

Name:           python-%{pypi_name}
Version:        0.6.1
Release:        1%{?dist}
Summary:        Mixed sync-async queue to interoperate between asyncio tasks and classic threads

License:        Apache 2
URL:            https://github.com/aio-libs/janus/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest) >= 5.4
BuildRequires:  python3dist(pytest-asyncio) >= 0.10
BuildRequires:  python3dist(setuptools)

%description
 janus Mixed sync-async queue, supposed to be used for communicating between
classic synchronous (threaded) code and asynchronous (in terms of asyncio_)
one.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
 janus Mixed sync-async queue, supposed to be used for communicating between
classic synchronous (threaded) code and asynchronous (in terms of asyncio_)
one.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Thu May 13 2021 Alex Manning <git@alex-m.co.uk> - 0.6.1-1
- Initial package.
