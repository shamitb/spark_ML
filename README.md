# spark_ML
Machine Learning using Spark MLlib


<div dir="ltr" style="text-align: left;" trbidi="on">
<br class="Apple-interchange-newline" />
On Linux: Ubuntu 14.04.5 LTS, Release: 14.04, trusty.<br />
<span style="color: orange;"><b><br /></b></span> <span style="color: orange;"><b>Hadoop</b></span> does <b><span style="color: orange;">batch processing</span></b> i.e processing of blocks of data already stored over a period of time. Initially Hadoop's MapReduce technique was the best framework for processing data in batches. Spark is an open-source <b>cluster computing framework</b> for real-time processing.&nbsp;<b><span style="color: red;">Spark</span>'s</b> additional functionality is that it can <span style="color: red;"><b>process data in real time</b></span> and since it was built on top of Hadoop MapReduce and it extends the MapReduce model to efficiently use more types of computations it is also about 100 times faster than Hadoop MapReduce in batch processing large data sets.<br />
<br />
Spark can create distributed datasets from any file stored in the Hadoop distributed filesystem (HDFS) or other storage systems supported by the Hadoop APIs (including your local filesystem, Amazon S3, Cassandra, Hive, HBase, etc.). Spark does not require Hadoop; it simply has support for storage systems implementing the Hadoop APIs. Spark supports text files, SequenceFiles etc and any other Hadoop InputFormat.<br />
<br />
More differences and Spark details are here:&nbsp;<a href="https://www.edureka.co/blog/spark-tutorial/">https://www.edureka.co/blog/spark-tutorial/</a><br />
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="https://2.bp.blogspot.com/-MKLd7OUT8Ww/Wes7k8_FSnI/AAAAAAAAVto/d_SsCroc2bo_gr6lnI_uypjoatgV4IPKACLcBGAs/s1600/Spark.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="430" data-original-width="582" height="295" src="https://2.bp.blogspot.com/-MKLd7OUT8Ww/Wes7k8_FSnI/AAAAAAAAVto/d_SsCroc2bo_gr6lnI_uypjoatgV4IPKACLcBGAs/s400/Spark.png" width="400" /></a></div>
<br />
<br />
<a href="https://www.digitalocean.com/community/tutorials/how-to-install-hadoop-in-stand-alone-mode-on-ubuntu-16-04" target="_blank"><b>Install Hadoop in Stand-Alone Mode on Ubuntu 16.04</b></a><br />
<br />
Once installed run it&nbsp;as:<br />
<span style="background-color: rgba(0 , 0 , 0 , 0.05); color: #3a3a3a; font-family: monospace; font-size: 14px; white-space: pre;">/usr/local/hadoop/bin/hadoop</span><br />
<span style="background-color: rgba(0 , 0 , 0 , 0.05); color: #3a3a3a; font-family: monospace; font-size: 14px; white-space: pre;"><br /></span>
<br />
Scikit-Learn ML Examples:<br />
<a href="http://scikit-learn.org/stable/auto_examples/index.html#">http://scikit-learn.org/stable/auto_examples/index.html#</a><br />
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="https://1.bp.blogspot.com/-2mx9wMwbf8o/WetyEYWQl3I/AAAAAAAAVuU/MCSVqhgvrMQ--F72U8PcoaM5pAoNPrJpgCLcBGAs/s1600/Screenshot%2Bfrom%2B2017-10-21%2B13%253A51%253A17.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" data-original-height="768" data-original-width="1366" height="358" src="https://1.bp.blogspot.com/-2mx9wMwbf8o/WetyEYWQl3I/AAAAAAAAVuU/MCSVqhgvrMQ--F72U8PcoaM5pAoNPrJpgCLcBGAs/s640/Screenshot%2Bfrom%2B2017-10-21%2B13%253A51%253A17.png" width="640" /></a></div>
<br />
<br />
<br />
<!--more--><br />
<br />
Spark Examples:<br />
<a href="https://spark.apache.org/examples.html">https://spark.apache.org/examples.html</a><br />
<br />
<pre class="pre codeblock hljs" style="background: rgb(240, 240, 240); border: 1px dotted rgb(102, 102, 102); box-sizing: border-box; color: #444444; font-family: monospace, serif; font-size: 13px; margin-bottom: 10px; margin-top: 10px; overflow: auto; padding: 5px; word-wrap: normal;">Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version ...
      /_/</pre>
<div>
<br /></div>
There was a problem such as the following while running pyspark<br />
<blockquote class="tr_bq">
</blockquote>
<blockquote class="tr_bq">
Exception in thread "main" java.lang.UnsupportedClassVersionError: org/apache/spark/launcher/Main : Unsupported major.minor version 52.0</blockquote>
<br />
Apache Maven and JDK 8 had to be installed. Details here:<br />
<a href="https://www.digitalocean.com/community/tutorials/how-to-install-java-with-apt-get-on-ubuntu-16-04">https://www.digitalocean.com/community/tutorials/how-to-install-java-with-apt-get-on-ubuntu-16-04</a><br />
<br />
Also another problem to keep in mind from some of the Spark MLib code on the website to add the context and session variables:<br />
<br />
<blockquote class="tr_bq">
from pyspark.context import SparkContext<br />
from pyspark.sql.session import SparkSession<br />
sc = SparkContext('local')<br />
spark = SparkSession(sc)</blockquote>
<br />
<br />
<b><span style="font-size: large;"><span style="color: red;">Big Data with Apache Spark</span>:</span></b><br />
<br />
<ul style="text-align: left;">
<li><b><a href="https://github.com/dipanjanS/BerkeleyX-CS100.1x-Big-Data-with-Apache-Spark/blob/master/Week%205%20-%20Introduction%20to%20Machine%20Learning%20with%20Apache%20Spark/lab4_machine_learning_student.ipynb" target="_blank"><span style="font-size: large;">Machine Learning using Spark</span></a></b></li>
<li><b><span style="font-size: large;"><a href="https://github.com/dipanjanS/BerkeleyX-CS100.1x-Big-Data-with-Apache-Spark/blob/master/Week%202%20-%20Introduction%20to%20Apache%20Spark/lab1_word_count_student.ipynb" target="_blank">Python Code to create RDD, Map and Collect etc.</a></span></b></li>
</ul>
<br />
<br />
HDFS with Spark:&nbsp;<a href="https://cbw.sh/spark.html">https://cbw.sh/spark.html</a><br />
<br />
Setting Up Your Environment - In order to use HDFS and Spark, you first need to configure your environment so that you have access to the required tools. The easiest way to do this is to modify the <b>.bashrc </b>configuration file in your home directory.</div>
