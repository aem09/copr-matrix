# Generated by go2rpm 1.3
%bcond_without check

%global go_generate_buildrequires %{nil}

%global commit 1ebfeedcb70181034ab863b89b63f0db10be16e9

# https://github.com/tulir/mautrix-whatsapp
%global goipath         maunium.net/go/mautrix-whatsapp
%global forgeurl        https://github.com/mautrix/whatsapp
Version:                0.2.3~rc2

%global goname mautrix-whatsapp

%gometa

%global common_description %{expand:
A Matrix-WhatsApp puppeting bridge.}

%global golicenses      LICENSE
%global godocs          README.md ROADMAP.md helm/mautrix-\\\
                        whatsapp/templates/NOTES.txt

Name:           %{goname}
Release:        1%{?dist}
Summary:        A Matrix-WhatsApp puppeting bridge

License:        AGPL-3.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        mautrix-whatsapp.service

BuildRequires:  git

BuildRequires:  libolm-devel
BuildRequires:  libolm

BuildRequires:  libstdc++-devel
BuildRequires:  libstdc++
BuildRequires:  libstdc++-static

BuildRequires: systemd-rpm-macros

%{?systemd_requires}

%global gomodulesmode GO111MODULE=auto

%description
%{common_description}

%gopkg

%prep
%goprep -k

sed -i '/\/\/go:build !cgo || nocrypto/ a // +build !cgo nocrypto' no-crypto.go
sed -i '/\/\/go:build cgo && !nocrypto/ a // +build cgo,!nocrypto' crypto.go
sed -i '\/\/go:build cgo && !nocrypto/ a // +build cgo,!nocrypto' database/cryptostore.go

%build
%gobuild -o %{gobuilddir}/bin/mautrix-whatsapp %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

install -p -D -T -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/mautrix-whatsapp.service
install -p -D -T -m 0644 %{gobuilddir}/../example-config.yaml %{buildroot}%{_sysconfdir}/mautrix/whatsapp/config.yaml

%post
%systemd_post mautrix-whatsapp.service

%preun
%systemd_preun mautrix-whatsapp.service

%postun
%systemd_postun_with_restart mautrix-whatsapp.service

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc README.md ROADMAP.md
%{_bindir}/*

%{_unitdir}/mautrix-whatsapp.service
%attr(755,root,root) %dir %{_sysconfdir}/mautrix/whatsapp
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/mautrix/whatsapp/*

%gopkgfiles

%changelog
* Sun Jan 31 11:31:33 GMT 2021 Alex Manning <git@alex-m.co.uk> - 0.1.5-1
- Initial package
