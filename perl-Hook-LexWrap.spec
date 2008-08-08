#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Hook
%define		pnam	LexWrap
Summary:	Hook::LexWrap - Lexically scoped subroutine wrappers
Name:		perl-Hook-LexWrap
Version:	0.20
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Hook/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e3aaeb59a3adddc80ed3867e4d16654e
URL:		http://search.cpan.org/dist/Hook-LexWrap/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hook::LexWrap allows you to install a pre- or post-wrapper (or both)
around an existing subroutine. Unlike other modules that provide this
capacity (e.g. Hook::PreAndPost and Hook::WrapSub), Hook::LexWrap
implements wrappers in such a way that the standard caller function
works correctly within the wrapped subroutine.

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
%doc Changes
%{perl_vendorlib}/Hook/*.pm
%{_mandir}/man3/*
