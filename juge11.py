import os

BENCHMARK_CLASSES = list(map(lambda x: x.split("="), """COLLECTIONS=org.apache.commons.collections4.multimap.ArrayListValuedHashMap
COLLECTIONS=org.apache.commons.collections4.bidimap.DualTreeBidiMap
COLLECTIONS=org.apache.commons.collections4.functors.CloneTransformer
COLLECTIONS=org.apache.commons.collections4.MapUtils
COLLECTIONS=org.apache.commons.collections4.bag.CollectionBag
COLLECTIONS=org.apache.commons.collections4.functors.DefaultEquator
COLLECTIONS=org.apache.commons.collections4.sequence.ReplacementsFinder
COLLECTIONS=org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer
COLLECTIONS=org.apache.commons.collections4.IteratorUtils
COLLECTIONS=org.apache.commons.collections4.iterators.ZippingIterator
COLLECTIONS=org.apache.commons.collections4.SetUtils
COLLECTIONS=org.apache.commons.collections4.map.LinkedMap
COLLECTIONS=org.apache.commons.collections4.set.CompositeSet
COLLECTIONS=org.apache.commons.collections4.ArrayStack
COLLECTIONS=org.apache.commons.collections4.TransformerUtils
COLLECTIONS=org.apache.commons.collections4.functors.EqualPredicate
COLLECTIONS=org.apache.commons.collections4.sequence.EditScript
COLLECTIONS=org.apache.commons.collections4.collection.CompositeCollection
COLLECTIONS=org.apache.commons.collections4.iterators.SingletonIterator
COLLECTIONS=org.apache.commons.collections4.map.MultiValueMap
COLLECTIONS=org.apache.commons.collections4.functors.PrototypeFactory
COLLECTIONS=org.apache.commons.collections4.list.TreeList
COLLECTIONS=org.apache.commons.collections4.ListUtils
COLLECTIONS=org.apache.commons.collections4.functors.ChainedTransformer
COLLECTIONS=org.apache.commons.collections4.map.CompositeMap
JSOUP=org.jsoup.examples.Wikipedia
JSOUP=org.jsoup.parser.HtmlTreeBuilder
JSOUP=org.jsoup.helper.DataUtil
JSOUP=org.jsoup.select.Selector
JSOUP=org.jsoup.parser.TokenQueue
JSOUP=org.jsoup.nodes.FormElement
JSOUP=org.jsoup.parser.CharacterReader
JSOUP=org.jsoup.nodes.Element
JSOUP=org.jsoup.select.Evaluator
JSOUP=org.jsoup.safety.Cleaner
JSOUP=org.jsoup.nodes.DocumentType
JSOUP=org.jsoup.internal.ConstrainableInputStream
JSOUP=org.jsoup.select.NodeTraversor
JSOUP=org.jsoup.nodes.TextNode
SPATIAL4J=org.locationtech.spatial4j.distance.GeodesicSphereDistCalc
SPATIAL4J=org.locationtech.spatial4j.io.WKTReader
SPATIAL4J=org.locationtech.spatial4j.shape.impl.PointImpl
SPATIAL4J=org.locationtech.spatial4j.shape.SpatialRelation
SPATIAL4J=org.locationtech.spatial4j.shape.impl.InfBufLine
SPATIAL4J=org.locationtech.spatial4j.context.SpatialContextFactory
SPATIAL4J=org.locationtech.spatial4j.SpatialPredicate
SPATIAL4J=org.locationtech.spatial4j.distance.DistanceUtils
SPATIAL4J=org.locationtech.spatial4j.shape.impl.BufferedLineString
SPATIAL4J=org.locationtech.spatial4j.io.GeoJSONWriter
SPATIAL4J=org.locationtech.spatial4j.shape.impl.BufferedLine
SPATIAL4J=org.locationtech.spatial4j.shape.impl.CircleImpl
SPATIAL4J=org.locationtech.spatial4j.io.PolyshapeReader
TA4J=org.ta4j.core.criteria.SqnCriterion
TA4J=org.ta4j.core.indicators.KAMAIndicator
TA4J=org.ta4j.core.aggregator.DurationBarAggregator
TA4J=org.ta4j.core.criteria.pnl.NetLossCriterion
TA4J=org.ta4j.core.criteria.helpers.StandardErrorCriterion
TA4J=org.ta4j.core.rules.StopGainRule
TA4J=org.ta4j.core.criteria.pnl.AverageProfitCriterion
TA4J=org.ta4j.core.utils.BarSeriesUtils
TA4J=org.ta4j.core.rules.StopLossRule
TA4J=org.ta4j.core.indicators.helpers.LossIndicator
TA4J=org.ta4j.core.indicators.LWMAIndicator
TA4J=org.ta4j.core.criteria.NumberOfBreakEvenPositionsCriterion
TA4J=org.ta4j.core.criteria.NumberOfLosingPositionsCriterion
TA4J=org.ta4j.core.analysis.cost.LinearTransactionCostModel
TA4J=org.ta4j.core.indicators.SMAIndicator
TA4J=org.ta4j.core.indicators.aroon.AroonUpIndicator
TA4J=org.ta4j.core.Trade
TA4J=org.ta4j.core.indicators.statistics.PearsonCorrelationIndicator
TA4J=org.ta4j.core.num.NaN
TA4J=org.ta4j.core.indicators.MACDIndicator
TA4J=org.ta4j.core.criteria.pnl.GrossProfitCriterion
TA4J=org.ta4j.core.rules.TimeRangeRule
TA4J=org.ta4j.core.indicators.aroon.AroonDownIndicator
TA4J=org.ta4j.core.Position
TA4J=org.ta4j.core.criteria.helpers.VarianceCriterion
TA4J=org.ta4j.core.indicators.UlcerIndexIndicator
TA4J=org.ta4j.core.indicators.statistics.VarianceIndicator
TA4J=org.ta4j.core.criteria.NumberOfConsecutivePositionsCriterion
TA4J=org.ta4j.core.indicators.statistics.SimpleLinearRegressionIndicator
TA4J=org.ta4j.core.analysis.Returns
THREETEN-EXTRA=org.threeten.extra.chrono.EthiopicEra
THREETEN-EXTRA=org.threeten.extra.Minutes
THREETEN-EXTRA=org.threeten.extra.scale.UtcInstant
THREETEN-EXTRA=org.threeten.extra.chrono.PaxEra
THREETEN-EXTRA=org.threeten.extra.chrono.AccountingEra
THREETEN-EXTRA=org.threeten.extra.PeriodDuration
THREETEN-EXTRA=org.threeten.extra.PackedFields
THREETEN-EXTRA=org.threeten.extra.chrono.Symmetry010Chronology
THREETEN-EXTRA=org.threeten.extra.LocalDateRange
THREETEN-EXTRA=org.threeten.extra.chrono.DiscordianChronology
THREETEN-EXTRA=org.threeten.extra.chrono.Symmetry454Date
THREETEN-EXTRA=org.threeten.extra.DayOfMonth
THREETEN-EXTRA=org.threeten.extra.chrono.CopticEra
THREETEN-EXTRA=org.threeten.extra.Months
THREETEN-EXTRA=org.threeten.extra.chrono.PaxDate
THREETEN-EXTRA=org.threeten.extra.scale.TaiInstant
THREETEN-EXTRA=org.threeten.extra.chrono.CopticChronology
THREETEN-EXTRA=org.threeten.extra.Seconds""".split("\n")))


