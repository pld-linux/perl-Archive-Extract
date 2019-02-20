#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Archive
%define		pnam	Extract
%include	/usr/lib/rpm/macros.perl
Summary:	Archive::Extract - A generic archive extracting mechanism
#Summary(pl.UTF-8):	
Name:		perl-Archive-Extract
Version:	0.80
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Archive/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	03bba7ac7f5190d55575764f38fe9028
URL:		http://search.cpan.org/dist/Archive-Extract/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Archive::Extract is a generic archive extraction mechanism.

It allows you to extract any archive file of the type .tar, .tar.gz,
.gz, .Z, tar.bz2, .tbz, .bz2, .zip, .xz,, .txz, .tar.xz or .lzma
without having to worry how it does so, or use different interfaces
for each type by using either perl modules, or commandline tools on
your system.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorlib}/Archive/Extract.pm
%{_mandir}/man3/*
