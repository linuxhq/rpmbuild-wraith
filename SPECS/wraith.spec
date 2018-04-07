Name:           wraith
Version:        1.4.8
Release:        1%{?dist}
Summary:        Wraith IRC Bot
Group:          Applications/Internet
License:        GPL
URL:            http://wraith.botpack.net
Source0:        http://downloads.sourceforge.net/project/wraithbotpack/src/tags/wraith-v1.4.8.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       expect
BuildRequires:  gcc, libstdc++-static, openssl-devel, tcl-devel

%description
Wraith is an open source IRC bot written in C++. It has been in 
development since late 2003. It is based on Eggdrop 1.6.12 but has 
since evolved into something much different at its core.

%prep
%setup -q -n %{name}-v%{version}
%build
%configure \
	--with-tclinc="%{_includedir}/tcl.h" \
	--with-tcllib="%{_libdir}/libtcl.so"
%{__make} %{?_smp_mflags}

%install
%{__install} -d -m 0755 %{buildroot}%{_bindir}
%{__install} -m 0554 %{name} %{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE README.md doc/ scripts/
%{_bindir}/%{name}

%changelog
* Fri Apr 06 2018 Taylor Kimball <tkimball@linuxhq.org> - 1.4.8-1
- Update to v1.4.8

* Thu Apr 28 2016 Taylor Kimball <tkimball@linuxhq.org> - 20160428git1ec454d-1
- Update to commit 1ec454d.

* Wed Sep 02 2015 Taylor Kimball <tkimball@linuxhq.org> - 20150902gitd28d690-1
- Initial package.
