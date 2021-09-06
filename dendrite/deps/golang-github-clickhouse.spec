# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/ClickHouse/clickhouse-go
%global goipath         github.com/ClickHouse/clickhouse-go
Version:                1.4.7

%gometa

%global common_description %{expand:
Golang driver for ClickHouse.}

%global golicenses      LICENSE lib/lz4/LICENSE
%global godocs          examples README.md CONTRIBUTING.md\\\
                        lib/protocol/README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Golang driver for ClickHouse

# Upstream license specification: BSD-2-Clause and MIT
License:        BSD and MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/jmoiron/sqlx)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/bkaradzic/go-lz4)
BuildRequires:  golang(github.com/cloudflare/golz4)
BuildRequires:  golang(github.com/pierrec/lz4)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in lib/codegen/nullable_appender; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE lib/lz4/LICENSE
%doc examples README.md CONTRIBUTING.md lib/protocol/README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Mon Sep 06 2021 Alexander Manning <mail@alex-m.co.uk> - 1.4.7-1%{?dist}
- Initial package

