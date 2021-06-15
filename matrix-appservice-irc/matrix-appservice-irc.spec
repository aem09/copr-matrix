%global npm_name matrix-appservice-irc

%global debug_package %{nil}

Version: 0.26.1

License:  Apache-2.0

Name:     %{npm_name}
Summary:  This is an IRC bridge for Matrix.
Release:  1%{?dist}
Source0:  http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
Source1:  %{npm_name}-%{version}-nm-prod.tgz
Source3:  %{npm_name}-%{version}-bundled-licenses.txt

ExclusiveArch: %{nodejs_arches}

BuildRequires: nodejs-devel

%description
This bridge will pass all IRC messages through to Matrix, and all Matrix messages through to IRC. It is highly configurable and is currently used on the matrix.org homeserver to bridge a number of popular IRC networks including Freenode and OFTC.

%prep
%setup -q -n package
cp %{SOURCE3} .

%build
# Setup bundled node modules
tar xfz %{SOURCE1}
mkdir -p node_modules
pushd node_modules
ln -s ../node_modules_prod/* .
ln -s ../node_modules_prod/.bin .
popd

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr app.js lib package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
# Copy over bundled nodejs modules
cp -pr node_modules node_modules_prod %{buildroot}%{nodejs_sitelib}/%{npm_name}

%check
#nodejs_symlink_deps --check
# Setup bundled dev node_modules for testing
#tar xfz %{SOURCE2}
#pushd node_modules
#ln -s ../node_modules_dev/* .
#popd
#pushd node_modules/.bin
#ln -s ../../node_modules_dev/.bin/* .
#popd

%files
%doc README.md
%license LICENSE %{npm_name}-%{version}-bundled-licenses.txt
%{nodejs_sitelib}/%{npm_name}
