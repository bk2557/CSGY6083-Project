CREATE DATABASE  IF NOT EXISTS `mydb` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `mydb`;
-- MySQL dump 10.13  Distrib 8.0.31, for macos12 (x86_64)
--
-- Host: 127.0.0.1    Database: mydb
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `Activity`
--

DROP TABLE IF EXISTS `Activity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Activity` (
  `idActivity` int NOT NULL AUTO_INCREMENT,
  `ActivityName` varchar(255) NOT NULL,
  `Distance` decimal(10,2) NOT NULL,
  `ElevationGain` decimal(10,2) NOT NULL,
  `ActivityDate` datetime NOT NULL,
  `idUser` int NOT NULL,
  `Addresses_idAddresses` int NOT NULL,
  `Activity_Type_idActivityType` int NOT NULL,
  `Route_Type_idRouteType` int NOT NULL,
  `Terrain_Type_idTerrain` int NOT NULL,
  `Difficulty_idDifficulty` int NOT NULL,
  PRIMARY KEY (`idActivity`),
  KEY `fk_Activity_Addresses1_idx` (`Addresses_idAddresses`),
  KEY `fk_Activity_Activity_Type1_idx` (`Activity_Type_idActivityType`),
  KEY `fk_Activity_Route_Type1_idx` (`Route_Type_idRouteType`),
  KEY `fk_Activity_Terrain_Type1_idx` (`Terrain_Type_idTerrain`),
  KEY `fk_Activity_Difficulty1_idx` (`Difficulty_idDifficulty`),
  CONSTRAINT `fk_Activity_Activity_Type1` FOREIGN KEY (`Activity_Type_idActivityType`) REFERENCES `Activity_Type` (`idActivityType`),
  CONSTRAINT `fk_Activity_Addresses1` FOREIGN KEY (`Addresses_idAddresses`) REFERENCES `Addresses` (`idAddresses`),
  CONSTRAINT `fk_Activity_Difficulty1` FOREIGN KEY (`Difficulty_idDifficulty`) REFERENCES `Difficulty` (`idDifficulty`),
  CONSTRAINT `fk_Activity_Route_Type1` FOREIGN KEY (`Route_Type_idRouteType`) REFERENCES `Route_Type` (`idRouteType`),
  CONSTRAINT `fk_Activity_Terrain_Type1` FOREIGN KEY (`Terrain_Type_idTerrain`) REFERENCES `Terrain_Type` (`idTerrain`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Activity`
--

LOCK TABLES `Activity` WRITE;
/*!40000 ALTER TABLE `Activity` DISABLE KEYS */;
INSERT INTO `Activity` VALUES (1,'Anthony\'s Nose',10.00,300.00,'2023-01-30 09:30:00',4,1,1,2,2,2),(2,'Anthony\'s Nose 2',10.00,300.00,'2023-02-14 10:55:00',2,1,1,2,2,2),(3,'other one',0.00,0.00,'2023-02-18 19:57:00',3,4,1,1,3,1),(4,'another one',10.00,300.00,'2022-06-19 12:35:00',1,2,1,3,4,3),(6,'TESTING CAPITALIZATION',134.44,560.43,'2013-03-23 23:44:22',5,5,4,3,2,1);
/*!40000 ALTER TABLE `Activity` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `upperINS` BEFORE INSERT ON `activity` FOR EACH ROW SET NEW.ActivityName = UPPER(NEW.ActivityName) */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `Activity_Type`
--

DROP TABLE IF EXISTS `Activity_Type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Activity_Type` (
  `idActivityType` int NOT NULL AUTO_INCREMENT,
  `Activity_Type_Name` varchar(255) NOT NULL,
  PRIMARY KEY (`idActivityType`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Activity_Type`
--

LOCK TABLES `Activity_Type` WRITE;
/*!40000 ALTER TABLE `Activity_Type` DISABLE KEYS */;
INSERT INTO `Activity_Type` VALUES (1,'Hike'),(2,'Thru Hike'),(3,'Section Hike'),(4,'Backpacking');
/*!40000 ALTER TABLE `Activity_Type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Addresses`
--

DROP TABLE IF EXISTS `Addresses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Addresses` (
  `idAddresses` int NOT NULL AUTO_INCREMENT,
  `idUSER` int NOT NULL,
  `line1` varchar(255) NOT NULL,
  `line2` varchar(255) DEFAULT NULL,
  `city` varchar(255) NOT NULL,
  `state` varchar(2) NOT NULL,
  `zipCD` varchar(10) NOT NULL,
  `phone` varchar(12) NOT NULL,
  `Region_idRegion` char(2) NOT NULL,
  PRIMARY KEY (`idAddresses`),
  KEY `fk_Addresses_Region_idx` (`Region_idRegion`),
  CONSTRAINT `fk_Addresses_Region` FOREIGN KEY (`Region_idRegion`) REFERENCES `Region` (`idRegion`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Addresses`
--

LOCK TABLES `Addresses` WRITE;
/*!40000 ALTER TABLE `Addresses` DISABLE KEYS */;
INSERT INTO `Addresses` VALUES (1,5,'107 Bear Mountain-Beacon Hwy','','Beacon','NY','10524','845-555-0123','NE'),(2,4,'100 Gorham Hill Rd','','Randolph','NH','03593','603-555-4567','NE'),(3,3,'321 Eldorado Springs Dr','','Boulder','CO','80303','303-555-8901','MT'),(4,2,'NF-9041','','North Bend','WA','98045','425-555-2345','NW'),(5,1,'200 Happy Isle Loop Rd','','Yosemite Valley','CA','95389','209-555-6789','SW');
/*!40000 ALTER TABLE `Addresses` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `upperINSadd` BEFORE INSERT ON `addresses` FOR EACH ROW SET NEW.state = UPPER(NEW.state) */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Temporary view structure for view `all_activities`
--

DROP TABLE IF EXISTS `all_activities`;
/*!50001 DROP VIEW IF EXISTS `all_activities`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `all_activities` AS SELECT 
 1 AS `idActivity`,
 1 AS `ActivityName`,
 1 AS `Distance`,
 1 AS `ElevationGain`,
 1 AS `ActivityDate`,
 1 AS `idUser`,
 1 AS `Addresses_idAddresses`,
 1 AS `Activity_Type_idActivityType`,
 1 AS `Route_Type_idRouteType`,
 1 AS `Terrain_Type_idTerrain`,
 1 AS `Difficulty_idDifficulty`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `Difficulty`
--

DROP TABLE IF EXISTS `Difficulty`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Difficulty` (
  `idDifficulty` int NOT NULL AUTO_INCREMENT,
  `Difficulty_Level` varchar(255) NOT NULL,
  PRIMARY KEY (`idDifficulty`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Difficulty`
--

LOCK TABLES `Difficulty` WRITE;
/*!40000 ALTER TABLE `Difficulty` DISABLE KEYS */;
INSERT INTO `Difficulty` VALUES (1,'Easy'),(2,'Moderate'),(3,'Challenging');
/*!40000 ALTER TABLE `Difficulty` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Region`
--

DROP TABLE IF EXISTS `Region`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Region` (
  `idRegion` char(2) NOT NULL,
  `RegionName` varchar(255) NOT NULL,
  PRIMARY KEY (`idRegion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Region`
--

LOCK TABLES `Region` WRITE;
/*!40000 ALTER TABLE `Region` DISABLE KEYS */;
INSERT INTO `Region` VALUES ('MT','Mountain'),('NE','North East'),('NW','Pacific North West'),('SE','South East'),('SW','South West');
/*!40000 ALTER TABLE `Region` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Route_Type`
--

DROP TABLE IF EXISTS `Route_Type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Route_Type` (
  `idRouteType` int NOT NULL AUTO_INCREMENT,
  `Route_Name` varchar(255) NOT NULL,
  PRIMARY KEY (`idRouteType`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Route_Type`
--

LOCK TABLES `Route_Type` WRITE;
/*!40000 ALTER TABLE `Route_Type` DISABLE KEYS */;
INSERT INTO `Route_Type` VALUES (1,'One Way'),(2,'Out and Back'),(3,'Loop');
/*!40000 ALTER TABLE `Route_Type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Terrain_Type`
--

DROP TABLE IF EXISTS `Terrain_Type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Terrain_Type` (
  `idTerrain` int NOT NULL AUTO_INCREMENT,
  `Terrian_Name` varchar(255) NOT NULL,
  PRIMARY KEY (`idTerrain`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Terrain_Type`
--

LOCK TABLES `Terrain_Type` WRITE;
/*!40000 ALTER TABLE `Terrain_Type` DISABLE KEYS */;
INSERT INTO `Terrain_Type` VALUES (1,'Hills'),(2,'Mountains'),(3,'Rivers'),(4,'Lakes');
/*!40000 ALTER TABLE `Terrain_Type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User` (
  `idUser` int NOT NULL AUTO_INCREMENT,
  `FirstName` varchar(255) NOT NULL,
  `LastName` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `Address` int DEFAULT NULL,
  `Addresses_idAddresses` int NOT NULL,
  PRIMARY KEY (`idUser`),
  UNIQUE KEY `email_UNIQUE` (`email`),
  KEY `fk_User_Addresses1_idx` (`Addresses_idAddresses`),
  CONSTRAINT `fk_User_Addresses1` FOREIGN KEY (`Addresses_idAddresses`) REFERENCES `Addresses` (`idAddresses`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (1,'Jyn','Erso','deathstars@gmail.com',1,1),(2,'Jon','Rambo','ramboooooo@yahoo.com',2,2),(3,'Snake','Plissken','snekysnek@aol.com',3,3),(4,'Lara','Croft','raid_yo_tomb@netscape.net',4,4),(5,'Indiana','Jones','indyjr@hotmail.com',5,5);
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User_Activities`
--

DROP TABLE IF EXISTS `User_Activities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User_Activities` (
  `User_idUser` int NOT NULL,
  `Activity_idActivity` int NOT NULL,
  `Activity_Activity Type_idActivity Type` int NOT NULL,
  `Activity_Route Type_idRoute Type` int NOT NULL,
  `Activity_Terrain Type_idTerrain` int NOT NULL,
  `Activity_Difficulty_idDifficulty` int NOT NULL,
  PRIMARY KEY (`User_idUser`,`Activity_idActivity`,`Activity_Activity Type_idActivity Type`,`Activity_Route Type_idRoute Type`,`Activity_Terrain Type_idTerrain`,`Activity_Difficulty_idDifficulty`),
  KEY `fk_User_has_Activity_Activity1_idx` (`Activity_idActivity`,`Activity_Activity Type_idActivity Type`,`Activity_Route Type_idRoute Type`,`Activity_Terrain Type_idTerrain`,`Activity_Difficulty_idDifficulty`),
  KEY `fk_User_has_Activity_User1_idx` (`User_idUser`),
  CONSTRAINT `fk_User_has_Activity_Activity1` FOREIGN KEY (`Activity_idActivity`) REFERENCES `Activity` (`idActivity`),
  CONSTRAINT `fk_User_has_Activity_User1` FOREIGN KEY (`User_idUser`) REFERENCES `User` (`idUser`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User_Activities`
--

LOCK TABLES `User_Activities` WRITE;
/*!40000 ALTER TABLE `User_Activities` DISABLE KEYS */;
/*!40000 ALTER TABLE `User_Activities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `wordstab`
--

DROP TABLE IF EXISTS `wordstab`;
/*!50001 DROP VIEW IF EXISTS `wordstab`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `wordstab` AS SELECT 
 1 AS `idActivity`,
 1 AS `ActivityName`,
 1 AS `Distance`,
 1 AS `ElevationGain`,
 1 AS `activity_date`,
 1 AS `activity_time`,
 1 AS `UserID`,
 1 AS `FirstName`,
 1 AS `LastName`,
 1 AS `ActivityType`,
 1 AS `RouteType`,
 1 AS `TerrainType`,
 1 AS `Difficulty`*/;
SET character_set_client = @saved_cs_client;

--
-- Dumping events for database 'mydb'
--

--
-- Dumping routines for database 'mydb'
--
/*!50003 DROP FUNCTION IF EXISTS `totalElevation` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` FUNCTION `totalElevation`(
		userID INT
) RETURNS decimal(10,2)
BEGIN
	-- declare output variable
	DECLARE total_elevation DECIMAL(10,2);
    
    -- select results
    SELECT SUM(ElevationGain) 
    INTO total_elevation
    FROM Activity 
    WHERE Activity.idUser = userID;
    
    RETURN(total_elevation);
    
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `totalMileage` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` FUNCTION `totalMileage`(
		userID INT
) RETURNS decimal(10,2)
BEGIN
	-- declare output variable
	DECLARE total_miles DECIMAL(10,2);
    
    -- select results
    SELECT SUM(Distance) 
    INTO total_miles 
    FROM Activity 
    WHERE Activity.idUser = userID;
    
    RETURN(total_miles);
    
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `allMetrics` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `allMetrics`()
BEGIN
    -- select results
    SELECT FirstName, LastName, SUM(ElevationGain) AS total_elevation, SUM(Distance) AS total_mileage
    -- INTO total_elevation
    FROM wordsTAB 
    GROUP BY FirstName, LastName;
    
    
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `metricsByUser` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `metricsByUser`(userID INT)
BEGIN

    -- select results
    SELECT FirstName, LastName, SUM(ElevationGain) AS total_elevation, SUM(Distance) AS total_mileage
    -- INTO total_elevation
    FROM wordsTAB 
    WHERE wordsTAB.UserID = userID
    GROUP BY FirstName, LastName;
    
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Final view structure for view `all_activities`
--

/*!50001 DROP VIEW IF EXISTS `all_activities`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `all_activities` AS select `activity`.`idActivity` AS `idActivity`,`activity`.`ActivityName` AS `ActivityName`,`activity`.`Distance` AS `Distance`,`activity`.`ElevationGain` AS `ElevationGain`,`activity`.`ActivityDate` AS `ActivityDate`,`activity`.`idUser` AS `idUser`,`activity`.`Addresses_idAddresses` AS `Addresses_idAddresses`,`activity`.`Activity_Type_idActivityType` AS `Activity_Type_idActivityType`,`activity`.`Route_Type_idRouteType` AS `Route_Type_idRouteType`,`activity`.`Terrain_Type_idTerrain` AS `Terrain_Type_idTerrain`,`activity`.`Difficulty_idDifficulty` AS `Difficulty_idDifficulty` from `activity` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `wordstab`
--

/*!50001 DROP VIEW IF EXISTS `wordstab`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `wordstab` AS select `activity`.`idActivity` AS `idActivity`,`activity`.`ActivityName` AS `ActivityName`,`activity`.`Distance` AS `Distance`,`activity`.`ElevationGain` AS `ElevationGain`,date_format(cast(`activity`.`ActivityDate` as date),'%b-%d-%Y') AS `activity_date`,date_format(`activity`.`ActivityDate`,'%l:%i %p') AS `activity_time`,`user`.`idUser` AS `UserID`,`user`.`FirstName` AS `FirstName`,`user`.`LastName` AS `LastName`,`activity_type`.`Activity_Type_Name` AS `ActivityType`,`route_type`.`Route_Name` AS `RouteType`,`terrain_type`.`Terrian_Name` AS `TerrainType`,`difficulty`.`Difficulty_Level` AS `Difficulty` from ((((((`activity` join `user` on((`activity`.`idUser` = `user`.`idUser`))) join `addresses` on((`activity`.`idUser` = `addresses`.`idAddresses`))) join `activity_type` on((`activity`.`Activity_Type_idActivityType` = `activity_type`.`idActivityType`))) join `route_type` on((`activity`.`Route_Type_idRouteType` = `route_type`.`idRouteType`))) join `terrain_type` on((`activity`.`Terrain_Type_idTerrain` = `terrain_type`.`idTerrain`))) join `difficulty` on((`activity`.`Difficulty_idDifficulty` = `difficulty`.`idDifficulty`))) order by `activity`.`idActivity` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-01  0:56:30
