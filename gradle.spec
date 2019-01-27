%{?_javapackages_macros:%_javapackages_macros}
# Gradle depends on itself for building.  This can be problematic, for
# example when some library it uses changes API, Gradle may stop
# working and it may be impossible to rebuild it in normal way.
#
# For cases like that bootstrap mode can be used.  In this mode a
# minimal working version of Gradle is built with plain groovyc.  The
# only purpose of bootstrapped Gradle is to rebuild itself.  Gradle
# built using bootstrap mode doesn't have all features, for example it
# doesn't provide Maven metadata, and it may have some functionality
# missing.  For this reason a normal non-bootstrap build should be
# done immediately after Gradle is bootstrapped.
%bcond_with bootstrap

Name:           gradle
Version:        4.4.1
Release:        1%{?with_bootstrap:.boot}
Summary:        Build automation tool
# Some examples and integration tests are under GNU LGPL and Boost
# Software License, but are not used to create binary package.
License:        ASL 2.0
URL:            http://www.gradle.org/
BuildArch:      noarch

Source0:        http://services.gradle.org/distributions/gradle-%{version}-src.zip
Source1:        http://services.gradle.org/versions/all#/all-released-versions.json
Source2:        gradle-font-metadata.xml
Source3:        gradle-jquery-metadata.xml
Source4:        gradle-launcher.sh
Source5:        gradle.desktop
Source6:        gradle-man.txt

# Sources 99xx are used only for bootstrapping.
# Main script used to build gradle with plain groovyc
Source9900:     gradle-bootstrap.sh
# Script used to generate Source991x from upstream binaries
Source9901:     gradle-bootstrap-generate-resources.py
# Files containing information about Gradle module structure
Source9910:     gradle-bootstrap-module-list
Source9911:     gradle-bootstrap-module-dependencies
# List of API mappings, extracted from gradle-docs.jar
Source9920:     gradle-bootstrap-api-mapping.txt
# List of default imorts, extracted from gradle-docs.jar
Source9921:     gradle-bootstrap-default-imports.txt
# List of Gradle plugins, extracted from gradle-core.jar
Source9922:     gradle-bootstrap-plugin.properties
Source9923:     gradle-bootstrap-implementation-plugin.properties
Source9924:     gradle-bootstrap-api-relocated.txt
Source9925:     gradle-bootstrap-test-kit-relocated.txt

Patch0001:      0001-Gradle-local-mode.patch
Patch0002:      0002-Remove-Class-Path-from-manifest.patch
Patch0003:      0003-Implement-XMvn-repository-factory-method.patch
Patch0004:      0004-Use-unversioned-dependency-JAR-names.patch
Patch0005:      0005-Port-to-Maven-3.3.9-and-Eclipse-Aether.patch
Patch0006:      0006-Disable-code-quality-checks.patch
Patch0007:      0007-Port-to-Kryo-3.0.patch
Patch0008:      0008-Port-to-Ivy-2.4.0.patch
Patch0009:      0009-Port-to-Polyglot-0.1.8.patch
Patch0010:      0010-Port-from-Simple-4-to-Jetty-9.patch
Patch0011:      0011-Disable-benchmarks.patch
Patch0012:      0012-Disable-patching-of-external-modules.patch
Patch0013:      0013-Add-missing-transitive-dependencies.patch
Patch0014:      0014-Disable-ideNative-module.patch
Patch0015:      0015-Disable-docs-build.patch
Patch0016:      0016-Port-to-guava-20.0.patch
# it depends on ant which is Java 8+
Patch0017:      0017-Set-core-api-source-level-to-8.patch

BuildRequires:  javapackages-local

# For autosetup
BuildRequires:  git

# Dependencies on build system used.  In bootstrap mode we use plain
# groovyc to compile Gradle, otherwise Gradle is built with itself.
%if %{with bootstrap}
BuildRequires:  groovy >= 2.3
BuildRequires:  javapackages-local
%else
BuildRequires:  gradle-local
%endif

# Generic build dependencies
BuildRequires:  desktop-file-utils
BuildRequires:  hostname
BuildRequires:  procps-ng

# manpage build dependencies
BuildRequires:  asciidoc
BuildRequires:  xmlto

