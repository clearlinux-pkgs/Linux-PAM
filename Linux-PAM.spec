#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x6D1A7F052E5924BB (kukuk@suse.de)
#
Name     : Linux-PAM
Version  : 1.3.1
Release  : 50
URL      : https://github.com/linux-pam/linux-pam/releases/download/v1.3.1/Linux-PAM-1.3.1.tar.xz
Source0  : https://github.com/linux-pam/linux-pam/releases/download/v1.3.1/Linux-PAM-1.3.1.tar.xz
Source1 : https://github.com/linux-pam/linux-pam/releases/download/v1.3.1/Linux-PAM-1.3.1.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: Linux-PAM-bin = %{version}-%{release}
Requires: Linux-PAM-data = %{version}-%{release}
Requires: Linux-PAM-lib = %{version}-%{release}
Requires: Linux-PAM-license = %{version}-%{release}
Requires: Linux-PAM-locales = %{version}-%{release}
Requires: Linux-PAM-man = %{version}-%{release}
Requires: Linux-PAM-setuid = %{version}-%{release}
BuildRequires : autoconf
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : bison-dev
BuildRequires : cracklib-dev
BuildRequires : flex
BuildRequires : flex-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gettext
BuildRequires : gettext-dev
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : libxml2-dev
BuildRequires : libxslt-bin
BuildRequires : pkg-config
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(libtirpc)
BuildRequires : pkgconfig(zlib)
BuildRequires : strace
BuildRequires : util-linux
BuildRequires : xauth
Patch1: 0001-libpam-Keep-existing-pamdir-for-transition.patch
Patch2: 0002-pam_securetty-Do-not-report-non-fatal-documented-beh.patch
Patch3: 0003-Support-altfiles-locations.patch
Patch4: 0004-pam_env-Only-report-non-ENOENT-errors-for-env-file.patch
Patch5: 0005-pam_shells-Support-a-stateless-configuration-by-defa.patch
Patch6: 0006-Add-common-pam.d-files.patch

%description
Linux-PAM (Pluggable Authentication Modules)

%package bin
Summary: bin components for the Linux-PAM package.
Group: Binaries
Requires: Linux-PAM-data = %{version}-%{release}
Requires: Linux-PAM-setuid = %{version}-%{release}
Requires: Linux-PAM-license = %{version}-%{release}

%description bin
bin components for the Linux-PAM package.


%package data
Summary: data components for the Linux-PAM package.
Group: Data

%description data
data components for the Linux-PAM package.


%package dev
Summary: dev components for the Linux-PAM package.
Group: Development
Requires: Linux-PAM-lib = %{version}-%{release}
Requires: Linux-PAM-bin = %{version}-%{release}
Requires: Linux-PAM-data = %{version}-%{release}
Provides: Linux-PAM-devel = %{version}-%{release}
Requires: Linux-PAM = %{version}-%{release}

%description dev
dev components for the Linux-PAM package.


%package dev32
Summary: dev32 components for the Linux-PAM package.
Group: Default
Requires: Linux-PAM-lib32 = %{version}-%{release}
Requires: Linux-PAM-bin = %{version}-%{release}
Requires: Linux-PAM-data = %{version}-%{release}
Requires: Linux-PAM-dev = %{version}-%{release}

%description dev32
dev32 components for the Linux-PAM package.


%package doc
Summary: doc components for the Linux-PAM package.
Group: Documentation
Requires: Linux-PAM-man = %{version}-%{release}

%description doc
doc components for the Linux-PAM package.


%package extras
Summary: extras components for the Linux-PAM package.
Group: Default

%description extras
extras components for the Linux-PAM package.


%package lib
Summary: lib components for the Linux-PAM package.
Group: Libraries
Requires: Linux-PAM-data = %{version}-%{release}
Requires: Linux-PAM-license = %{version}-%{release}

%description lib
lib components for the Linux-PAM package.


%package lib32
Summary: lib32 components for the Linux-PAM package.
Group: Default
Requires: Linux-PAM-data = %{version}-%{release}
Requires: Linux-PAM-license = %{version}-%{release}

%description lib32
lib32 components for the Linux-PAM package.


%package license
Summary: license components for the Linux-PAM package.
Group: Default

%description license
license components for the Linux-PAM package.


%package locales
Summary: locales components for the Linux-PAM package.
Group: Default

%description locales
locales components for the Linux-PAM package.


