# Generated by go2rpm 1.5.0
%bcond_without check

%global go_generate_buildrequires %{nil}

# https://github.com/matrix-org/dendrite
%global goipath         github.com/matrix-org/dendrite
Version:                0.5.0

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

Name:           %{goname}
Release:        1%{?dist}
Summary:        Dendrite is a second-generation Matrix homeserver written in Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

# These ones result from using go-get.
BuildRequires:   git
BuildRequires:   breezy
BuildRequires:   golang(launchpad.net/gocheck)
#BuildRequires:  libolm-devel
#BuildRequires:  libolm

#BuildRequires:  libstdc++-devel
#BuildRequires:  libstdc++
#BuildRequires:  libstdc++-static

# These are all the "normal" dependencies.

BuildRequires:  golang(github.com/Arceliar/ironwood/types)
#BuildRequires:  golang(github.com/codeclysm/extract)
BuildRequires:  golang(github.com/docker/docker/api/types)
BuildRequires:  golang(github.com/docker/docker/api/types/container)
BuildRequires:  golang(github.com/docker/docker/api/types/filters)
BuildRequires:  golang(github.com/docker/docker/api/types/mount)
BuildRequires:  golang(github.com/docker/docker/api/types/volume)
BuildRequires:  golang(github.com/docker/docker/client)
BuildRequires:  golang(github.com/docker/go-connections/nat)
#BuildRequires:  golang(github.com/getsentry/sentry-go)
#BuildRequires:  golang(github.com/getsentry/sentry-go/http)
BuildRequires:  golang(github.com/gologme/log)
BuildRequires:  golang(github.com/gorilla/mux)
BuildRequires:  golang(github.com/gorilla/websocket)
BuildRequires:  golang(github.com/hashicorp/golang-lru)
BuildRequires:  golang(github.com/lib/pq)
#BuildRequires:  golang(github.com/libp2p/go-libp2p)
#BuildRequires:  golang(github.com/libp2p/go-libp2p-circuit)
#BuildRequires:  golang(github.com/libp2p/go-libp2p-core/crypto)
#BuildRequires:  golang(github.com/libp2p/go-libp2p-core/host)
#BuildRequires:  golang(github.com/libp2p/go-libp2p-core/peer)
#BuildRequires:  golang(github.com/libp2p/go-libp2p-core/peerstore)
#BuildRequires:  golang(github.com/libp2p/go-libp2p-core/routing)
#BuildRequires:  golang(github.com/libp2p/go-libp2p-gostream)
#BuildRequires:  golang(github.com/libp2p/go-libp2p-http)
#BuildRequires:  golang(github.com/libp2p/go-libp2p-kad-dht)
#BuildRequires:  golang(github.com/libp2p/go-libp2p-pubsub)
#BuildRequires:  golang(github.com/libp2p/go-libp2p-record)
#BuildRequires:  golang(github.com/libp2p/go-libp2p/p2p/discovery)
BuildRequires:  golang(github.com/lucas-clemente/quic-go)
BuildRequires:  golang(github.com/Masterminds/semver/v3)
BuildRequires:  golang(github.com/matrix-org/dugong)
BuildRequires:  golang(github.com/matrix-org/gomatrix)
BuildRequires:  golang(github.com/matrix-org/gomatrixserverlib)
BuildRequires:  golang(github.com/matrix-org/gomatrixserverlib/tokens)
#BuildRequires:  golang(github.com/matrix-org/naffka)
#BuildRequires:  golang(github.com/matrix-org/naffka/storage)
#BuildRequires:  golang(github.com/matrix-org/pinecone/multicast)
#BuildRequires:  golang(github.com/matrix-org/pinecone/router)
#BuildRequires:  golang(github.com/matrix-org/pinecone/sessions)
#BuildRequires:  golang(github.com/matrix-org/pinecone/types)
BuildRequires:  golang(github.com/matrix-org/util)
BuildRequires:  golang(github.com/mattn/go-sqlite3)
#BuildRequires:  golang(github.com/neilalexander/utp)
BuildRequires:  golang(github.com/nfnt/resize)
#BuildRequires:  golang(github.com/ngrok/sqlmw)
BuildRequires:  golang(github.com/opentracing/opentracing-go)
BuildRequires:  golang(github.com/opentracing/opentracing-go/ext)
BuildRequires:  golang(github.com/patrickmn/go-cache)
BuildRequires:  golang(github.com/pkg/errors)
#BuildRequires:  golang(github.com/pressly/goose)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus/promauto)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus/promhttp)
BuildRequires:  golang(github.com/Shopify/sarama)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(github.com/sirupsen/logrus/hooks/syslog)
BuildRequires:  golang(github.com/tidwall/gjson)
BuildRequires:  golang(github.com/tidwall/sjson)
BuildRequires:  golang(github.com/uber/jaeger-client-go/config)
BuildRequires:  golang(github.com/uber/jaeger-lib/metrics)
##BuildRequires:  golang(github.com/yggdrasil-network/yggdrasil-go/src/config)
##BuildRequires:  golang(github.com/yggdrasil-network/yggdrasil-go/src/core)
##BuildRequires:  golang(github.com/yggdrasil-network/yggdrasil-go/src/defaults)
##BuildRequires:  golang(github.com/yggdrasil-network/yggdrasil-go/src/multicast)
BuildRequires:  golang(go.uber.org/atomic)
BuildRequires:  golang(golang.org/x/crypto/bcrypt)
BuildRequires:  golang(golang.org/x/crypto/blake2b)
BuildRequires:  golang(golang.org/x/crypto/curve25519)
BuildRequires:  golang(golang.org/x/crypto/ed25519)
BuildRequires:  golang(golang.org/x/mobile/bind)
BuildRequires:  golang(golang.org/x/net/http2)
BuildRequires:  golang(golang.org/x/net/http2/h2c)
BuildRequires:  golang(golang.org/x/term)
BuildRequires:  golang(gopkg.in/yaml.v2)
BuildRequires:  golang(nhooyr.io/websocket)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/DATA-DOG/go-sqlmock)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%global gomodulesmode GO111MODULE=auto
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%global gomodulesmode GO111MODULE=auto
%gocheck
%endif

%files
%license LICENSE
%doc docs README.md CHANGES.md appservice/README.md mediaapi/README.md
%doc syncapi/README.md roomserver/README.md clientapi/README.md
%doc cmd/goose/README.md cmd/dendrite-demo-yggdrasil/README.md
%doc build/docker/README.md build/scripts/README.md keyserver/README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Sun Sep 05 2021 Alexander Manning <mail@alex-m.co.uk> - 0.5.0-1%{?dist}
- Initial package
