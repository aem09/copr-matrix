%global debug_package %{nil}
%global forgeurl https://gitlab.com/signald/signald
#global commit 986558ee528e39d5f53668e3125ac2bee7db5637
Version:        0.17.0

%forgemeta

# Signald is built using gradle, and try as I might I can't get it to build in any other way/offline.
# So this requires an online build.

Name:           signald
Release:        1%{?dist}
Summary:        Signald

License:        GPL
URL:            %forgeurl
Source0:        %forgesource
Source1:        signald.service

BuildRequires:  git
BuildRequires:  java-devel
BuildRequires:  make
BuildRequires:  systemd-rpm-macros

Requires:       java-headless

%description
Signald

%prep
%forgesetup

%build
make installDist
sed -i 's|$APP_HOME|%{_libdir}/%{name}|g' build/install/signald/bin/signald
rm build/install/signald/bin/signald.bat

%install
mkdir -p %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_bindir}

cp -r build/install/signald/lib %{buildroot}%{_libdir}/%{name}/lib
cp build/install/signald/bin/signald %{buildroot}%{_bindir}/

install -p -D -T -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/signald.service

%post
%systemd_post signald.service

%preun
%systemd_preun signald.service

%postun
%systemd_postun_with_restart signald.service

%files
%{_libdir}/%{name}
%{_bindir}/signald
%{_unitdir}/signald.service

%license LICENSE
%doc README.md

%changelog
* Tue May 11 13:45:15 BST 2021 Alex Manning <git@alex-m.co.uk>
-
