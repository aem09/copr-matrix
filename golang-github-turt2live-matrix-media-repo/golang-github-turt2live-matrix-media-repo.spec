# Generated by go2rpm 1.5.0
%bcond_without check

%global go_generate_buildrequires %{nil}

# https://github.com/turt2live/matrix-media-repo
%global goipath         github.com/turt2live/matrix-media-repo
Version:                1.2.12

%gometa

%global common_description %{expand:
Matrix media repository with multi-domain in mind.}

%global golicenses      LICENSE
%global godocs          docs README.md CONTRIBUTING.md CHANGELOG.md

Name:           matrix-media-repo
Release:        1%{?dist}
Summary:        Matrix media repository with multi-domain in mind

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        matrix-media-repo.service

BuildRequires:   git
BuildRequires:   systemd

Requires:       systemd
%{?systemd_requires}

%global gocompilerflags -mod=vendor %gocompilerflags
%global gomodulesmode GO111MODULE=auto

%description
%{common_description}

%gopkg

%prep
%goprep -k

cd %{_builddir}/matrix-media-repo-%{version}
go mod edit \
    -replace github.com/jdeng/goheif=github.com/adrium/goheif@v0.0.0-20210309200126-b184a7b446fa

go mod download github.com/jdeng/goheif

go get github.com/adrium/goheif/heif
go get github.com/adrium/goheif/libde265

cd %{_builddir}/%{name}-%{version}
GOBIN=$PWD/bin go install -v ./cmd/compile_assets
$PWD/bin/compile_assets
go mod vendor -v


%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_libexecdir}/%{name}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_libexecdir}/%{name}/

install -m 0755 -vd                      %{buildroot}%{_sysconfdir}/%{name}
install -m 0644 -vp config.sample.yaml %{buildroot}%{_sysconfdir}/%{name}/config.yaml

install -m 0644 -vpD %{SOURCE1}          %{buildroot}%{_unitdir}/%{name}.service

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc docs README.md CONTRIBUTING.md CHANGELOG.md

%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*

%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/*

%{_unitdir}/%{name}.service

%gopkgfiles

%changelog
* Wed Sep 29 2021 Alexander Manning <mail@alex-m.co.uk> - 1.2.8-1%{?dist}
- Initial package
