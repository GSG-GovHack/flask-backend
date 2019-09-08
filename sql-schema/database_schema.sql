-- --------------------------------------------------------
-- Host:                         10.0.0.4
-- Server version:               10.1.41-MariaDB-0ubuntu0.18.04.1 - Ubuntu 18.04
-- Server OS:                    debian-linux-gnueabihf
-- HeidiSQL Version:             10.2.0.5599
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for instaplace
CREATE DATABASE IF NOT EXISTS `instaplace` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `instaplace`;

-- Dumping structure for table instaplace.animal_sightings
CREATE TABLE IF NOT EXISTS `animal_sightings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` datetime NOT NULL,
  `lat` decimal(10,6) NOT NULL DEFAULT '0.000000',
  `lon` decimal(10,6) NOT NULL DEFAULT '0.000000',
  `animal_type` text NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Data exporting was unselected.

-- Dumping structure for table instaplace.pois
CREATE TABLE IF NOT EXISTS `pois` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `poi_type` varchar(5) NOT NULL DEFAULT 'UNKWN',
  `poi_name` char(50) NOT NULL DEFAULT '0',
  `lat` decimal(10,6) NOT NULL DEFAULT '0.000000',
  `lon` decimal(10,6) NOT NULL DEFAULT '0.000000',
  `time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  UNIQUE KEY `id_unq` (`id`),
  KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- Data exporting was unselected.

-- Dumping structure for table instaplace.search_cache
CREATE TABLE IF NOT EXISTS `search_cache` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `search_query` text,
  `json_data` longtext,
  `search_url` varchar(191) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `search_url` (`search_url`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- Data exporting was unselected.

-- Dumping structure for table instaplace.test_table
CREATE TABLE IF NOT EXISTS `test_table` (
  `id` int(11) DEFAULT NULL,
  `name` char(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Data exporting was unselected.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