def prepare_classpath(base_path: str, classpath: str) -> str:
    return ":".join(map(lambda x: os.path.join(base_path, x.strip()), classpath.split("\n")))


def collections_classpath(base_path: str) -> str:
    return prepare_classpath(
        base_path,
        """infrastructure/benchmarks_11th/projects/commons-collections/target/commons-collections4-4.5-SNAPSHOT.jar
infrastructure/benchmarks_11th/projects/commons-collections/target/dependency/error_prone_annotations-2.18.0.jar
infrastructure/benchmarks_11th/projects/commons-collections/target/dependency/junit-jupiter-params-5.9.3.jar
infrastructure/benchmarks_11th/projects/commons-collections/target/dependency/hamcrest-core-1.3.jar
infrastructure/benchmarks_11th/projects/commons-collections/target/dependency/easymock-5.1.0.jar
infrastructure/benchmarks_11th/projects/commons-collections/target/dependency/checker-qual-3.33.0.jar
infrastructure/benchmarks_11th/projects/commons-collections/target/dependency/junit-jupiter-engine-5.9.3.jar
infrastructure/benchmarks_11th/projects/commons-collections/target/dependency/junit-platform-engine-1.9.3.jar
infrastructure/benchmarks_11th/projects/commons-collections/target/dependency/commons-lang3-3.13.0.jar
infrastructure/benchmarks_11th/projects/commons-collections/target/dependency/listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar
infrastructure/benchmarks_11th/projects/commons-collections/target/dependency/junit-jupiter-api-5.9.3.jar
infrastructure/benchmarks_11th/projects/commons-collections/target/dependency/commons-codec-1.16.0.jar
infrastructure/benchmarks_11th/projects/commons-collections/target/dependency/junit-platform-commons-1.9.3.jar
infrastructure/benchmarks_11th/projects/commons-collections/target/dependency/apiguardian-api-1.1.2.jar
infrastructure/benchmarks_11th/projects/commons-collections/target/dependency/opentest4j-1.2.0.jar
infrastructure/benchmarks_11th/projects/commons-collections/target/dependency/failureaccess-1.0.1.jar
infrastructure/benchmarks_11th/projects/commons-collections/target/dependency/jsr305-3.0.2.jar
infrastructure/benchmarks_11th/projects/commons-collections/target/dependency/objenesis-3.3.jar
infrastructure/benchmarks_11th/projects/commons-collections/target/dependency/guava-testlib-32.1.2-jre.jar
infrastructure/benchmarks_11th/projects/commons-collections/target/dependency/j2objc-annotations-2.8.jar
infrastructure/benchmarks_11th/projects/commons-collections/target/dependency/hamcrest-2.2.jar
infrastructure/benchmarks_11th/projects/commons-collections/target/dependency/junit-4.13.2.jar
infrastructure/benchmarks_11th/projects/commons-collections/target/dependency/commons-io-2.13.0.jar
infrastructure/benchmarks_11th/projects/commons-collections/target/dependency/guava-32.1.2-jre.jar"""
    )

