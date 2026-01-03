#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Archive
%define		pnam	Extract
Summary:	Archive::Extract - A generic archive extracting mechanism
Summary(pl.UTF-8):	Archive::Extract - ogólny mechanizm rozpakowywania archiwów
Name:		perl-Archive-Extract
Version:	0.88
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Archive/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	371b449317ac009a4deed6577da85b8c
URL:		https://metacpan.org/release/Archive-Extract
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Archive::Extract is a generic archive extraction mechanism.

It allows you to extract any archive file of the type .tar, .tar.gz,
.gz, .Z, .tar.bz2, .tbz, .bz2, .zip, .xz,, .txz, .tar.xz or .lzma
without having to worry how it does so, or use different interfaces
for each type by using either perl modules, or commandline tools on
your system.

%description -l pl.UTF-8
Archive::Extract to ogólny mechanizm rozpakowywania archiwów.

Pozwala rozpakowywać dowolne pliki archiwów typu .tar, .tar.gz, .gz,
.Z, .tar.bz2, .tbz, .bz2, .zip, .xz, .txz, .tar.gz lub .lzma bez
zastanawiania się, jak to robi albo używania różnych interfejsów dla
każdego rodzaju pliku i w zależności od tego wykorzystywania modułów
perlowych lub narzędzi linii poleceń.

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
%{_mandir}/man3/Archive::Extract.3pm*
