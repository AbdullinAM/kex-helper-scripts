import os

BENCHMARK_CLASSES = list(map(lambda x: x.split("="), """FASTJSON=com.alibaba.fastjson.serializer.BooleanCodec
FASTJSON=com.alibaba.fastjson.parser.deserializer.JavaObjectDeserializer
FASTJSON=com.alibaba.fastjson.util.IOUtils
FASTJSON=com.alibaba.fastjson.serializer.ClobSeriliazer
FASTJSON=com.alibaba.fastjson.parser.deserializer.DefaultFieldDeserializer
FASTJSON=com.alibaba.fastjson.parser.deserializer.ResolveFieldDeserializer
FASTJSON=com.alibaba.fastjson.parser.deserializer.MapDeserializer
FASTJSON=com.alibaba.fastjson.serializer.ASMSerializerFactory
FASTJSON=com.alibaba.fastjson.support.hsf.HSFJSONUtils
FASTJSON=com.alibaba.fastjson.serializer.StringCodec
FASTJSON=com.alibaba.fastjson.serializer.ArraySerializer
FASTJSON=com.alibaba.fastjson.parser.DefaultJSONParser
FASTJSON=com.alibaba.fastjson.asm.Type
FASTJSON=com.alibaba.fastjson.serializer.JSONSerializer
FASTJSON=com.alibaba.fastjson.serializer.AwtCodec
FASTJSON=com.alibaba.fastjson.parser.ParserConfig
FASTJSON=com.alibaba.fastjson.serializer.CharArrayCodec
FASTJSON=com.alibaba.fastjson.asm.ByteVector
FASTJSON=com.alibaba.fastjson.support.spring.FastJsonHttpMessageConverter
FASTJSON=com.alibaba.fastjson.JSONReader
SPOON=spoon.support.reflect.cu.position.SourcePositionImpl
SPOON=spoon.reflect.factory.TypeFactory
SPOON=spoon.support.reflect.code.CtForImpl
SPOON=spoon.reflect.visitor.filter.LineFilter
SPOON=spoon.reflect.visitor.PrintingContext
SPOON=spoon.support.reflect.code.CtAssignmentImpl
SPOON=spoon.reflect.visitor.filter.CompositeFilter
SPOON=spoon.support.compiler.jdt.JDTBatchCompiler
SPOON=spoon.support.compiler.jdt.JDTSnippetCompiler
SPOON=spoon.support.DefaultCoreFactory
SPOON=spoon.reflect.visitor.ModelConsistencyChecker
SPOON=spoon.pattern.internal.node.MapEntryNode
SPOON=spoon.reflect.visitor.AstParentConsistencyChecker
SPOON=spoon.support.reflect.CtExtendedModifier
SPOON=spoon.support.reflect.code.CtStatementListImpl
GUAVA=com.google.common.base.Throwables
GUAVA=com.google.common.base.internal.Finalizer
GUAVA=com.google.common.primitives.Shorts
GUAVA=com.google.common.collect.SparseImmutableTable
GUAVA=com.google.common.collect.Queues
GUAVA=com.google.common.base.CaseFormat
GUAVA=com.google.common.math.IntMath
GUAVA=com.google.common.util.concurrent.AtomicDoubleArray
GUAVA=com.google.common.util.concurrent.SimpleTimeLimiter
GUAVA=com.google.common.collect.ReverseOrdering
GUAVA=com.google.common.collect.TopKSelector
GUAVA=com.google.common.primitives.Booleans
GUAVA=com.google.common.io.FileBackedOutputStream
GUAVA=com.google.common.collect.TreeRangeMap
GUAVA=com.google.common.math.PairedStatsAccumulator
SEATA=io.seata.core.protocol.MessageFuture
SEATA=io.seata.core.rpc.RpcContext
SEATA=io.seata.core.protocol.MergedWarpMessage
SEATA=io.seata.core.rpc.netty.RpcServerHandler
SEATA=io.seata.core.rpc.netty.ShutdownHook
SEATA=io.seata.core.protocol.transaction.BranchRegisterRequest
SEATA=io.seata.core.rpc.netty.RpcServer
SEATA=io.seata.core.store.StoreMode
SEATA=io.seata.core.protocol.RegisterRMRequest
SEATA=io.seata.core.rpc.netty.RmRpcClient
SEATA=io.seata.core.protocol.transaction.BranchReportRequest
SEATA=io.seata.core.rpc.netty.NettyPoolableFactory
SEATA=io.seata.core.rpc.netty.TmRpcClient
SEATA=io.seata.core.rpc.DefaultServerMessageListenerImpl
SEATA=io.seata.core.protocol.transaction.GlobalBeginResponse""".split("\n")))


