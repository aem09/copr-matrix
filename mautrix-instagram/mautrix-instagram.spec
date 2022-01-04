%global srcname mautrix-instagram

%{?python_enable_dependency_generator}

%global forgeurl https://github.com/mautrix/instagram
%global commit b3779f7c5624b6f0e0d56d7ec6e42b82ad82d67b
Version:    0.1.2~rc6

%forgemeta

Name:       mautrix-instagram
Release:    1%{?dist}
Summary:    Matrix to instagram messenger bridge written in python.
License:    AGPL 3
URL:        %{forgeurl}
Source0:    %{forgesource}
Source1:    mautrix-instagram.service
BuildArch:  noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  systemd-rpm-macros

Requires:       systemd

#Manually include the end-to-end dependencies.
#This is because python-olm is called libolm-python3 in fedora.
Requires:       libolm-python3
Requires:       python3-unpaddedbase64
%py_provides    mautrix-instagram+e2be

Suggests:       mautrix-instagram+imageconvert

%{?systemd_requires}

%description
instagram to Matrix Bridge

%{?python_extras_subpkg:%python_extras_subpkg -n %{name} -i %{python3_sitelib}/*.egg-info metrics imageconvert}

%prep
%forgesetup
%autopatch -p0

%build
%py3_build

%install
%py3_install

install -p -D -T -m 0600 %{buildroot}%{python3_sitelib}/mautrix_instagram/example-config.yaml %{buildroot}%{_sysconfdir}/mautrix/instagram/config.yaml
rm -r %{buildroot}%{_prefix}/example-config.yaml

install -p -D -T -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/mautrix-instagram.service

%post
%systemd_post mautrix-instagram.service

%preun
%systemd_preun mautrix-instagram.service

%postun
%systemd_postun_with_restart mautrix-instagram.service


%files
%license LICENSE
%doc *.md
%{python3_sitelib}/mautrix_instagram/
%{python3_sitelib}/mautrix_instagram*.egg-info/

%{python3_sitelib}/mauigpapi/

%{_unitdir}/mautrix-instagram.service
%attr(755,root,root) %dir %{_sysconfdir}/mautrix/instagram
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/mautrix/instagram/*
