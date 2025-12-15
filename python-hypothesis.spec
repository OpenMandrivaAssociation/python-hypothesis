%define srcname hypothesis

Name:           python-%{srcname}
Version:        6.148.7
Release:        1
Summary:        A library for property based testing
Group:          Development/Python
License:        MPLv2.0
URL:            https://github.com/HypothesisWorks/hypothesis
Source0:        https://pypi.io/packages/source/h/hypothesis/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildSystem:	python
BuildRequires:  pkgconfig(python)
BuildRequires:  python%{pyver}dist(setuptools)
Recommends:     python%{pyver}dist(numpy)
Recommends:     python%{pyver}dist(pytz)

%description
Hypothesis is a library for testing your Python code against a much
larger range of examples than you would ever want to write by
hand. It’s based on the Haskell library, Quickcheck, and is designed
to integrate seamlessly into your existing Python unit testing work
flow.

%prep -a
rm -rf src/%{srcname}.egg-info

# remove Django tests for now
rm -rf tests/django

# remove fakefactory tests, not packaged yet
rm -rf tests/fakefactory

# remove slow tests
rm -rf tests/nocover

%files
%license LICENSE.txt
%{_bindir}/hypothesis
%{python_sitelib}/__pycache__/*
%{python_sitelib}/hypothesis-%{version}.dist-info
%{python_sitelib}/_*.py
%{python_sitelib}/hypothesis
