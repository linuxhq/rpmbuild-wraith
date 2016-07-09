%global date 20160428
%global wraith_commit 1ec454d4673a297194630c6770f7a70dd558b32e
%global bdlib_commit 71efa7a30ea6c08759d7a50ab503be4f6a901f95
%global wraith_short_commit %(c=%{wraith_commit}; echo ${c:0:7})

Name:           wraith
Version:        %{date}git%{wraith_short_commit}
Release:        1%{?dist}
Summary:        Wraith IRC Bot
Group:          Applications/Internet
License:        GPL
URL:            https://github.com/%{name}/%{name}
Source0:        https://github.com/%{name}/%{name}/archive/%{wraith_commit}/%{name}-%{wraith_commit}.tar.gz
Source1:        https://github.com/bdrewery/bdlib/archive/%{bdlib_commit}/bdlib-%{bdlib_commit}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       expect, openssl, perl(Digest::MD5), tcl
BuildRequires:  libstdc++-static, openssl-devel, tcl-devel
%if 0%{?el6}
BuildRequires:  devtoolset-1.1-gcc, devtoolset-1.1-gcc-c++, devtoolset-1.1-libstdc++-devel
BuildRequires:  devtoolset-1.1-runtime, scl-utils
%else 
BuildRequires:  gcc, gcc-c++
%endif

%description
Wraith is an open source IRC bot written in C++. It has been in 
development since late 2003. It is based on Eggdrop 1.6.12 but has 
since evolved into something much different at its core.

%prep
%setup -q -n %{name}-%{wraith_commit}
%build
%{__sed} -i -e 's/GIT_REQUIRED=1/GIT_REQUIRED=0/' configure
%{__tar} zxvf %{SOURCE1} -C ./lib/bdlib --strip-components=1
%if 0%{?el6}
export CC=/opt/centos/devtoolset-1.1/root/usr/bin/gcc
export CPP=/opt/centos/devtoolset-1.1/root/usr/bin/cpp
export CXX=/opt/centos/devtoolset-1.1/root/usr/bin/c++
%endif
%configure \
	--with-tclinc="%{_includedir}/tcl.h" \
	--with-tcllib="%{_libdir}/libtcl.so"
%{__make} %{?_smp_mflags}

%install
%{__install} -d -m 0755 %{buildroot}%{_bindir}
%{__install} -m 0755 %{name} %{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc CONTRIBUTING.md FEATURES.md LICENSE README.md doc/* scripts/*
%{_bindir}/%{name}

%changelog
* Thu Apr 28 2016 Taylor Kimball <taylor@linuxhq.org> - 20160428git1ec454d-1
- Update to commit 1ec454d.

* Wed Sep 02 2015 Taylor Kimball <taylor@linuxhq.org> - 20150902gitd28d690-1
- Initial package.
