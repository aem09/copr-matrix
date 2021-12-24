%{?python_enable_dependency_generator}

%global forgeurl https://github.com/mautrix/signal
%global commit 986558ee528e39d5f53668e3125ac2bee7db5637
Version:    0.2.2~rc3

%forgemeta

Name:       mautrix-signal
Release:    1%{?dist}
Summary:    Matrix to signal messenger bridge written in python.
License:    AGPL 3
URL:        %{forgeurl}
Source0:    %{forgesource}
Source1:    mautrix-signal.service
BuildArch:  noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  systemd-rpm-macros

Requires:       systemd
Requires:       signald

#Manually include the end-to-end dependencies.
#This is because python-olm is called libolm-python3 in fedora.
Requires:       libolm-python3
Requires:       python3-unpaddedbase64
%py_provides    mautrix-signal+e2be

Suggests:       mautrix-signal+formattednumbers
Suggests:       mautrix-signal+qrlink
Suggests:       mautrix-signal+stickers

%{?systemd_requires}

%description
signal to Matrix Bridge

%{?python_extras_subpkg:%python_extras_subpkg -n %{name} -i %{python3_sitelib}/*.egg-info metrics formattednumbers qrlink stickers}

%prep
%forgesetup
%autopatch -p0

%build
%py3_build

%install
%py3_install

install -p -D -T -m 0600 %{buildroot}%{python3_sitelib}/mautrix_signal/example-config.yaml %{buildroot}%{_sysconfdir}/mautrix/signal/config.yaml
rm -r %{buildroot}%{_prefix}/example-config.yaml

install -p -D -T -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/mautrix-signal.service

%post
%systemd_post mautrix-signal.service

%preun
%systemd_preun mautrix-signal.service

%postun
%systemd_postun_with_restart mautrix-signal.service


%files
%license LICENSE
%doc *.md
%{python3_sitelib}/mautrix_signal/
%{python3_sitelib}/mautrix_signal*.egg-info/

%{python3_sitelib}/mausignald/

%{_unitdir}/mautrix-signal.service
%attr(755,root,root) %dir %{_sysconfdir}/mautrix/signal
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/mautrix/signal/*