%package man
Summary: man components for the Linux-PAM package.
Group: Default

%description man
man components for the Linux-PAM package.


%package setuid
Summary: setuid components for the Linux-PAM package.
Group: Default

%description setuid
setuid components for the Linux-PAM package.


%prep
%setup -q -n Linux-PAM-1.3.1
cd %{_builddir}/Linux-PAM-1.3.1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
pushd ..
cp -a Linux-PAM-1.3.1 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1572549539
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static --includedir=/usr/include/security \
--sysconfdir=/usr/share \
--with-db-uniquename=_pam \
--enable-nls \
--disable-nis \
--disable-regenerate-docu \
--disable-prelude \
--disable-audit --libdir=/usr/lib64
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static --includedir=/usr/include/security \
--sysconfdir=/usr/share \
--with-db-uniquename=_pam \
--enable-nls \
--disable-nis \
--disable-regenerate-docu \
--disable-prelude \
--disable-audit   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :
cd ../build32;
make VERBOSE=1 V=1 %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1572549539
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Linux-PAM
cp %{_builddir}/Linux-PAM-1.3.1/COPYING %{buildroot}/usr/share/package-licenses/Linux-PAM/5fb122a984b09d5c687513bb34a51eeeff2b13a7
cp %{_builddir}/Linux-PAM-1.3.1/Copyright %{buildroot}/usr/share/package-licenses/Linux-PAM/5fb122a984b09d5c687513bb34a51eeeff2b13a7
cp %{_builddir}/Linux-PAM-1.3.1/libpamc/License %{buildroot}/usr/share/package-licenses/Linux-PAM/c6f28267889e6d36329831cfb36f80cdf4612523
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
%find_lang Linux-PAM
## install_append content
rm -f %{buildroot}/usr/share/environment
install -d %{buildroot}/usr/share/pam.d/
for FILE in common-account common-auth common-password \
common-session common-session-noninteractive \
other; do
install -m 0644 $FILE %{buildroot}/usr/share/pam.d/
done
chmod 4755 %{buildroot}/usr/bin/unix_chkpwd
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mkhomedir_helper
/usr/bin/pam_tally
/usr/bin/pam_tally2
/usr/bin/pam_timestamp_check
/usr/bin/unix_update

%files data
%defattr(-,root,root,-)
/usr/share/pam.d/common-account
/usr/share/pam.d/common-auth
/usr/share/pam.d/common-password
/usr/share/pam.d/common-session
/usr/share/pam.d/common-session-noninteractive
/usr/share/pam.d/other
/usr/share/security/access.conf
/usr/share/security/group.conf
/usr/share/security/limits.conf
/usr/share/security/namespace.conf
/usr/share/security/namespace.init
/usr/share/security/pam_env.conf
/usr/share/security/time.conf

