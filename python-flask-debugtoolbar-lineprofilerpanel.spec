#
# Conditional build:
%bcond_with	doc		# don't build doc (not povided by package)
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module
## TODO: consider rename to  flask_debugtoolbar_lineprofilerpanel  ?
%define 	module	flask-debugtoolbar-lineprofilerpanel
Summary:	Panel for the Flask Debug toolbar to capture and view line-by-line profiling stats
Summary(pl.UTF-8):	Pandel do Flask Debug toolbar do analizy statystyk wykonania kodu linia po linii
Name:		python-%{module}
Version:	1.0.2
Release:	8
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/F/Flask-DebugToolbar-LineProfilerPanel/Flask-DebugToolbar-LineProfilerPanel-%{version}.tar.gz
# Source0-md5:	005d47cb98cff464ce9042b9bf66c230
URL:		https://github.com/phleet/flask_debugtoolbar_lineprofilerpanel
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	rpm-pythonprov
%if %{with python2}
BuildRequires:	python-distribute
BuildRequires:	python-flask-debugtoolbar
BuildRequires:	python-line_profiler

%endif
%if %{with python3}
BuildRequires:	python3-distribute
BuildRequires:	python3-flask-debugtoolbar
BuildRequires:	python3-line_profiler
BuildRequires:	python3-modules

%endif
# Below Rs only work for main package (python2)
#Requires:		python-libs
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Panel for flask_debugtoolbar which enables the ability to view line
profiling information from selected functions. The line profile
information comes from the line_profiler module.

%description -l pl.UTF-8
Panel dla flask_debugtoolbar który pozwala zobaczyć i zanalizować
czasy wykonania linii wybranych funkcji. Informacje są pobierane z
modułu line_profiler.

%package -n python3-%{module}
Summary:	Panel for the Flask Debug toolbar to capture and view line-by-line profiling stats
Summary(pl.UTF-8):	Pandel do Flask Debug toolbar do analizy statystyk wykonania kodu linia po linii
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
Panel for flask_debugtoolbar which enables the ability to view line
profiling information from selected functions. The line profile
information comes from the line_profiler module.

%description -n python3-%{module} -l pl.UTF-8
Panel dla flask_debugtoolbar który pozwala zobaczyć i zanalizować
czasy wykonania linii wybranych funkcji. Informacje są pobierane z
modułu line_profiler.

%package apidocs
Summary:	%{module} API documentation
Summary(pl.UTF-8):	Dokumentacja API %{module}
Group:		Documentation

%description apidocs
API documentation for %{module}.

%description apidocs -l pl.UTF-8
Dokumentacja API %{module}.

%prep
%setup -q -n Flask-DebugToolbar-LineProfilerPanel-%{version}
# Until fixed upstream: 
sed -i 's/line-profiler>=1.0b3/line_profiler>=1.0/g' setup.py

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
cd docs
%{__make} -j1 html
rm -rf _build/html/_sources
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
%{py_sitescriptdir}/flask_debugtoolbar_lineprofilerpanel
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/Flask_DebugToolbar_LineProfilerPanel-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%{py3_sitescriptdir}/flask_debugtoolbar_lineprofilerpanel
%{py3_sitescriptdir}/Flask_DebugToolbar_LineProfilerPanel-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
