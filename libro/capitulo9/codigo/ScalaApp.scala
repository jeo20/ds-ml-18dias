import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._

/**
 * Programa con invocaciones de ejemplos operaciones en los RDD
 * - filter
 * - flatMap
 * - union
 * - collect
 * - distinct
 * - foreach
 * - take
 * - count
 */
object ScalaApp extends App {

  val sc = new SparkContext("local", "Simple", "$SPARK_HOME"
    , List("target/SparkExamples1-1.0.jar"))

  val file = sc.textFile("README.md")
  file.persist()

  //filtradas lineas que contienen la palabra python
  val pythonLines = file.filter(lines => lines.contains("Python"))
  //filtradas lineas que contienen la palabra scala
  val scalaLines = file.filter(lines => lines.contains("Scala"))

  //RDD con lineas filtradas que contienen las palabras python y scala (resultado de la union)
  val pythonAndScalaLines = pythonLines.union(scalaLines);

  //muestra todas las lineas
  pythonAndScalaLines.collect().foreach(println)

  //No muestra la misma linea en mas de una ocasión
  pythonAndScalaLines.distinct().collect().foreach(println)

  val words = pythonAndScalaLines.flatMap(line => line.split(" "))
  //Total de palabras
  println("Total: " + words.count())

  //listado de 10 palabras con el numero de veces que se repite c/u
  words.countByValue().take(10).foreach(println)
}