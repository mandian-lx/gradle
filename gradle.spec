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
Version:        2.2.1
Release:        0.3 #6%{?dist}
Summary:        Build automation tool
Group:          Development/Java
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

# Sources 99xx are used only for bootstrapping.
# Main script used to build gradle with plain groovyc
Source9900:     gradle-bootstrap.sh
# Script used to generate Source991x from upstream binaries
Source9901:     gradle-bootstrap-gererate-resources.py
# Files containing information about Gradle module structure
Source9910:     gradle-bootstrap-module-list
Source9911:     gradle-bootstrap-module-dependencies
# List of default imorts, extracted from gradle-docs.jar
Source9920:     gradle-bootstrap-default-imports.txt
# List of Gradle plugins, extracted from gradle-core.jar
Source9921:     gradle-bootstrap-plugin.properties

Patch0:         0001-Gradle-local-mode.patch
Patch1:         0002-Use-Maven-Wagon-2.8.patch
Patch2:         0003-Use-bndlib-1.50.0.patch
Patch3:         0004-Port-to-Jetty-9.patch
Patch4:         0005-Use-jansi-1.11.patch
Patch5:         0006-Port-to-Maven-3.1.1-and-Aether-Ant-Tasks.patch
Patch6:         0007-Remove-Class-Path-from-manifest.patch
Patch7:         0008-Implement-XMvn-repository-factory-method.patch
# Forwarded upstream: https://github.com/gradle/gradle/pull/354
Patch8:         0009-Use-hostname-command-as-fallback-way-of-getting-buil.patch
# TODO: forward upstream
Patch9:         0010-Compatibility-with-Guava-18.0.patch
Patch10:        0011-Add-build-dependency-on-ASM-5.0.3.patch
Patch11:        0012-Port-from-Simple-4-to-Jetty-9.patch
Patch12:        0013-Use-unversioned-dependency-JAR-names.patch
Patch13:        0014-Don-t-declare-dependency-on-jarjars.patch

# from gradle-2.13-7.fc26
Patch100:       0009-Port-to-Polyglot-0.1.8.patch
Patch101:       0011-Port-to-Kryo-3.0.patch

# Dependencies on build system used.  In bootstrap mode we use plain
# groovyc to compile Gradle, otherwise Gradle is built with itself.
%if %{with bootstrap}
BuildRequires:  groovy #>= 2.3
BuildRequires:  javapackages-local
%else
BuildRequires:  gradle-local >= 2.2
%endif

# Generic build dependencies
BuildRequires:  desktop-file-utils
BuildRequires:  hostname

