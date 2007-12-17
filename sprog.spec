%define module	Sprog
%define name	sprog
%define version	0.14
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A graphical tool to build programs by plugging parts together
License:	GPL or Artistic
Group:		Development/Perl
Source0:	%{module}-%{version}.tar.bz2
Url:		http://sprog.sourceforge.net/
BuildArch:	noarch
BuildRequires:	perl-Apache-LogRegex
BuildRequires:	perl-devel
BuildRequires:	perl-Gnome2-Canvas
BuildRequires:	perl-Gtk2-GladeXML
BuildRequires:	perl-Imager

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