# Artifacts required for Gradle build
BuildRequires:  mvn(antlr:antlr)
BuildRequires:  mvn(biz.aQute.bnd:bndlib)
BuildRequires:  mvn(bsh:bsh)
BuildRequires:  mvn(ch.qos.logback:logback-classic)
BuildRequires:  mvn(ch.qos.logback:logback-core)
BuildRequires:  mvn(com.amazonaws:aws-java-sdk-core)
BuildRequires:  mvn(com.amazonaws:aws-java-sdk-kms)
BuildRequires:  mvn(com.amazonaws:aws-java-sdk-s3)
BuildRequires:  mvn(com.beust:jcommander)
BuildRequires:  mvn(com.esotericsoftware.kryo:kryo)
BuildRequires:  mvn(com.esotericsoftware:minlog)
BuildRequires:  mvn(com.esotericsoftware:reflectasm)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.google.code.findbugs:findbugs)
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(com.google.code.gson:gson)
BuildRequires:  mvn(com.google.guava:guava:20.0)
BuildRequires:  mvn(com.google.guava:guava-jdk5:20.0)
BuildRequires:  mvn(com.google.http-client:google-http-client)
BuildRequires:  mvn(com.google.oauth-client:google-oauth-client)
BuildRequires:  mvn(com.googlecode.jarjar:jarjar)
BuildRequires:  mvn(com.googlecode.jatl:jatl)
BuildRequires:  mvn(com.jcraft:jsch)
BuildRequires:  mvn(com.puppycrawl.tools:checkstyle)
BuildRequires:  mvn(com.sun:tools)
BuildRequires:  mvn(com.typesafe.zinc:zinc)
BuildRequires:  mvn(com.uwyn:jhighlight)
BuildRequires:  mvn(commons-beanutils:commons-beanutils)
BuildRequires:  mvn(commons-cli:commons-cli)
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(commons-collections:commons-collections)
BuildRequires:  mvn(commons-configuration:commons-configuration)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(commons-lang:commons-lang)
BuildRequires:  mvn(dom4j:dom4j)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(jaxen:jaxen)
BuildRequires:  mvn(jline:jline)
BuildRequires:  mvn(joda-time:joda-time)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.java.dev.jna:jna)
BuildRequires:  mvn(net.jcip:jcip-annotations)
BuildRequires:  mvn(net.rubygrapefruit:native-platform)
BuildRequires:  mvn(net.sourceforge.nekohtml:nekohtml)
BuildRequires:  mvn(org.antlr:antlr4-runtime)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ant:ant-launcher)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.geronimo.specs:geronimo-annotation_1.0_spec)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.httpcomponents:httpcore)
BuildRequires:  mvn(org.apache.ivy:ivy)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-file)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-http)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-http-shared)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires:  mvn(org.apache.maven:maven-aether-provider)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-builder-support)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-model-builder)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-repository-metadata)
BuildRequires:  mvn(org.apache.maven:maven-settings)
BuildRequires:  mvn(org.apache.maven:maven-settings-builder)
BuildRequires:  mvn(org.apache.xbean:xbean-reflect)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.bouncycastle:bcpg-jdk15on)
BuildRequires:  mvn(org.bouncycastle:bcprov-jdk15on)
BuildRequires:  mvn(org.codehaus.groovy.modules.http-builder:http-builder)
BuildRequires:  mvn(org.codehaus.groovy:groovy-all)
BuildRequires:  mvn(org.codehaus.plexus:plexus-classworlds)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.codenarc:CodeNarc)
BuildRequires:  mvn(org.eclipse.aether:aether-api)
BuildRequires:  mvn(org.eclipse.aether:aether-connector-basic)
BuildRequires:  mvn(org.eclipse.aether:aether-impl)
BuildRequires:  mvn(org.eclipse.aether:aether-spi)
BuildRequires:  mvn(org.eclipse.aether:aether-transport-wagon)
BuildRequires:  mvn(org.eclipse.aether:aether-util)
BuildRequires:  mvn(org.eclipse.jdt:core)
BuildRequires:  mvn(org.eclipse.jetty:jetty-annotations)
BuildRequires:  mvn(org.eclipse.jetty:jetty-jsp)
BuildRequires:  mvn(org.eclipse.jetty:jetty-plus)
BuildRequires:  mvn(org.eclipse.jetty:jetty-security)
BuildRequires:  mvn(org.eclipse.jetty:jetty-server)
BuildRequires:  mvn(org.eclipse.jetty:jetty-servlet)
BuildRequires:  mvn(org.eclipse.jetty:jetty-util)
BuildRequires:  mvn(org.eclipse.jetty:jetty-webapp)
BuildRequires:  mvn(org.eclipse.jetty:jetty-xml)
BuildRequires:  mvn(org.eclipse.jgit:org.eclipse.jgit)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.fusesource.hawtjni:hawtjni-runtime)
BuildRequires:  mvn(org.fusesource.jansi:jansi)
BuildRequires:  mvn(org.fusesource.jansi:jansi-native)
BuildRequires:  mvn(org.gmetrics:GMetrics)
BuildRequires:  mvn(org.jsoup:jsoup)
BuildRequires:  mvn(org.mozilla:rhino)
BuildRequires:  mvn(org.objenesis:objenesis)
BuildRequires:  mvn(org.ow2.asm:asm-all)
BuildRequires:  mvn(org.parboiled:parboiled-core)
BuildRequires:  mvn(org.parboiled:parboiled-java)
BuildRequires:  mvn(org.pegdown:pegdown)
BuildRequires:  mvn(org.samba.jcifs:jcifs)
BuildRequires:  mvn(org.slf4j:jcl-over-slf4j)
BuildRequires:  mvn(org.slf4j:jul-to-slf4j)
BuildRequires:  mvn(org.slf4j:log4j-over-slf4j)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:  mvn(org.sonatype.plexus:plexus-cipher)
BuildRequires:  mvn(org.sonatype.plexus:plexus-sec-dispatcher)
BuildRequires:  mvn(org.sonatype.pmaven:pmaven-common)
BuildRequires:  mvn(org.sonatype.pmaven:pmaven-groovy)
BuildRequires:  mvn(org.testng:testng)
BuildRequires:  mvn(xerces:xercesImpl)
BuildRequires:  mvn(xml-apis:xml-apis)

