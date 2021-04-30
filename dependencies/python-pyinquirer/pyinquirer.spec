# Created by pyp2rpm-3.3.5
%global pypi_name PyInquirer

Name:           python-%{pypi_name}
Version:        1.0.3
Release:        1%{?dist}
Summary:        A Python module for collection of common interactive command line user interfaces, based on Inquirer

License:        MIT
URL:            https://github.com/CITGuru/PyInquirer/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
 PythonInquirerA collection of common interactive command line user interfaces.
It is originally called [whaaaaaat]( created by **finklabs**, but due to bad
naming and in need of fixes, I decided to rename and apply some necessary fixes
on it. I'll also carry out the author's TODO. Table of Contents 1.
[Documentation](documentation) 1. [Installation](installation) 2.
[Examples](examples) 3....

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(prompt-toolkit) >= 1.0.14
Requires:       python3dist(pygments) >= 2.2
Requires:       python3dist(regex) >= 2016.11.21
%description -n python3-%{pypi_name}
 PythonInquirerA collection of common interactive command line user interfaces.
It is originally called [whaaaaaat]( created by **finklabs**, but due to bad
naming and in need of fixes, I decided to rename and apply some necessary fixes
on it. I'll also carry out the author's TODO. Table of Contents 1.
[Documentation](documentation) 1. [Installation](installation) 2.
[Examples](examples) 3....


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

rm -rf %{buildroot}%{python3_sitelib}

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Apr 30 2021 Alex Manning <git@alex-m.co.uk> - 1.0.0-1
- Initial package.
