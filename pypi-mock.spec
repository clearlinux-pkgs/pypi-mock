#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-mock
Version  : 5.0.1
Release  : 112
URL      : https://files.pythonhosted.org/packages/a9/c8/7f5fc5ee6a666d7e4ee7a3222bcb37ebebaea3697d7bf54517728f56bb28/mock-5.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/a9/c8/7f5fc5ee6a666d7e4ee7a3222bcb37ebebaea3697d7bf54517728f56bb28/mock-5.0.1.tar.gz
Summary  : Rolling backport of unittest.mock for all Pythons
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-mock-license = %{version}-%{release}
Requires: pypi-mock-python = %{version}-%{release}
Requires: pypi-mock-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
mock is a library for testing in Python. It allows you to replace parts of
your system under test with mock objects and make assertions about how they
have been used.

%package license
Summary: license components for the pypi-mock package.
Group: Default

%description license
license components for the pypi-mock package.


%package python
Summary: python components for the pypi-mock package.
Group: Default
Requires: pypi-mock-python3 = %{version}-%{release}

%description python
python components for the pypi-mock package.


%package python3
Summary: python3 components for the pypi-mock package.
Group: Default
Requires: python3-core
Provides: pypi(mock)

%description python3
python3 components for the pypi-mock package.


%prep
%setup -q -n mock-5.0.1
cd %{_builddir}/mock-5.0.1
pushd ..
cp -a mock-5.0.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1673369427
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
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
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-mock
cp %{_builddir}/mock-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-mock/2eec66c59087d1cf096a35fc620161b222591e05 || :
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
/usr/share/package-licenses/pypi-mock/2eec66c59087d1cf096a35fc620161b222591e05

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
