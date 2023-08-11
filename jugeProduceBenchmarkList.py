#!/bin/python

import os
import json

JUGE_HOME = 'JUGE/infrastructure/benchmarks_11th/'
JUGE_DOCKER_HOME = '/var/benchmarks/'

def print_benchmark(benchmark, benchmark_klass):
	benchmark_src = ''
	benchmark_bin = ''
	benchmark_classpath = ''
	if benchmark.startswith('collections'):
		benchmark_src = JUGE_DOCKER_HOME + 'projects/commons-collections/src/main/java'
		benchmark_bin = JUGE_DOCKER_HOME + 'projects/commons-collections/target/classes'
		benchmark_classpath += JUGE_DOCKER_HOME + 'projects/commons-collections/target/commons-collections4-4.5-SNAPSHOT.jar'
		dependency_path = JUGE_HOME + 'projects/commons-collections/target/dependency'
		dependencies = [
			(dependency_path + '/' + path).replace(JUGE_HOME, JUGE_DOCKER_HOME)
		 	for path in os.listdir(dependency_path)
		]
		benchmark_classpath += ','
		benchmark_classpath += ','.join(dependencies)
	elif benchmark.startswith('jsoup'):
		benchmark_src = JUGE_DOCKER_HOME + 'projects/jsoup/src/main/java'
		benchmark_bin = JUGE_DOCKER_HOME + 'projects/jsoup/target/classes'
		benchmark_classpath += JUGE_DOCKER_HOME + 'projects/jsoup/target/jsoup-1.16.2-SNAPSHOT.jar'
		dependency_path = JUGE_HOME + 'projects/jsoup/target/dependency'
		dependencies = [
			(dependency_path + '/' + path).replace(JUGE_HOME, JUGE_DOCKER_HOME)
		 	for path in os.listdir(dependency_path)
		]
		benchmark_classpath += ','
		benchmark_classpath += ','.join(dependencies)
	elif benchmark.startswith('spatial4j'):
		benchmark_src = JUGE_DOCKER_HOME + 'projects/spatial4j/src/main/java'
		benchmark_bin = JUGE_DOCKER_HOME + 'projects/spatial4j/target/classes'
		benchmark_classpath += JUGE_DOCKER_HOME + 'projects/spatial4j/target/spatial4j-0.9-SNAPSHOT.jar'
		dependency_path = JUGE_HOME + 'projects/spatial4j/target/dependency'
		dependencies = [
			(dependency_path + '/' + path).replace(JUGE_HOME, JUGE_DOCKER_HOME)
		 	for path in os.listdir(dependency_path)
		]
		benchmark_classpath += ','
		benchmark_classpath += ','.join(dependencies)
	elif benchmark.startswith('ta4j'):
		benchmark_src = JUGE_DOCKER_HOME + 'projects/ta4j/ta4j-core/src/main/java'
		benchmark_bin = JUGE_DOCKER_HOME + 'projects/ta4j/ta4j-core/target/classes'
		benchmark_classpath += JUGE_DOCKER_HOME + 'projects/ta4j/ta4j-core/target/ta4j-core-0.15.jar'
		dependency_path = JUGE_HOME + 'projects/ta4j/ta4j-core/target/dependency'
		dependencies = [
			(dependency_path + '/' + path).replace(JUGE_HOME, JUGE_DOCKER_HOME)
		 	for path in os.listdir(dependency_path)
		]
		benchmark_classpath += ','
		benchmark_classpath += ','.join(dependencies)
	elif benchmark.startswith('threeten-extra'):
		benchmark_src = JUGE_DOCKER_HOME + 'projects/threeten-extra/src/main/java'
		benchmark_bin = JUGE_DOCKER_HOME + 'projects/threeten-extra/target/classes'
		benchmark_classpath += JUGE_DOCKER_HOME + 'projects/threeten-extra/target/threeten-extra-1.7.3-SNAPSHOT.jar'
		dependency_path = JUGE_HOME + 'projects/threeten-extra/target/dependency'
		dependencies = [
			(dependency_path + '/' + path).replace(JUGE_HOME, JUGE_DOCKER_HOME)
		 	for path in os.listdir(dependency_path)
		]
		benchmark_classpath += ','
		benchmark_classpath += ','.join(dependencies)



	print("{}=".format(benchmark.upper()) + '{')
	print("\tsrc={}".format(benchmark_src))
	print("\tbin={}".format(benchmark_bin))
	print("\tclasses=(")
	print("\t\t{}".format(benchmark_klass))
	print("\t)")
	print("\tclasspath=(")
	print("\t\t{}".format(benchmark_classpath))
	print("\t)")
	print("}")