def prepare_classpath(base_path: str, classpath: str) -> str:
    return ":".join(map(lambda x: os.path.join(base_path, x.strip()), classpath.split("\n")))


def fastjson_classpath(base_path: str) -> str:
    return prepare_classpath(
        base_path,
        """infrastructure/benchmarks_10th/projects/fastjson/target/fastjson-1.2.50-SNAPSHOT.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/accessors-smart-1.1.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/annotations-13.0.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/antlr-2.7.7.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/aopalliance-1.0.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/aopalliance-repackaged-2.5.0-b05.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/asm-4.0.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/asm-analysis-4.0.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/asm-commons-4.0.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/asm-debug-all-5.0.4.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/asm-tree-4.0.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/asm-util-4.0.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/cglib-nodep-2.2.2.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/classmate-1.3.1.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/clojure-1.5.1.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/commons-beanutils-1.8.0.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/commons-collections-3.2.1.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/commons-collections4-4.1.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/commons-io-1.4.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/commons-lang-2.5.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/commons-lang3-3.4.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/commons-logging-1.1.1.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/commons-math3-3.2.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/cxf-core-3.1.2.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/cxf-rt-frontend-jaxrs-3.1.2.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/cxf-rt-rs-client-3.1.2.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/cxf-rt-transports-http-3.1.2.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/deeptestutils-1.1.0.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/dom4j-1.6.1.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/ezmorph-1.0.6.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/groovy-2.1.5.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/gson-2.6.2.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/guava-18.0.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/hamcrest-core-1.3.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/hibernate-commons-annotations-5.0.1.Final.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/hibernate-core-5.2.10.Final.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/hibernate-jpa-2.1-api-1.0.0.Final.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/hk2-api-2.5.0-b05.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/hk2-locator-2.5.0-b05.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/hk2-utils-2.5.0-b05.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jackson-annotations-2.9.0.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jackson-core-2.9.0.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jackson-core-asl-1.9.13.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jackson-databind-2.9.0.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jackson-jaxrs-base-2.8.7.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jackson-jaxrs-json-provider-2.8.7.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jackson-mapper-asl-1.9.13.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jackson-module-afterburner-2.9.0.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jackson-module-jaxb-annotations-2.8.7.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jackson-module-kotlin-2.9.0.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jandex-2.0.3.Final.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/javaslang-2.0.6.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/javaslang-match-2.0.6.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/javassist-3.18.0-GA.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/javax.annotation-api-1.2.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/javax.inject-2.5.0-b05.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/javax.servlet-3.0.0.v201112011016.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/javax.servlet-api-3.1.0.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/javax.ws.rs-api-2.0.1.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jboss-logging-3.3.0.Final.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jboss-transaction-api_1.2_spec-1.0.1.Final.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jcl-over-slf4j-1.7.25.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jersey-client-2.23.2.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jersey-common-2.23.2.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jersey-container-jdk-http-2.23.2.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jersey-container-servlet-2.23.2.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jersey-container-servlet-core-2.23.2.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jersey-entity-filtering-2.23.2.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jersey-guava-2.23.2.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jersey-media-jaxb-2.23.2.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jersey-media-json-jackson-2.23.2.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jersey-server-2.23.2.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jersey-test-framework-core-2.23.2.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jersey-test-framework-provider-jdk-http-2.23.2.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jetty-continuation-8.1.8.v20121106.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jetty-http-8.1.8.v20121106.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jetty-io-8.1.8.v20121106.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jetty-security-8.1.8.v20121106.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jetty-server-8.1.8.v20121106.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jetty-servlet-8.1.8.v20121106.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jetty-util-8.1.8.v20121106.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jetty-webapp-8.1.8.v20121106.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jetty-xml-8.1.8.v20121106.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jmh-core-1.21.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jmh-generator-annprocess-1.21.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jopt-simple-4.6.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/jsoniter-0.9.8.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/json-lib-2.4-jdk15.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/json-path-2.3.0.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/json-simple-1.1.1.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/json-smart-2.2.1.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/kotlin-reflect-1.1.3-2.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/kotlin-stdlib-1.1.3-2.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/lombok-1.14.4.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/mockito-all-1.10.19.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/mockito-core-1.10.19.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/objenesis-2.5.1.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/okhttp-3.6.0.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/okio-1.11.0.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/osgi-resource-locator-1.0.1.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/powermock-api-mockito-1.6.6.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/powermock-api-mockito-common-1.6.6.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/powermock-api-support-1.6.6.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/powermock-core-1.6.6.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/powermock-module-junit4-1.6.6.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/powermock-module-junit4-common-1.6.6.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/powermock-reflect-1.6.6.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/retrofit-2.1.0.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/slf4j-api-1.7.25.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/spring-aop-4.3.7.RELEASE.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/spring-beans-4.3.7.RELEASE.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/spring-context-4.3.7.RELEASE.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/spring-context-support-4.3.10.RELEASE.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/spring-core-4.3.7.RELEASE.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/spring-data-commons-1.13.6.RELEASE.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/spring-data-commons-core-1.4.1.RELEASE.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/spring-data-keyvalue-1.2.6.RELEASE.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/spring-data-redis-1.8.6.RELEASE.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/spring-expression-4.3.7.RELEASE.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/springfox-core-2.6.1.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/springfox-spi-2.6.1.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/springfox-spring-web-2.6.1.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/spring-messaging-4.3.7.RELEASE.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/spring-oxm-4.3.10.RELEASE.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/spring-plugin-core-1.2.0.RELEASE.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/spring-plugin-metadata-1.2.0.RELEASE.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/spring-security-config-3.2.10.RELEASE.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/spring-security-core-4.2.3.RELEASE.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/spring-security-oauth2-2.3.3.RELEASE.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/spring-security-web-4.2.3.RELEASE.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/spring-test-4.3.7.RELEASE.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/spring-tx-4.3.10.RELEASE.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/spring-web-4.3.7.RELEASE.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/spring-webmvc-4.3.7.RELEASE.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/spring-websocket-4.3.7.RELEASE.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/stax2-api-3.1.4.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/validation-api-1.1.0.Final.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/woodstox-core-asl-4.4.1.jar
        infrastructure/benchmarks_10th/projects/fastjson/target/dependency/xmlschema-core-2.2.1.jar"""
    )


