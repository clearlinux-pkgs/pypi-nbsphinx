#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-nbsphinx
Version  : 0.8.9
Release  : 54
URL      : https://files.pythonhosted.org/packages/36/a8/431455c29bf2a5f559bba7f890a640d474f8e3f870cabb57bc08ca9ac5d9/nbsphinx-0.8.9.tar.gz
Source0  : https://files.pythonhosted.org/packages/36/a8/431455c29bf2a5f559bba7f890a640d474f8e3f870cabb57bc08ca9ac5d9/nbsphinx-0.8.9.tar.gz
Summary  : Jupyter Notebook Tools for Sphinx
Group    : Development/Tools
License  : MIT
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

%description
This folder contains the source files for the documentation.
See ../CONTRIBUTING.rst for how to create the HTML and LaTeX
files from these sources.

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
%setup -q -n nbsphinx-0.8.9
cd %{_builddir}/nbsphinx-0.8.9
pushd ..
cp -a nbsphinx-0.8.9 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1654383906
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
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
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
