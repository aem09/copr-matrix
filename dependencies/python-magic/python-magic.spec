# Created by pyp2rpm-3.3.5
%global pypi_name python-magic
%global srcname python-magic

Name:           python-magic
Version:        0.4.22
Release:        1%{?dist}
Epoch:          1
Summary:        File type identification using libmagic

License:        PSF
URL:            http://github.com/ahupp/python-magic
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
This module uses ctypes to access the libmagic file type identification
library. It makes use of the local magic database and supports both textual and
MIME-type output.

%package -n     python3-magic
Summary:        %{summary}
%{?python_provide:%python_provide python3-magic}

%description -n python3-magic
This module uses ctypes to access the libmagic file type identification
library. It makes use of the local magic database and supports both textual and
MIME-type output.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-magic
#%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/magic/*
%{python3_sitelib}/python_magic-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Apr 30 2021 Alex Manning <git@alex-m.co.uk> - 0.2-1
- Initial package.
