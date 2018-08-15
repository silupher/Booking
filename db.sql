-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: localhost    Database: dbo.schema
-- ------------------------------------------------------
-- Server version	5.7.23-0ubuntu0.18.04.1

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
-- Current Database: `dbo.schema`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `dbo.schema` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `dbo.schema`;

--
-- Table structure for table `dbo.AdminUsers`
--

DROP TABLE IF EXISTS `dbo.AdminUsers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.AdminUsers` (
  `Id` int(11) NOT NULL,
  `UserId` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `UserIdReference_idx` (`UserId`),
  CONSTRAINT `UserIdReference` FOREIGN KEY (`UserId`) REFERENCES `dbo.Users` (`Id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.AdminUsers`
--

LOCK TABLES `dbo.AdminUsers` WRITE;
/*!40000 ALTER TABLE `dbo.AdminUsers` DISABLE KEYS */;
INSERT INTO `dbo.AdminUsers` VALUES (0,3);
/*!40000 ALTER TABLE `dbo.AdminUsers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.Roles`
--

DROP TABLE IF EXISTS `dbo.Roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.Roles` (
  `Id` int(11) NOT NULL,
  `Role` varchar(45) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.Roles`
--

LOCK TABLES `dbo.Roles` WRITE;
/*!40000 ALTER TABLE `dbo.Roles` DISABLE KEYS */;
INSERT INTO `dbo.Roles` VALUES (1,'User'),(2,'TeamLeader');
/*!40000 ALTER TABLE `dbo.Roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.SystemConfigurations`
--

DROP TABLE IF EXISTS `dbo.SystemConfigurations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.SystemConfigurations` (
  `Key` varchar(50) CHARACTER SET utf8 NOT NULL,
  `Value` varchar(50) CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY (`Key`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.SystemConfigurations`
--

LOCK TABLES `dbo.SystemConfigurations` WRITE;
/*!40000 ALTER TABLE `dbo.SystemConfigurations` DISABLE KEYS */;
INSERT INTO `dbo.SystemConfigurations` VALUES ('Date','20180804'),('Environment','Preview');
/*!40000 ALTER TABLE `dbo.SystemConfigurations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.TeamMemberships`
--

DROP TABLE IF EXISTS `dbo.TeamMemberships`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.TeamMemberships` (
  `Id` int(11) NOT NULL,
  `TeamId` int(11) NOT NULL,
  `UserId` int(11) NOT NULL,
  `RoleId` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `TeamReference_idx` (`TeamId`),
  KEY `UserReference_idx` (`UserId`),
  KEY `RoleReference_idx` (`RoleId`),
  CONSTRAINT `RoleReference` FOREIGN KEY (`RoleId`) REFERENCES `dbo.Roles` (`Id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `TeamReference` FOREIGN KEY (`TeamId`) REFERENCES `dbo.Teams` (`Id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `UserReference` FOREIGN KEY (`UserId`) REFERENCES `dbo.Users` (`Id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.TeamMemberships`
--

LOCK TABLES `dbo.TeamMemberships` WRITE;
/*!40000 ALTER TABLE `dbo.TeamMemberships` DISABLE KEYS */;
INSERT INTO `dbo.TeamMemberships` VALUES (0,0,0,2),(1,0,1,1),(2,1,2,1),(3,1,3,2);
/*!40000 ALTER TABLE `dbo.TeamMemberships` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.Teams`
--

DROP TABLE IF EXISTS `dbo.Teams`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.Teams` (
  `Id` int(11) NOT NULL,
  `Name` varchar(45) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.Teams`
--

LOCK TABLES `dbo.Teams` WRITE;
/*!40000 ALTER TABLE `dbo.Teams` DISABLE KEYS */;
INSERT INTO `dbo.Teams` VALUES (0,'RedTeam'),(1,'GreenTeam');
/*!40000 ALTER TABLE `dbo.Teams` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.Tickets`
--

DROP TABLE IF EXISTS `dbo.Tickets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.Tickets` (
  `Id` int(11) NOT NULL,
  `TeamId` int(11) NOT NULL,
  `Month` char(6) CHARACTER SET utf8 NOT NULL,
  `Tickets` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `TeamId_idx` (`TeamId`),
  CONSTRAINT `TeamId` FOREIGN KEY (`TeamId`) REFERENCES `dbo.Teams` (`Id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.Tickets`
--

LOCK TABLES `dbo.Tickets` WRITE;
/*!40000 ALTER TABLE `dbo.Tickets` DISABLE KEYS */;
INSERT INTO `dbo.Tickets` VALUES (0,0,'201808',59),(1,1,'201808',3),(2,0,'201807',5),(3,1,'201807',4);
/*!40000 ALTER TABLE `dbo.Tickets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.Users`
--

DROP TABLE IF EXISTS `dbo.Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.Users` (
  `Id` int(11) NOT NULL,
  `Name` varchar(45) NOT NULL,
  `Password` varchar(50) CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `Name_UNIQUE` (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.Users`
--

LOCK TABLES `dbo.Users` WRITE;
/*!40000 ALTER TABLE `dbo.Users` DISABLE KEYS */;
INSERT INTO `dbo.Users` VALUES (0,'jim','8a6ec0ea3a19e75020d79132e5d7560d'),(1,'tom','5caf72868c94f184650f43413092e82c'),(2,'dan','0f281d173f0fdfdccccd7e5b8edc21f1'),(3,'jessica','84f3ea20769026be4b6512d3e0399832'),(4,'min','07105a4643a5c133207afd3ccd98badc'),(5,'luke','85242bd9419eb073a907d7f756b5f8dd'),(6,'helen','3fe4c917f62e537e040eb6424ef3d304\r');
/*!40000 ALTER TABLE `dbo.Users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-08-15 17:31:37
