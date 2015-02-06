%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Win32::(.*)\\)'
%endif

Name:		fusioninventory-agent-plugin-ocsdeploy
Version:	1.0.5
Release:	4
Summary:	OCS Inventory Software deployment support for FusionInventory agent
License:	GPL
Group:		System/Servers
URL:		http://fusioninventory.org/wordpress/
Source0:	http://search.cpan.org/CPAN/authors/id/G/GO/GONERI/FusionInventory-Agent-Task-OcsDeploy-%{version}.tar.gz
BuildArch:  noarch
BuildRequires: perl-devel

%description
With this module, FusionInventory can accept software deployment request from
an OCS Inventory server.

%prep
%setup -q -n FusionInventory-Agent-Task-OcsDeploy-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc AUTHORS Changes README LICENSE
%{perl_vendorlib}/FusionInventory
%{_mandir}/man3/*

