
%define plugin	alcd
%define name	vdr-plugin-%plugin
%define version	1.2.2
%define rel	3

Summary:	VDR plugin: Activy300 LCD-Plugin
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.htpc-forum.de/
Source:		vdr-%plugin-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi

%description
Enables the LCD display of the Activy300 boxes from Siemens.

%prep
%setup -q -c
cd %plugin
chmod a-x BUGS TODO

%vdr_plugin_params_begin %{plugin}
# script to execute after pic reset
# default: %{_bindir}/activy.sh
var=RESETSCRIPT
param=--resetscript=RESETSCRIPT
default=%{_bindir}/activy.sh
%vdr_plugin_params_end

%build
cd %plugin
%vdr_plugin_build

%install
rm -rf %{buildroot}
cd %plugin
%vdr_plugin_install

install -d -m755 %{buildroot}%{_bindir}
install -m755 scripts/*.sh %{buildroot}%{_bindir}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%clean
rm -rf %{buildroot}

%files -f %plugin/%plugin.vdr
%defattr(-,root,root)
%doc alcd/BUGS alcd/HISTORY alcd/README alcd/TODO
%{_bindir}/*.sh


