%define srcname hypothesis

Name:           python-%{srcname}
Version:        6.130.4
Release:        2
Summary:        A library for property based testing
Group:          Development/Python
License:        MPLv2.0
URL:            https://github.com/DRMacIver/hypothesis
Source0:        https://pypi.io/packages/source/h/hypothesis/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
Recommends:       python3dist(numpy)
Recommends:       python3dist(pytz)
%{?python_provide:%python_provide python3-%{srcname}}

%description
Hypothesis is a library for testing your Python code against a much
larger range of examples than you would ever want to write by
hand. It’s based on the Haskell library, Quickcheck, and is designed
to integrate seamlessly into your existing Python unit testing work
flow.

%prep
%autosetup -n %{srcname}-%{version} -p1

rm -rf src/%{srcname}.egg-info

# remove Django tests for now
rm -rf tests/django

# remove fakefactory tests, not packaged yet
rm -rf tests/fakefactory

# remove slow tests
rm -rf tests/nocover

%build
%py_build

%install
%py_install

%files
%license LICENSE.txt
%{_bindir}/hypothesis
%{python_sitelib}/hypothesis-%{version}-py*.*.egg-info
%{python_sitelib}/_*.py
%{python_sitelib}/hypothesis