# Artifacts required for Gradle build
BuildRequires:  mvn(antlr:antlr)
BuildRequires:  mvn(asm:asm)
BuildRequires:  mvn(asm:asm-tree)
BuildRequires:  mvn(biz.aQute:bndlib)
BuildRequires:  mvn(biz.source_code:base64coder)
BuildRequires:  mvn(bsf:bsf)
BuildRequires:  mvn(cglib:cglib)
BuildRequires:  mvn(cglib:cglib-nodep)
BuildRequires:  mvn(ch.qos.logback:logback-classic)
BuildRequires:  mvn(ch.qos.logback:logback-core)
BuildRequires:  mvn(com.beust:jcommander)
BuildRequires:  mvn(com.esotericsoftware.kryo:kryo)
BuildRequires:  mvn(com.esotericsoftware.minlog:minlog)
BuildRequires:  mvn(com.esotericsoftware.reflectasm:reflectasm)
BuildRequires:  mvn(com.google.code.findbugs:findbugs)
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(com.google.code.gson:gson)
BuildRequires:  mvn(com.googlecode.jarjar:jarjar)
BuildRequires:  mvn(com.googlecode.jatl:jatl)
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(com.google.guava:guava-jdk5)
BuildRequires:  mvn(com.jcraft:jsch)
BuildRequires:  mvn(com.jcraft:jzlib)
BuildRequires:  mvn(commons-beanutils:commons-beanutils-core)
BuildRequires:  mvn(commons-cli:commons-cli)
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(commons-collections:commons-collections)
BuildRequires:  mvn(commons-configuration:commons-configuration)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(commons-lang:commons-lang)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(com.puppycrawl.tools:checkstyle)
BuildRequires:  mvn(com.sun:tools)
BuildRequires:  mvn(com.thoughtworks.qdox:qdox)
BuildRequires:  mvn(com.thoughtworks.xstream:xstream)
BuildRequires:  mvn(com.uwyn:jhighlight)
BuildRequires:  mvn(dom4j:dom4j)
BuildRequires:  mvn(isorelax:isorelax)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(javax.mail:mail)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(javax.xml.stream:stax-api)
BuildRequires:  mvn(jaxen:jaxen)
BuildRequires:  mvn(jdom:jdom)
BuildRequires:  mvn(jline:jline)
BuildRequires:  mvn(joda-time:joda-time)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(log4j:log4j)
BuildRequires:  mvn(net.java.dev.jna:jna)
BuildRequires:  mvn(net.java.dev.msv:msv-core)
BuildRequires:  mvn(net.java.dev.msv:xsdlib)
BuildRequires:  mvn(net.jcip:jcip-annotations)
BuildRequires:  mvn(net.rubygrapefruit:native-platform)
BuildRequires:  mvn(net.sf.kxml:kxml2)
BuildRequires:  mvn(net.sf.kxml:kxml2-min)
BuildRequires:  mvn(net.sourceforge.cobertura:cobertura)
BuildRequires:  mvn(net.sourceforge.nekohtml:nekohtml)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ant:ant-antlr)
BuildRequires:  mvn(org.apache.ant:ant-junit)
BuildRequires:  mvn(org.apache.ant:ant-launcher)
BuildRequires:  mvn(org.apache.ant:ant-parent:pom:)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.felix:org.osgi.core)
BuildRequires:  mvn(org.apache.geronimo.specs:geronimo-annotation_1.0_spec)
BuildRequires:  mvn(org.apache.geronimo.specs:geronimo-jms_1.1_spec)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.httpcomponents:httpcore)
BuildRequires:  mvn(org.apache.ivy:ivy)
BuildRequires:  mvn(org.apache.maven:maven-aether-provider)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-model-builder)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-repository-metadata)
BuildRequires:  mvn(org.apache.maven:maven-settings)
BuildRequires:  mvn(org.apache.maven:maven-settings-builder)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-http)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-http-shared)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires:  mvn(org.apache.tomcat:tomcat-servlet-api)
BuildRequires:  mvn(org.apache.xbean:xbean-reflect)
BuildRequires:  mvn(org.beanshell:bsh)
BuildRequires:  mvn(org.bouncycastle:bcpg-jdk15)
BuildRequires:  mvn(org.bouncycastle:bcprov-jdk15)
BuildRequires:  mvn(org.codehaus.gpars:gpars)
BuildRequires:  mvn(org.codehaus.groovy:groovy)
BuildRequires:  mvn(org.codehaus.groovy:groovy-all)
BuildRequires:  mvn(org.codehaus.jcsp:jcsp)
BuildRequires:  mvn(org.codehaus.jettison:jettison)
BuildRequires:  mvn(org.codehaus.jsr166-mirror:extra166y)
BuildRequires:  mvn(org.codehaus.plexus:plexus-classworlds)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.codehaus.sonar:sonar-batch)
BuildRequires:  mvn(org.codehaus.sonar:sonar-batch-bootstrapper)
BuildRequires:  mvn(org.codehaus.sonar:sonar-plugin-api)
BuildRequires:  mvn(org.codehaus.woodstox:stax2-api)
BuildRequires:  mvn(org.codehaus.woodstox:woodstox-core-asl)
BuildRequires:  mvn(org.codenarc:CodeNarc)
BuildRequires:  mvn(org.eclipse.aether:aether-ant-tasks)
BuildRequires:  mvn(org.eclipse.aether:aether-api)
BuildRequires:  mvn(org.eclipse.aether:aether-connector-basic)
BuildRequires:  mvn(org.eclipse.aether:aether-impl)
BuildRequires:  mvn(org.eclipse.aether:aether-spi)
BuildRequires:  mvn(org.eclipse.aether:aether-transport-classpath)
BuildRequires:  mvn(org.eclipse.aether:aether-transport-file)
BuildRequires:  mvn(org.eclipse.aether:aether-transport-http)
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
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.fusesource.hawtjni:hawtjni-runtime)
BuildRequires:  mvn(org.fusesource.jansi:jansi)
BuildRequires:  mvn(org.fusesource.jansi:jansi-native)
BuildRequires:  mvn(org.gmetrics:GMetrics)
BuildRequires:  mvn(org.gradle.jarjar:jarjar)
BuildRequires:  mvn(org.hamcrest:hamcrest-core)
BuildRequires:  mvn(org.hamcrest:hamcrest-parent:pom:)
BuildRequires:  mvn(org.jboss.netty:netty:3)
BuildRequires:  mvn(org.jdom:jdom)
BuildRequires:  mvn(org.jdom:jdom2)
BuildRequires:  mvn(org.joda:joda-convert)
BuildRequires:  mvn(org.jsoup:jsoup)
BuildRequires:  mvn(org.mozilla:rhino)
BuildRequires:  mvn(org.multiverse:multiverse-core)
BuildRequires:  mvn(org.objenesis:objenesis)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-all)
BuildRequires:  mvn(org.ow2.asm:asm-analysis)
BuildRequires:  mvn(org.ow2.asm:asm-tree)
BuildRequires:  mvn(org.ow2.asm:asm-util)
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
BuildRequires:  mvn(org.spockframework:spock-core)
BuildRequires:  mvn(org.testng:testng)
BuildRequires:  mvn(org.yaml:snakeyaml)
BuildRequires:  mvn(oro:oro)
BuildRequires:  mvn(relaxngDatatype:relaxngDatatype)
BuildRequires:  mvn(stax:stax)
BuildRequires:  mvn(stax:stax-api)
BuildRequires:  mvn(xalan:serializer)
BuildRequires:  mvn(xalan:xalan)
BuildRequires:  mvn(xerces:xercesImpl)
BuildRequires:  mvn(xml-apis:xml-apis)
BuildRequires:  mvn(xml-resolver:xml-resolver)
BuildRequires:  mvn(xom:xom)