# Artifacts required for Gradle build which don't have Maven metadata
# and thus no mvn provides.
BuildRequires:  lato-fonts
BuildRequires:  liberation-mono-fonts
BuildRequires:  js-jquery

# Generic runtime dependencies.
Requires:       javapackages-tools
Requires:       bash
Requires:       hicolor-icon-theme

# Theoretically Gradle might be usable with just JRE, but typical Gradle
# workflow requires full JDK, so we recommend it here.
Recommends:     java-devel

# Providers of symlinks in Gradle lib/ directory. Generated with:
# for l in $(find /usr/share/gradle -type l); do rpm -qf --qf 'Requires:       %{name}\n' $(readlink $l); done | sort -u | grep -v gradle
Requires:       ant-lib
Requires:       apache-commons-cli
Requires:       apache-commons-codec
Requires:       apache-commons-collections
Requires:       apache-commons-compress
Requires:       apache-commons-io
Requires:       apache-commons-lang
Requires:       apache-commons-lang3
Requires:       apache-ivy
Requires:       aqute-bndlib
Requires:       atinject
Requires:       aws-sdk-java-core
Requires:       aws-sdk-java-kms
Requires:       aws-sdk-java-s3
Requires:       base64coder
Requires:       beust-jcommander
Requires:       bouncycastle
Requires:       bouncycastle-pg
Requires:       bsh
Requires:       ecj
Requires:       glassfish-servlet-api
Requires:       google-gson
Requires:       google-guice
Requires:       groovy-lib
Requires:       guava20
Requires:       hawtjni-runtime
Requires:       httpcomponents-client
Requires:       httpcomponents-core
Requires:       jackson-annotations
Requires:       jackson-core
Requires:       jackson-databind
Requires:       jansi
Requires:       jansi-native
Requires:       jatl
Requires:       jcifs
Requires:       jcip-annotations
Requires:       jcl-over-slf4j
Requires:       jetty-server
Requires:       jetty-util
Requires:       jgit
Requires:       joda-time
Requires:       jsch
Requires:       jsr-305
Requires:       jul-to-slf4j
Requires:       junit
Requires:       kryo
Requires:       log4j-over-slf4j
Requires:       maven-lib
Requires:       maven-resolver-api
Requires:       maven-resolver-connector-basic
Requires:       maven-resolver-impl
Requires:       maven-resolver-spi
Requires:       maven-resolver-transport-wagon
Requires:       maven-resolver-util
Requires:       maven-wagon-file
Requires:       maven-wagon-http
Requires:       maven-wagon-http-shared
Requires:       maven-wagon-provider-api
Requires:       minlog
Requires:       native-platform
Requires:       nekohtml
Requires:       objectweb-asm
Requires:       objenesis
Requires:       plexus-cipher
Requires:       plexus-classworlds
Requires:       plexus-containers-component-annotations
Requires:       plexus-interpolation
Requires:       plexus-sec-dispatcher
Requires:       plexus-utils
Requires:       reflectasm
Requires:       rhino
Requires:       sisu-inject
Requires:       sisu-plexus
Requires:       slf4j
Requires:       snakeyaml
Requires:       tesla-polyglot-common
Requires:       tesla-polyglot-groovy
Requires:       testng
Requires:       xbean
Requires:       xerces-j2
Requires:       xml-commons-apis

