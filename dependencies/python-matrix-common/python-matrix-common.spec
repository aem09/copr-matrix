# Created by pyp2rpm-3.3.8
%global pypi_name matrix_common

Name:           python-%{pypi_name}
Version:        1.2.1
Release:        0%{?dist}
Summary:        Common utilities for Synapse, Sydent and Sygnal

License:        ASL
URL:            https://github.com/matrix-org/matrix-python-common
Source:         %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Common utilities for Synapse, Sydent and Sygnal.
}
%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

#check
#tox

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.*

%changelog
