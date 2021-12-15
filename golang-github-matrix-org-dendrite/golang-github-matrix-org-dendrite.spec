# Generated by go2rpm 1.5.0
%bcond_without check

%global go_generate_buildrequires %{nil}

# https://github.com/matrix-org/dendrite
%global goipath         github.com/matrix-org/dendrite
Version:                0.5.1
%global tag             v%{version}

%gometa

%global common_description %{expand:
Dendrite is a second-generation Matrix homeserver written in Go!}

%global golicenses      LICENSE
%global godocs          docs README.md CHANGES.md appservice/README.md\\\
                        mediaapi/README.md syncapi/README.md\\\
                        roomserver/README.md clientapi/README.md\\\
                        cmd/goose/README.md cmd/dendrite-demo-\\\
                        yggdrasil/README.md build/docker/README.md\\\
                        build/scripts/README.md keyserver/README.md

Name:           matrix-dendrite
Release:        1%{?dist}
Summary:        Dendrite is a second-generation Matrix homeserver written in Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        dendrite.service

BuildRequires:   git
BuildRequires:   breezy
BuildRequires:   systemd

Requires(pre):  shadow-utils
Requires:       systemd
%{?systemd_requires}

%global gocompilerflags -mod=vendor %gocompilerflags
%global gomodulesmode GO111MODULE=auto

%if %{with check}
# Tests
BuildRequires:  golang(github.com/DATA-DOG/go-sqlmock)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep -k
cd %{_builddir}/dendrite-%{version}
go mod edit \
    -replace launchpad.net/gocheck=gopkg.in/check.v1@22ab2dfb190cbb38b02b67920174fe020e164d0e \
    -replace launchpad.net/xmlpath=gopkg.in/xmlpath.v1@a146725ea6e7e357ca683ef3e02e8a403742b9c0
go mod vendor -v

%pre
getent group dendrite >/dev/null || groupadd -r dendrite
getent passwd dendrite >/dev/null || \
    useradd -r -g dendrite -d %{_sharedstatedir}/dendrite -s /sbin/nologin \
    -c "The user for the dendrite Matrix server" dendrite
exit 0

%post
%systemd_post dendrite.service

%preun
%systemd_preun dendrite.service

%postun
%systemd_postun_with_restart dendrite.service

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall

install -m 0755 -vd                     %{buildroot}/%{_sharedstatedir}/dendrite

install -m 0755 -vd                     %{buildroot}%{_libexecdir}/dendrite
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_libexecdir}/dendrite/

install -m 0755 -vd                      %{buildroot}%{_sysconfdir}/dendrite
install -m 0644 -vp dendrite-config.yaml %{buildroot}%{_sysconfdir}/dendrite/dendrite-config.yaml

install -m 0644 -vpD %{SOURCE1}          %{buildroot}%{_unitdir}/dendrite.service


%if %{with check}
%check
mkdir ./testdeps
export PATH=$PWD/testdeps:$PATH
cp /usr/bin/go-rpm-integration ./testdeps/go-rpm-integration
sed -i "s/GO111MODULE=off/GO111MODULE=auto/g" ./testdeps/go-rpm-integration
sed -i "s/GO111MODULE: off/GO111MODULE: auto/g" ./testdeps/go-rpm-integration
%gocheck
%endif

%files
%license LICENSE
%doc docs README.md CHANGES.md appservice/README.md mediaapi/README.md
%doc syncapi/README.md roomserver/README.md clientapi/README.md
%doc cmd/goose/README.md cmd/dendrite-demo-yggdrasil/README.md
%doc build/docker/README.md build/scripts/README.md keyserver/README.md

%dir %{_sysconfdir}/dendrite
%config(noreplace) %{_sysconfdir}/dendrite/*

%dir %{_libexecdir}/dendrite
%{_libexecdir}/dendrite/*

%{_unitdir}/dendrite.service

%gopkgfiles

%changelog
* Mon Sep 06 2021 Alexander Manning <mail@alex-m.co.uk> - 0.5.0-1%{?dist}
- Initial package