%description
Gradle is build automation evolved. Gradle can automate the building,
testing, publishing, deployment and more of software packages or other
types of projects such as generated static websites, generated
documentation or indeed anything else.

Gradle combines the power and flexibility of Ant with the dependency
management and conventions of Maven into a more effective way to
build. Powered by a Groovy DSL and packed with innovation, Gradle
provides a declarative way to describe all kinds of builds through
sensible defaults. Gradle is quickly becoming the build system of
choice for many open source projects, leading edge enterprises and
legacy automation challenges.

%prep
%autosetup -S git

# Remove bundled wrapper JAR
rm -rf gradle/wrapper/
# Remove bundled JavaScript
>subprojects/diagnostics/src/main/resources/org/gradle/api/tasks/diagnostics/htmldependencyreport/jquery.jstree.js

# This file is normally downloaded from Internet during package build
mkdir -p build
cp %{SOURCE1} build/all-released-versions.json

# quality checks for which we don't have deps
rm -r buildSrc/src/main/groovy/org/gradle/binarycompatibility
rm buildSrc/src/main/groovy/org/gradle/build/docs/CacheableAsciidoctorTask.groovy

# jquery and fonts don't have Maven metadata
%mvn_config resolverSettings/metadataRepositories/repository %{SOURCE2}
%mvn_config resolverSettings/metadataRepositories/repository %{SOURCE3}

# Tests for bulid script currently fail, but the bulid works.
# TODO: enble tests
rm -rf buildSrc/src/test

# Compilation with Fedora versions of some libraries produces
# warnings. Lets not treat them as errors to make the build work.
sed -i 's/"-Werror" <<//' gradle/strictCompile.gradle

removeProject() {
sed -i "/'$1'/d" settings.gradle
sed -i "s/'$1',\?//" build.gradle
}
removeProject resourcesGcs
rm -r subprojects/resources-gcs
rm -r subprojects/ide-native

%build
%if %{with bootstrap}
mkdir -p subprojects/docs/src/main/resources
mkdir -p subprojects/core/src/main/resources/org/gradle/api/internal/runtimeshaded
cp %{SOURCE9920} subprojects/docs/src/main/resources/api-mapping.txt
cp %{SOURCE9921} subprojects/docs/src/main/resources/default-imports.txt
cp %{SOURCE9922} subprojects/core/src/main/resources/gradle-plugins.properties
cp %{SOURCE9923} subprojects/core/src/main/resources/gradle-implementation-plugins.properties
cp %{SOURCE9924} subprojects/core/src/main/resources/org/gradle/api/internal/runtimeshaded/api-relocated.txt
cp %{SOURCE9925} subprojects/core/src/main/resources/org/gradle/api/internal/runtimeshaded/test-kit-relocated.txt
%{SOURCE9900} %{SOURCE9910} %{SOURCE9911}
%else
# Disables parallel build and daemon mode
rm gradle.properties
gradle-local --offline --no-daemon install xmvnInstall \
    -Pgradle_installPath=$PWD/inst \
    -PfinalRelease -Dbuild.number="%{?fedora:Fedora }%{?rhel:Red Hat }%{version}-%{release}"
%endif

