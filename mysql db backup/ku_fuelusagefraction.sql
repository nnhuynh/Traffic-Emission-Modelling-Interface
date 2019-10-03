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
-- Table structure for table `fuelusagefraction`
--

DROP TABLE IF EXISTS `fuelusagefraction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fuelusagefraction` (
  `countyID` int(11) NOT NULL,
  `fuelYearID` int(11) NOT NULL,
  `modelYearGroupID` int(11) NOT NULL,
  `sourceBinFuelTypeID` smallint(6) NOT NULL,
  `fuelSupplyFuelTypeID` smallint(6) NOT NULL,
  `usageFraction` double DEFAULT NULL,
  PRIMARY KEY (`countyID`,`fuelYearID`,`modelYearGroupID`,`sourceBinFuelTypeID`,`fuelSupplyFuelTypeID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fuelusagefraction`
--

LOCK TABLES `fuelusagefraction` WRITE;
/*!40000 ALTER TABLE `fuelusagefraction` DISABLE KEYS */;
INSERT INTO `fuelusagefraction` VALUES (1091,2019,0,1,1,1),(1091,2019,0,2,2,1),(1091,2019,0,3,3,1),(1091,2019,0,4,4,1),(1091,2019,0,5,1,1),(1091,2019,0,5,5,0),(1091,2019,0,9,9,1);
/*!40000 ALTER TABLE `fuelusagefraction` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-10-03  9:59:32
