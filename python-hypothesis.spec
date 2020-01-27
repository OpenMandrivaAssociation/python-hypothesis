%define srcname hypothesis

Name:           python-%{srcname}
Version:        4.36.2
Release:        %mkrel 1
Summary:        A library for property based testing
Group:          Development/Python
License:        MPLv2.0
URL:            https://github.com/DRMacIver/hypothesis
Source0:        https://pypi.io/packages/source/h/hypothesis/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)

%description
Hypothesis is a library for testing your Python code against a much
larger range of examples than you would ever want to write by
hand. It’s based on the Haskell library, Quickcheck, and is designed
to integrate seamlessly into your existing Python unit testing work
flow.

%package     -n python3-%{srcname}
Group:          Development/Python
Summary:        A library for property based testing
Suggests:       python3dist(numpy)
Suggests:       python3dist(pytz)
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
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
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/*
