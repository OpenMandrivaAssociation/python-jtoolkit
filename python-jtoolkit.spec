%define oname jToolkit
%define pname jtoolkit
%define name python-%{pname}
%define version 0.7.8
%define release %mkrel 6

Summary: Web application framework
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{oname}-%{version}.tar.bz2
License: GPL
Group: Development/Python
Url: http://jtoolkit.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: python-devel

%description
jToolkit is a Python web application framework built on modpython and
Apache. It can also run in standalone mode using its own builtin HTTP
server.

It is aimed at dynamically generated pages rather than mostly-static
pages (for which there are templating solutions). Pages can be
produced using a variety of widgets or a new templating system. It
handles sessions and database connections.

%prep
%setup -q -n %{oname}-%{version}

%build
./jToolkitSetup.py build

%install
rm -rf %{buildroot}
./jToolkitSetup.py install --prefix=%{buildroot}%{_prefix}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{py_puresitedir}/%{oname}
%{py_puresitedir}/*.egg-info




%changelog
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.7.8-6mdv2010.0
+ Revision: 442202
- rebuild

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 0.7.8-5mdv2009.1
+ Revision: 323734
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.7.8-4mdv2009.0
+ Revision: 259651
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.7.8-3mdv2009.0
+ Revision: 247493
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.7.8-1mdv2008.1
+ Revision: 136450
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Jan 12 2007 Olivier Blin <oblin@mandriva.com> 0.7.8-1mdv2007.0
+ Revision: 108002
- buildrequire python-devel
- initial python-jtoolkit release
- Create python-jtoolkit

