-- MySQL dump 10.13  Distrib 5.7.13, for osx10.9 (x86_64)
--
-- Host: localhost    Database: devopss
-- ------------------------------------------------------
-- Server version	5.7.13

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(22,'Can add department',8,'add_department'),(23,'Can change department',8,'change_department'),(24,'Can delete department',8,'delete_department'),(28,'Can add profile',10,'add_profile'),(29,'Can change profile',10,'change_profile'),(30,'Can delete profile',10,'delete_profile');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$24000$OLdbY53BsiDr$CYysnKTeceKePmrJwmDiKxvbT+CG7dmpoxv2UdLJ+QI=','2017-04-08 02:31:09.140929',1,'admin','','','416077492@qq.com',1,1,'2017-03-19 15:05:55.674483'),(46,'pbkdf2_sha256$24000$R8zVZZ3aLGfj$GDW+AMdid9uYn2pLj7+Zvajlwyuv+TPmS76pxlS0Xxs=',NULL,0,'xiaoming','','','11@123.com',0,1,'2017-03-26 14:43:03.591794'),(47,'pbkdf2_sha256$24000$3mOVTIVNZhpI$yvoR+0yfX9LSDqg/2ul+mDhZrLL72JG+bv2A/7wEau4=',NULL,0,'xiaoming1','','','11@1234.com',0,1,'2017-03-26 14:43:59.486949'),(48,'pbkdf2_sha256$24000$nQZxNmmrGRjA$yB8z6ErKTgbV65LtS6f0rDvVvgHQ8gkmx+PrpJl5+fU=',NULL,0,'xiaoming2','','','abc@qq.com',0,1,'2017-03-26 14:44:07.821687'),(50,'pbkdf2_sha256$24000$2vO2PEBa9a26$bhyWw7XX5eWpIxWyZw5fgEMl3SNBwxhY2TSixOjte9c=',NULL,0,'xiaoming4','','','11111.@qq.com',0,1,'2017-03-26 15:05:54.757015');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `department` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `department_name_b30e3a6b_uniq` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES (3,'技术部'),(2,'运维部');
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2017-03-19 15:51:40.117661','2','xiaoming',1,'Added.',4,1),(2,'2017-03-26 14:41:17.032258','45','xiaoli',3,'',4,1),(3,'2017-03-26 14:41:17.047402','43','xiaoming',3,'',4,1),(4,'2017-03-26 14:41:17.054184','3','xiaoming1',3,'',4,1),(5,'2017-03-26 14:41:17.060733','12','xiaoming10',3,'',4,1),(6,'2017-03-26 14:41:17.065701','13','xiaoming11',3,'',4,1),(7,'2017-03-26 14:41:17.072184','14','xiaoming12',3,'',4,1),(8,'2017-03-26 14:41:17.076897','15','xiaoming13',3,'',4,1),(9,'2017-03-26 14:41:17.081825','16','xiaoming14',3,'',4,1),(10,'2017-03-26 14:41:17.088624','17','xiaoming15',3,'',4,1),(11,'2017-03-26 14:41:17.094897','18','xiaoming16',3,'',4,1),(12,'2017-03-26 14:41:17.099228','19','xiaoming17',3,'',4,1),(13,'2017-03-26 14:41:17.105511','20','xiaoming18',3,'',4,1),(14,'2017-03-26 14:41:17.113357','21','xiaoming19',3,'',4,1),(15,'2017-03-26 14:41:17.119067','4','xiaoming2',3,'',4,1),(16,'2017-03-26 14:41:17.127996','22','xiaoming20',3,'',4,1),(17,'2017-03-26 14:41:17.135324','23','xiaoming21',3,'',4,1),(18,'2017-03-26 14:41:17.142153','24','xiaoming22',3,'',4,1),(19,'2017-03-26 14:41:17.146205','25','xiaoming23',3,'',4,1),(20,'2017-03-26 14:41:17.151738','26','xiaoming24',3,'',4,1),(21,'2017-03-26 14:41:17.159592','27','xiaoming25',3,'',4,1),(22,'2017-03-26 14:41:17.164015','28','xiaoming26',3,'',4,1),(23,'2017-03-26 14:41:17.168983','29','xiaoming27',3,'',4,1),(24,'2017-03-26 14:41:17.174495','30','xiaoming28',3,'',4,1),(25,'2017-03-26 14:41:17.179514','31','xiaoming29',3,'',4,1),(26,'2017-03-26 14:41:17.187395','5','xiaoming3',3,'',4,1),(27,'2017-03-26 14:41:17.195083','32','xiaoming30',3,'',4,1),(28,'2017-03-26 14:41:17.200390','33','xiaoming31',3,'',4,1),(29,'2017-03-26 14:41:17.204574','34','xiaoming32',3,'',4,1),(30,'2017-03-26 14:41:17.208404','35','xiaoming33',3,'',4,1),(31,'2017-03-26 14:41:17.212730','36','xiaoming34',3,'',4,1),(32,'2017-03-26 14:41:17.216764','37','xiaoming35',3,'',4,1),(33,'2017-03-26 14:41:17.220643','38','xiaoming36',3,'',4,1),(34,'2017-03-26 14:41:17.225559','39','xiaoming37',3,'',4,1),(35,'2017-03-26 14:41:17.229578','40','xiaoming38',3,'',4,1),(36,'2017-03-26 14:41:17.233810','41','xiaoming39',3,'',4,1),(37,'2017-03-26 14:41:17.239402','6','xiaoming4',3,'',4,1),(38,'2017-03-26 14:41:17.243733','7','xiaoming5',3,'',4,1),(39,'2017-03-26 14:41:17.248599','8','xiaoming6',3,'',4,1),(40,'2017-03-26 14:41:17.253658','9','xiaoming7',3,'',4,1),(41,'2017-03-26 14:41:17.258845','10','xiaoming8',3,'',4,1),(42,'2017-03-26 14:41:17.264444','11','xiaoming9',3,'',4,1),(43,'2017-03-26 14:41:17.268513','44','xiaowang',3,'',4,1),(44,'2017-04-08 02:53:48.925624','1','xiaoming4',2,'Changed name.',10,1),(45,'2017-04-08 02:54:07.296625','2','xiaoming1',2,'Changed name.',10,1),(46,'2017-04-08 02:54:16.388356','3','xiaoming2',2,'Changed name.',10,1),(47,'2017-04-08 02:54:25.765911','4','xiaoming',2,'Changed name.',10,1),(48,'2017-04-08 02:54:38.622822','5','admin',2,'Changed name.',10,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(8,'users','department'),(10,'users','profile');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2017-03-19 15:04:55.686988'),(2,'auth','0001_initial','2017-03-19 15:04:56.102070'),(3,'admin','0001_initial','2017-03-19 15:04:56.182190'),(4,'admin','0002_logentry_remove_auto_add','2017-03-19 15:04:56.217076'),(5,'contenttypes','0002_remove_content_type_name','2017-03-19 15:04:56.297250'),(6,'auth','0002_alter_permission_name_max_length','2017-03-19 15:04:56.346883'),(7,'auth','0003_alter_user_email_max_length','2017-03-19 15:04:56.385309'),(8,'auth','0004_alter_user_username_opts','2017-03-19 15:04:56.402499'),(9,'auth','0005_alter_user_last_login_null','2017-03-19 15:04:56.438658'),(10,'auth','0006_require_contenttypes_0002','2017-03-19 15:04:56.441760'),(11,'auth','0007_alter_validators_add_error_messages','2017-03-19 15:04:56.455666'),(12,'sessions','0001_initial','2017-03-19 15:04:56.485534'),(13,'users','0001_initial','2017-03-26 08:50:04.946907'),(14,'users','0002_auto_20170326_1730','2017-03-26 09:30:37.458489'),(15,'users','0003_auto_20170326_2206','2017-03-26 14:07:23.964790'),(16,'users','0004_auto_20170326_2207','2017-03-26 14:07:24.001304'),(17,'users','0005_profile','2017-03-26 14:08:36.635759'),(18,'users','0006_auto_20170326_2231','2017-03-26 14:31:14.418944'),(19,'users','0007_profile','2017-03-26 14:32:27.153813'),(20,'users','0008_profile_name','2017-04-08 02:43:55.806100');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('4s37rp3stt3j4qsuqjcn86i0s8cewxem','NTczNWNhZDM1OTM4OTQxMWQ5ZDk4OTFjYjU0MDUyNzc5MWRlZThjNzp7Il9hdXRoX3VzZXJfaGFzaCI6IjFhMmNlNDU2OWM4YWY4NDFjYTkzMjBkY2RjMzhkM2I1ZGM1NjZmNmUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-04-22 02:31:09.164482'),('9701zw6i1hzflmcvlxn7nzyr9zl4xeyu','NTczNWNhZDM1OTM4OTQxMWQ5ZDk4OTFjYjU0MDUyNzc5MWRlZThjNzp7Il9hdXRoX3VzZXJfaGFzaCI6IjFhMmNlNDU2OWM4YWY4NDFjYTkzMjBkY2RjMzhkM2I1ZGM1NjZmNmUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-04-09 02:08:35.755386');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_profile`
--

DROP TABLE IF EXISTS `user_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_profile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `phone` varchar(11) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  `department_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `user_profile_department_id_fc0a31ad_fk_department_id` (`department_id`),
  CONSTRAINT `user_profile_department_id_fc0a31ad_fk_department_id` FOREIGN KEY (`department_id`) REFERENCES `department` (`id`),
  CONSTRAINT `user_profile_user_id_8fdce8e2_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_profile`
--

LOCK TABLES `user_profile` WRITE;
/*!40000 ALTER TABLE `user_profile` DISABLE KEYS */;
INSERT INTO `user_profile` VALUES (1,'12341234123','运维',3,50,'小明4'),(2,'11111111111','运维',2,47,'小明1'),(3,'11111111112','运维',2,48,'小明2'),(4,'22222222222','运维',2,46,'小明'),(5,'11111111111','运维',3,1,'管理员');
/*!40000 ALTER TABLE `user_profile` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-04-08 11:36:11
