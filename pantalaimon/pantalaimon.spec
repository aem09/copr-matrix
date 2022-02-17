%{?!python3_pkgversion:%global python3_pkgversion 3}

%global forgeurl https://github.com/matrix-org/pantalaimon
Version:        0.10.4
%global tag     %version

BuildArch:      noarch

%forgemeta

Name:           pantalaimon
Release:        3%{?dist}
Summary:        A Matrix proxy daemon that adds E2E encryption capabilities
License:        Apache License, Version 2.0
URL:            %forgeurl
Source0:        %forgesource
Source1:        pantalaimon.service

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  systemd-rpm-macros

%{?python_enable_dependency_generator}

Requires:       libolm-devel

%description
pantalaimon Pantalaimon is an end-to-end encryption aware Matrix reverse proxy
daemon. Pantalaimon acts as a good man in the middle that handles the
encryption for you.Messages are transparently encrypted and decrypted for
clients inside of pantalaimon.![Pantalaimon in
action](docs/pan.gif)Installation The [Olm]( C library is required to be
installed before installing pantalaimon.If your...

%{?python_extras_subpkg:%python_extras_subpkg -n %{name} -i %{python3_sitelib}/*.egg-info ui}

%prep
%forgesetup

sed -i 's|"PyGObject >= 3.36, < 3.39"|"PyGObject >= 3.36, < 4"|g' setup.py

%build
%py3_build

%install
%py3_install

mkdir -p %{buildroot}%{_mandir}/man{1,5,8}
cp docs/man/*.1 %{buildroot}%{_mandir}/man1
cp docs/man/*.5 %{buildroot}%{_mandir}/man5
cp docs/man/*.8 %{buildroot}%{_mandir}/man8

install -p -D -T -m 0644 contrib/pantalaimon.service %{buildroot}%{_userunitdir}/%{name}.service
install -p -D -T -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

install -p -D -T -m 0644 contrib/pantalaimon.conf %{buildroot}%{_sysconfdir}/pantalaimon/pantalaimon.conf

%post
%systemd_post %{name}.service
%systemd_user_post %{name}.service

%preun
%systemd_preun %{name}.service
%systemd_user_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service
%systemd_user_postun_with_restart %{name}.service

%files
%license LICENSE
%doc README.md

%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}*.egg-info/

%{_mandir}/man{1,5,8}/*
%{_bindir}/panctl
%{_bindir}/pantalaimon

%{_userunitdir}/%{name}.service
%{_unitdir}/%{name}.service

%attr(755,root,root) %dir %{_sysconfdir}/%{name}
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/pantalaimon.conf

%changelog
* Thu May 13 14:12:55 BST 2021 Alex Manning <git@alex-m.co.uk>
-
