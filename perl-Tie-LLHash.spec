%include	/usr/lib/rpm/macros.perl
%define	pdir	Tie
%define	pnam	LLHash
Summary:	Tie::LLHash Perl module - ordered hashes
Summary(pl):	Modu³ Perla Tie::LLHash - uporz±dkowane hasze
Name:		perl-Tie-LLHash
Version:	1.002
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class implements an ordered hash-like object. It's a cross
between a Perl hash and a linked list. Use it whenever you want the
speed and structure of a Perl hash, but the orderedness of a list.

%description -l pl
Ta klasa jest implementacj± obiektu podobnego do hasza. Jest on
skrzy¿owaniem pomiêdzy perlowym haszem a list±. Przydaje siê kiedy
potrzeba szybko¶ci i struktury perlowych haszy, ale uporz±dkowania
listy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Tie/LLHash.pm
%{_mandir}/man3/*
