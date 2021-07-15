%{?!python3_pkgversion:%global python3_pkgversion 3}

#global forgeurl https://github.com/matrix-org/mjolnir
#global tag v0.1.17
%global forgeurl https://github.com/aem09/mjolnir
%global branch newinterface

%?python_enable_dependency_generator

%forgemeta

Name:           mjolnir
# The version of the python module, NOT the name of mjolnir as a whole.
Version:        0.0.2
Release:        1%{?dist}
Summary:        A moderation tool for Matrix. Visit #mjolnir:matrix.org for more information.
License:        Apache
URL:            %forgeurl
Source0:        %forgesource

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%{?python_enable_dependency_generator}

%global debug_package %{nil}

%description
...

%package -n python%{python3_pkgversion}-%{name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{name}}

%description -n python%{python3_pkgversion}-%{name}
...

%prep
%forgesetup

%build
cd synapse_antispam
%py3_build

%install
cd synapse_antispam
%py3_install

%files -n  python%{python3_pkgversion}-%{name}
%license LICENSE
%doc README.md docs/*.md
# For noarch packages: sitelib
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Wed Feb 24 15:27:51 GMT 2021 Alex Manning <git@alex-m.co.uk>
-
