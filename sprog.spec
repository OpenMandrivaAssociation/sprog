%define module	Sprog
%define name	sprog
%define version	0.14
%define	release	%mkrel 5

%define	_requires_exceptions perl(Sprog::Gear::$parent)

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A graphical tool to build programs by plugging parts together
License:	GPL or Artistic
Group:		Development/Perl
Source0:	%{module}-%{version}.tar.bz2
Url:		http://sprog.sourceforge.net/
BuildRequires:	perl-Apache-LogRegex
BuildRequires:	perl-devel
BuildRequires:	perl-Gnome2-Canvas
BuildRequires:	perl-Gtk2-GladeXML
BuildRequires:	perl-Imager
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Sprog is a tool for working with data. It allows you to do all the things those
clever Unix geeks can do with their cryptic command lines but you can now do it
all with point-n-click and drag-n-drop.

A Sprog machine has many similarities to a shell script. It is built from small
reusable parts (called gears) that are connected together to filter and massage
your data. Once you have built a machine, you can save it and run it again and
again to automatically perform repetitive tasks.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
#- needs X11
#%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/%{module}/*
%{perl_vendorlib}/%{module}.pm
%{_mandir}/*/*
%{_bindir}/sprog



%changelog
* Sun Jul 26 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-5mdv2010.0
+ Revision: 400262
- fix dependencies

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.14-3mdv2009.0
+ Revision: 253009
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.14-1mdv2008.1
+ Revision: 127566
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import sprog


* Sun Jul 31 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.14-1mdk
- 0.14

* Mon Jul 04 2005 Lenny Cartier <lenny@mandriva.com> 0.13-1mdk
- 0.13

* Tue Jun 28 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.12-1mdk
- 0.12

* Fri Jun 24 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.11-1mdk
- First Mandriva release
