Name:           perl-DirTree
Version:        0.01
Release:        1%{?dist}
Summary:        DirTree Perl module
License:        CHECK(Distributable)
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/DirTree/
Source0:        http://www.cpan.org/modules/by-module/DirTree/DirTree-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5.006
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
DirTree, similar to tree, perl implementation to display project struture

%prep
%setup -q -n DirTree-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Nov 19 2015 Gang Liang <gang.liang.2011@gmail.com> 0.01-1
- Specfile autogenerated by cpanspec 1.78.
