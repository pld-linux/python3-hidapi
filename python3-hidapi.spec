#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Cython interface to HIDAPI library
Summary(pl.UTF-8):	Cythonowy interfejs do biblioteki HIDAPI
Name:		python3-hidapi
Version:	0.14.0
Release:	2
License:	GPL v3 or BSD or HIDAPI
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/hidapi/
Source0:	https://files.pythonhosted.org/packages/source/h/hidapi/hidapi-%{version}.tar.gz
# Source0-md5:	261310752df90b76fa4e22f3f60ad733
URL:		https://pypi.org/project/hidapi/
BuildRequires:	hidapi-devel >= 0.14.0
BuildRequires:	libusb-devel >= 1.0
BuildRequires:	python3-Cython
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-setuptools >= 1:19.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	hidapi >= 0.14.0
Requires:	python3-libs >= 1:3.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cython interface to HIDAPI library.

%description -l pl.UTF-8
Cythonowy interfejs do biblioteki HIDAPI.

%prep
%setup -q -n hidapi-%{version}

%build
%py3_build \
	--with-system-hidapi

%if %{with tests}
PYTHONPATH=$(echo build-3/lib.*) \
%{__python3} -m unittest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt LICENSE-bsd.txt LICENSE-orig.txt README.rst
%attr(755,root,root) %{py3_sitedir}/hid.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/hidraw.cpython-*.so
%{py3_sitedir}/hidapi-%{version}-py*.egg-info
