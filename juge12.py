import os

BENCHMARK_CLASSES = list(map(lambda x: x.split("="), """BYTEBUDDY=net.bytebuddy.agent.builder.LambdaFactory
BYTEBUDDY=net.bytebuddy.matcher.SuperTypeMatcher
BYTEBUDDY=net.bytebuddy.implementation.auxiliary.MethodCallProxy
BYTEBUDDY=net.bytebuddy.dynamic.loading.ClassReloadingStrategy
BYTEBUDDY=net.bytebuddy.dynamic.loading.ByteArrayClassLoader
BYTEBUDDY=net.bytebuddy.implementation.bytecode.member.MethodReturn
BYTEBUDDY=net.bytebuddy.implementation.bytecode.assign.primitive.PrimitiveWideningDelegate
BYTEBUDDY=net.bytebuddy.implementation.bind.ArgumentTypeResolver
BYTEBUDDY=net.bytebuddy.implementation.bytecode.StackSize
BYTEBUDDY=net.bytebuddy.matcher.SubTypeMatcher
BYTEBUDDY=net.bytebuddy.matcher.InheritedAnnotationMatcher
BYTEBUDDY=net.bytebuddy.matcher.DeclaringTypeMatcher
BYTEBUDDY=net.bytebuddy.matcher.AnnotationTargetMatcher
ERRORPRONE=com.google.errorprone.bugpatterns.InexactVarargsConditional
ERRORPRONE=com.google.errorprone.bugpatterns.Incomparable
ERRORPRONE=com.google.errorprone.bugpatterns.IdentityBinaryExpression
ERRORPRONE=com.google.errorprone.bugpatterns.inject.guice.OverridesJavaxInjectableMethod
ERRORPRONE=com.google.errorprone.bugpatterns.IntLongMath
ERRORPRONE=com.google.errorprone.bugpatterns.LongFloatConversion
ERRORPRONE=com.google.errorprone.bugpatterns.flogger.FloggerMessageFormat
ERRORPRONE=com.google.errorprone.refaster.AutoValue_LocalVarBinding
ERRORPRONE=com.google.errorprone.bugpatterns.collectionincompatibletype.AutoValue_IncompatibleArgumentType_RequiredType
ERRORPRONE=com.google.errorprone.bugpatterns.StringBuilderInitWithChar
ERRORPRONE=com.google.errorprone.bugpatterns.PrivateConstructorForUtilityClass
ERRORPRONE=com.google.errorprone.refaster.AutoValue_UOfKind
ERRORPRONE=com.google.errorprone.bugpatterns.EmptyCatch
ERRORPRONE=com.google.errorprone.bugpatterns.UnnecessarySetDefault
ERRORPRONE=com.google.errorprone.bugpatterns.JUnitAssertSameCheck
ERRORPRONE=com.google.errorprone.bugpatterns.javadoc.AlmostJavadoc
ERRORPRONE=com.google.errorprone.refaster.AutoValue_UTry
ERRORPRONE=com.google.errorprone.bugpatterns.UnnecessaryAnonymousClass
ERRORPRONE=com.google.errorprone.bugpatterns.flogger.FloggerWithCause
ERRORPRONE=com.google.errorprone.bugpatterns.RedundantCondition
ERRORPRONE=com.google.errorprone.refaster.AutoValue_ULambda
ERRORPRONE=com.google.errorprone.bugpatterns.MutableConstantField
ERRORPRONE=com.google.errorprone.bugpatterns.BigDecimalLiteralDouble
ERRORPRONE=com.google.errorprone.bugpatterns.MissingSuperCall
ERRORPRONE=com.google.errorprone.bugpatterns.FallThrough
ERRORPRONE=com.google.errorprone.bugpatterns.EmptyIfStatement
ERRORPRONE=com.google.errorprone.bugpatterns.threadsafety.GuardedBySymbolResolver
ERRORPRONE=com.google.errorprone.bugpatterns.MockitoUsage
ERRORPRONE=com.google.errorprone.refaster.Unifier
ERRORPRONE=com.google.errorprone.bugpatterns.DoNotCallSuggester
ERRORPRONE=com.google.errorprone.bugpatterns.ImmutableSetForContains
ERRORPRONE=com.google.errorprone.bugpatterns.inject.AutoFactoryAtInject
ERRORPRONE=com.google.errorprone.bugpatterns.FieldCanBeFinal
ERRORPRONE=com.google.errorprone.bugpatterns.NonFinalCompileTimeConstant
ERRORPRONE=com.google.errorprone.bugpatterns.UnusedAnonymousClass
ERRORPRONE=com.google.errorprone.bugpatterns.AutoValue_TypeCompatibilityUtils_TypeCompatibilityReport
ERRORPRONE=com.google.errorprone.bugpatterns.UnusedVariable
ERRORPRONE=com.google.errorprone.refaster.AutoValue_UIf
ERRORPRONE=com.google.errorprone.bugpatterns.InconsistentCapitalization
ERRORPRONE=com.google.errorprone.refaster.AutoValue_UVariableDecl
ERRORPRONE=com.google.errorprone.bugpatterns.OptionalOfRedundantMethod
ERRORPRONE=com.google.errorprone.refaster.AutoValue_UTypeCast
ERRORPRONE=com.google.errorprone.bugpatterns.CanBeStaticAnalyzer
JAVAPOET=com.squareup.javapoet.Util
JAVAPOET=com.squareup.javapoet.JavaFile""".split("\n")))

