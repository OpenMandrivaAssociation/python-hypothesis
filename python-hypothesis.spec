%define module hypothesis

# The Rust extension has no C sources for the debugsource package to list.
%global _empty_manifest_terminate_build 0

Name:		python-hypothesis
Version:	6.169.0
Release:	1
Summary:	A library for property based testing
Group:		Development/Python
License:	MPLv2.0
URL:		https://github.com/HypothesisWorks/hypothesis
Source0:	https://pypi.io/packages/source/h/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:	cargo-vendor-for-hypothesis-%{version}.tar.xz
Source2:	cargo-config.toml

BuildSystem:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(maturin)
BuildRequires:	cargo
BuildRequires:	clang
Recommends:	python%{pyver}dist(numpy)
Recommends:	python%{pyver}dist(pytz)

%description
Hypothesis is a library for testing your Python code against a much
larger range of examples than you would ever want to write by
hand. It’s based on the Haskell library, Quickcheck, and is designed
to integrate seamlessly into your existing Python unit testing work
flow.

%prep -a
rm -rf src/%{module}.egg-info
tar -xf %{SOURCE1}
install -D -m 0644 %{SOURCE2} .cargo/config.toml

%build -p
export CARGO_NET_OFFLINE=true
export CC=clang
export CXX=clang++

%files
%license LICENSE.txt
%{_bindir}/hypothesis
%{python_sitearch}/hypothesis
%{python_sitearch}/hypothesis-*.dist-info
%{python_sitearch}/_hypothesis_globals.py
%{python_sitearch}/_hypothesis_ftz_detector.py
%{python_sitearch}/_hypothesis_pytestplugin.py
%{python_sitearch}/__pycache__/
