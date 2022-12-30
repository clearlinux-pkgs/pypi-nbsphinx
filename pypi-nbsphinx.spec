#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-nbsphinx
Version  : 0.8.11
Release  : 63
URL      : https://files.pythonhosted.org/packages/c1/fd/cba6885b1244a6fc1e0c05bad26a1374d52e56d57ee585dfd1ef169e6ea7/nbsphinx-0.8.11.tar.gz
Source0  : https://files.pythonhosted.org/packages/c1/fd/cba6885b1244a6fc1e0c05bad26a1374d52e56d57ee585dfd1ef169e6ea7/nbsphinx-0.8.11.tar.gz
Summary  : Jupyter Notebook Tools for Sphinx
Group    : Development/Tools
License  : MIT
Requires: pypi-nbsphinx-license = %{version}-%{release}
Requires: pypi-nbsphinx-python = %{version}-%{release}
Requires: pypi-nbsphinx-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(docutils)
BuildRequires : pypi(ipywidgets)
BuildRequires : pypi(jinja2)
BuildRequires : pypi(jupyterlab)
BuildRequires : pypi(jupytext)
BuildRequires : pypi(matplotlib)
BuildRequires : pypi(nbconvert)
BuildRequires : pypi(nbformat)
BuildRequires : pypi(pandas)
BuildRequires : pypi(sphinx)
BuildRequires : pypi(traitlets)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This folder contains the source files for the documentation.
See ../CONTRIBUTING.rst for how to create the HTML and LaTeX
files from these sources.

%package license
Summary: license components for the pypi-nbsphinx package.
Group: Default

%description license
license components for the pypi-nbsphinx package.


%package python
Summary: python components for the pypi-nbsphinx package.
Group: Default
Requires: pypi-nbsphinx-python3 = %{version}-%{release}

%description python
python components for the pypi-nbsphinx package.


%package python3
Summary: python3 components for the pypi-nbsphinx package.
Group: Default
Requires: python3-core
Provides: pypi(nbsphinx)
Requires: pypi(docutils)
Requires: pypi(ipywidgets)
Requires: pypi(jinja2)
Requires: pypi(jupyterlab)
Requires: pypi(jupytext)
Requires: pypi(matplotlib)
Requires: pypi(nbconvert)
Requires: pypi(nbformat)
Requires: pypi(pandas)
Requires: pypi(sphinx)
Requires: pypi(traitlets)

%description python3
python3 components for the pypi-nbsphinx package.


%prep
%setup -q -n nbsphinx-0.8.11
cd %{_builddir}/nbsphinx-0.8.11
pushd ..
cp -a nbsphinx-0.8.11 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672417622
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-nbsphinx
cp %{_builddir}/nbsphinx-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-nbsphinx/04e8f78556b643f05427eaa7b4152e79b317f242 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-nbsphinx/04e8f78556b643f05427eaa7b4152e79b317f242

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
