Name:           Linux-PAM
Version:        1.2.1
Release:        30
License:        GPL-2.0+ BSD-3-Clause
Summary:        Linux-PAM (Pluggable Authentication Modules)
Url:            https://fedorahosted.org/linux-pam/
Group:          base
Source0:        http://linux-pam.org/library/Linux-PAM-1.2.1.tar.bz2
Source2:        common-account
Source3:        common-auth
Source4:        common-password
Source5:        common-session
Source6:        common-session-noninteractive
Source7:        other
Patch0:         0001-libpam-Keep-existing-pamdir-for-transition.patch
Patch1:         0002-Support-altfiles-locations.patch
Patch2:         0003-pam_env-Only-report-non-ENOENT-errors-for-env-file.patch
Patch3:         0001-pam_securetty-Do-not-report-non-fatal-documented-beh.patch
Patch4:         0004-pam_shells-Support-a-stateless-configuration-by-defa.patch
BuildRequires:  autoconf  automake automake-dev gettext gettext-dev libtool libtool-dev pkg-config-dev
BuildRequires:  bison-dev
BuildRequires:  cracklib-dev
BuildRequires:  flex-dev
BuildRequires:  pkgconfig(zlib)
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32

# FIXME: should name the base package "pam" instead, and provide libpam
Provides:       pam

%description
Linux-PAM (Pluggable Authentication Modules).

%package dev
Summary:        Linux-PAM (Pluggable Authentication Modules)
Group:          devel
Requires:       %{name} = %{version}-%{release}

%description dev
Linux-PAM (Pluggable Authentication Modules).

%package dev32
Summary:        Linux-PAM (Pluggable Authentication Modules)
Group:          devel
Requires:       %{name} = %{version}-%{release}
Requires:       Linux-PAM-lib32

%description dev32
Linux-PAM (Pluggable Authentication Modules).

%package lib32
Summary:        Linux-PAM (Pluggable Authentication Modules)
Group:          devel
Requires:       %{name} = %{version}-%{release}

%description lib32
Linux-PAM (Pluggable Authentication Modules).

%package doc
Summary:        Linux-PAM (Pluggable Authentication Modules)
Group:          doc

%description doc
Linux-PAM (Pluggable Authentication Modules).

%package locale
Summary:        Translations for the libpam package
Group:          libs

%description locale
Linux-PAM (Pluggable Authentication Modules).

%prep
%setup -q -n Linux-PAM-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

pushd ..
cp -a Linux-PAM-%{version} build32
popd


%build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto -fno-semantic-interposition "

autoreconf -fi
%configure \
 --with-db-uniquename=_pam \
 --includedir=/usr/include/security \
 --libdir=/usr/lib64 \
 --disable-nis \
 --disable-regenerate-docu \
 --disable-prelude \
 --enable-nls \
 --disable-audit \
 --sysconfdir=/usr/share

make %{?_smp_mflags}

pushd ../build32/
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
autoreconf -fi
%configure \
 --with-db-uniquename=_pam \
 --includedir=/usr/include/security \
 --libdir=/usr/lib32 \
 --disable-nis \
 --disable-regenerate-docu \
 --disable-prelude \
 --enable-nls \
 --disable-audit \
 --sysconfdir=/usr/share

make %{?_smp_mflags}

popd


%install
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do mv $i 32$i ; done
popd
fi
popd

%make_install

rm -f %{buildroot}/usr/share/environment

install -d %{buildroot}/usr/share/pam.d/
install -m 0644 %{SOURCE2} %{buildroot}/usr/share/pam.d/
install -m 0644 %{SOURCE3} %{buildroot}/usr/share/pam.d/
install -m 0644 %{SOURCE4} %{buildroot}/usr/share/pam.d/
install -m 0644 %{SOURCE5} %{buildroot}/usr/share/pam.d/
install -m 0644 %{SOURCE6} %{buildroot}/usr/share/pam.d/
install -m 0644 %{SOURCE7} %{buildroot}/usr/share/pam.d/

# The lsb requires unix_chkpwd has setuid permission
chmod 4755 %{buildroot}/usr/bin/unix_chkpwd

echo "session optional pam_systemd.so" >> %{buildroot}/usr/share/pam.d/common-session

%find_lang Linux-PAM %{name}.lang

%files
/usr/share/pam.d/common-auth
/usr/share/pam.d/common-session
/usr/share/pam.d/common-password
/usr/share/pam.d/other
/usr/share/pam.d/common-session-noninteractive
/usr/share/pam.d/common-account
/usr/share/security/time.conf
/usr/share/security/limits.conf
/usr/share/security/access.conf
/usr/share/security/pam_env.conf
/usr/share/security/namespace.conf
/usr/share/security/namespace.init
/usr/share/security/group.conf
/usr/lib64/libpam.so.*
/usr/lib64/libpam_misc.so.*
/usr/lib64/libpamc.so.*
/usr/lib64/security/*.so
/usr/lib64/security/pam_filter/upperLOWER
/usr/bin/mkhomedir_helper
/usr/bin/pam_tally
/usr/bin/pam_tally2
/usr/bin/pam_timestamp_check
/usr/bin/unix_chkpwd
/usr/bin/unix_update

%files dev
/usr/include/security/*.h
/usr/lib64/libpam_misc.so
/usr/lib64/libpamc.so
/usr/lib64/libpam.so
/usr/lib64/libpam.so.0

%files dev32
/usr/include/security/*.h
/usr/lib32/libpam_misc.so
/usr/lib32/libpamc.so
/usr/lib32/libpam.so
/usr/lib32/libpam.so.0

%files lib32
%exclude /usr/lib32/security
/usr/lib32/libpam.so.*
/usr/lib32/libpam_misc.so.*
/usr/lib32/libpamc.so.*


%files doc
%{_mandir}/man3/*
%{_mandir}/man5/*
%{_mandir}/man8/*
/usr/share/doc/Linux-PAM/draft-morgan-pam-current.txt
/usr/share/doc/Linux-PAM/index.html
/usr/share/doc/Linux-PAM/rfc86.0.txt

%files locale -f %{name}.lang
