# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/tulir/mautrix-whatsapp
%global goipath         maunium.net/go/mautrix-whatsapp
%global forgeurl        https://github.com/tulir/mautrix-whatsapp
Version:                0.1.6

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

Patch0:         logpath.patch

#BuildRequires:  golang(github.com/gorilla/websocket)
#BuildRequires:  golang(github.com/lib/pq)
#BuildRequires:  golang(github.com/mattn/go-sqlite3)
#BuildRequires:  golang(github.com/prometheus/client_golang/prometheus)
#BuildRequires:  golang(github.com/prometheus/client_golang/prometheus/promauto)
#BuildRequires:  golang(github.com/prometheus/client_golang/prometheus/promhttp)
#BuildRequires:  golang(github.com/Rhymen/go-whatsapp)
#BuildRequires:  golang(github.com/Rhymen/go-whatsapp/binary)
#BuildRequires:  golang(github.com/Rhymen/go-whatsapp/binary/proto)
#BuildRequires:  golang(github.com/skip2/go-qrcode)
#BuildRequires:  golang(gopkg.in/yaml.v2)
#BuildRequires:  golang(maunium.net/go/mauflag)
#BuildRequires:  golang(maunium.net/go/maulogger/v2)
#BuildRequires:  golang(maunium.net/go/mautrix)
#BuildRequires:  golang(maunium.net/go/mautrix/appservice)
#BuildRequires:  golang(maunium.net/go/mautrix/crypto)
#BuildRequires:  golang(maunium.net/go/mautrix/crypto/attachment)
#BuildRequires:  golang(maunium.net/go/mautrix/crypto/sql_store_upgrade)
#BuildRequires:  golang(maunium.net/go/mautrix/event)
#BuildRequires:  golang(maunium.net/go/mautrix/format)
#BuildRequires:  golang(maunium.net/go/mautrix/id)
#BuildRequires:  golang(maunium.net/go/mautrix/pushrules)

BuildRequires:  git

BuildRequires:  libolm-devel
BuildRequires:  libolm

BuildRequires:  libstdc++-devel
BuildRequires:  libstdc++
BuildRequires:  libstdc++-static

BuildRequires: systemd-rpm-macros

%{?systemd_requires}

%description
%{common_description}

%gopkg

%prep
%goprep
%autopatch

%generate_buildrequires
%go_generate_buildrequires

%build
%global gomodulesmode GO111MODULE=auto
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