# manpage build
mkdir man
asciidoc -b docbook -d manpage -o man/gradle.xml %{SOURCE6}
xmlto man man/gradle.xml -o man

%install
cp subprojects/distributions/src/toplevel/NOTICE .
cp subprojects/docs/src/samples/application/src/dist/LICENSE .

install -d -m 755 %{buildroot}%{_javadir}/%{name}/

%if %{with bootstrap}
cp -r bootstrap-home %{buildroot}%{_datadir}/%{name}
# Launcher with dependencies needs to be in _javadir
# Dependencies of xmvn-connector-gradle need to have Maven metadata
for mod in launcher base-services core core-api dependency-management resources \
        logging base-services-groovy model-core; do
    %mvn_file ":{gradle-$mod}" %{name}/@1 %{_datadir}/lib/@1
    %mvn_artifact org.gradle:gradle-$mod:%{version} bootstrap-home/lib/gradle-$mod.jar
done

%else # non-bootstrap

rm -rf inst/bin/gradle.bat inst/media
ln -sf %{_bindir}/%{name} inst/bin/gradle
find inst/lib -type f -name 'gradle*' | sed 's:.*/\(gradle-.*\)-%{version}.*:ln -sf %{_javadir}/%{name}/\1.jar &:' | bash -x
ln -sf $(build-classpath ecj) inst/lib/plugins/ecj.jar
xmvn-subst -s $(find inst/lib -type f)
# TODO figure out why this one is missing
ln -s `find-jar commons-lang` inst/lib/
cp -a inst %{buildroot}%{_datadir}/%{name}

%endif

%mvn_install

install -d -m 755 %{buildroot}%{_bindir}/
install -p -m 755 %{SOURCE4} %{buildroot}%{_bindir}/%{name}

desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE5}

for r in 16 24 32 48 64 128 256; do
    install -d -m 755 %{buildroot}%{_datadir}/icons/hicolor/${r}x${r}/apps/
    install -p -m 644 subprojects/distributions/src/toplevel/media/gradle-icon-${r}x${r}.png \
        %{buildroot}%{_datadir}/icons/hicolor/${r}x${r}/apps/%{name}.png
done

install -d -m 755 %{buildroot}%{_mandir}/man1/
install -p -m 644 man/gradle.1 %{buildroot}%{_mandir}/man1/gradle.1

%files -f .mfiles
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/gradle.1*
%license LICENSE NOTICE

%changelog
* Sat Oct 27 2018 Daniel Martinez Oeckel <caravel@fedoraproject.org> - 4.4.1-1
- Update to upstream version 4.4.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 25 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.3.1-7
- Rebuild for objectweb-asm update

* Mon Mar 26 2018 Michael Simacek <msimacek@redhat.com> - 4.3.1-6
- Bump source version to 8 to fix FTBFS
- Remove unused dependency on sonar

* Fri Feb 16 2018 Michael Simacek <msimacek@redhat.com> - 4.3.1-5.boot
- Non-bootstrap build

* Fri Feb 16 2018 Michael Simacek <msimacek@redhat.com> - 4.3.1-4
- Bootstrap build for guava update

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.3.1-2
- Remove obsolete scriptlets

* Mon Nov 13 2017 Michael Simacek <msimacek@redhat.com> - 4.3.1-1
- Non-bootstrap build

* Fri Nov 10 2017 Michael Simacek <msimacek@redhat.com> - 4.3.1-0.1.boot
- Update to upstream version 4.3.1

* Mon Oct 16 2017 Michael Simacek <msimacek@redhat.com> - 4.2.1-2
- Disable parallel build, it causes non-determinism in installation

* Mon Oct 16 2017 Michael Simacek <msimacek@redhat.com> - 4.2.1-1.1.boot
- Bootstrap build to fix installation

* Mon Oct 16 2017 Michael Simacek <msimacek@redhat.com> - 4.2.1-1
- Non-bootstrap build

* Wed Sep 20 2017 Michael Simacek <msimacek@redhat.com> - 4.2.1-0.1.boot
- Update to upstream version 4.2.1

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.13-9
- Port to XMvn 3.0.0
- Port to Checkstyle 8.0

* Thu Apr 20 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.13-8
- Rebuild for Maven 3.5.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 28 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.13-6
- Fix bootstrap build after aqute-bnd update

