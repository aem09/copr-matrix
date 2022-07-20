# Generated by go2rpm 1.6.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/tulir/libsignal-protocol-go
%global goipath         go.mau.fi/libsignal
%global forgeurl        https://github.com/tulir/libsignal-protocol-go
%global commit          4d18b66b087eaedb672af0bc1658ca92d8612c1e
Version:        0.0.1

%gometa

%global common_description %{expand:
Go implementation of the Signal protocol for WhatsApp
(https://github.com/tulir/whatsmeow).}

%global golicenses      LICENSE
%global godocs          CREDITS.md README.md

Name:           %{goname}
Release:        0.1%{?dist}
Summary:        Go implementation of the Signal protocol for WhatsApp (https://github.com/tulir/whatsmeow)

# Upstream license specification: GPL-3.0-only
License:        GPLv3
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

#if %{with check}
#check
#gocheck
#endif

%gopkgfiles

%changelog
* Mon Jun 13 2022 Alex Manning <mail@alex-m.co.uk> - 0-0.1.20220613gitc40c839
- Initial package
