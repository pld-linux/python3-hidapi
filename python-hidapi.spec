#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Cython interface to HIDAPI library
Summary(pl.UTF-8):	Cythonowy interfejs do biblioteki HIDAPI
Name:		python-hidapi
Version:	0.7.99.post21
Release:	3
License:	GPL v3 or BSD or HIDAPI
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/h/hidapi/hidapi-%{version}.tar.gz
# Source0-md5:	c343ac9bf1a204f89e6f94e9c569faa0
URL:		https://pypi.org/project/hidapi/
BuildRequires:	hidapi-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-Cython
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-setuptools >= 19.0
%endif
%if %{with python3}
BuildRequires:	python3-Cython
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-setuptools >= 19.0
%endif
Requires:	python-libs >= 1:2.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cython interface to HIDAPI library.

%description -l pl.UTF-8
Cythonowy interfejs do biblioteki HIDAPI.

%package -n python3-hidapi
Summary:	Cython interface to HIDAPI library
Summary(pl.UTF-8):	Cythonowy interfejs do biblioteki HIDAPI
Group:		Libraries/Python
Requires:	python3-libs >= 1:3.2

%description -n python3-hidapi
Cython interface to HIDAPI library.

%description -n python3-hidapi -l pl.UTF-8
Cythonowy interfejs do biblioteki HIDAPI.

%prep
%setup -q -n hidapi-%{version}

%build
%if %{with python2}
%py_build \
	--with-system-hidapi

%if %{with tests}
PYTHONPATH=$(echo build-2/lib.*) \
%{__python} -m unittest tests
%endif
%endif

%if %{with python3}
%py3_build \
	--with-system-hidapi

%if %{with tests}
PYTHONPATH=$(echo build-3/lib.*) \
%{__python3} -m unittest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE.txt LICENSE-bsd.txt LICENSE-orig.txt README.rst
%attr(755,root,root) %{py_sitedir}/hid.so
%attr(755,root,root) %{py_sitedir}/hidraw.so
%{py_sitedir}/hidapi-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-hidapi
%defattr(644,root,root,755)
%doc LICENSE.txt LICENSE-bsd.txt LICENSE-orig.txt README.rst
%attr(755,root,root) %{py3_sitedir}/hid.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/hidraw.cpython-*.so
%{py3_sitedir}/hidapi-%{version}-py*.egg-info
%endif