def spoon_classpath(base_path: str) -> str:
    return prepare_classpath(
        base_path,
        """infrastructure/benchmarks_10th/projects/spoon/target/spoon-core-7.0.0.jar
        infrastructure/benchmarks_10th/projects/spoon/target/dependency/bridge-method-annotation-1.13.jar
        infrastructure/benchmarks_10th/projects/spoon/target/dependency/commons-io-2.5.jar
        infrastructure/benchmarks_10th/projects/spoon/target/dependency/commons-lang3-3.5.jar
        infrastructure/benchmarks_10th/projects/spoon/target/dependency/guava-18.0.jar
        infrastructure/benchmarks_10th/projects/spoon/target/dependency/hamcrest-core-1.3.jar
        infrastructure/benchmarks_10th/projects/spoon/target/dependency/jackson-annotations-2.9.0.jar
        infrastructure/benchmarks_10th/projects/spoon/target/dependency/jackson-core-2.9.2.jar
        infrastructure/benchmarks_10th/projects/spoon/target/dependency/jackson-databind-2.9.2.jar
        infrastructure/benchmarks_10th/projects/spoon/target/dependency/jsap-2.1.jar
        infrastructure/benchmarks_10th/projects/spoon/target/dependency/log4j-1.2.17.jar
        infrastructure/benchmarks_10th/projects/spoon/target/dependency/maven-model-3.3.9.jar
        infrastructure/benchmarks_10th/projects/spoon/target/dependency/mockito-all-2.0.2-beta.jar
        infrastructure/benchmarks_10th/projects/spoon/target/dependency/org.eclipse.core.commands-3.10.100.jar
        infrastructure/benchmarks_10th/projects/spoon/target/dependency/org.eclipse.core.contenttype-3.8.100.jar
        infrastructure/benchmarks_10th/projects/spoon/target/dependency/org.eclipse.core.expressions-3.8.100.jar
        infrastructure/benchmarks_10th/projects/spoon/target/dependency/org.eclipse.core.filesystem-1.9.200.jar
        infrastructure/benchmarks_10th/projects/spoon/target/dependency/org.eclipse.core.jobs-3.12.0.jar
        infrastructure/benchmarks_10th/projects/spoon/target/dependency/org.eclipse.core.resources-3.16.0.jar
        infrastructure/benchmarks_10th/projects/spoon/target/dependency/org.eclipse.core.runtime-3.24.0.jar
        infrastructure/benchmarks_10th/projects/spoon/target/dependency/org.eclipse.equinox.app-1.6.100.jar
        infrastructure/benchmarks_10th/projects/spoon/target/dependency/org.eclipse.equinox.common-3.15.100.jar
        infrastructure/benchmarks_10th/projects/spoon/target/dependency/org.eclipse.equinox.preferences-3.9.100.jar
        infrastructure/benchmarks_10th/projects/spoon/target/dependency/org.eclipse.equinox.registry-3.11.100.jar
        infrastructure/benchmarks_10th/projects/spoon/target/dependency/org.eclipse.jdt.core-3.13.102.jar
        infrastructure/benchmarks_10th/projects/spoon/target/dependency/org.eclipse.osgi-3.17.100.jar
        infrastructure/benchmarks_10th/projects/spoon/target/dependency/org.eclipse.text-3.12.0.jar
        infrastructure/benchmarks_10th/projects/spoon/target/dependency/plexus-utils-3.0.22.jar
        infrastructure/benchmarks_10th/projects/spoon/target/dependency/querydsl-core-3.6.9.jar
        infrastructure/benchmarks_10th/projects/spoon/target/dependency/system-rules-1.9.0.jar"""
    )


