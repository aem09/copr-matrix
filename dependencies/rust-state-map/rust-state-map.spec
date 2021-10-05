# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate state-map
%global forgeurl https://github.com/matrix-org/rust-matrix-state-map
%global branch master
%forgemeta

Name:           rust-%{crate}
Version:        0.1.0
Release:        1%{?dist}
Summary:        A container for memory efficient handling of Matrix state maps.

License:        ASL2

URL:            %{forgeurl}
Source:         %{forgesource}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
A container for memory efficient handling of Matrix state maps.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%forgesetup
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Tue Oct 05 12:45:41 BST 2021 Alexander Manning <mail@alex-m.co.uk> - 0.1.0-1
- Initial package
