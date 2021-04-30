%global srcname asyncpg

Name:           python-%{srcname}
Version:        0.21.0
Release:        1%{?dist}
Summary:        asyncpg is a database interface library designed specifically for PostgreSQL and Python/asyncio.

License:        ASL 2.0
URL:            https://pypi.org/project/asyncpg/
Source0:        %{pypi_source}

%global _description %{expand:
asyncpg is a database interface library designed specifically for PostgreSQL and Python/asyncio. asyncpg is an efficient, clean implementation of PostgreSQL server binary protocol for use with Python’s asyncio frameworki.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# Required only for tests.
BuildRequires:  python3-sqlalchemy
BuildRequires:  python3-ruamel-yaml
BuildRequires:  libpq-devel
BuildRequires:  postgresql-server
BuildRequires:  postgresql-contrib
BuildRequires:  gcc

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{python3} setup.py test

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitearch}/%{srcname}-*.egg-info/
%{python3_sitearch}/%{srcname}/
