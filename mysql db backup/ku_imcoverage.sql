-- MySQL dump 10.13  Distrib 8.0.17, for Win64 (x86_64)
--
-- Host: localhost    Database: ku
-- ------------------------------------------------------
-- Server version	5.7.27-log

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
-- Table structure for table `imcoverage`
--

DROP TABLE IF EXISTS `imcoverage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `imcoverage` (
  `polProcessID` int(11) NOT NULL DEFAULT '0',
  `stateID` smallint(6) NOT NULL DEFAULT '0',
  `countyID` int(11) NOT NULL DEFAULT '0',
  `yearID` smallint(6) NOT NULL DEFAULT '0',
  `sourceTypeID` smallint(6) NOT NULL DEFAULT '0',
  `fuelTypeID` smallint(6) NOT NULL DEFAULT '0',
  `IMProgramID` smallint(6) NOT NULL DEFAULT '0',
  `begModelYearID` smallint(6) NOT NULL DEFAULT '0',
  `endModelYearID` smallint(6) NOT NULL DEFAULT '0',
  `inspectFreq` smallint(6) DEFAULT NULL,
  `testStandardsID` smallint(6) NOT NULL DEFAULT '0',
  `useIMyn` char(1) NOT NULL DEFAULT 'Y',
  `complianceFactor` float DEFAULT NULL,
  PRIMARY KEY (`polProcessID`,`stateID`,`countyID`,`yearID`,`sourceTypeID`,`fuelTypeID`,`IMProgramID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `imcoverage`
--

LOCK TABLES `imcoverage` WRITE;
/*!40000 ALTER TABLE `imcoverage` DISABLE KEYS */;
/*!40000 ALTER TABLE `imcoverage` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-10-03  9:59:34
