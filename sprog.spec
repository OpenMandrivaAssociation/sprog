%define module	Sprog

Name:		sprog
Version:	0.14
Release:	6
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
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/%{module}/*
%{perl_vendorlib}/%{module}.pm
%{_mandir}/*/*
%{_bindir}/sprog
