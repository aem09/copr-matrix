# Created by pyp2rpm-3.3.8
%global pypi_name matrix_common
%global pypi_version 1.2.1

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Common utilities for Synapse, Sydent and Sygnal

License:        None
URL:            https://github.com/matrix-org/matrix-python-common
Source0:        %{pypi_name}-%{pypi_version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(aiounittest)
BuildRequires:  python3dist(aiounittest)
BuildRequires:  python3dist(attrs)
BuildRequires:  python3dist(black) = 22.3
#BuildRequires:  python3dist(build) = 0.8
BuildRequires:  python3dist(flake8) = 4.0.1
BuildRequires:  python3dist(importlib-metadata) >= 1.4
#BuildRequires:  python3dist(isort) = 5.9.3
#BuildRequires:  python3dist(mypy) = 0.910
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(tox)
BuildRequires:  python3dist(tox)
#BuildRequires:  python3dist(twine) = 4.0.1
BuildRequires:  python3dist(twisted)
BuildRequires:  python3dist(twisted)

%description
 matrix-python-commonCommon utilities for Synapse, Sydent and Sygnal.
Installationshell pip install matrix-common Usageimport matrix_common
DevelopmentIn a virtual environment with pip ≥ 21.1, runpip install -e .[dev]
To run the unit tests, you can either use:tox -e pyortrial tests To run the
linters and mypy type checker, use ./scripts-dev/lint.sh. ReleasingThe exact
steps for releasing will...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(aiounittest)
Requires:       python3dist(attrs)
Requires:       python3dist(importlib-metadata) >= 1.4
Requires:       python3dist(tox)
Requires:       python3dist(twisted)
%description -n python3-%{pypi_name}
 matrix-python-commonCommon utilities for Synapse, Sydent and Sygnal.
Installationshell pip install matrix-common Usageimport matrix_common
DevelopmentIn a virtual environment with pip ≥ 21.1, runpip install -e .[dev]
To run the unit tests, you can either use:tox -e pyortrial tests To run the
linters and mypy type checker, use ./scripts-dev/lint.sh. ReleasingThe exact
steps for releasing will...


%prep
%autosetup -n %{pypi_name}-%{pypi_version}
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
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Wed Jul 20 2022 Alex Manning <mail@alex-m.co.uk> - 1.2.1-1
- Initial package.
