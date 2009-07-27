
%define plugin	alcd
%define name	vdr-plugin-%plugin
%define version	1.5.1
%define rel	3

Summary:	VDR plugin: Activy300 LCD-Plugin
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.htpc-forum.de/
Source:		vdr-%plugin-%version.tgz
Source1:	activy.init
Patch0:		alcd-invalid-const-char-conversion.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
Enables the LCD display of the Activy300 boxes from Siemens.

%prep
%setup -q -c
cd %plugin
%patch0 -p1
chmod a-x BUGS TODO
%vdr_plugin_prep

%vdr_plugin_params_begin %{plugin}
# script to execute after pic reset
# default: %{_bindir}/activy.sh
var=RESETSCRIPT
param=--resetscript=RESETSCRIPT
default=%{_bindir}/activy.sh
%vdr_plugin_params_end

%build
cd %plugin
%vdr_plugin_build afp-tool -j1

%install
rm -rf %{buildroot}
cd %plugin
%vdr_plugin_install

install -d -m755 %{buildroot}%{_bindir}
install -m755 scripts/*.sh %{buildroot}%{_bindir}

install -d -m755 %{buildroot}%{_initrddir}
install -m755 %{SOURCE1} %{buildroot}%{_initrddir}/activy

%make install PREFIX=%{buildroot}%{_prefix}

%post
%vdr_plugin_post %plugin
%_post_service activy

%preun
%_preun_service activy

%postun
%vdr_plugin_postun %plugin

%clean
rm -rf %{buildroot}

%files -f %plugin/%plugin.vdr
%defattr(-,root,root)
%doc alcd/BUGS alcd/HISTORY alcd/README alcd/TODO
%{_initrddir}/activy
%{_bindir}/afp-tool
%{_bindir}/*.sh