def jsoup_classpath(base_path: str) -> str:
    return prepare_classpath(
        base_path,
        """infrastructure/benchmarks_11th/projects/jsoup/target/classes
infrastructure/benchmarks_11th/projects/jsoup/target/dependency/junit-jupiter-params-5.9.3.jar
infrastructure/benchmarks_11th/projects/jsoup/target/dependency/gson-2.10.1.jar
infrastructure/benchmarks_11th/projects/jsoup/target/dependency/jetty-util-ajax-9.4.51.v20230217.jar
infrastructure/benchmarks_11th/projects/jsoup/target/dependency/junit-jupiter-engine-5.9.3.jar
infrastructure/benchmarks_11th/projects/jsoup/target/dependency/jetty-server-9.4.51.v20230217.jar
infrastructure/benchmarks_11th/projects/jsoup/target/dependency/junit-platform-engine-1.9.3.jar
infrastructure/benchmarks_11th/projects/jsoup/target/dependency/junit-jupiter-api-5.9.3.jar
infrastructure/benchmarks_11th/projects/jsoup/target/dependency/junit-platform-commons-1.9.3.jar
infrastructure/benchmarks_11th/projects/jsoup/target/dependency/apiguardian-api-1.1.2.jar
infrastructure/benchmarks_11th/projects/jsoup/target/dependency/opentest4j-1.2.0.jar
infrastructure/benchmarks_11th/projects/jsoup/target/dependency/javax.servlet-api-3.1.0.jar
infrastructure/benchmarks_11th/projects/jsoup/target/dependency/jetty-util-9.4.51.v20230217.jar
infrastructure/benchmarks_11th/projects/jsoup/target/dependency/jetty-http-9.4.51.v20230217.jar
infrastructure/benchmarks_11th/projects/jsoup/target/dependency/jetty-security-9.4.51.v20230217.jar
infrastructure/benchmarks_11th/projects/jsoup/target/dependency/jsr305-3.0.2.jar
infrastructure/benchmarks_11th/projects/jsoup/target/dependency/jetty-io-9.4.51.v20230217.jar
infrastructure/benchmarks_11th/projects/jsoup/target/dependency/junit-jupiter-5.9.3.jar
infrastructure/benchmarks_11th/projects/jsoup/target/dependency/jetty-servlet-9.4.51.v20230217.jar"""
    )


