#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Tie
%define		pnam	LLHash
Summary:	Tie::LLHash Perl module - ordered hashes
Summary(pl.UTF-8):	Moduł Perla Tie::LLHash - uporządkowane hasze
Name:		perl-Tie-LLHash
Version:	1.003
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b5890351e3e4a1eab89267d9aa410147
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class implements an ordered hash-like object. It's a cross
between a Perl hash and a linked list. Use it whenever you want the
speed and structure of a Perl hash, but the orderedness of a list.

%description -l pl.UTF-8
Ta klasa jest implementacją obiektu podobnego do hasza. Jest on
skrzyżowaniem pomiędzy perlowym haszem a listą. Przydaje się kiedy
potrzeba szybkości i struktury perlowych haszy, ale uporządkowania
listy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Tie/LLHash.pm
%{_mandir}/man3/*
