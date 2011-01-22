Summary:	Command line tools for the Google Data APIs
Name:		googlecl
Version:	0.9.12
Release:	1
License:	Apache v2.0
Group:		Applications/Text
Source0:	http://googlecl.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	a7470a169871ae4918e5b146f025364b
URL:		http://code.google.com/p/googlecl/
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	rpm-pythonprov
Requires:	python-gdata >= 2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Google Data APIs allow programmatic access to various Google
services. This package wraps a subset of those APIs into a
command-line tool that makes it easy to do things like posting to a
Blogger blog, uploading files to Picasa, or editing a Google Docs
file.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man1
install man/google.1 $RPM_BUILD_ROOT%{_mandir}/man1

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changelog README.config README.new-usage README.txt
%attr(755,root,root) %{_bindir}/google
%{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/*.egg-info
%{_mandir}/man1/google.1*