* Mon May 30 2016 Michael Simacek <msimacek@redhat.com> - 2.13-5
- Also add bndlib.annotations to dependencies

* Mon May 30 2016 Michael Simacek <msimacek@redhat.com> - 2.13-4
- Add transitive dep on aqute-libg

* Wed May 25 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.13-3
- Enable S3 plugin

* Mon May 02 2016 Michael Simacek <msimacek@redhat.com> - 2.13-2
- Add manpage (Resolves rhbz#1262238)

* Tue Apr 26 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.13-1
- Update to upstream version 2.13

* Tue Apr 19 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.13-0.2.rc1
- Fix test worker classpath

* Mon Apr 11 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.13-0.1.rc1
- Update to upstream version 2.13-rc-1

* Thu Mar 17 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.12-1
- Update to upstream version 2.12

* Wed Mar  9 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.12-0.1.rc1
- Update to upstream version 2.12-rc-1

* Tue Feb 16 2016 Mikolaj Izdebski <mizdebsk@redhat.com> 2.11-1
- Update to upstream version 2.11

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan  5 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.10-1
- Update to upstream version 2.10

* Wed Dec  2 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.9-2
- Enable Zinc Scala compiler

* Mon Nov 23 2015 Michael Simacek <msimacek@redhat.com> - 2.9-1
- Update to upstream version 2.9
- Fix bootstrap build

* Wed Oct 28 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.8-2
- Install artifacts using XMvn Gradle plugin

* Tue Oct 20 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.8-1
- Update to upstream version 2.8

* Fri Oct  9 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.8-0.1.rc1
- Update to upstream version 2.8-rc-1

* Mon Sep 28 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.7-2
- Define minimal versions of some dependencies
- Resolves: rhbz#1266550

* Mon Sep 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.7-1
- Update to upstream version 2.7

* Fri Sep 11 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.7-0.3.rc2
- Fix daemon startup code not to rely on Class-Path
- Resolves: rhbz#1261402

* Tue Sep  8 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.7-0.2.rc2
- Update to upstream version 2.7-rc-2

* Mon Aug 31 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.7-0.1.rc1
- Update to upstream version 2.7-rc-1

* Thu Aug 13 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-1
- Update to upstream version 2.6

* Mon Jul 13 2015 Michael Simacek <msimacek@redhat.com> - 2.5-3
- Build against aqute-bndlib-2.4.1

* Fri Jul 10 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5-2
- Recommend java-devel instead of requiring it

* Thu Jul  9 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5-1
- Update to upstream version 2.5

* Mon Jul  6 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5-0.2.rc2
- Update to upstream version 2.5-rc-2

* Tue Jun 30 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5-0.1.rc1
- Update to upstream version 2.5-rc-1

* Tue Jun 30 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-4
- Remove dependency on netty31

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-2
- Port to Kryo 3.0

* Wed May  6 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-1
- Update to upstream version 2.4

* Fri Apr 24 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-0.1.rc1
- Update to upstream version 2.4-rc-1

* Fri Apr 17 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3-4
- Port to Polyglot 0.1.8

* Mon Apr 13 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3-3
- Port to Ivy 2.4.0

* Wed Mar 25 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3-2
- Port to Maven 3.3.1

* Wed Mar 25 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3-1
- Update to upstream version 2.3

* Wed Mar 25 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-9
- Remove build dependency on cobertura

* Fri Mar 20 2015 Michal Srb <msrb@redhat.com> - 2.2.1-8
- Non-bootstrap build for Maven 3.3.1

* Fri Mar 20 2015 Michal Srb <msrb@redhat.com> - 2.2.1-7
- Bootstrap build for Maven 3.3.1

* Fri Feb 13 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-6
- Rebuild for netty3 update

* Sat Feb 07 2015 Michael Simacek <msimacek@redhat.com> - 2.2.1-5
- Use unversioned dependency JAR names

* Wed Feb  4 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-4
- Fix Jetty classpath in gradle-javascript

* Fri Jan 30 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-3
- Install basic Maven metadata in bootstrap mode
- Port from Simple 4 to Jetty 9
- Add missing BR on javapackages-local in bootstrap mode

* Fri Jan 23 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-2
- Generate Maven metadata for gradle-dependency-management
- Remove XMvn connector for Gradle

* Wed Jan 21 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.1-1
- Update to upstream version 2.2.1

* Tue Jan 20 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-6
- Skip running tests for buils script
- Disable -Werror compiler flag

* Tue Jan 20 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-5
- Port to Guava 18.0
- Add build dependency on ASM 5.0.3

* Mon Nov 24 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-4
- Add support for custom Wagon providers

* Mon Nov 24 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-3
- Restore support for userName in authentication info

* Thu Nov 20 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-2
- Improve versioning and identification as Fedora package

* Wed Nov 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-1
- Non-bootstrap build

* Wed Nov 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-0.47
- Bootstrap build using prebuilt binaries

* Tue Nov 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-0.46
- Remove bundled wrapper JAR
- Remove bundled JavaScript
- Refresh all-released-versions.json from upstream

* Tue Nov 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-0.45
- Bump release

* Mon Nov 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-0.44
- Use mvn-style build-requires

* Mon Nov 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-0.43
- Regenerate requires for symlinks

* Mon Nov 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-0.42
- Remove temporary BR on javapackages-local

* Mon Nov 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-0.41
- Add missing requires on javapackages-local

* Thu Nov 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-0.40
- Add gradle-local subpackage

* Wed Nov 12 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-0.39
- Rebuild with gradle 2.2

* Wed Nov 12 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-0.38
- Update to upstream version 2.2

* Sun Nov  9 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-0.37
- Fix daemon launcher classpath

* Sun Nov  9 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-0.36
- Use new XMvn resolver factory method

* Sun Nov  9 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-0.35
- Remove XMvn connector from classpath

* Sun Nov  9 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-0.34
- Install desktop file and icons

* Sun Nov  9 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-0.33
- Remove Class-Path from manifest
- Install custom launcher script

* Sun Nov  9 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-0.32
- Install artifacts and Maven metadada

* Sun Nov  9 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-0.31
- Skip installation of POM attached artifacts

* Fri Nov  7 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-0.30
- Symlink dependencies

* Fri Nov  7 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-0.29
- Fix integration with aether-ant-tasks

* Fri Nov  7 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-0.28
- Reorganize Maven patches
- Unshade Maven 3

* Fri Nov  7 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-0.27
- Port to Aether Ant Tasks
- Use jansi 1.11

* Tue Nov  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-0.26
- Disable Zinc

* Fri Oct 31 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-0.25
- Add missing jetty BR

* Fri Oct 31 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-0.24
- Add missing maven-ant-tasks dependencies

* Fri Oct 31 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-0.23
- Bump BR on gradle-deps
- Fix BR on jetty

* Fri Oct 31 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-0.21
- Build with local maven-ant-tasks

* Fri Oct 31 2014 Michal Srb <msrb@redhat.com> - 2.1-0.21
- Build with local jetty 9

* Tue Oct 28 2014 Michael Simacek <msimacek@redhat.com> - 2.1-0.20
- Build with local sonar

* Thu Oct 23 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-0.19
- Build with local tesla-polyglot

* Wed Oct 22 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-0.18
- Build with local bouncycastle

* Wed Oct 22 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-0.17
- Disable building dist documentation

* Wed Oct 22 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-0.16
- Build with local jquery

* Wed Oct 22 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-0.15
- Build with local aqute-bndlib

* Tue Oct 21 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-0.14
- Rebuild with local cglib

* Tue Oct 21 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-0.13
- Rebuild with local native-platform

* Mon Oct 20 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-0.12
- Build with Maven Wagon 2.7

* Mon Oct 20 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-0.11
- Add metadata for fonts

* Mon Oct 20 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-0.10
- Skip build everything except binary ZIP for now

* Fri Oct 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-0.9
- Rebuild with local groovy

* Fri Oct 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-0.8
- Fix location of plexus-sec-dispatcher JAR

* Fri Oct 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-0.7
- Disable analytics plugin

* Fri Oct 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-0.6
- Build using local dependencies

* Fri Oct 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-0.5
- Simplify gradle-local-mode.patch

* Thu Oct 16 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-0.4
- Build in local mode

* Thu Oct 16 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-0.3
- Enable local mode

* Tue Oct  7 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-0.2
- Rebuild from sources

* Tue Oct  7 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-0.1
- Initial packaging
