%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define module_name arkcli

Name:           python-%{module_name}
Version:        0.0.1
Release:        1
Summary:        arkcli - CLI that wraps arkservers.net

License:        ASLv2
URL:            https://github.com/teriyakichild/arkcli
Source0:        %{module_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-setuptools

Requires:       npm, nodejs


%description

%prep
%setup -q -n %{module_name}-%{version}


%build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT

%files
%doc README.md
%{python_sitelib}/*
%attr(0755,-,-) %{_bindir}/arkcli

%changelog
* Fri Jan 22 2016 Tony Rogers <tony.rogers@rackspace.com> - 1.0.0
* Tue Nov 25 2014 Tony Rogers <tony.rogers@rackspace.com> - 0.1.1
* Mon Sep 8 2014 Tony Rogers <tony.rogers@rackspace.com> - 0.1.0
- Initial spec