def guava_classpath(base_path: str) -> str:
    return prepare_classpath(
        base_path,
        """infrastructure/benchmarks_10th/projects/guava/guava/target/guava-26.0-jre.jar
        infrastructure/benchmarks_10th/projects/guava/guava/target/dependency/animal-sniffer-annotations-1.14.jar
        infrastructure/benchmarks_10th/projects/guava/guava/target/dependency/checker-qual-2.5.2.jar
        infrastructure/benchmarks_10th/projects/guava/guava/target/dependency/error_prone_annotations-2.1.3.jar
        infrastructure/benchmarks_10th/projects/guava/guava/target/dependency/j2objc-annotations-1.1.jar
        infrastructure/benchmarks_10th/projects/guava/guava/target/dependency/jsr305-3.0.2.jar"""
    )


def seata_classpath(base_path: str) -> str:
    return prepare_classpath(
        base_path,
        """infrastructure/benchmarks_10th/projects/seata/core/target/seata-core-0.5.0.jar
        infrastructure/benchmarks_10th/projects/seata/core/target/dependency/assertj-core-2.6.0.jar
        infrastructure/benchmarks_10th/projects/seata/core/target/dependency/byte-buddy-1.9.3.jar
        infrastructure/benchmarks_10th/projects/seata/core/target/dependency/byte-buddy-agent-1.9.3.jar
        infrastructure/benchmarks_10th/projects/seata/core/target/dependency/commons-lang-2.6.jar
        infrastructure/benchmarks_10th/projects/seata/core/target/dependency/commons-pool-1.6.jar
        infrastructure/benchmarks_10th/projects/seata/core/target/dependency/commons-pool2-2.4.2.jar
        infrastructure/benchmarks_10th/projects/seata/core/target/dependency/config-1.2.1.jar
        infrastructure/benchmarks_10th/projects/seata/core/target/dependency/fastjson-1.2.48.jar
        infrastructure/benchmarks_10th/projects/seata/core/target/dependency/hamcrest-core-1.3.jar
        infrastructure/benchmarks_10th/projects/seata/core/target/dependency/mockito-core-2.23.4.jar
        infrastructure/benchmarks_10th/projects/seata/core/target/dependency/netty-all-4.1.24.Final.jar
        infrastructure/benchmarks_10th/projects/seata/core/target/dependency/objenesis-2.6.jar
        infrastructure/benchmarks_10th/projects/seata/core/target/dependency/seata-common-0.5.0.jar
        infrastructure/benchmarks_10th/projects/seata/core/target/dependency/seata-config-core-0.5.0.jar
        infrastructure/benchmarks_10th/projects/seata/core/target/dependency/seata-discovery-core-0.5.0.jar"""
    )
