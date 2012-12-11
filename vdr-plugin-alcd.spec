
%define plugin	alcd
%define name	vdr-plugin-%plugin
%define version	1.5.2
%define rel	1

Summary:	VDR plugin: Activy300 LCD-Plugin
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.htpc-forum.de/
Source:		vdr-%plugin-%version.tgz
Source1:	activy.init
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
Enables the LCD display of the Activy300 boxes from Siemens.

%prep
%setup -q -c
cd %plugin
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




%changelog
* Sat Aug 14 2010 Anssi Hannula <anssi@mandriva.org> 1.5.2-1mdv2011.0
+ Revision: 569790
- new version
- drop upstreamed const-char-conversion.patch

* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 1.5.1-3mdv2011.0
+ Revision: 401089
- actually rebuild for new VDR
- rebuild for new VDR

* Wed Jul 15 2009 Anssi Hannula <anssi@mandriva.org> 1.5.1-1mdv2010.0
+ Revision: 396062
- disable parallel build, it is broken
- new version
- include afp-tool
- provide initscript for activy
- fix build with GCC 4.4 (invalid-const-char-conversion.patch)

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 1.3.0-2mdv2009.1
+ Revision: 359274
- rebuild for new vdr

* Sun May 11 2008 Anssi Hannula <anssi@mandriva.org> 1.3.0-1mdv2009.0
+ Revision: 205450
- new version
- drop i18n patch, fixed upstream

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 1.2.4-2mdv2009.0
+ Revision: 197891
- rebuild for new vdr
- new version
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 1.2.2-7mdv2008.1
+ Revision: 145004
- rebuild for new vdr

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 1.2.2-6mdv2008.1
+ Revision: 144966
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 1.2.2-5mdv2008.1
+ Revision: 103052
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 1.2.2-4mdv2008.0
+ Revision: 49961
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 1.2.2-3mdv2008.0
+ Revision: 42048
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 1.2.2-2mdv2008.0
+ Revision: 22685
- rebuild for new vdr

* Tue May 01 2007 Anssi Hannula <anssi@mandriva.org> 1.2.2-1mdv2008.0
+ Revision: 19749
- 1.2.2


* Sun Jan 21 2007 Anssi Hannula <anssi@mandriva.org> 1.2.1-1mdv2007.0
+ Revision: 111481
- 1.2.1

* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 1.2.0-2mdv2007.1
+ Revision: 90883
- rebuild for new vdr

* Fri Nov 03 2006 Anssi Hannula <anssi@mandriva.org> 1.2.0-1mdv2007.1
+ Revision: 76328
- 1.2.0

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 1.0.0-8mdv2007.1
+ Revision: 73936
- rebuild for new vdr
- Import vdr-plugin-alcd

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 1.0.0-7mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 1.0.0-6mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 1.0.0-5mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 1.0.0-4mdv2007.0
- rebuild for new vdr

* Tue Jun 20 2006 Anssi Hannula <anssi@mandriva.org> 1.0.0-3mdv2007.0
- rebuild for new vdr

* Mon Jun 05 2006 Anssi Hannula <anssi@mandriva.org> 1.0.0-2mdv2007.0
- rebuild for new vdr

* Sat Jun 03 2006 Anssi Hannula <anssi@mandriva.org> 1.0.0-1mdv2007.0
- initial Mandriva release

