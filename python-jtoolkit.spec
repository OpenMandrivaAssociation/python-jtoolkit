%define oname jToolkit
%define pname jtoolkit
%define name python-%{pname}
%define version 0.7.8
%define release %mkrel 1

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


