Name:           matrix-appservice-discord
Version:        1.0.0
Release:        1%{?dist}
Summary:        Bridge Discord to Matrix

License:        Apache plus many bundled ones.
URL:            https://github.com/Half-Shot/matrix-appservice-discord
Source0:        matrix-appservice-discord-%{version}.tgz

BuildRequires: nodejs-devel

ExclusiveArch: %{nodejs_arches} noarch


%description
%summary

%prep
%autosetup -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{name}
cp -pr * %{buildroot}%{nodejs_sitelib}/%{name}


%files
%license LICENSE
%doc README.md
%{nodejs_sitelib}/%{name}

%changelog
* Sat Feb 27 00:15:40 GMT 2021 Alex Manning <git@alex-m.co.uk>
-