# Artifacts required for Gradle build which don't have Maven metadata
# and thus no mvn provides.
BuildRequires:  fonts-ttf-lato
BuildRequires:  fonts-ttf-liberation
#BuildRequires:  js-jquery

# Generic runtime dependencies.
Requires:       javapackages-tools
Requires:       java-devel
Requires:       bash
Requires:       hicolor-icon-theme

# Providers of symlinks in Gradle lib/ directory. Generated with:
# for l in $(find /usr/share/gradle -type l); do rpm -qf --qf 'Requires:       %{name}\n' $(readlink $l); done | sort -u | grep -v gradle
Requires:       aether-ant-tasks
Requires:       aether-api
Requires:       aether-connector-basic
Requires:       aether-impl
Requires:       aether-spi
Requires:       aether-transport-classpath
Requires:       aether-transport-file
Requires:       aether-transport-http
Requires:       aether-transport-wagon
Requires:       aether-util
Requires:       ant
Requires:       ant-antlr
Requires:       ant-junit
Requires:       antlr-tool
Requires:       apache-commons-cli
Requires:       apache-commons-codec
Requires:       apache-commons-collections
Requires:       apache-commons-io
Requires:       apache-commons-lang
Requires:       apache-commons-logging
Requires:       apache-ivy
Requires:       aqute-bndlib
Requires:       atinject
Requires:       base64coder
Requires:       bea-stax
Requires:       bea-stax-api
Requires:       beust-jcommander
Requires:       bouncycastle
Requires:       bouncycastle-pg
Requires:       bsf
Requires:       bsh
Requires:       cglib
Requires:       dom4j
Requires:       ecj
Requires:       extra166y
Requires:       felix-osgi-core
Requires:       geronimo-annotation
Requires:       geronimo-jms
Requires:       glassfish-servlet-api
Requires:       google-gson
Requires:       gpars
Requires:       groovy-lib
Requires:       guava
Requires:       hamcrest
Requires:       hawtjni
Requires:       httpcomponents-client
Requires:       httpcomponents-core
Requires:       isorelax
Requires:       jansi
Requires:       jansi-native
Requires:       jarjar
Requires:       jatl
Requires:       javamail
Requires:       jaxen
Requires:       jcifs
Requires:       jcip-annotations
Requires:       jcl-over-slf4j
Requires:       jcsp
Requires:       jdom
Requires:       jdom2
Requires:       jettison
Requires:       jetty-annotations
Requires:       jetty-jsp
Requires:       jetty-plus
Requires:       jetty-security
Requires:       jetty-server
Requires:       jetty-servlet
Requires:       jetty-util
Requires:       jetty-webapp
Requires:       jetty-xml
Requires:       jline
Requires:       jna
Requires:       joda-convert
Requires:       joda-time
Requires:       jsch
Requires:       jul-to-slf4j
Requires:       junit
Requires:       jzlib
Requires:       kryo
Requires:       kxml
Requires:       log4j12
Requires:       log4j-over-slf4j
Requires:       logback
Requires:       maven
Requires:       maven-wagon-http
Requires:       maven-wagon-http-shared
Requires:       maven-wagon-provider-api
Requires:       minlog
Requires:       msv-msv
Requires:       msv-xsdlib
Requires:       multiverse
Requires:       native-platform
Requires:       nekohtml
Requires:       netty3
Requires:       objectweb-asm
Requires:       objenesis
Requires:       plexus-cipher
Requires:       plexus-classworlds
Requires:       plexus-containers-component-annotations
Requires:       plexus-containers-container-default
Requires:       plexus-interpolation
Requires:       plexus-sec-dispatcher
Requires:       plexus-utils
Requires:       qdox
Requires:       reflectasm
Requires:       relaxngDatatype
Requires:       rhino
Requires:       sisu-plexus
Requires:       slf4j
Requires:       snakeyaml
Requires:       sonar-batch-bootstrapper
Requires:       stax2-api
Requires:       tesla-polyglot-common
Requires:       tesla-polyglot-groovy
Requires:       testng
Requires:       woodstox-core
Requires:       xalan-j2
Requires:       xbean
Requires:       xerces-j2
Requires:       xml-commons-apis
Requires:       xml-commons-resolver
Requires:       xom
Requires:       xstream

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
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

