%global srcname mautrix
#global tag v0.15.0-rc4

Name:           python-%{srcname}
Version:        0.15.8
Release:        1%{?dist}
Summary:        A Python 3.6+ asyncio Matrix framework.

License:        MPLv2.0
URL:            https://pypi.org/project/mautrix/
Source0:        %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
A Python 3.6+ asyncio Matrix framework.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sqlalchemy
BuildRequires:  python3-ruamel-yaml
BuildRequires:  libolm-python3
BuildRequires:  python3-CommonMark
BuildRequires:  python3-yarl
BuildRequires:  python3-attrs
BuildRequires:  python3-aiohttp
BuildRequires:  python3-asyncpg
BuildRequires:  python3-unpaddedbase64
BuildRequires:  python3-crypto
BuildRequires:  python3-lxml

Provides: python3.10dist(mautrix) = 0.15~rc4

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

#check
#{python3} setup.py test

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/
