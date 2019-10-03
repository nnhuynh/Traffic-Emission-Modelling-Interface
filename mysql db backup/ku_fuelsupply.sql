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
-- Table structure for table `fuelsupply`
--

DROP TABLE IF EXISTS `fuelsupply`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fuelsupply` (
  `fuelRegionID` int(11) NOT NULL DEFAULT '0',
  `fuelYearID` smallint(6) NOT NULL DEFAULT '0',
  `monthGroupID` smallint(6) NOT NULL DEFAULT '0',
  `fuelFormulationID` smallint(6) NOT NULL DEFAULT '0',
  `marketShare` float DEFAULT NULL,
  `marketShareCV` float DEFAULT NULL,
  PRIMARY KEY (`fuelRegionID`,`fuelFormulationID`,`monthGroupID`,`fuelYearID`),
  KEY `fuelRegionID` (`fuelRegionID`),
  KEY `yearID` (`fuelYearID`),
  KEY `monthGroupID` (`monthGroupID`),
  KEY `fuelSubtypeID` (`fuelFormulationID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fuelsupply`
--

LOCK TABLES `fuelsupply` WRITE;
/*!40000 ALTER TABLE `fuelsupply` DISABLE KEYS */;
INSERT INTO `fuelsupply` VALUES (100000000,2019,7,10,0.749731,0.5),(100000000,2019,7,1002,0.250269,0.5),(100000000,2019,7,20,1,0.5);
/*!40000 ALTER TABLE `fuelsupply` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-10-03  9:59:33
