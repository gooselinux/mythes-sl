Name: mythes-sl
Summary: Slovenian thesaurus
%define upstreamid 20090908
Version: 0.%{upstreamid}
Release: 1%{?dist}
Source: http://193.2.66.133:85/download/thes_sl_SI_v2.zip
Group: Applications/Text
URL: http://www.tezaver.si/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: python, perl
License: LGPLv2+
BuildArch: noarch

%description
Slovenian thesaurus.

%prep
%setup -q -c

%build
chmod -x *
for i in README_th_sl_SI_v2.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_sl_SI_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_th_sl_SI_v2.txt
%dir %{_datadir}/mythes
%{_datadir}/mythes/*

%changelog
* Tue Sep 08 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090908-1
- latest version

* Sat Aug 08 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090808-1
- latest version

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090708-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090708-2
- tidy spec

* Wed Jul 08 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090708-1
- latest version

* Mon Jun 08 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090608-1
- latest version

* Sat Mar 28 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090328-1
- latest version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090222-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 22 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090222-1
- latest version

* Wed Jan 21 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090121-1
- initial version
