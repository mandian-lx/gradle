#!/bin/sh
# Build Gradle with plain groovyc
#
# Usage: $0 <path-to-module-list> <path-to-module-dependencies>
#
# Author: Mikolaj Izdebski <mizdebsk@redhat.com>

set -e
test $# -eq 2

LANG=en_US.utf8

# External dependencies needed by Gradle.
external_deps="
ant/ant
ant/ant-launcher
antlr
apache-commons-collections
apache-commons-configuration
apache-commons-lang
apache-commons-lang3
apache-ivy/ivy
aqute-bnd/aQute.libg
aqute-bnd/biz.aQute.bndlib
atinject
aws-sdk-java/aws-java-sdk-core
aws-sdk-java/aws-java-sdk-kms
aws-sdk-java/aws-java-sdk-s3
bcpg
bcprov
beust-jcommander
bsh
commons-cli
commons-codec
commons-compress
commons-io
dom4j/dom4j
ecj
findbugs
geronimo-annotation
glassfish-servlet-api
google-gson/gson
google-http-java-client
google-oauth-java-client
groovy/groovy-all
guava20
jsr-305
guice/google-guice-no_aop
hawtjni/hawtjni-runtime
httpcomponents/httpclient
httpcomponents/httpcore
jackson-annotations
jackson-core
jackson-databind
jansi-native/jansi-native
jansi/jansi
jarjar/jarjar
jatl
jaxen
jcifs
jcip-annotations
jetty/apache-jsp
jetty/jetty-annotations
jetty/jetty-plus
jetty/jetty-security
jetty/jetty-server
jetty/jetty-servlet
jetty/jetty-util
jetty/jetty-webapp
jetty/jetty-xml
jgit
jline/jline
jna
joda-time
js
jsch
junit
kryo
maven-resolver/maven-resolver-api
maven-resolver/maven-resolver-connector-basic
maven-resolver/maven-resolver-impl
maven-resolver/maven-resolver-spi
maven-resolver/maven-resolver-transport-wagon
maven-resolver/maven-resolver-util
maven-shared-utils
maven-wagon/provider-api
maven/maven-artifact
maven/maven-builder-support
maven/maven-compat
maven/maven-core
maven/maven-model
maven/maven-model-builder
maven/maven-plugin-api
maven/maven-repository-metadata
maven/maven-resolver-provider
maven/maven-settings
maven/maven-settings-builder
minlog
native-platform
nekohtml
objectweb-asm/asm-all
objenesis/objenesis
org.eclipse.sisu.inject
org.eclipse.sisu.plexus
plexus-classworlds
plexus-containers/plexus-component-annotations
plexus/interpolation
plexus/plexus-cipher
plexus/plexus-sec-dispatcher
plexus/utils
reflectasm
sbt/api
sbt/classpath
sbt/control
sbt/compile
sbt/compiler-integration
sbt/incremental-compiler
sbt/interface
sbt/io
sbt/launcher-interface
sbt/logging
sbt/process
sbt/relation
scala/scala-compiler
scala/scala-library
scala/scala-reflect
slf4j/jcl-over-slf4j
slf4j/jul-to-slf4j
slf4j/log4j-over-slf4j
slf4j/slf4j-api
tesla-polyglot/polyglot-common
tesla-polyglot/polyglot-groovy
testng
xbean/xbean-reflect
xerces-j2
xml-commons-apis
zinc/zinc
"

# Generate some dummy build properties - they don't need to be 100 % correct.
cat <<EOF >subprojects/core/src/main/resources/org/gradle/build-receipt.properties
buildNumber=none
buildTimestampIso=20150101000000+0000
commitId=foo
hostname=localhost
isSnapshot=false
javaVersion=1.8.0
osName=Linux
osVersion=3.1.0
project=gradle
rcNumber=
username=mock
versionBase=2.0
versionNumber=2.0
EOF

rm -rf bootstrap-home
mkdir -p bootstrap-home/lib/plugins

echo "******************************"
echo "*** GRADLE BOOTSTRAP BUILD ***"
echo "******************************"

echo "== finding external dependencies..."
build-jar-repository -s -p bootstrap-home/lib/plugins $external_deps
for old in bootstrap-home/lib/plugins/*; do
    new=${old///*_//lib/plugins/}
    if [ $old != $new ]; then
        mv $old $new
    fi
done
classpath=$(build-classpath $external_deps)

dep_runtime=$(ls bootstrap-home/lib/plugins | xargs | sed s/\ /,/g)

rm -rf bootstrap-classes
mkdir bootstrap-classes

# Process all modules in topological order
for mod in $(cat "$1"); do
    classes_dir=bootstrap-classes/$mod
    resources_dir=subprojects/${mod/gradle-/}/src/main/resources
    mkdir -p $classes_dir $resources_dir

    # Find Java/Groovy sources
    srcdirs=""
    for lang in groovy java; do
	dir=subprojects/${mod/gradle-/}/src/main/$lang
	[[ -d $dir ]] && srcdirs="$srcdirs $dir"
    done

    # Compile sources if there are any (some modules have only
    # resources, but no compilable sources)
    if [[ -n "$srcdirs" ]]; then
	echo "== groovyc $mod..."
	groovyc -cp $classpath -j -J source=8 -J target=8 -d $classes_dir $(find $srcdirs -name *.java -o -name *.groovy)
    fi

    # Create JAR with classes, but not yet resources
    jar=$PWD/bootstrap-home/lib/$mod.jar
    (cd ./$classes_dir && jar cf $jar .)

    # Generate classpath.properties resource file
    sed -n "/^$mod=/{s//projects=/;p}" "$2" >$resources_dir/$mod-classpath.properties
    echo "runtime=$dep_runtime" >>$resources_dir/$mod-classpath.properties

    # Add resources to JAR
    (cd ./subprojects/${mod/gradle-/}/src/main/resources && jar uf $jar .)
    classpath=$classpath:$jar
done