%files dev
%defattr(-,root,root,-)
/usr/include/security/_pam_compat.h
/usr/include/security/_pam_macros.h
/usr/include/security/_pam_types.h
/usr/include/security/pam_appl.h
/usr/include/security/pam_client.h
/usr/include/security/pam_ext.h
/usr/include/security/pam_filter.h
/usr/include/security/pam_misc.h
/usr/include/security/pam_modules.h
/usr/include/security/pam_modutil.h
/usr/lib64/libpam.so
/usr/lib64/libpam_misc.so
/usr/lib64/libpamc.so
/usr/share/man/man3/misc_conv.3
/usr/share/man/man3/pam.3
/usr/share/man/man3/pam_acct_mgmt.3
/usr/share/man/man3/pam_authenticate.3
/usr/share/man/man3/pam_chauthtok.3
/usr/share/man/man3/pam_close_session.3
/usr/share/man/man3/pam_conv.3
/usr/share/man/man3/pam_end.3
/usr/share/man/man3/pam_error.3
/usr/share/man/man3/pam_fail_delay.3
/usr/share/man/man3/pam_get_authtok.3
/usr/share/man/man3/pam_get_authtok_noverify.3
/usr/share/man/man3/pam_get_authtok_verify.3
/usr/share/man/man3/pam_get_data.3
/usr/share/man/man3/pam_get_item.3
/usr/share/man/man3/pam_get_user.3
/usr/share/man/man3/pam_getenv.3
/usr/share/man/man3/pam_getenvlist.3
/usr/share/man/man3/pam_info.3
/usr/share/man/man3/pam_misc_drop_env.3
/usr/share/man/man3/pam_misc_paste_env.3
/usr/share/man/man3/pam_misc_setenv.3
/usr/share/man/man3/pam_open_session.3
/usr/share/man/man3/pam_prompt.3
/usr/share/man/man3/pam_putenv.3
/usr/share/man/man3/pam_set_data.3
/usr/share/man/man3/pam_set_item.3
/usr/share/man/man3/pam_setcred.3
/usr/share/man/man3/pam_sm_acct_mgmt.3
/usr/share/man/man3/pam_sm_authenticate.3
/usr/share/man/man3/pam_sm_chauthtok.3
/usr/share/man/man3/pam_sm_close_session.3
/usr/share/man/man3/pam_sm_open_session.3
/usr/share/man/man3/pam_sm_setcred.3
/usr/share/man/man3/pam_start.3
/usr/share/man/man3/pam_strerror.3
/usr/share/man/man3/pam_syslog.3
/usr/share/man/man3/pam_verror.3
/usr/share/man/man3/pam_vinfo.3
/usr/share/man/man3/pam_vprompt.3
/usr/share/man/man3/pam_vsyslog.3
/usr/share/man/man3/pam_xauth_data.3

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libpam.so
/usr/lib32/libpam_misc.so
/usr/lib32/libpamc.so

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/Linux\-PAM/*

%files extras
%defattr(-,root,root,-)
/usr/lib32/security/pam_filter/upperLOWER
/usr/lib64/security/pam_filter/upperLOWER

%files lib
%defattr(-,root,root,-)
/usr/lib64/libpam.so.0
/usr/lib64/libpam.so.0.84.2
/usr/lib64/libpam_misc.so.0
/usr/lib64/libpam_misc.so.0.82.1
/usr/lib64/libpamc.so.0
/usr/lib64/libpamc.so.0.82.1
/usr/lib64/security/pam_access.so
/usr/lib64/security/pam_cracklib.so
/usr/lib64/security/pam_debug.so
/usr/lib64/security/pam_deny.so
/usr/lib64/security/pam_echo.so
/usr/lib64/security/pam_env.so
/usr/lib64/security/pam_exec.so
/usr/lib64/security/pam_faildelay.so
/usr/lib64/security/pam_filter.so
/usr/lib64/security/pam_ftp.so
/usr/lib64/security/pam_group.so
/usr/lib64/security/pam_issue.so
/usr/lib64/security/pam_keyinit.so
/usr/lib64/security/pam_lastlog.so
/usr/lib64/security/pam_limits.so
/usr/lib64/security/pam_listfile.so
/usr/lib64/security/pam_localuser.so
/usr/lib64/security/pam_loginuid.so
/usr/lib64/security/pam_mail.so
/usr/lib64/security/pam_mkhomedir.so
/usr/lib64/security/pam_motd.so
/usr/lib64/security/pam_namespace.so
/usr/lib64/security/pam_nologin.so
/usr/lib64/security/pam_permit.so
/usr/lib64/security/pam_pwhistory.so
/usr/lib64/security/pam_rhosts.so
/usr/lib64/security/pam_rootok.so
/usr/lib64/security/pam_securetty.so
/usr/lib64/security/pam_shells.so
/usr/lib64/security/pam_stress.so
/usr/lib64/security/pam_succeed_if.so
/usr/lib64/security/pam_tally.so
/usr/lib64/security/pam_tally2.so
/usr/lib64/security/pam_time.so
/usr/lib64/security/pam_timestamp.so
/usr/lib64/security/pam_umask.so
/usr/lib64/security/pam_unix.so
/usr/lib64/security/pam_warn.so
/usr/lib64/security/pam_wheel.so
/usr/lib64/security/pam_xauth.so

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libpam.so.0
/usr/lib32/libpam.so.0.84.2
/usr/lib32/libpam_misc.so.0
/usr/lib32/libpam_misc.so.0.82.1
/usr/lib32/libpamc.so.0
/usr/lib32/libpamc.so.0.82.1
/usr/lib32/security/pam_access.so
/usr/lib32/security/pam_debug.so
/usr/lib32/security/pam_deny.so
/usr/lib32/security/pam_echo.so
/usr/lib32/security/pam_env.so
/usr/lib32/security/pam_exec.so
/usr/lib32/security/pam_faildelay.so
/usr/lib32/security/pam_filter.so
/usr/lib32/security/pam_ftp.so
/usr/lib32/security/pam_group.so
/usr/lib32/security/pam_issue.so
/usr/lib32/security/pam_keyinit.so
/usr/lib32/security/pam_lastlog.so
/usr/lib32/security/pam_limits.so
/usr/lib32/security/pam_listfile.so
/usr/lib32/security/pam_localuser.so
/usr/lib32/security/pam_loginuid.so
/usr/lib32/security/pam_mail.so
/usr/lib32/security/pam_mkhomedir.so
/usr/lib32/security/pam_motd.so
/usr/lib32/security/pam_namespace.so
/usr/lib32/security/pam_nologin.so
/usr/lib32/security/pam_permit.so
/usr/lib32/security/pam_pwhistory.so
/usr/lib32/security/pam_rhosts.so
/usr/lib32/security/pam_rootok.so
/usr/lib32/security/pam_securetty.so
/usr/lib32/security/pam_shells.so
/usr/lib32/security/pam_stress.so
/usr/lib32/security/pam_succeed_if.so
/usr/lib32/security/pam_tally.so
/usr/lib32/security/pam_tally2.so
/usr/lib32/security/pam_time.so
/usr/lib32/security/pam_timestamp.so
/usr/lib32/security/pam_umask.so
/usr/lib32/security/pam_unix.so
/usr/lib32/security/pam_warn.so
/usr/lib32/security/pam_wheel.so
/usr/lib32/security/pam_xauth.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Linux-PAM/5fb122a984b09d5c687513bb34a51eeeff2b13a7
/usr/share/package-licenses/Linux-PAM/c6f28267889e6d36329831cfb36f80cdf4612523

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/access.conf.5
/usr/share/man/man5/environment.5
/usr/share/man/man5/group.conf.5
/usr/share/man/man5/limits.conf.5
/usr/share/man/man5/namespace.conf.5
/usr/share/man/man5/pam.conf.5
/usr/share/man/man5/pam.d.5
/usr/share/man/man5/pam_env.conf.5
/usr/share/man/man5/time.conf.5
/usr/share/man/man8/PAM.8
/usr/share/man/man8/mkhomedir_helper.8
/usr/share/man/man8/pam.8
/usr/share/man/man8/pam_access.8
/usr/share/man/man8/pam_cracklib.8
/usr/share/man/man8/pam_debug.8
/usr/share/man/man8/pam_deny.8
/usr/share/man/man8/pam_echo.8
/usr/share/man/man8/pam_env.8
/usr/share/man/man8/pam_exec.8
/usr/share/man/man8/pam_faildelay.8
/usr/share/man/man8/pam_filter.8
/usr/share/man/man8/pam_ftp.8
/usr/share/man/man8/pam_group.8
/usr/share/man/man8/pam_issue.8
/usr/share/man/man8/pam_keyinit.8
/usr/share/man/man8/pam_lastlog.8
/usr/share/man/man8/pam_limits.8
/usr/share/man/man8/pam_listfile.8
/usr/share/man/man8/pam_localuser.8
/usr/share/man/man8/pam_loginuid.8
/usr/share/man/man8/pam_mail.8
/usr/share/man/man8/pam_mkhomedir.8
/usr/share/man/man8/pam_motd.8
/usr/share/man/man8/pam_namespace.8
/usr/share/man/man8/pam_nologin.8
/usr/share/man/man8/pam_permit.8
/usr/share/man/man8/pam_pwhistory.8
/usr/share/man/man8/pam_rhosts.8
/usr/share/man/man8/pam_rootok.8
/usr/share/man/man8/pam_securetty.8
/usr/share/man/man8/pam_shells.8
/usr/share/man/man8/pam_succeed_if.8
/usr/share/man/man8/pam_tally.8
/usr/share/man/man8/pam_tally2.8
/usr/share/man/man8/pam_time.8
/usr/share/man/man8/pam_timestamp.8
/usr/share/man/man8/pam_timestamp_check.8
/usr/share/man/man8/pam_umask.8
/usr/share/man/man8/pam_unix.8
/usr/share/man/man8/pam_warn.8
/usr/share/man/man8/pam_wheel.8
/usr/share/man/man8/pam_xauth.8
/usr/share/man/man8/unix_chkpwd.8
/usr/share/man/man8/unix_update.8

%files setuid
%defattr(-,root,root,-)
%attr(4755, root, root) /usr/bin/unix_chkpwd

%files locales -f Linux-PAM.lang
%defattr(-,root,root,-)

