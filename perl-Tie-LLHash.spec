%include	/usr/lib/rpm/macros.perl
%define	pdir	Tie
%define	pnam	LLHash
Summary:	Tie::LLHash.pm - ordered hashes
Name:		perl-Tie-LLHash
Version:	1.002
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class implements an ordered hash-like object.  It's a cross between
a Perl hash and a linked list.  Use it whenever you want the speed and
structure of a Perl hash, but the orderedness of a list.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Tie/LLHash.pm
%{_mandir}/man3/*
