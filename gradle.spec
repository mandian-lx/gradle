%global __jar_repack 0
%global __provides_exclude_from .*
%global __requires_exclude_from .*
%global __noautoreq '^.*$'
%global __noautoprov '^.*$'

Name:           gradle
Version:        2.2.1
Release:        0.1%{?dist}
Summary:        XXX
License:        XXX
URL:            XXX
BuildArch:      noarch

Source0:        http://services.gradle.org/distributions/gradle-%{version}-bin.zip

Requires:       javapackages-tools
Requires:       java-devel

%description
XXX

%prep
%setup -cT

%install
install -d -m 755 %{buildroot}%{_datadir}/%{name}/
unzip %{SOURCE0}
rm -rf gradle-%{version}/bin/gradle.bat
mv gradle-%{version}/{changelog.txt,LICENSE,NOTICE,getting-started.html} .
cp -a gradle-%{version}/* %{buildroot}%{_datadir}/%{name}/
install -d -m 755 %{buildroot}%{_bindir}/
ln -s %{_datadir}/%{name}/bin/gradle %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%doc changelog.txt LICENSE NOTICE getting-started.html

%changelog
* Tue Oct  7 2014 Mikolaj Izdebski <mizdebsk@redhat.com>
- Initial packaging

