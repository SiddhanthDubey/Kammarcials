CREATE DATABASE  IF NOT EXISTS `kammarcials` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `kammarcials`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: kammarcials
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.28-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `coupons`
--

DROP TABLE IF EXISTS `coupons`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coupons` (
  `idcoupons` int(11) NOT NULL AUTO_INCREMENT,
  `coupon_code` varchar(45) NOT NULL,
  `is_used` varchar(45) NOT NULL,
  PRIMARY KEY (`idcoupons`,`coupon_code`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coupons`
--

LOCK TABLES `coupons` WRITE;
/*!40000 ALTER TABLE `coupons` DISABLE KEYS */;
INSERT INTO `coupons` VALUES (1,'87dhashd9a8d','False'),(2,'o23h49283h4982','True'),(3,'8ahsdf87ahsf9','False');
/*!40000 ALTER TABLE `coupons` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `google_users`
--

DROP TABLE IF EXISTS `google_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `google_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `mobile` varchar(45) NOT NULL,
  `age` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`,`username`,`email`,`mobile`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `google_users`
--

LOCK TABLES `google_users` WRITE;
/*!40000 ALTER TABLE `google_users` DISABLE KEYS */;
INSERT INTO `google_users` VALUES (1,'fff','ss@ss.ss','897654678',13);
/*!40000 ALTER TABLE `google_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questions`
--

DROP TABLE IF EXISTS `questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questions` (
  `question_id` int(10) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `question` text NOT NULL,
  `option_a` tinytext NOT NULL,
  `option_b` tinytext NOT NULL,
  `option_c` tinytext NOT NULL,
  `option_d` tinytext NOT NULL,
  PRIMARY KEY (`question_id`),
  KEY `option_a_key` (`option_a`(255)),
  KEY `option_b_key` (`option_b`(255)),
  KEY `option_c_key` (`option_c`(255)),
  KEY `option_d_key` (`option_d`(255))
) ENGINE=InnoDB AUTO_INCREMENT=4294967296 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questions`
--

LOCK TABLES `questions` WRITE;
/*!40000 ALTER TABLE `questions` DISABLE KEYS */;
INSERT INTO `questions` VALUES (0000000001,'How was veg burger?','good','best','average','bad'),(0000000002,'How was customer service?','good','best','average','bad'),(0000000003,'wwcaracrwe','good','best','average','bad'),(0000000004,'wkejhfbjdsj','good','best','average','bad'),(0000000005,'dfvyjfufddd','good','best','average','bad'),(0000000006,'gfsdfgsdfgdfg','good','best','average','bad'),(0000000007,'dsfsdfsdfsdfs','good','best','average','bad'),(0000000008,'sdafdscasd','good','best','average','bad'),(0000000009,'fasdfasdfasdfafasf','good','best','average','bad'),(0000000010,'asdfasdcasdfaewf','good','best','average','bad'),(0000000011,'asfdasdfasdfa','good','best','average','bad'),(0000000012,'fgadfsfhgdg','good','best','average','bad'),(0000000013,'fdsgdgsdgfsdfgdfg','good','best','average','bad'),(0000000014,'sasfdasfasfdasdfasdfasdf','good','best','average','bad'),(0000000015,'hjjkjghfvdsdfvd','good','best','average','bad'),(0000000016,'fdvsdghdtyhth','good','best','average','bad'),(0000000017,'amsdvkfavskdfv','good','best','average','bad');
/*!40000 ALTER TABLE `questions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `response_detail`
--

DROP TABLE IF EXISTS `response_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `response_detail` (
  `time` datetime NOT NULL,
  `survey_id` varchar(45) NOT NULL,
  `user_id` varchar(45) NOT NULL,
  `q1` varchar(45) NOT NULL,
  `q2` varchar(45) NOT NULL,
  `q3` varchar(45) NOT NULL,
  `q4` varchar(45) NOT NULL,
  `q5` varchar(45) NOT NULL,
  `q6` varchar(45) NOT NULL,
  `q7` varchar(45) NOT NULL,
  `q8` varchar(45) NOT NULL,
  `q9` varchar(45) NOT NULL,
  `q10` varchar(45) NOT NULL,
  `q11` varchar(45) NOT NULL,
  `q12` varchar(45) NOT NULL,
  `response_status` varchar(45) NOT NULL,
  PRIMARY KEY (`time`,`survey_id`,`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `response_detail`
--

LOCK TABLES `response_detail` WRITE;
/*!40000 ALTER TABLE `response_detail` DISABLE KEYS */;
INSERT INTO `response_detail` VALUES ('2024-03-04 21:10:51','23454322','46','c','a','a','a','a','a','a','a','a','a','c','c','complete'),('2024-03-07 18:25:12','23423423','51','c','c','c','c','c','c','c','c','c','c','c','c','complete'),('2024-03-07 18:26:01','23454322','44','b','b','b','b','b','b','b','b','b','b','b','a','complete'),('2024-03-07 18:29:16','23454322','51','c','c','c','c','c','c','c','c','c','c','c','c','incomplete');
/*!40000 ALTER TABLE `response_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `survey`
--

DROP TABLE IF EXISTS `survey`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `survey` (
  `survey_id` int(11) NOT NULL,
  `q1` varchar(45) NOT NULL,
  `q2` varchar(45) NOT NULL,
  `q3` varchar(45) NOT NULL,
  `q4` varchar(45) NOT NULL,
  `q5` varchar(45) NOT NULL,
  `q6` varchar(45) NOT NULL,
  `q7` varchar(45) NOT NULL,
  `q8` varchar(45) NOT NULL,
  `q9` varchar(45) NOT NULL,
  `q10` varchar(45) NOT NULL,
  `q11` varchar(45) NOT NULL,
  `q12` varchar(45) NOT NULL,
  PRIMARY KEY (`survey_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `survey`
--

LOCK TABLES `survey` WRITE;
/*!40000 ALTER TABLE `survey` DISABLE KEYS */;
INSERT INTO `survey` VALUES (23423423,'1','2','3','4','5','6','7','8','9','10','11','12'),(23454322,'8','7','6','5','4','3','8','1','2','10','14','12'),(23458765,'9','8','7','6','5','4','3','2','1','11','10','13'),(34534535,'3','4','5','6','7','8','9','10','11','12','13','14'),(56789987,'8','7','6','5','4','3','1','12','2','14','11','10'),(76545678,'5','4','3','2','1','6','7','8','10','13','11','12'),(98765453,'2','4','3','7','8','3','9','13','14','12','11','6'),(98765456,'9','8','7','6','5','4','1','2','3','11','12','14');
/*!40000 ALTER TABLE `survey` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `survey_details`
--

DROP TABLE IF EXISTS `survey_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `survey_details` (
  `survey_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(45) NOT NULL,
  `age_lower` int(11) NOT NULL,
  `age_upper` int(11) NOT NULL,
  `company_name` varchar(45) NOT NULL,
  `total` varchar(45) NOT NULL,
  `surveys_left` varchar(45) NOT NULL,
  `surveys_done` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`survey_id`)
) ENGINE=InnoDB AUTO_INCREMENT=98765457 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `survey_details`
--

LOCK TABLES `survey_details` WRITE;
/*!40000 ALTER TABLE `survey_details` DISABLE KEYS */;
INSERT INTO `survey_details` VALUES (23423423,'KFC Chicken',15,50,'KFC','10','9','1'),(23454322,'Delloite Service',15,38,'Delloite','20','19','1'),(23458765,'Netflix Movies',15,35,'Netflix','11','11','0'),(34534535,'MCD burger',20,40,'MCD','10','10','0'),(56789987,'Amazon Products',15,36,'Amazon','12','12','0'),(76545678,'Google Service',23,37,'Google','12','12','0'),(98765453,'Meta Social',24,39,'Meta','13','13','0'),(98765456,'HP Laptop',25,41,'HP','11','11','0');
/*!40000 ALTER TABLE `survey_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `survey_status`
--

DROP TABLE IF EXISTS `survey_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `survey_status` (
  `user_id` int(11) NOT NULL,
  `survey_id` varchar(45) NOT NULL,
  `status` varchar(45) NOT NULL,
  PRIMARY KEY (`user_id`,`survey_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `survey_status`
--

LOCK TABLES `survey_status` WRITE;
/*!40000 ALTER TABLE `survey_status` DISABLE KEYS */;
INSERT INTO `survey_status` VALUES (44,'23454322','complete'),(46,'23454322','complete'),(51,'23423423','complete'),(51,'23454322','incomplete'),(51,'34534535','complete');
/*!40000 ALTER TABLE `survey_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_queries`
--

DROP TABLE IF EXISTS `user_queries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_queries` (
  `email` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `useri_id` varchar(45) NOT NULL,
  `query` varchar(100) NOT NULL,
  PRIMARY KEY (`email`,`useri_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_queries`
--

LOCK TABLES `user_queries` WRITE;
/*!40000 ALTER TABLE `user_queries` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_queries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int(11) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `email` varchar(45) NOT NULL,
  `age` int(11) NOT NULL,
  `password` varchar(45) NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`,`email`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (00000000043,'fff@fff.fff',13,'l~olo','',''),(00000000044,'sss@sss.sss',30,'~~~','',''),(00000000045,'aaa@aaa.aaa',16,'lll','',''),(00000000046,'ss@ss.ss',23,'~~','',''),(00000000047,'dd@dd.dd',22,'oo','',''),(00000000048,'ff@ff.ff',21,'qq','',''),(00000000051,'jj@jj.jj',24,'uu','j','j');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-09 10:14:07
