Summary:	Command line tools for the Google Data APIs
Name:		googlecl
Version:	0.9.7
Release:	0.1
License:	Apache v2.0
Group:		Applications/Text
Source0:	http://googlecl.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	936bdb036c340eb1f9d5b9b6b592e1b2
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

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/google
%{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/*.egg-info
