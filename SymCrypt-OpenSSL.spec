Name:           SymCrypt-OpenSSL
Version:        1.3.0
Release:        1%{?dist}
Summary:        The SymCrypt engine for OpenSSL

License:        MIT
URL:            https://github.com/microsoft/SymCrypt-OpenSSL
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

Patch1:         0001-SymCrypt-provider-base-57.patch

BuildRequires:  cmake
BuildRequires:  openssl-devel
BuildRequires:  SymCrypt-devel
BuildRequires:  gcc gcc-c++
BuildRequires:  pkgconf-pkg-config
BuildRequires:  sed
Requires:       SymCrypt openssl-libs

%description
The SymCrypt engine for OpenSSL (SCOSSL) allows the use of OpenSSL with SymCrypt as the provider
for core cryptographic operations. It leverages the OpenSSL engine interface to
override the cryptographic implementations in OpenSSL's libcrypto.so with SymCrypt's implementations.
The primary motivation for this is to support FIPS certification,
as vanilla OpenSSL 1.1.1 does not have a FIPS-certified cryptographic module.

%package devel
Summary: Development headers for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development headers for the core cryptographic
Windows library OpenSSL module.



%prep
%autosetup -p1


%build
sed -e 's,(${SYMCRYPT_ROOT_DIR}/inc),(${SYMCRYPT_ROOT_DIR}),' -i CMakeLists.txt
%cmake -DSYMCRYPT_ROOT_DIR="%{_includedir}/SymCrypt"
%cmake_build


%install
%cmake_install


%files
%license LICENSE NOTICE
%doc README.md SECURITY.md
%{_libdir}/ossl-modules/symcryptprovider.so
%{_libdir}/engines-*/symcryptengine.so

%files devel
%{_includedir}/scossl.h
%{_includedir}/p_scossl*.h

%changelog
* Wed Mar 08 2023 Petr Menšík <pemensik@redhat.com>
- initial build