def spatial4j_classpath(base_path: str) -> str:
    return prepare_classpath(
        base_path,
        """infrastructure/benchmarks_11th/projects/spatial4j/target/spatial4j-0.9-SNAPSHOT.jar
infrastructure/benchmarks_11th/projects/spatial4j/target/dependency/randomizedtesting-runner-2.5.3.jar
infrastructure/benchmarks_11th/projects/spatial4j/target/dependency/slf4j-simple-1.7.25.jar
infrastructure/benchmarks_11th/projects/spatial4j/target/dependency/hamcrest-core-1.3.jar
infrastructure/benchmarks_11th/projects/spatial4j/target/dependency/jackson-core-2.13.4.jar
infrastructure/benchmarks_11th/projects/spatial4j/target/dependency/jackson-databind-2.13.4.2.jar
infrastructure/benchmarks_11th/projects/spatial4j/target/dependency/noggit-0.8.jar
infrastructure/benchmarks_11th/projects/spatial4j/target/dependency/jts-core-1.18.1.jar
infrastructure/benchmarks_11th/projects/spatial4j/target/dependency/junit-4.13.1.jar
infrastructure/benchmarks_11th/projects/spatial4j/target/dependency/jackson-annotations-2.13.4.jar
infrastructure/benchmarks_11th/projects/spatial4j/target/dependency/slf4j-api-1.7.25.jar"""
    )


def threeten_extra_classpath(base_path: str) -> str:
    return prepare_classpath(
        base_path,
        """infrastructure/benchmarks_11th/projects/threeten-extra/target/threeten-extra-1.7.3-SNAPSHOT.jar
infrastructure/benchmarks_11th/projects/threeten-extra/target/dependency/junit-platform-engine-1.9.1.jar
infrastructure/benchmarks_11th/projects/threeten-extra/target/dependency/junit-jupiter-api-5.9.1.jar
infrastructure/benchmarks_11th/projects/threeten-extra/target/dependency/joda-convert-2.2.2.jar
infrastructure/benchmarks_11th/projects/threeten-extra/target/dependency/junit-jupiter-params-5.9.1.jar
infrastructure/benchmarks_11th/projects/threeten-extra/target/dependency/junit-platform-launcher-1.9.1.jar
infrastructure/benchmarks_11th/projects/threeten-extra/target/dependency/junit-pioneer-1.9.1.jar
infrastructure/benchmarks_11th/projects/threeten-extra/target/dependency/junit-platform-commons-1.9.1.jar
infrastructure/benchmarks_11th/projects/threeten-extra/target/dependency/listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar
infrastructure/benchmarks_11th/projects/threeten-extra/target/dependency/junit-jupiter-5.9.1.jar
infrastructure/benchmarks_11th/projects/threeten-extra/target/dependency/apiguardian-api-1.1.2.jar
infrastructure/benchmarks_11th/projects/threeten-extra/target/dependency/opentest4j-1.2.0.jar
infrastructure/benchmarks_11th/projects/threeten-extra/target/dependency/failureaccess-1.0.1.jar
infrastructure/benchmarks_11th/projects/threeten-extra/target/dependency/junit-jupiter-engine-5.9.1.jar
infrastructure/benchmarks_11th/projects/threeten-extra/target/dependency/guava-32.1.2-jre.jar"""
    )


def ta4j_classpath(base_path: str) -> str:
    return prepare_classpath(
        base_path,
        """infrastructure/benchmarks_11th/projects/ta4j/ta4j-core/target/ta4j-core-0.15.jar
infrastructure/benchmarks_11th/projects/ta4j/ta4j-core/target/dependency/hamcrest-core-1.3.jar
infrastructure/benchmarks_11th/projects/ta4j/ta4j-core/target/dependency/commons-io-2.11.0.jar
infrastructure/benchmarks_11th/projects/ta4j/ta4j-core/target/dependency/logback-classic-1.2.3.jar
infrastructure/benchmarks_11th/projects/ta4j/ta4j-core/target/dependency/commons-math3-3.6.1.jar
infrastructure/benchmarks_11th/projects/ta4j/ta4j-core/target/dependency/SparseBitSet-1.2.jar
infrastructure/benchmarks_11th/projects/ta4j/ta4j-core/target/dependency/log4j-api-2.17.2.jar
infrastructure/benchmarks_11th/projects/ta4j/ta4j-core/target/dependency/junit-4.13.1.jar
infrastructure/benchmarks_11th/projects/ta4j/ta4j-core/target/dependency/logback-core-1.2.3.jar
infrastructure/benchmarks_11th/projects/ta4j/ta4j-core/target/dependency/poi-5.2.2.jar
infrastructure/benchmarks_11th/projects/ta4j/ta4j-core/target/dependency/commons-codec-1.15.jar
infrastructure/benchmarks_11th/projects/ta4j/ta4j-core/target/dependency/commons-collections4-4.4.jar
infrastructure/benchmarks_11th/projects/ta4j/ta4j-core/target/dependency/slf4j-api-1.7.25.jar"""
    )
