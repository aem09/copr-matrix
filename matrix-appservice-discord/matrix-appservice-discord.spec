%global forgeurl https://github.com/Half-Shot/matrix-appservice-discord
Version: 1.0.1~rc2
#global tag #version
%global commit 172fedf1b2577b09741553a036bcb63d2bc91fb3

%forgemeta

Name:           matrix-appservice-discord
Release:        2%{?dist}
Summary:        Matrix Bridge for Discord.

License:        Apache 2
URL:            %forgeurl
Source0:        %forgesource
Source1:        %{name}.service

# One of the dependencies has two -- in it and I can't seem to fix it.
AutoProv: no
Provides: config(%{name}) 

BuildRequires:  nodejs-devel
BuildRequires:  npm
BuildRequires:  systemd-rpm-macros
BuildRequires:  git
BuildRequires:  make
BuildRequires:  g++

Requires:       nodejs

%global debug_package %{nil}

%description
Matrix bridge for Discord.

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%prep
%forgesetup

%build
npm install --no-audit --no-fund
#npm run build
chmod -R -x+X *

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{name}
cp -pr \
    package.json \
    build \
    %{buildroot}%{nodejs_sitelib}/%{name}
cp -pr node_modules %{buildroot}%{nodejs_sitelib}/%{name}

install -m 600 -D config/config.sample.yaml %{buildroot}%{_sysconfdir}/%{name}/config.yaml
install -m 644 -D %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

%files
%license LICENSE
%doc README.md
%{nodejs_sitelib}/%{name}
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/%{name}

%changelog
* Fri Feb 26 12:10:49 GMT 2021 Alex Manning <git@alex-m.co.uk>
-
