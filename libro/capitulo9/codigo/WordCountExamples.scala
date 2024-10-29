import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._

/**
 * 2 alternativas del popular ejemplo de wordcount
 */
object WordCountExamples extends App {

  val sc = new SparkContext("local", "Simple", "$SPARK_HOME"
    , List("target/SparkExamples1-1.0.jar"))

  val file = sc.textFile("README.md")

  val words = file.flatMap(line => line.split(" ")).persist()

  //alternativa #1
  val wordsPar = words.map(word => (word, 1))
  val result1 = wordsPar.reduceByKey((x, y) => x + y)

  result1.sortBy(_._2, false).collect().take(10).foreach(println)

  //alternativa #2
  val result2 = words.countByValue()

  result2.take(10).foreach(println)
}
