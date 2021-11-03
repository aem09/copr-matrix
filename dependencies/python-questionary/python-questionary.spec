# Created by pyp2rpm-3.3.5
%global pypi_name questionary

Name:           python-%{pypi_name}
Version:        1.10.0
Release:        1%{?dist}
Summary:        Python library to build pretty command line user prompts ⭐️

License:        None
URL:            https://github.com/tmbo/questionary
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
 Questionary[![Version]( [![License]( [![Continuous Integration]( [![Coverage](
[![Supported Python Versions]( [![Documentation](

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       (python3dist(prompt-toolkit) >= 2 with python3dist(prompt-toolkit) < 4)
#Requires:       (python3dist(sphinx) >= 3.3 with python3dist(sphinx) < 4)
#Requires:       (python3dist(sphinx-autobuild) >= 2020.9.1 with python3dist(sphinx-autobuild) < 2021)
#Requires:       (python3dist(sphinx-autodoc-typehints) >= 1.11.1 with python3dist(sphinx-autodoc-typehints) < 2)
#Requires:       (python3dist(sphinx-copybutton) >= 0.3.1 with python3dist(sphinx-copybutton) < 0.4)
#Requires:       (python3dist(sphinx-rtd-theme) >= 0.5 with python3dist(sphinx-rtd-theme) < 0.6)
%description -n python3-%{pypi_name}
 Questionary[![Version]( [![License]( [![Continuous Integration]( [![Coverage](
[![Supported Python Versions]( [![Documentation](


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Nov 03 2021 Alexander Manning <mail@alex-m.co.uk> - 1.10.0-1
- Initial package.