%patch100 -p1 -b.orig
%patch101 -p1 -b.orig

# Remove bundled wrapper JAR
rm -rf gradle/wrapper/
# Remove bundled JavaScript
#>subprojects/diagnostics/src/main/resources/org/gradle/api/tasks/diagnostics/htmldependencyreport/jquery.jstree.js

# Remove Zinc support as Zinc is not yet packaged for Fedora
rm -f $(find -name ZincScalaCompiler.java)
sed -i /zinc/d subprojects/scala/scala.gradle

# This file is normally downloaded from Internet during package build
mkdir -p build
cp %{SOURCE1} build/all-released-versions.json

# jquery and fonts don't have Maven metadata
%mvn_config resolverSettings/metadataRepositories/repository %{SOURCE2}
%mvn_config resolverSettings/metadataRepositories/repository %{SOURCE3}

# Tests for bulid script currently fail, but the bulid works.
# TODO: enble tests
rm -rf buildSrc/src/test

# Compilation with Fedora versions of some librarios produces
# warnings. Lets not treat them as errors to make the build work.
sed -i 's/"-Werror" <<//' gradle/strictCompile.gradle

# Generate Maven metadata for gradle-dependency-management
# (required by XMvn connector).
sed -i "/publishedProjects =/s/.*/& project(':dependencyManagement'),/" build.gradle