BENCHMARK_CLASSES = list(map(lambda x: x.split("="), """collections-10	org.apache.commons.collections4.multimap.ArrayListValuedHashMap
collections-11	org.apache.commons.collections4.bidimap.DualTreeBidiMap
collections-12	org.apache.commons.collections4.functors.CloneTransformer
collections-13	org.apache.commons.collections4.MapUtils
collections-14	org.apache.commons.collections4.bag.CollectionBag
collections-15	org.apache.commons.collections4.functors.DefaultEquator
collections-16	org.apache.commons.collections4.sequence.ReplacementsFinder
collections-17	org.apache.commons.collections4.trie.analyzer.StringKeyAnalyzer
collections-18	org.apache.commons.collections4.IteratorUtils
collections-19	org.apache.commons.collections4.iterators.ZippingIterator
collections-1	org.apache.commons.collections4.SetUtils
collections-20	org.apache.commons.collections4.map.LinkedMap
collections-21	org.apache.commons.collections4.set.CompositeSet
collections-22	org.apache.commons.collections4.ArrayStack
collections-23	org.apache.commons.collections4.TransformerUtils
collections-24	org.apache.commons.collections4.functors.EqualPredicate
collections-25	org.apache.commons.collections4.sequence.EditScript
collections-2	org.apache.commons.collections4.collection.CompositeCollection
collections-3	org.apache.commons.collections4.iterators.SingletonIterator
collections-4	org.apache.commons.collections4.map.MultiValueMap
collections-5	org.apache.commons.collections4.functors.PrototypeFactory
collections-6	org.apache.commons.collections4.list.TreeList
collections-7	org.apache.commons.collections4.ListUtils
collections-8	org.apache.commons.collections4.functors.ChainedTransformer
collections-9	org.apache.commons.collections4.map.CompositeMap
jsoup-26	org.jsoup.examples.Wikipedia
jsoup-27	org.jsoup.parser.HtmlTreeBuilder
jsoup-28	org.jsoup.helper.DataUtil
jsoup-29	org.jsoup.select.Selector
jsoup-30	org.jsoup.parser.TokenQueue
jsoup-31	org.jsoup.nodes.FormElement
jsoup-32	org.jsoup.parser.CharacterReader
jsoup-33	org.jsoup.nodes.Element
jsoup-34	org.jsoup.select.Evaluator
jsoup-35	org.jsoup.safety.Cleaner
jsoup-36	org.jsoup.nodes.DocumentType
jsoup-37	org.jsoup.internal.ConstrainableInputStream
jsoup-38	org.jsoup.select.NodeTraversor
jsoup-39	org.jsoup.nodes.TextNode
spatial4j-40	org.locationtech.spatial4j.distance.GeodesicSphereDistCalc
spatial4j-41	org.locationtech.spatial4j.io.WKTReader
spatial4j-42	org.locationtech.spatial4j.shape.impl.PointImpl
spatial4j-43	org.locationtech.spatial4j.shape.SpatialRelation
spatial4j-44	org.locationtech.spatial4j.shape.impl.InfBufLine
spatial4j-45	org.locationtech.spatial4j.context.SpatialContextFactory
spatial4j-46	org.locationtech.spatial4j.SpatialPredicate
spatial4j-47	org.locationtech.spatial4j.distance.DistanceUtils
spatial4j-48	org.locationtech.spatial4j.shape.impl.BufferedLineString
spatial4j-49	org.locationtech.spatial4j.io.GeoJSONWriter
spatial4j-50	org.locationtech.spatial4j.shape.impl.BufferedLine
spatial4j-51	org.locationtech.spatial4j.shape.impl.CircleImpl
spatial4j-52	org.locationtech.spatial4j.io.PolyshapeReader
ta4j-53	org.ta4j.core.criteria.SqnCriterion
ta4j-54	org.ta4j.core.indicators.KAMAIndicator
ta4j-55	org.ta4j.core.aggregator.DurationBarAggregator
ta4j-56	org.ta4j.core.criteria.pnl.NetLossCriterion
ta4j-57	org.ta4j.core.criteria.helpers.StandardErrorCriterion
ta4j-58	org.ta4j.core.rules.StopGainRule
ta4j-59	org.ta4j.core.criteria.pnl.AverageProfitCriterion
ta4j-60	org.ta4j.core.utils.BarSeriesUtils
ta4j-61	org.ta4j.core.rules.StopLossRule
ta4j-62	org.ta4j.core.indicators.helpers.LossIndicator
ta4j-63	org.ta4j.core.indicators.LWMAIndicator
ta4j-64	org.ta4j.core.criteria.NumberOfBreakEvenPositionsCriterion
ta4j-65	org.ta4j.core.criteria.NumberOfLosingPositionsCriterion
ta4j-66	org.ta4j.core.analysis.cost.LinearTransactionCostModel
ta4j-67	org.ta4j.core.indicators.SMAIndicator
ta4j-68	org.ta4j.core.indicators.aroon.AroonUpIndicator
ta4j-69	org.ta4j.core.Trade
ta4j-70	org.ta4j.core.indicators.statistics.PearsonCorrelationIndicator
ta4j-71	org.ta4j.core.num.NaN
ta4j-72	org.ta4j.core.indicators.MACDIndicator
ta4j-73	org.ta4j.core.criteria.pnl.GrossProfitCriterion
ta4j-74	org.ta4j.core.rules.TimeRangeRule
ta4j-75	org.ta4j.core.indicators.aroon.AroonDownIndicator
ta4j-76	org.ta4j.core.Position
ta4j-77	org.ta4j.core.criteria.helpers.VarianceCriterion
ta4j-78	org.ta4j.core.indicators.UlcerIndexIndicator
ta4j-79	org.ta4j.core.indicators.statistics.VarianceIndicator
ta4j-80	org.ta4j.core.criteria.NumberOfConsecutivePositionsCriterion
ta4j-81	org.ta4j.core.indicators.statistics.SimpleLinearRegressionIndicator
ta4j-82	org.ta4j.core.analysis.Returns
threeten-extra-100	org.threeten.extra.chrono.EthiopicEra
threeten-extra-83	org.threeten.extra.Minutes
threeten-extra-84	org.threeten.extra.scale.UtcInstant
threeten-extra-85	org.threeten.extra.chrono.PaxEra
threeten-extra-86	org.threeten.extra.chrono.AccountingEra
threeten-extra-87	org.threeten.extra.PeriodDuration
threeten-extra-88	org.threeten.extra.PackedFields
threeten-extra-89	org.threeten.extra.chrono.Symmetry010Chronology
threeten-extra-90	org.threeten.extra.LocalDateRange
threeten-extra-91	org.threeten.extra.chrono.DiscordianChronology
threeten-extra-92	org.threeten.extra.chrono.Symmetry454Date
threeten-extra-93	org.threeten.extra.DayOfMonth
threeten-extra-94	org.threeten.extra.chrono.CopticEra
threeten-extra-95	org.threeten.extra.Months
threeten-extra-96	org.threeten.extra.chrono.PaxDate
threeten-extra-97	org.threeten.extra.scale.TaiInstant
threeten-extra-98	org.threeten.extra.chrono.CopticChronology
threeten-extra-99	org.threeten.extra.Seconds""".split("\n")))


for line in BENCHMARK_CLASSES:
	name = line[0].split('\t')[0]
	klass = line[0].split('\t')[1]
	print_benchmark(name, klass)