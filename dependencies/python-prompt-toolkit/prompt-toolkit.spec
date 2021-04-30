# Created by pyp2rpm-3.3.5
%global pypi_name prompt-toolkit

Name:           python-%{pypi_name}
Version:        0.1
Release:        1%{?dist}
Summary:        UNKNOWN

License:        LICENSE.txt
URL:            https://github.com/jonathanslenders/python-prompt-toolkit
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/prompt_toolkit-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Python Prompt Toolkit
=====================

(WORK IN PROGRESS)

Library for building interactive command lines in Python.

It could be a replacement for `readline`, but it's more powerful:

- Syntax highlighting of the input while typing. (Usually with a Pygments
lexer.)
- Multiline input.
- Advanced code completion.

The Python repl
---------------

Run `./bin/prompt_toolkit-python-repl` to...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(docopt)
Requires:       python3dist(pygments)
Requires:       python3dist(six)
%description -n python3-%{pypi_name}
Python Prompt Toolkit
=====================

(WORK IN PROGRESS)

Library for building interactive command lines in Python.

It could be a replacement for `readline`, but it's more powerful:

- Syntax highlighting of the input while typing. (Usually with a Pygments
lexer.)
- Multiline input.
- Advanced code completion.

The Python repl
---------------

Run `./bin/prompt_toolkit-python-repl` to...


%prep
%autosetup -n prompt_toolkit-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%{_bindir}/prompt-toolkit-python-repl
%{python3_sitelib}/prompt_toolkit
%{python3_sitelib}/prompt_toolkit-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Apr 30 2021 Alex Manning <git@alex-m.co.uk> - 0.1-1
- Initial package.