def prepare_classpath(base_path: str, classpath: str) -> str:
    return ":".join(map(lambda x: os.path.join(base_path, x.strip()), classpath.split("\n")))


def bytebuddy_classpath(base_path: str) -> str:
    return prepare_classpath(
        base_path,
        """infrastructure/benchmarks_12th/projects/byte-buddy/byte-buddy-dep/target/classes
infrastructure/benchmarks_12th/projects/byte-buddy/byte-buddy-dep/target/dependency/asm-9.6.jar
infrastructure/benchmarks_12th/projects/byte-buddy/byte-buddy-dep/target/dependency/asm-commons-9.6.jar"""
    )

def errorprone_classpath(base_path: str) -> str:
    return prepare_classpath(
        base_path,
        """infrastructure/benchmarks_12th/projects/error-prone/core/target/classes
infrastructure/benchmarks_12th/projects/error-prone/core/target/dependency/error_prone_annotation-2.10.0.jar
infrastructure/benchmarks_12th/projects/error-prone/core/target/dependency/caffeine-2.8.8.jar
infrastructure/benchmarks_12th/projects/error-prone/core/target/dependency/jFormatString-3.0.0.jar
infrastructure/benchmarks_12th/projects/error-prone/core/target/dependency/pcollections-2.1.2.jar
infrastructure/benchmarks_12th/projects/error-prone/core/target/dependency/failureaccess-1.0.1.jar
infrastructure/benchmarks_12th/projects/error-prone/core/target/dependency/org.eclipse.jgit-4.4.1.201607150455-r.jar
infrastructure/benchmarks_12th/projects/error-prone/core/target/dependency/listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar
infrastructure/benchmarks_12th/projects/error-prone/core/target/dependency/error_prone_check_api-2.10.0.jar
infrastructure/benchmarks_12th/projects/error-prone/core/target/dependency/software-and-algorithms-1.0.jar
infrastructure/benchmarks_12th/projects/error-prone/core/target/dependency/auto-common-1.1.2.jar
infrastructure/benchmarks_12th/projects/error-prone/core/target/dependency/protobuf-java-3.4.0.jar
infrastructure/benchmarks_12th/projects/error-prone/core/target/dependency/javac-9+181-r4173-1.jar
infrastructure/benchmarks_12th/projects/error-prone/core/target/dependency/guava-30.1-jre.jar
infrastructure/benchmarks_12th/projects/error-prone/core/target/dependency/jsr305-3.0.0.jar
infrastructure/benchmarks_12th/projects/error-prone/core/target/dependency/auto-service-annotations-1.0-rc6.jar
infrastructure/benchmarks_12th/projects/error-prone/core/target/dependency/checker-qual-3.5.0.jar
infrastructure/benchmarks_12th/projects/error-prone/core/target/dependency/error_prone_type_annotations-2.10.0.jar
infrastructure/benchmarks_12th/projects/error-prone/core/target/dependency/j2objc-annotations-1.3.jar
infrastructure/benchmarks_12th/projects/error-prone/core/target/dependency/auto-value-annotations-1.7.jar
infrastructure/benchmarks_12th/projects/error-prone/core/target/dependency/java-diff-utils-4.0.jar
infrastructure/benchmarks_12th/projects/error-prone/core/target/dependency/dataflow-errorprone-3.15.0.jar
infrastructure/benchmarks_12th/projects/error-prone/core/target/dependency/error_prone_annotations-2.10.0.jar"""
    )

def javapoet_classpath(base_path: str) -> str:
    return prepare_classpath(
        base_path,
        """infrastructure/benchmarks_12th/projects/javapoet/target/classes"""
    )