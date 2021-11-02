Name:           matrix-systemd-target
Version:        0.0.1
Release:        1%{?dist}
Summary:        Systemd Target and Slice for matrix bridges.

License:        ?
URL:            https://github.com/aem09/copr-matrix
Source0:        matrix.target
Source1:        matrix.slice

BuildRequires:  systemd-rpm-macros
Requires:       systemd

%description
Systemd Target and Slice for matrix bridges.

%prep
%autosetup

#build
#configure
#make_build

%install
install -m 644 -D %{SOURCE0} %{buildroot}%{_unitdir}/matrix.target
install -m 644 -D %{SOURCE1} %{buildroot}%{_unitdir}/matrix.slice

%files
%{_unitdir}/matrix.target
%{_unitdir}/matrix.slice
#license add-license-file-here

%changelog
* Wed Jun 16 21:21:26 BST 2021 Alexander Manning <mail@alex-m.co.uk>
-
