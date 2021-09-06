# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/ipfs/go-datastore
%global goipath         github.com/ipfs/go-datastore
%global goipaths0       github.com/ipfs/go-datastore
%global goipathsex0     github.com/ipfs/go-ds-flatfs

%global goipaths1       github.com/ipfs/go-ds-flatfs
Version:                0.4.6

%gometa

%global common_description %{expand:
Key-value datastore interfaces.}

%global golicenses      LICENSE
%global godocs          examples README.md fuzz/README.md autobatch/README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Key-value datastore interfaces

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/ipfs/go-detect-race)
#BuildRequires:  golang(github.com/ipfs/go-ds-flatfs)
BuildRequires:  golang(github.com/ipfs/go-ipfs-delay)
BuildRequires:  golang(github.com/jbenet/goprocess)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(go.uber.org/multierr)
BuildRequires:  golang(golang.org/x/xerrors)

%if %{with check}
# Tests
BuildRequires:  golang(gopkg.in/check.v1)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Mon Sep 06 2021 Alexander Manning <mail@alex-m.co.uk> - 0.4.6-1%{?dist}
- Initial package
