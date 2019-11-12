CREATE DATABASE  IF NOT EXISTS `pulselearning` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `pulselearning`;
-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: localhost    Database: pulselearning
-- ------------------------------------------------------
-- Server version	5.7.17-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `assignment`
--

DROP TABLE IF EXISTS `assignment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `assignment` (
  `assignmentID` int(11) NOT NULL AUTO_INCREMENT,
  `assignmentName` varchar(50) NOT NULL,
  `duedate` datetime DEFAULT NULL,
  PRIMARY KEY (`assignmentID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `assignment`
--

LOCK TABLES `assignment` WRITE;
/*!40000 ALTER TABLE `assignment` DISABLE KEYS */;
INSERT INTO `assignment` VALUES (1,'Report 1','2018-04-25 11:59:59'),(2,'Report 2','2018-05-25 11:59:59'),(3,'Essay 1','2018-04-29 11:59:59'),(4,'Essay 2','2018-05-29 11:59:59'),(5,'Exam 1','2018-05-29 11:59:59'),(6,'Exam 2','2018-05-21 11:59:59'),(7,'Presentation 1','2018-05-29 11:59:59'),(8,'Presentation 2','2018-05-23 11:59:59'),(9,'Quiz 1','2018-05-22 11:59:59'),(10,'Quiz 2','2018-05-29 11:59:59');
/*!40000 ALTER TABLE `assignment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `enrolments`
--

DROP TABLE IF EXISTS `enrolments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `enrolments` (
  `unitID` int(11) NOT NULL,
  `studentID` int(11) NOT NULL,
  PRIMARY KEY (`unitID`,`studentID`),
  KEY `studentID` (`studentID`),
  CONSTRAINT `studentID` FOREIGN KEY (`studentID`) REFERENCES `student` (`studentID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `unitID` FOREIGN KEY (`unitID`) REFERENCES `unit` (`unitID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enrolments`
--

LOCK TABLES `enrolments` WRITE;
/*!40000 ALTER TABLE `enrolments` DISABLE KEYS */;
INSERT INTO `enrolments` VALUES (101,1001),(102,1001),(103,1001),(104,1001),(101,1002),(102,1002),(103,1002),(104,1002),(101,1003),(102,1003),(103,1003),(104,1003),(101,1004),(102,1004),(103,1004),(104,1004),(105,1005),(105,1006),(106,1007),(101,1008),(102,1008),(101,1009),(102,1009),(101,1010),(102,1010),(103,1010),(101,1011),(102,1011);
/*!40000 ALTER TABLE `enrolments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grade`
--

DROP TABLE IF EXISTS `grade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `grade` (
  `studentID` int(11) NOT NULL,
  `assignmentID` int(11) NOT NULL,
  `grade` int(11) DEFAULT NULL,
  PRIMARY KEY (`studentID`,`assignmentID`),
  KEY `assignmentID` (`assignmentID`),
  CONSTRAINT `assignmentID` FOREIGN KEY (`assignmentID`) REFERENCES `assignment` (`assignmentID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `studentID2` FOREIGN KEY (`studentID`) REFERENCES `student` (`studentID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grade`
--

LOCK TABLES `grade` WRITE;
/*!40000 ALTER TABLE `grade` DISABLE KEYS */;
INSERT INTO `grade` VALUES (1001,1,75),(1002,2,78),(1003,3,76),(1004,4,79),(1005,5,50),(1006,1,61),(1007,2,62),(1008,3,72),(1009,4,99),(1010,5,85);
/*!40000 ALTER TABLE `grade` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phonenumber`
--

DROP TABLE IF EXISTS `phonenumber`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `phonenumber` (
  `studentID` int(11) NOT NULL AUTO_INCREMENT,
  `phoneNumber` char(10) NOT NULL,
  PRIMARY KEY (`studentID`,`phoneNumber`),
  CONSTRAINT `phonenumber_ibfk_1` FOREIGN KEY (`studentID`) REFERENCES `student` (`studentID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=1012 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phonenumber`
--

LOCK TABLES `phonenumber` WRITE;
/*!40000 ALTER TABLE `phonenumber` DISABLE KEYS */;
INSERT INTO `phonenumber` VALUES (1001,'0450331222'),(1001,'0733665423'),(1001,'0733695760'),(1002,'0262537777'),(1002,'0734523456'),(1003,'0444555777'),(1004,'0499876345'),(1005,'0245673338'),(1005,'0433772311'),(1006,'0733512150'),(1006,'0756784432'),(1007,'0433281768'),(1007,'0738887645'),(1008,'0567432777'),(1008,'0738756644'),(1009,'0433211765'),(1009,'0566664356'),(1010,'0398887444'),(1010,'0411333991'),(1011,'0477891265');
/*!40000 ALTER TABLE `phonenumber` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sleeppatterns`
--

DROP TABLE IF EXISTS `sleeppatterns`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sleeppatterns` (
  `sleepID` int(11) NOT NULL,
  `studentID` int(11) NOT NULL,
  `date` datetime DEFAULT NULL,
  `timeAsleep` int(11) DEFAULT NULL,
  `timeAwake` int(11) DEFAULT NULL,
  PRIMARY KEY (`sleepID`),
  KEY `studentID3` (`studentID`),
  CONSTRAINT `studentID3` FOREIGN KEY (`studentID`) REFERENCES `student` (`studentID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sleeppatterns`
--

LOCK TABLES `sleeppatterns` WRITE;
/*!40000 ALTER TABLE `sleeppatterns` DISABLE KEYS */;
INSERT INTO `sleeppatterns` VALUES (1,1001,'2018-04-20 10:00:00',7,17),(2,1002,'2018-04-20 10:00:00',8,16),(3,1003,'2018-04-20 10:00:00',5,19),(4,1004,'2018-04-20 10:00:00',6,18),(5,1005,'2018-04-20 10:00:00',5,19),(6,1006,'2018-04-20 10:00:00',7,17),(7,1007,'2018-04-20 10:00:00',6,18),(8,1008,'2018-04-20 10:00:00',5,19),(9,1009,'2018-04-20 10:00:00',6,18),(10,1010,'2018-04-20 10:00:00',5,19),(11,1011,'2018-04-20 10:00:00',6,18),(12,1012,'2018-04-20 10:00:00',8,16),(13,1001,'2018-03-20 10:00:00',7,17),(14,1002,'2018-03-20 10:00:00',8,16),(15,1003,'2018-03-20 10:00:00',5,19),(16,1004,'2018-03-20 10:00:00',6,18),(17,1005,'2018-03-20 10:00:00',5,19),(18,1006,'2018-03-20 10:00:00',7,17),(19,1007,'2018-03-20 10:00:00',6,18),(20,1008,'2018-03-20 10:00:00',5,19),(21,1009,'2018-03-20 10:00:00',6,18),(22,1010,'2018-03-20 10:00:00',5,19),(23,1011,'2018-03-20 10:00:00',6,18),(24,1012,'2018-03-20 10:00:00',8,16);
/*!40000 ALTER TABLE `sleeppatterns` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student` (
  `studentID` int(11) NOT NULL AUTO_INCREMENT,
  `firstName` varchar(50) NOT NULL,
  `surname` varchar(50) NOT NULL,
  `email` varchar(320) NOT NULL,
  `streetNumber` varchar(15) DEFAULT NULL,
  `streetName` varchar(30) DEFAULT NULL,
  `suburb` varchar(45) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `state` enum('QLD','SA','VIC','NSW','TAS','WA','NT','ACT') DEFAULT NULL,
  `postcode` char(4) DEFAULT NULL,
  `watchType` enum('FitBit','Suunto','Apple Watch','Samsung Gear') DEFAULT NULL,
  `watchSerialNumber` varchar(30) DEFAULT NULL,
  `buddyID` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`studentID`)
) ENGINE=InnoDB AUTO_INCREMENT=1022 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (1001,'Harry','Smith','h.smith@gmail.com','1112','Lorem Street','Brisbane','Brisbane','QLD','4000','Suunto','Y102567',NULL),(1002,'Marcus','McCarthy','mmccarthy@outlook.com','78','Ipsum Street','Fortitude Valley','Brisbane','QLD','4006','Suunto','XT4576',NULL),(1003,'Samantha','Jones','samantha@email.com','3444','Dolor Drive','Herston','Brisbane','QLD','4010','Suunto','Y123',NULL),(1004,'Lisa','Simpson','l.simpson@gmail.com','180','Zelda Street','Linkburb','Brisbane','QLD','4011','Suunto','Y124',NULL),(1005,'Ronaldo','Drake','ronnie@outlook.com','78','Amet Street','Newstead','Brisbane','QLD','4011','FitBit','Y125',NULL),(1006,'Thomas','Courtney','Tommy@email.com','90','Vim Street','Everton Hills','Brisbane','QLD','4053','FitBit','Y126',NULL),(1007,'Martha','Jordan','marthajordan@gmail.com','20','In Street','Newstead','Brisbane','QLD','4011','FitBit','Y212','1005'),(1008,'Carrie','Jones','carriejones@email.com','113','Mazim Street','Spring Hill','Brisbane','QLD','4003','FitBit','Y213',NULL),(1009,'Kayne','West','kanye@kanye.com','40','Errem Road','Spring Hill','Brisbane','QLD','4003','FitBit','Y214','1002'),(1010,'Lloyd','Miguel','miguel@iinet.net.au','4678','Sit Street','Spring Hill','Brisbane','QLD','4003','Apple Watch','Y217',NULL),(1011,'Jerry','Seinfield','jerry@seinfield.com.au','6789','In Street','Spring Hill','Brisbane','QLD','4003','Apple Watch','Y313',NULL),(1012,'Johnathon','Snow','jon@got.com.au','43267','Perciulis Road','Everton Park','Brisbane','QLD','4003','Apple Watch','Y312','1006'),(1013,'Alex','Smith','alexsmith@gmail.com','1/211','Consulatu Drive','Everton Hills','Brisbane','QLD','4020','Apple Watch','Y314',NULL),(1014,'Donny','Tee','dt@email.com','567','Eum Place','Paddington','Brisbane','QLD','4020','Apple Watch','Y315','1003'),(1015,'Christopher','Brown','brownie@outlook.com','778','Ut Lane','Paddington','Brisbane','QLD','4020','Apple Watch','Y316',NULL),(1016,'George','Costanza','george@gmail.com','3/45','Invidunt Grove','Paddington','Brisbane','QLD','4020','Apple Watch','Y317','1012'),(1017,'Trevor','Hill','thill@email.com','2/12','Accusamus Street','Everton Park','Brisbane','QLD','4006','Apple Watch','Y414',NULL),(1018,'Frank','Ocean','frankie@ocean.com','1/2','Efficantur Street','Teneriffe','Brisbane','QLD','4006','Apple Watch','Y415',NULL),(1019,'Angela','Smith','angies@gmail.com','180','Zelda Street','Linkburb','Brisbane','QLD','4006','Apple Watch','Y417',NULL),(1020,'Mario','Taylor','mariot@hotmail.com','678','Ornatus Drive','Everly','Brisbane','QLD','4000','Apple Watch','Y515','1004'),(1021,'Jennifer','Hill','hillsey@email.com','1/799','Intellegam Street','Brisbane','Brisbane','QLD','4000','Apple Watch','Y512','1003');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tutor`
--

DROP TABLE IF EXISTS `tutor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tutor` (
  `staffID` int(11) NOT NULL AUTO_INCREMENT,
  `firstName` varchar(50) NOT NULL,
  `surname` varchar(50) NOT NULL,
  `email` varchar(320) NOT NULL,
  PRIMARY KEY (`staffID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tutor`
--

LOCK TABLES `tutor` WRITE;
/*!40000 ALTER TABLE `tutor` DISABLE KEYS */;
INSERT INTO `tutor` VALUES (1,'Gazzy','Garcia','Gazzy@Pulse.com'),(2,'Jane','Doe','Jane@Pulse.com'),(3,'Jon','Snow','Jon@Pulse.com'),(4,'Jeff','Myers','Jeff@Pulse.com'),(5,'Josh','Pump','Pump@Pulse.com');
/*!40000 ALTER TABLE `tutor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unit`
--

DROP TABLE IF EXISTS `unit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `unit` (
  `unitID` int(11) NOT NULL AUTO_INCREMENT,
  `unitName` varchar(45) NOT NULL,
  `unitCode` char(6) NOT NULL,
  `year` year(4) DEFAULT NULL,
  `semester` enum('1','2','Summer') DEFAULT NULL,
  PRIMARY KEY (`unitID`)
) ENGINE=InnoDB AUTO_INCREMENT=114 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unit`
--

LOCK TABLES `unit` WRITE;
/*!40000 ALTER TABLE `unit` DISABLE KEYS */;
INSERT INTO `unit` VALUES (101,'Introduction to University','QUT101',2018,'1'),(102,'Programming','QUT102',2018,'1'),(103,'IT Systems','QUT103',2018,'1'),(104,'Databases','QUT104',2018,'1'),(105,'Design','QUT105',2018,'1'),(106,'Systems Design','QUT106',2018,'1'),(107,'Networks','QUT107',2018,'1'),(108,'Algorithms','QUT108',2018,'1'),(109,'Discrete Structures','QUT792',2018,'1'),(110,'Fun Class','QUT101',2018,'2'),(111,'Singing','QUT102',2018,'2'),(112,'Creative Writing','QUT103',2018,'2'),(113,'Programming 2','QUT104',2018,'2');
/*!40000 ALTER TABLE `unit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unittutor`
--

DROP TABLE IF EXISTS `unittutor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `unittutor` (
  `unitID` int(11) NOT NULL,
  `staffID` int(11) NOT NULL,
  PRIMARY KEY (`unitID`,`staffID`),
  KEY `staffID` (`staffID`),
  CONSTRAINT `staffID` FOREIGN KEY (`staffID`) REFERENCES `tutor` (`staffID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `unitID2` FOREIGN KEY (`unitID`) REFERENCES `unit` (`unitID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unittutor`
--

LOCK TABLES `unittutor` WRITE;
/*!40000 ALTER TABLE `unittutor` DISABLE KEYS */;
INSERT INTO `unittutor` VALUES (101,1),(105,1),(109,1),(113,1),(102,2),(106,2),(110,2),(103,3),(107,3),(111,3),(104,4),(108,4),(112,4);
/*!40000 ALTER TABLE `unittutor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-04-29 12:50:44
