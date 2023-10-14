-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: stockinfo_db
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `digikey_products`
--

DROP TABLE IF EXISTS `digikey_products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `digikey_products` (
  `ProductName` varchar(255) NOT NULL,
  `ProductQuantity` int DEFAULT NULL,
  PRIMARY KEY (`ProductName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `digikey_products`
--

LOCK TABLES `digikey_products` WRITE;
/*!40000 ALTER TABLE `digikey_products` DISABLE KEYS */;
INSERT INTO `digikey_products` VALUES ('aa0402jr-0710kl',0),('ap21510fm-7',128529),('ap2151aw-7',90236),('ap2151dm8g-13',0);
/*!40000 ALTER TABLE `digikey_products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tme_products`
--

DROP TABLE IF EXISTS `tme_products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tme_products` (
  `ProductName` varchar(255) NOT NULL,
  `ProductQuantity` int DEFAULT NULL,
  PRIMARY KEY (`ProductName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tme_products`
--

LOCK TABLES `tme_products` WRITE;
/*!40000 ALTER TABLE `tme_products` DISABLE KEYS */;
INSERT INTO `tme_products` VALUES ('0105whf1000tde',19500),('aa0402jr-0710kl',9100),('ap21510fm-7',0),('ap2151aw-7',10453);
/*!40000 ALTER TABLE `tme_products` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-14  3:00:01