%build
%if %{with bootstrap}
mkdir -p subprojects/docs/src/main/resources && cp %{SOURCE9920} subprojects/docs/src/main/resources/default-imports.txt
cp %{SOURCE9921} subprojects/core/src/main/resources/gradle-plugins.properties
sh %{SOURCE9900} %{SOURCE9910} %{SOURCE9911}
%else
gradle -x docs:distDocs --offline -s install -Pgradle_installPath=$PWD/inst \
    -PfinalRelease -Dbuild.number="%{?fedora:Fedora }%{?rhel:Red Hat }%{version}-%{release}"
%endif

%install
install -d -m 755 %{buildroot}%{_javadir}/%{name}/

%if %{with bootstrap}
cp -r bootstrap-home %{buildroot}%{_datadir}/%{name}
# Launcher with dependencies needs to be in _javadir
for mod in launcher core base-services; do
    ln -s %{_datadir}/%{name}/lib/gradle-$mod.jar %{buildroot}%{_javadir}/%{name}/gradle-$mod.jar
done
# Dependencies of xmvn-connector-gradle need to have Maven metadata
for mod in base-services core dependency-management resources; do
    %add_maven_depmap org.gradle:gradle-$mod:%{version} ../%{name}/lib/gradle-$mod.jar
done
cp subprojects/distributions/src/toplevel/{changelog.txt,LICENSE,NOTICE} .
%else

repo=$HOME/.m2/repository

install -d -m 755 %{buildroot}%{_datadir}/%{name}/
rm -rf inst/bin/gradle.bat inst/media
ln -sf %{_bindir}/%{name} inst/bin/gradle
mv inst/{changelog.txt,LICENSE,NOTICE} .
find inst/lib -type f -not -name 'gradle*' -delete
cp -a deps/* inst/lib/
cp -a inst/* %{buildroot}%{_datadir}/%{name}/

for f in gradle-base-services gradle-base-services-groovy gradle-cli gradle-core gradle-docs \
         gradle-launcher gradle-messaging gradle-model-core gradle-model-groovy gradle-native \
         gradle-open-api gradle-resources gradle-tooling-api gradle-ui gradle-wrapper \
         plugins/gradle-announce plugins/gradle-antlr plugins/gradle-build-comparison \
         plugins/gradle-build-init plugins/gradle-code-quality plugins/gradle-cunit \
         plugins/gradle-dependency-management plugins/gradle-diagnostics plugins/gradle-ear \
         plugins/gradle-ide plugins/gradle-ide-native plugins/gradle-ivy plugins/gradle-jacoco \
         plugins/gradle-javascript plugins/gradle-jetty plugins/gradle-language-groovy \
         plugins/gradle-language-java plugins/gradle-language-jvm plugins/gradle-language-native \
         plugins/gradle-maven plugins/gradle-osgi plugins/gradle-platform-base \
         plugins/gradle-platform-jvm plugins/gradle-platform-native plugins/gradle-plugin-development \
         plugins/gradle-plugins plugins/gradle-plugin-use plugins/gradle-publish plugins/gradle-reporting \
         plugins/gradle-resources-http plugins/gradle-scala plugins/gradle-signing plugins/gradle-sonar
do
    mod=$(basename $f)
    pom=$repo/org/gradle/$mod/%{version}*/$mod-%{version}*.pom
    jar=$repo/org/gradle/$mod/%{version}*/$mod-%{version}*.jar
    if [ -f $jar ]; then
        # Gradle JAR that has Maven metadata
        %mvn_artifact $pom $jar
    else
        # Gradle JAR without Maven metadata (most of internal Gradle
        # JARs are not published in remote repositories)
        cp %{buildroot}%{_datadir}/%{name}/lib/$f-%{version}*.jar %{buildroot}%{_javadir}/%{name}/$mod.jar
    fi
    ln -sf %{_javadir}/%{name}/$mod.jar %{buildroot}%{_datadir}/%{name}/lib/$f-%{version}*.jar
done

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

%post
update-desktop-database &>/dev/null || :
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
update-desktop-database &>/dev/null || :
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files -f .mfiles
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_javadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%doc changelog.txt
%doc LICENSE NOTICE

%changelog
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
