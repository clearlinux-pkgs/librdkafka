#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v27
# autospec commit: 65cf152
#
Name     : librdkafka
Version  : 2.10.1
Release  : 13
URL      : https://github.com/edenhill/librdkafka/archive/v2.10.1/librdkafka-2.10.1.tar.gz
Source0  : https://github.com/edenhill/librdkafka/archive/v2.10.1/librdkafka-2.10.1.tar.gz
Summary  : The Apache Kafka C library
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause ISC MIT Zlib
Requires: librdkafka-data = %{version}-%{release}
Requires: librdkafka-lib = %{version}-%{release}
Requires: librdkafka-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : curl-dev
BuildRequires : glibc-dev
BuildRequires : openssl-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(liblz4)
BuildRequires : pkgconfig(libsasl2)
BuildRequires : pkgconfig(libzstd)
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
librdkafka is the C/C++ client library implementation of the Apache Kafka protocol, containing both Producer and Consumer support.

%package data
Summary: data components for the librdkafka package.
Group: Data

%description data
data components for the librdkafka package.


%package dev
Summary: dev components for the librdkafka package.
Group: Development
Requires: librdkafka-lib = %{version}-%{release}
Requires: librdkafka-data = %{version}-%{release}
Provides: librdkafka-devel = %{version}-%{release}
Requires: librdkafka = %{version}-%{release}

%description dev
dev components for the librdkafka package.


%package lib
Summary: lib components for the librdkafka package.
Group: Libraries
Requires: librdkafka-data = %{version}-%{release}
Requires: librdkafka-license = %{version}-%{release}

%description lib
lib components for the librdkafka package.


%package license
Summary: license components for the librdkafka package.
Group: Default

%description license
license components for the librdkafka package.


%prep
%setup -q -n librdkafka-2.10.1
cd %{_builddir}/librdkafka-2.10.1
pushd ..
cp -a librdkafka-2.10.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1749652853
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test || :
cd ../../buildavx2/clr-build-avx2;
make test || : || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1749652853
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/librdkafka
cp %{_builddir}/librdkafka-%{version}/LICENSE.cjson %{buildroot}/usr/share/package-licenses/librdkafka/5c753d7bf6e7cf01c2dde51c78a18f640d405369 || :
cp %{_builddir}/librdkafka-%{version}/LICENSE.crc32c %{buildroot}/usr/share/package-licenses/librdkafka/1c729ec87a41f94eabbabb496454e54cf770c678 || :
cp %{_builddir}/librdkafka-%{version}/LICENSE.hdrhistogram %{buildroot}/usr/share/package-licenses/librdkafka/25c13cb8c65676499760570c0bb60538e34c6b90 || :
cp %{_builddir}/librdkafka-%{version}/LICENSE.murmur2 %{buildroot}/usr/share/package-licenses/librdkafka/199b0086de98cc0044deeedf89a7f819c9f9a5ce || :
cp %{_builddir}/librdkafka-%{version}/LICENSE.opentelemetry %{buildroot}/usr/share/package-licenses/librdkafka/9a15442c3973a5fc80ade513dddd95eb12dbbc28 || :
cp %{_builddir}/librdkafka-%{version}/LICENSE.pycrc %{buildroot}/usr/share/package-licenses/librdkafka/e8651e180555376b5c2b5ecd114981481a512546 || :
cp %{_builddir}/librdkafka-%{version}/LICENSE.queue %{buildroot}/usr/share/package-licenses/librdkafka/7f653fbf85dbdf0f48138299d18381a6bfb101f1 || :
cp %{_builddir}/librdkafka-%{version}/LICENSE.snappy %{buildroot}/usr/share/package-licenses/librdkafka/7e81b2429a98f39ef348b68a40eaac4b834f29a7 || :
cp %{_builddir}/librdkafka-%{version}/LICENSE.tinycthread %{buildroot}/usr/share/package-licenses/librdkafka/14107287e77706772572744b1b3ecfde8960472d || :
cp %{_builddir}/librdkafka-%{version}/LICENSE.wingetopt %{buildroot}/usr/share/package-licenses/librdkafka/e612d1fbaad7c0a278b025734f37cfa6bbb0b678 || :
cp %{_builddir}/librdkafka-%{version}/LICENSES.txt %{buildroot}/usr/share/package-licenses/librdkafka/d0e31cd8e85b759eb027859cf8e53556e1f68341 || :
cp %{_builddir}/librdkafka-%{version}/debian/copyright %{buildroot}/usr/share/package-licenses/librdkafka/87f4b5b0f5bce542751ece2daa6e314473cb7b4f || :
cp %{_builddir}/librdkafka-%{version}/packaging/cmake/Modules/LICENSE.FindZstd %{buildroot}/usr/share/package-licenses/librdkafka/b5ec887319537fbea3fa9804ac9a5cd5e40afd2e || :
cp %{_builddir}/librdkafka-%{version}/packaging/debian/copyright %{buildroot}/usr/share/package-licenses/librdkafka/a35749a8a0906df91ed2468874e9229b95a8fba7 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/licenses/librdkafka/LICENSES.txt

%files dev
%defattr(-,root,root,-)
/usr/include/librdkafka/rdkafka.h
/usr/include/librdkafka/rdkafka_mock.h
/usr/include/librdkafka/rdkafkacpp.h
/usr/lib64/cmake/RdKafka/FindLZ4.cmake
/usr/lib64/cmake/RdKafka/RdKafkaConfig.cmake
/usr/lib64/cmake/RdKafka/RdKafkaConfigVersion.cmake
/usr/lib64/cmake/RdKafka/RdKafkaTargets-relwithdebinfo.cmake
/usr/lib64/cmake/RdKafka/RdKafkaTargets.cmake
/usr/lib64/librdkafka++.so
/usr/lib64/librdkafka.so
/usr/lib64/pkgconfig/rdkafka++.pc
/usr/lib64/pkgconfig/rdkafka.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/librdkafka++.so.1
/V3/usr/lib64/librdkafka.so.1
/usr/lib64/librdkafka++.so.1
/usr/lib64/librdkafka.so.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/librdkafka/14107287e77706772572744b1b3ecfde8960472d
/usr/share/package-licenses/librdkafka/199b0086de98cc0044deeedf89a7f819c9f9a5ce
/usr/share/package-licenses/librdkafka/1c729ec87a41f94eabbabb496454e54cf770c678
/usr/share/package-licenses/librdkafka/25c13cb8c65676499760570c0bb60538e34c6b90
/usr/share/package-licenses/librdkafka/5c753d7bf6e7cf01c2dde51c78a18f640d405369
/usr/share/package-licenses/librdkafka/7e81b2429a98f39ef348b68a40eaac4b834f29a7
/usr/share/package-licenses/librdkafka/7f653fbf85dbdf0f48138299d18381a6bfb101f1
/usr/share/package-licenses/librdkafka/87f4b5b0f5bce542751ece2daa6e314473cb7b4f
/usr/share/package-licenses/librdkafka/9a15442c3973a5fc80ade513dddd95eb12dbbc28
/usr/share/package-licenses/librdkafka/a35749a8a0906df91ed2468874e9229b95a8fba7
/usr/share/package-licenses/librdkafka/b5ec887319537fbea3fa9804ac9a5cd5e40afd2e
/usr/share/package-licenses/librdkafka/d0e31cd8e85b759eb027859cf8e53556e1f68341
/usr/share/package-licenses/librdkafka/e612d1fbaad7c0a278b025734f37cfa6bbb0b678
/usr/share/package-licenses/librdkafka/e8651e180555376b5c2b5ecd114981481a512546
