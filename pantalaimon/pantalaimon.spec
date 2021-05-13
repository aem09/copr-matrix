%{?!python3_pkgversion:%global python3_pkgversion 3}

%global forgeurl https://github.com/matrix-org/pantalaimon
Version:        0.9.2
%global tag     %version

BuildArch:      noarch

%forgemeta

Name:           pantalaimon
Release:        1%{?dist}
Summary:        A Matrix proxy daemon that adds E2E encryption capabilities
License:        Apache License, Version 2.0
URL:            %forgeurl
Source0:        %forgesource

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%{?python_enable_dependency_generator}

Requires:       libolm-devel

%description
pantalaimon Pantalaimon is an end-to-end encryption aware Matrix reverse proxy
daemon. Pantalaimon acts as a good man in the middle that handles the
encryption for you.Messages are transparently encrypted and decrypted for
clients inside of pantalaimon.![Pantalaimon in
action](docs/pan.gif)Installation The [Olm]( C library is required to be
installed before installing pantalaimon.If your...

%{?python_extras_subpkg:%python_extras_subpkg -n python%{python3_pkgversion}-%{name} -i %{python3_sitelib}/*.egg-info ui}

%prep
%forgesetup

%build
%py3_build

%install
%py3_install

mkdir -p %{buildroot}%{_mandir}/man{1,5,8}
cp docs/man/*.1 %{buildroot}%{_mandir}/man1
cp docs/man/*.5 %{buildroot}%{_mandir}/man5
cp docs/man/*.8 %{buildroot}%{_mandir}/man8

%files
%license LICENSE
%doc README.md

%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info/

%{_mandir}
%{_bindir}



%changelog
* Thu May 13 14:12:55 BST 2021 Alex Manning <git@alex-m.co.uk>
-
