-- MySQL dump 10.13  Distrib 5.7.18, for Win64 (x86_64)
--
-- Host: localhost    Database: testdb
-- ------------------------------------------------------
-- Server version	5.7.18-log

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
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
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
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add privilege',7,'add_privilege'),(26,'Can change privilege',7,'change_privilege'),(27,'Can delete privilege',7,'delete_privilege'),(28,'Can view privilege',7,'view_privilege'),(29,'Can add user',8,'add_user'),(30,'Can change user',8,'change_user'),(31,'Can delete user',8,'delete_user'),(32,'Can view user',8,'view_user'),(33,'Can add product',9,'add_product'),(34,'Can change product',9,'change_product'),(35,'Can delete product',9,'delete_product'),(36,'Can view product',9,'view_product'),(37,'Can add status',10,'add_status'),(38,'Can change status',10,'change_status'),(39,'Can delete status',10,'delete_status'),(40,'Can view status',10,'view_status'),(41,'Can add test case',11,'add_testcase'),(42,'Can change test case',11,'change_testcase'),(43,'Can delete test case',11,'delete_testcase'),(44,'Can view test case',11,'view_testcase'),(45,'Can add case module',12,'add_casemodule'),(46,'Can change case module',12,'change_casemodule'),(47,'Can delete case module',12,'delete_casemodule'),(48,'Can view case module',12,'view_casemodule'),(49,'Can add script',13,'add_script'),(50,'Can change script',13,'change_script'),(51,'Can delete script',13,'delete_script'),(52,'Can view script',13,'view_script'),(53,'Can add script type',14,'add_scripttype'),(54,'Can change script type',14,'change_scripttype'),(55,'Can delete script type',14,'delete_scripttype'),(56,'Can view script type',14,'view_scripttype'),(57,'Can add suit case mapping',15,'add_suitcasemapping'),(58,'Can change suit case mapping',15,'change_suitcasemapping'),(59,'Can delete suit case mapping',15,'delete_suitcasemapping'),(60,'Can view suit case mapping',15,'view_suitcasemapping'),(61,'Can add test suite',16,'add_testsuite'),(62,'Can change test suite',16,'change_testsuite'),(63,'Can delete test suite',16,'delete_testsuite'),(64,'Can view test suite',16,'view_testsuite'),(65,'Can add suit product mapping',17,'add_suitproductmapping'),(66,'Can change suit product mapping',17,'change_suitproductmapping'),(67,'Can delete suit product mapping',17,'delete_suitproductmapping'),(68,'Can view suit product mapping',17,'view_suitproductmapping'),(69,'Can add task status',18,'add_taskstatus'),(70,'Can change task status',18,'change_taskstatus'),(71,'Can delete task status',18,'delete_taskstatus'),(72,'Can view task status',18,'view_taskstatus'),(73,'Can add test task',19,'add_testtask'),(74,'Can change test task',19,'change_testtask'),(75,'Can delete test task',19,'delete_testtask'),(76,'Can view test task',19,'view_testtask'),(77,'Can add result',20,'add_result'),(78,'Can change result',20,'change_result'),(79,'Can delete result',20,'delete_result'),(80,'Can view result',20,'view_result'),(81,'Can add task suite mapping',21,'add_tasksuitemapping'),(82,'Can change task suite mapping',21,'change_tasksuitemapping'),(83,'Can delete task suite mapping',21,'delete_tasksuitemapping'),(84,'Can view task suite mapping',21,'view_tasksuitemapping'),(85,'Can add test result type',22,'add_testresulttype'),(86,'Can change test result type',22,'change_testresulttype'),(87,'Can delete test result type',22,'delete_testresulttype'),(88,'Can view test result type',22,'view_testresulttype'),(89,'Can add product type',23,'add_producttype'),(90,'Can change product type',23,'change_producttype'),(91,'Can delete product type',23,'delete_producttype'),(92,'Can view product type',23,'view_producttype'),(93,'Can add cached task',24,'add_cachedtask'),(94,'Can change cached task',24,'change_cachedtask'),(95,'Can delete cached task',24,'delete_cachedtask'),(96,'Can view cached task',24,'view_cachedtask');
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
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$120000$oWkUreWWOJT8$JPH7oMa4e9p+vOnzjTKQiFdCz30E/m2MEPOTxbW7AM0=','2018-09-12 09:38:43.848536',1,'admin','','','',1,1,'2018-09-11 06:17:04.977234');
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
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
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
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
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
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2018-09-11 06:17:56.322211','2','User object (2)',1,'[{\"added\": {}}]',8,1),(2,'2018-09-11 06:18:14.254264','3','User object (3)',1,'[{\"added\": {}}]',8,1),(3,'2018-09-11 06:18:35.121395','4','User object (4)',1,'[{\"added\": {}}]',8,1),(4,'2018-09-11 08:06:07.201086','1','Product object (1)',1,'[{\"added\": {}}]',9,1),(5,'2018-09-11 08:06:29.935784','2','Product object (2)',1,'[{\"added\": {}}]',9,1),(6,'2018-09-11 08:06:33.473327','2','Product object (2)',2,'[]',9,1),(7,'2018-09-11 08:07:05.543056','3','Product object (3)',1,'[{\"added\": {}}]',9,1),(8,'2018-09-11 08:07:27.461690','4','Product object (4)',1,'[{\"added\": {}}]',9,1),(9,'2018-09-11 08:07:28.816489','4','Product object (4)',2,'[]',9,1),(10,'2018-09-11 08:07:43.280754','5','Product object (5)',1,'[{\"added\": {}}]',9,1),(11,'2018-09-11 09:33:17.038726','1','Status object (1)',1,'[{\"added\": {}}]',10,1),(12,'2018-09-11 09:33:23.007112','2','Status object (2)',1,'[{\"added\": {}}]',10,1),(13,'2018-09-11 09:33:39.106019','3','Status object (3)',1,'[{\"added\": {}}]',10,1),(14,'2018-09-11 09:34:00.153609','1','Status object (1)',2,'[{\"changed\": {\"fields\": [\"status\", \"desc\"]}}]',10,1),(15,'2018-09-11 09:34:43.113787','2','Status object (2)',2,'[{\"changed\": {\"fields\": [\"status\", \"desc\"]}}]',10,1),(16,'2018-09-11 09:35:10.973843','4','Status object (4)',1,'[{\"added\": {}}]',10,1),(17,'2018-09-14 02:39:30.089743','1','CaseModule object (1)',1,'[{\"added\": {}}]',12,1),(18,'2018-09-14 02:39:52.474037','2','CaseModule object (2)',1,'[{\"added\": {}}]',12,1),(19,'2018-09-14 02:40:24.379364','3','CaseModule object (3)',1,'[{\"added\": {}}]',12,1),(20,'2018-09-14 02:40:50.465073','4','CaseModule object (4)',1,'[{\"added\": {}}]',12,1),(21,'2018-09-14 02:45:48.331333','1','TestCase object (1)',1,'[{\"added\": {}}]',11,1),(22,'2018-09-14 02:50:23.210812','2','TestCase object (2)',1,'[{\"added\": {}}]',11,1),(23,'2018-09-14 02:52:07.019847','3','TestCase object (3)',1,'[{\"added\": {}}]',11,1),(24,'2018-09-14 03:00:10.312444','4','TestCase object (4)',1,'[{\"added\": {}}]',11,1),(25,'2018-09-14 03:03:15.237424','5','TestCase object (5)',1,'[{\"added\": {}}]',11,1),(26,'2018-09-14 03:03:43.083910','6','TestCase object (6)',1,'[{\"added\": {}}]',11,1),(27,'2018-09-14 03:06:21.490325','7','TestCase object (7)',1,'[{\"added\": {}}]',11,1),(28,'2018-09-14 03:07:01.117215','8','TestCase object (8)',1,'[{\"added\": {}}]',11,1),(29,'2018-09-14 03:07:27.888292','9','TestCase object (9)',1,'[{\"added\": {}}]',11,1),(30,'2018-09-14 03:07:46.393436','10','TestCase object (10)',1,'[{\"added\": {}}]',11,1),(31,'2018-09-14 06:48:05.960908','4','TestCase object (4)',2,'[{\"changed\": {\"fields\": [\"title\"]}}]',11,1),(32,'2018-09-14 06:48:08.147193','4','TestCase object (4)',2,'[]',11,1),(33,'2018-09-14 06:48:13.912722','5','TestCase object (5)',2,'[{\"changed\": {\"fields\": [\"title\"]}}]',11,1),(34,'2018-09-14 06:48:18.460499','6','TestCase object (6)',2,'[{\"changed\": {\"fields\": [\"title\"]}}]',11,1),(35,'2018-09-14 06:48:27.344901','7','TestCase object (7)',2,'[{\"changed\": {\"fields\": [\"title\"]}}]',11,1),(36,'2018-09-14 06:48:32.862232','8','TestCase object (8)',2,'[{\"changed\": {\"fields\": [\"title\"]}}]',11,1),(37,'2018-09-14 06:48:37.533845','9','TestCase object (9)',2,'[{\"changed\": {\"fields\": [\"title\"]}}]',11,1),(38,'2018-09-14 06:48:42.732027','10','TestCase object (10)',2,'[{\"changed\": {\"fields\": [\"title\"]}}]',11,1),(39,'2018-09-29 11:48:44.144761','1','TestSuite object (1)',1,'[{\"added\": {}}]',16,1),(40,'2018-09-29 11:48:58.707665','2','TestSuite object (2)',1,'[{\"added\": {}}]',16,1),(41,'2018-09-29 11:49:29.452339','3','TestSuite object (3)',1,'[{\"added\": {}}]',16,1),(42,'2018-09-29 11:52:41.748988','1','SuitCaseMapping object (1)',1,'[{\"added\": {}}]',15,1),(43,'2018-10-08 08:35:17.687356','1','ScriptType object (1)',1,'[{\"added\": {}}]',14,1),(44,'2018-10-08 08:35:27.986547','2','ScriptType object (2)',1,'[{\"added\": {}}]',14,1),(45,'2018-10-08 08:35:36.703309','3','ScriptType object (3)',1,'[{\"added\": {}}]',14,1),(46,'2018-10-08 08:36:24.751234','4','ScriptType object (4)',1,'[{\"added\": {}}]',14,1),(47,'2018-10-08 08:36:34.259454','5','ScriptType object (5)',1,'[{\"added\": {}}]',14,1),(48,'2018-10-09 11:38:27.794090','11','TestCase object (11)',1,'[{\"added\": {}}]',11,1),(49,'2018-10-09 11:39:40.189379','12','TestCase object (12)',1,'[{\"added\": {}}]',11,1);
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
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(9,'product','product'),(23,'product','producttype'),(10,'product','status'),(17,'product','suitproductmapping'),(13,'script','script'),(14,'script','scripttype'),(6,'sessions','session'),(24,'task','cachedtask'),(20,'task','result'),(18,'task','taskstatus'),(21,'task','tasksuitemapping'),(22,'task','testresulttype'),(19,'task','testtask'),(12,'testcase','casemodule'),(15,'testcase','suitcasemapping'),(11,'testcase','testcase'),(16,'testcase','testsuite'),(7,'user','privilege'),(8,'user','user');
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
)
  ENGINE = InnoDB
  AUTO_INCREMENT = 54
  DEFAULT CHARSET = utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2018-09-14 02:35:21.417064'),
  (2, 'auth', '0001_initial', '2018-09-14 02:35:21.426089'), (3, 'admin', '0001_initial', '2018-09-14 02:35:21.430585'),
  (4, 'admin', '0002_logentry_remove_auto_add', '2018-09-14 02:35:21.436573'),
  (5, 'admin', '0003_logentry_add_action_flag_choices', '2018-09-14 02:35:21.441586'),
  (6, 'contenttypes', '0002_remove_content_type_name', '2018-09-14 02:35:21.446634'),
  (7, 'auth', '0002_alter_permission_name_max_length', '2018-09-14 02:35:21.453767'),
  (8, 'auth', '0003_alter_user_email_max_length', '2018-09-14 02:35:21.458196'),
  (9, 'auth', '0004_alter_user_username_opts', '2018-09-14 02:35:21.462772'),
  (10, 'auth', '0005_alter_user_last_login_null', '2018-09-14 02:35:21.468794'),
  (11, 'auth', '0006_require_contenttypes_0002', '2018-09-14 02:35:21.473802'),
  (12, 'auth', '0007_alter_validators_add_error_messages', '2018-09-14 02:35:21.478817'),
  (13, 'auth', '0008_alter_user_username_max_length', '2018-09-14 02:35:21.483829'),
  (14, 'auth', '0009_alter_user_last_name_max_length', '2018-09-14 02:35:21.490368'),
  (15, 'product', '0001_initial', '2018-09-14 02:35:21.494378'),
  (16, 'product', '0002_auto_20180911_1615', '2018-09-14 02:35:21.499402'),
  (17, 'product', '0003_product_status', '2018-09-14 02:35:21.506441'),
  (18, 'product', '0004_auto_20180912_1421', '2018-09-14 02:35:21.510452'),
  (19, 'product', '0005_auto_20180914_1021', '2018-09-14 02:35:21.514484'),
  (20, 'sessions', '0001_initial', '2018-09-14 02:35:21.522484'),
  (21, 'user', '0001_initial', '2018-09-14 02:35:21.527497'),
  (22, 'user', '0002_auto_20180910_1654', '2018-09-14 02:35:21.531507'),
  (23, 'testcase', '0001_initial', '2018-09-14 02:36:13.405621'),
  (24, 'testcase', '0002_auto_20180914_1042', '2018-09-14 02:42:48.218609'),
  (25, 'testcase', '0003_auto_20180919_1557', '2018-09-19 07:57:23.862907'),
  (26, 'testcase', '0004_auto_20180919_1726', '2018-09-19 09:26:51.339110'),
  (27, 'script', '0001_initial', '2018-09-20 09:14:49.354937'),
  (28, 'script', '0002_auto_20180921_0858', '2018-09-21 00:58:35.689544'),
  (29, 'testcase', '0003_auto_20180919_2226', '2018-09-21 00:58:35.700503'),
  (30, 'testcase', '0005_merge_20180920_2243', '2018-09-21 00:58:35.705346'),
  (31, 'script', '0002_auto_20180923_1818', '2018-09-29 11:41:35.738963'),
  (32, 'script', '0003_suitcasemapping_testsuite', '2018-09-29 11:41:35.799638'),
  (33, 'script', '0004_auto_20180929_1753', '2018-09-29 11:41:35.828715'),
  (34, 'script', '0005_merge_20180929_1941', '2018-09-29 11:41:35.833970'),
  (35, 'testcase', '0006_suitcasemapping_testsuite', '2018-09-29 11:41:35.897152'),
  (36, 'testcase', '0007_auto_20180929_1954', '2018-09-29 11:54:38.082641'),
  (37, 'product', '0006_suitproductmapping', '2018-10-08 08:03:36.693247'),
  (38, 'task', '0001_initial', '2018-10-08 08:03:36.754508'),
  (39, 'testcase', '0008_auto_20181008_1603', '2018-10-08 08:03:37.111077'),
  (40, 'task', '0002_remove_testtask_test_times', '2018-10-29 03:58:02.731495'),
  (41, 'task', '0003_auto_20181101_0957', '2018-11-01 01:58:02.587666'),
  (42, 'user', '0003_user_real_name', '2018-11-01 02:25:44.513232'),
  (43, 'task', '0004_auto_20181101_1427', '2018-11-01 06:27:28.133764'),
  (44, 'task', '0005_auto_20181105_1651', '2018-11-05 08:52:40.413150'),
  (45, 'task', '0006_testtask_last_run_user', '2018-11-06 02:31:21.643439'),
  (46, 'task', '0007_auto_20181106_1121', '2018-11-06 03:22:07.987699'),
  (47, 'task', '0008_auto_20181106_1743', '2018-11-06 09:44:08.415282'),
  (48, 'product', '0007_auto_20181107_1430', '2018-11-07 06:30:42.207704'),
  (49, 'task', '0009_cachedtask', '2018-11-08 06:54:13.759181'),
  (50, 'testcase', '0009_auto_20181108_1454', '2018-11-08 06:54:13.905402'),
  (51, 'task', '0010_auto_20181108_1544', '2018-11-08 07:45:08.094552'),
  (52, 'task', '0011_auto_20181108_1649', '2018-11-08 08:49:40.721737'),
  (53, 'testcase', '0010_auto_20181115_1644', '2018-11-15 08:44:12.718299');
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
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('36zo1koziry7abqkrwvv84u2crk4k072',
                                     'ZGNiODA0MDZmODE1N2I2NmMwODdjZmY0NzBjZTQ2OTM2MzY4NmUwZDp7InVzZXIiOiJhZG1pbiIsImN1cnJlbnRfY2FzZV9pZCI6MX0=',
                                     '2018-10-02 10:03:32.153489'), ('3ymzwuxs7ojdn72i5qim6lesa7mwpwsh',
                                                                     'MjRmNDIwODYzNDA4OWFhYmM3MWQ5OTRhMWNmMjg1ZTU1NWI4OTQwNTp7InVzZXIiOiJhZG1pbiIsImNhc2VfaWQiOjR9',
                                                                     '2018-11-29 08:04:33.040428'),
  ('dsqn0ioomz1s282oagoq4gv7rgafg45o', 'M2UzODQ5NDA0ZDMwZGY4ZTMwMDJhMGJmMjUzOTJjYWRmZWZiMWNiZTp7InVzZXIiOiJhZG1pbiJ9',
   '2018-11-22 11:58:56.662167'), ('myp1axwbo5kclxfjv9h840b9c5h9p61g',
                                   'ZjI1MTk1NWFlMjY1MmJiMTY3N2FhNGQ4MTlkM2M0ODVlMGQyMmE4MTp7InVzZXIiOiJhZG1pbiIsImNhc2VfaWQiOjJ9',
                                   '2018-11-26 07:02:11.341818'), ('s1yneeozx15k0sm8mnuo44cjtl1b8ce9',
                                                                   'ZjI1MTk1NWFlMjY1MmJiMTY3N2FhNGQ4MTlkM2M0ODVlMGQyMmE4MTp7InVzZXIiOiJhZG1pbiIsImNhc2VfaWQiOjJ9',
                                                                   '2018-11-23 09:22:08.947270'),
  ('wgixk0hhp4yvmkigocq2y9cpzub8bpda', 'M2UzODQ5NDA0ZDMwZGY4ZTMwMDJhMGJmMjUzOTJjYWRmZWZiMWNiZTp7InVzZXIiOiJhZG1pbiJ9',
   '2018-11-27 01:57:52.631513'), ('xo3k9hwajotn29bzzyqw3jkwulmrbesw',
                                   'YTA1NGNlYzgzYmVjYjdmZmQyOTg5YmRjNTM0MDg5Y2Q5Yzc3M2VjMTp7InVzZXIiOiJhZG1pbiIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwM2QxOGRmYmM4YjhmMWNmOWVjOGJlOTNlZTk3YzM4ODk0MmU0N2QxIn0=',
                                   '2018-09-25 06:17:29.157499');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_product`
--

DROP TABLE IF EXISTS `product_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `inChargeUser` int(11) NOT NULL,
  `createUser` int(11) NOT NULL,
  `createTime` date NOT NULL,
  `desc` longtext NOT NULL,
  `status` int(11) NOT NULL,
  `manager` varchar(50) NOT NULL,
  `productType` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_product`
--

LOCK TABLES `product_product` WRITE;
/*!40000 ALTER TABLE `product_product` DISABLE KEYS */;
INSERT INTO `product_product` VALUES (1,'UI自动化项目',2,2,'2018-09-11','UI自动化项目，用于进行信息化项目的UI自动化测试',1,'暂无',2),(2,'接口自动化',2,2,'2018-09-11','用于进行信息化项目的接口自动化测试',1,'暂无',2),(3,'自动化测试平台',2,2,'2018-09-11','用户进行自动化测试的相关功能建设',1,'暂无',2),(4,'跑得快',3,3,'2018-09-11','跑的快游戏项目',1,'暂无',5),(5,'斗地主',3,3,'2018-09-11','斗地主单机项目',1,'暂无',5);
/*!40000 ALTER TABLE `product_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_producttype`
--

DROP TABLE IF EXISTS `product_producttype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product_producttype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_producttype`
--

LOCK TABLES `product_producttype` WRITE;
/*!40000 ALTER TABLE `product_producttype` DISABLE KEYS */;
INSERT INTO `product_producttype` VALUES (1,'API自动化'),(2,'WEB自动化'),(3,'Android自动化'),(4,'IOS自动化'),(5,'Unity自动化');
/*!40000 ALTER TABLE `product_producttype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_status`
--

DROP TABLE IF EXISTS `product_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product_status` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` varchar(40) NOT NULL,
  `desc` longtext NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `status` (`status`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_status`
--

LOCK TABLES `product_status` WRITE;
/*!40000 ALTER TABLE `product_status` DISABLE KEYS */;
INSERT INTO `product_status` VALUES (1,'正常','产品处于正常研发状态'),(2,'延期','产品目前被延期'),(3,'中止','产品被中止'),(4,'完成','产品已经被完成');
/*!40000 ALTER TABLE `product_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_suitproductmapping`
--

DROP TABLE IF EXISTS `product_suitproductmapping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product_suitproductmapping` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product` int(11) NOT NULL,
  `suit` int(11) NOT NULL,
  PRIMARY KEY (`id`)
)
  ENGINE = InnoDB
  AUTO_INCREMENT = 5
  DEFAULT CHARSET = utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_suitproductmapping`
--

LOCK TABLES `product_suitproductmapping` WRITE;
/*!40000 ALTER TABLE `product_suitproductmapping` DISABLE KEYS */;
INSERT INTO `product_suitproductmapping` VALUES (1, 1, 5), (2, 2, 5), (3, 1, 4), (4, 2, 4);
/*!40000 ALTER TABLE `product_suitproductmapping` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `script_script`
--

DROP TABLE IF EXISTS `script_script`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `script_script` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `desc` varchar(255) DEFAULT NULL,
  `path` varchar(100) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `create_user` int(11) NOT NULL,
  `run_count` int(11) NOT NULL,
  `last_run_time` datetime(6) DEFAULT NULL,
  `related_case` int(11) DEFAULT NULL,
  `last_edit_time` datetime(6) NOT NULL,
  `last_edit_user` int(11) DEFAULT NULL,
  `script_type` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `script_script`
--

LOCK TABLES `script_script` WRITE;
/*!40000 ALTER TABLE `script_script` DISABLE KEYS */;
INSERT INTO `script_script` VALUES (1,'一个测试百度的脚本','WEB自动化\\TestBaidu1539222138766.py','2018-10-11 01:42:18.772704',1,0,NULL,7,'2018-10-11 01:42:18.772704',1,2,'TestBaidu.py'),(2,'无描述','WEB自动化\\TestBaidu1539222737992.py','2018-10-11 01:52:17.997147',1,0,NULL,3,'2018-10-11 01:52:17.997147',1,2,'TestBaidu.py');
/*!40000 ALTER TABLE `script_script` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `script_scripttype`
--

DROP TABLE IF EXISTS `script_scripttype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `script_scripttype` (
  `desc` varchar(255) DEFAULT NULL,
  `name` varchar(20) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `script_scripttype`
--

LOCK TABLES `script_scripttype` WRITE;
/*!40000 ALTER TABLE `script_scripttype` DISABLE KEYS */;
INSERT INTO `script_scripttype` VALUES ('API自动化','API自动化',1),('WEB自动化','WEB自动化',2),('API自动化','API自动化',3),('通用Setup','通用Setup',4),('通用TearDown','通用TearDown',5);
/*!40000 ALTER TABLE `script_scripttype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `task_cachedtask`
--

DROP TABLE IF EXISTS `task_cachedtask`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `task_cachedtask` (
  `task_id` int(11) NOT NULL,
  `async_result_id` varchar(255) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  PRIMARY KEY (`task_id`),
  UNIQUE KEY `task_cachedtask_task_id_bbc42b29_uniq` (`task_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `task_cachedtask`
--

LOCK TABLES `task_cachedtask` WRITE;
/*!40000 ALTER TABLE `task_cachedtask` DISABLE KEYS */;
INSERT INTO `task_cachedtask` VALUES (2,'24df4c8e-6126-48e7-8c10-944e947e39dc','2018-11-09 02:11:36.269125'),(3,'b2293c34-716f-4ed9-ac60-2b250f63e0a3','2018-11-09 05:47:17.987384');
/*!40000 ALTER TABLE `task_cachedtask` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `task_result`
--

DROP TABLE IF EXISTS `task_result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `task_result` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `report_title` varchar(100) NOT NULL,
  `log_title` varchar(100) NOT NULL,
  `task` int(11) NOT NULL,
  `result` int(11) NOT NULL,
  `run_time` datetime(6) NOT NULL,
  `run_user` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=98 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `task_result`
--

LOCK TABLES `task_result` WRITE;
/*!40000 ALTER TABLE `task_result` DISABLE KEYS */;
INSERT INTO `task_result` VALUES (1,'Test Result','测试任务1，添加于11_11541404239548627.2.log',2,1,'2018-11-06 03:22:07.841416',1),(2,'Test Result','测试任务1，添加于11_11541404866286642.8.log',2,1,'2018-11-06 03:22:07.841416',1),(3,'Test Result','测试任务1，添加于11_11541404867805681.8.log',2,1,'2018-11-06 03:22:07.841416',2),(4,'Test Result','测试任务1，添加于11_11541404864583223.5.log',2,1,'2018-11-06 03:22:07.841416',3),(5,'Test Result','测试任务1，添加于11_11541405384335169.5.log',2,1,'2018-11-06 03:22:07.841416',1),(6,'Test Result','测试任务1，添加于11_11541405700135618.2.log',2,1,'2018-11-06 03:22:07.841416',2),(7,'Test Result','测试任务1，添加于11_11541406025061924.0.log',2,1,'2018-11-06 03:22:07.841416',3),(8,'Test Result','测试任务1，添加于11_11541406290274968.5.log',2,1,'2018-11-06 03:22:07.841416',1),(9,'Test Result','测试任务1，添加于11_11541406458718920.2.log',2,2,'2018-11-06 03:22:07.841416',2),(10,'Test Result','测试任务1，添加于11_11541406635296766.5.log',2,4,'2018-11-06 03:22:07.841416',1),(11,'Test Result','测试任务1，添加于11_11541406789576251.5.log',2,3,'2018-11-06 03:22:07.841416',3),(12,'Test_TestBaidu1539222138766.CollectProjects_2018-11-06_16-39-03.html','测试任务1，添加于11_11541493543636869.5.log',2,1,'2018-11-06 08:39:20.912998',1),(13,'Test_TestBaidu1539222138766.CollectProjects_2018-11-06_17-25-49.html','测试任务1，添加于11_11541496346597857.0.log',2,1,'2018-11-06 09:26:07.006374',1),(14,'Test_TestBaidu1539222138766.CollectProjects_2018-11-06_17-31-58.html','测试任务1，添加于11_11541496715627538.5.log',2,1,'2018-11-06 09:32:15.776255',1),(15,'Test_TestBaidu1539222138766.CollectProjects_2018-11-06_17-38-48.html','测试任务1，添加于11_11541497124980191.8.log',2,1,'2018-11-06 09:39:05.252693',1),(16,'Test_TestBaidu1539222138766.CollectProjects_2018-11-06_17-46-53.html','测试任务1，添加于11_11541497610096875.8.log',2,1,'2018-11-06 09:47:10.000000',1),(17,'Test_TestBaidu1539222138766.CollectProjects_2018-11-06_19-23-42.html','测试任务1，添加于11_11541503418928040.5.log',2,1,'2018-11-06 11:23:59.000000',1),(18,'Test_TestBaidu1539222138766.CollectProjects_2018-11-06_19-35-51.html','测试任务1，添加于11_11541504148208173.2.log',2,1,'2018-11-06 11:36:08.000000',1),(19,'Test_TestBaidu1539222138766.CollectProjects_2018-11-06_19-39-10.html','测试任务1，添加于11_11541504347283678.5.log',2,1,'2018-11-06 11:39:30.000000',1),(20,'Test_TestBaidu1539222138766.CollectProjects_2018-11-06_19-40-25.html','测试任务1，添加于11_11541504422120898.8.log',2,1,'2018-11-06 11:40:42.000000',1),(21,'Test_TestBaidu1539222138766.CollectProjects_2018-11-07_10-32-08.html','测试任务1，添加于11_11541557712834801.8.log',2,1,'2018-11-07 02:32:28.000000',1),(22,'Test_TestBaidu1539222138766.CollectProjects_2018-11-07_10-32-08.html','测试任务1，添加于11_11541556866441960.2.log',2,1,'2018-11-07 02:32:29.000000',1),(23,'Test_TestBaidu1539222138766.CollectProjects_2018-11-07_10-34-44.html','测试任务1，添加于11_11541558081119433.8.log',2,1,'2018-11-07 02:35:01.000000',1),(24,'Test_TestBaidu1539222138766.CollectProjects_2018-11-07_10-42-51.html','测试任务1，添加于11_11541558571862367.0.log',2,1,'2018-11-07 02:43:08.000000',1),(25,'Test_TestBaidu1539222138766.CollectProjects_2018-11-07_10-44-40.html','测试任务1，添加于11_11541558680654950.5.log',2,1,'2018-11-07 02:44:57.000000',1),(26,'Test_TestBaidu1539222138766.CollectProjects_2018-11-07_10-48-14.html','第三个测试任务1541558894274765.0.log',4,1,'2018-11-07 02:48:31.000000',1),(27,'Test_TestBaidu1539222138766.CollectProjects_2018-11-07_10-49-13.html','第二个测试任务1541558953833350.2.log',3,1,'2018-11-07 02:49:30.000000',1),(28,'Test_TestBaidu1539222138766.CollectProjects_2018-11-07_10-49-15.html','第三个测试任务1541558955721825.8.log',4,1,'2018-11-07 02:49:33.000000',1),(29,'Test_TestBaidu1539222138766.CollectProjects_2018-11-07_14-34-32.html','测试任务1，添加于11_1_2018-11-07 14_34_2974.log',2,1,'2018-11-07 06:34:49.000000',1),(30,'Test_TestBaidu1539222138766.CollectProjects_2018-11-07_14-34-50.html','测试任务1，添加于11_1_2018-11-07 14_34_5068.log',2,1,'2018-11-07 06:35:07.000000',1),(31,'Test_TestBaidu1539222138766.CollectProjects_2018-11-07_14-41-44.html','测试任务1，添加于11_1_2018-11-07 14_41_4421.log',2,1,'2018-11-07 06:42:01.000000',1),(32,'Test_TestBaidu1539222138766.CollectProjects_2018-11-07_15-34-45.html','测试任务1，添加于11_1_2018-11-07 15_34_4281.log',2,1,'2018-11-07 07:35:04.000000',1),(33,'Test_TestBaidu1539222138766.CollectProjects_2018-11-07_15-34-58.html','第二个测试任务_2018-11-07 15_34_5812.log',3,1,'2018-11-07 07:35:15.000000',1),(34,'Test_TestBaidu1539222138766.CollectProjects_2018-11-07_15-38-23.html','测试任务1，添加于11_1_2018-11-07 15_38_2041.log',2,1,'2018-11-07 07:38:52.000000',1),(35,'Test_TestBaidu1539222138766.CollectProjects_2018-11-07_15-39-00.html','第二个测试任务_2018-11-07 15_39_0048.log',3,1,'2018-11-07 07:39:16.000000',1),(36,'Test_TestBaidu1539222138766.CollectProjects_2018-11-07_15-42-23.html','测试任务1，添加于11_1_2018-11-07 15_42_2065.log',2,1,'2018-11-07 07:42:40.000000',1),(37,'Test_TestBaidu1539222138766.CollectProjects_2018-11-07_15-44-31.html','测试任务1，添加于11_1_2018-11-07 15_44_3187.log',2,1,'2018-11-07 07:44:48.000000',1),(38,'Test_TestBaidu1539222138766.CollectProjects_2018-11-07_15-47-53.html','测试任务1，添加于11_1_2018-11-07 15_47_5331.log',2,1,'2018-11-07 07:48:10.000000',1),(39,'Test_TestBaidu1539222138766.CollectProjects_2018-11-07_15-53-08.html','测试任务1，添加于11_1_2018-11-07 15_53_0549.log',2,1,'2018-11-07 07:53:24.000000',1),(40,'Test_TestBaidu1539222138766.CollectProjects_2018-11-07_15-54-49.html','测试任务1，添加于11_1_2018-11-07 15_54_4989.log',2,1,'2018-11-07 07:55:06.000000',1),(41,'Test_TestBaidu1539222138766.CollectProjects_2018-11-07_17-07-58.html','测试任务1，添加于11_1_2018-11-07 17_07_5433.log',2,1,'2018-11-07 09:08:15.000000',1),(42,'Test_TestBaidu1539222138766.CollectProjects_2018-11-07_17-08-22.html','第二个测试任务_2018-11-07 17_08_2273.log',3,1,'2018-11-07 09:08:39.000000',1),(43,'Test_TestBaidu1539222138766.CollectProjects_2018-11-07_17-10-31.html','测试任务1，添加于11_1_2018-11-07 17_10_2820.log',2,1,'2018-11-07 09:10:48.000000',1),(44,'Test_TestBaidu1539222138766.CollectProjects_2018-11-07_17-11-15.html','第二个测试任务_2018-11-07 17_11_1534.log',3,1,'2018-11-07 09:11:32.000000',1),(45,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_14-14-40.html','测试任务1，添加于11_1_2018-11-08 14_14_393.log',2,1,'2018-11-08 06:14:58.000000',1),(46,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_14-18-08.html','测试任务1，添加于11_1_2018-11-08 14_18_0661.log',2,1,'2018-11-08 06:18:26.000000',1),(47,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_14-21-38.html','测试任务1，添加于11_1_2018-11-08 14_21_3554.log',2,1,'2018-11-08 06:21:55.000000',1),(48,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_14-23-32.html','测试任务1，添加于11_1_2018-11-08 14_23_292.log',2,1,'2018-11-08 06:23:49.000000',1),(49,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_14-24-19.html','测试任务1，添加于11_1_2018-11-08 14_24_1643.log',2,1,'2018-11-08 06:24:36.000000',1),(50,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_14-26-18.html','测试任务1，添加于11_1_2018-11-08 14_26_1771.log',2,1,'2018-11-08 06:26:35.000000',1),(51,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_15-01-44.html','测试任务1，添加于11_1_2018-11-08 15_01_4196.log',2,1,'2018-11-08 07:02:02.000000',1),(52,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_15-05-48.html','第二个测试任务_2018-11-08 15_05_4730.log',3,1,'2018-11-08 07:06:05.000000',1),(53,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_15-09-32.html','测试任务1，添加于11_1_2018-11-08 15_09_2962.log',2,1,'2018-11-08 07:09:50.000000',1),(54,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_15-09-34.html','第二个测试任务_2018-11-08 15_09_3449.log',3,1,'2018-11-08 07:09:54.000000',1),(55,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_16-50-05.html','测试任务1，添加于11_1_2018-11-08 16_50_0167.log',2,1,'2018-11-08 08:50:22.000000',1),(56,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_16-56-17.html','第二个测试任务_2018-11-08 16_56_1755.log',3,1,'2018-11-08 08:56:35.000000',1),(57,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_16-59-43.html','第二个测试任务_2018-11-08 16_59_434.log',3,1,'2018-11-08 09:00:11.000000',1),(58,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_17-00-54.html','第二个测试任务_2018-11-08 17_00_5271.log',3,1,'2018-11-08 09:01:12.000000',1),(59,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_17-04-25.html','测试任务1，添加于11_1_2018-11-08 17_04_2578.log',2,1,'2018-11-08 09:04:44.000000',1),(60,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_17-04-36.html','第二个测试任务_2018-11-08 17_04_3666.log',3,1,'2018-11-08 09:04:54.000000',1),(61,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_18-44-19.html','测试任务1，添加于11_1_2018-11-08 18_44_1762.log',2,1,'2018-11-08 10:44:36.000000',1),(62,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_19-00-40.html','测试任务1，添加于11_1_2018-11-08 19_00_3843.log',2,1,'2018-11-08 11:00:57.000000',1),(63,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_19-04-04.html','第二个测试任务_2018-11-08 19_04_0275.log',3,1,'2018-11-08 11:04:21.000000',1),(64,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_19-09-47.html','测试任务1，添加于11_1_2018-11-08 19_09_4537.log',2,1,'2018-11-08 11:10:04.000000',1),(65,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_19-13-08.html','第二个测试任务_2018-11-08 19_13_0648.log',3,1,'2018-11-08 11:13:27.000000',1),(66,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_19-13-47.html','第二个测试任务_2018-11-08 19_13_4582.log',3,1,'2018-11-08 11:14:08.000000',1),(67,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_19-18-21.html','第二个测试任务_2018-11-08 19_18_1923.log',3,1,'2018-11-08 11:18:39.000000',1),(68,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_19-21-46.html','第二个测试任务_2018-11-08 19_21_4622.log',3,1,'2018-11-08 11:22:04.000000',1),(69,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_19-24-12.html','测试任务1，添加于11_1_2018-11-08 19_24_123.log',2,1,'2018-11-08 11:24:30.000000',1),(70,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_19-32-02.html','第二个测试任务_2018-11-08 19_31_5992.log',3,1,'2018-11-08 11:32:36.000000',1),(71,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_19-34-53.html','第二个测试任务_2018-11-08 19_34_5148.log',3,1,'2018-11-08 11:35:26.000000',1),(72,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_19-38-26.html','第二个测试任务_2018-11-08 19_38_244.log',3,1,'2018-11-08 11:39:02.000000',1),(73,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_19-41-08.html','第二个测试任务_2018-11-08 19_41_0683.log',3,1,'2018-11-08 11:41:42.000000',1),(74,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_19-43-07.html','第二个测试任务_2018-11-08 19_43_0585.log',3,1,'2018-11-08 11:43:41.000000',1),(75,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_19-44-52.html','第二个测试任务_2018-11-08 19_44_5044.log',3,1,'2018-11-08 11:45:25.000000',1),(76,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_19-51-30.html','第二个测试任务_2018-11-08 19_51_2714.log',3,1,'2018-11-08 11:52:06.000000',1),(77,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_19-52-46.html','第二个测试任务_2018-11-08 19_52_4482.log',3,1,'2018-11-08 11:53:20.000000',1),(78,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_19-54-39.html','第二个测试任务_2018-11-08 19_54_3670.log',3,1,'2018-11-08 11:55:12.000000',1),(79,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_19-56-11.html','第二个测试任务_2018-11-08 19_56_0929.log',3,1,'2018-11-08 11:56:47.000000',1),(80,'Test_TestBaidu1539222138766.CollectProjects_2018-11-08_19-58-55.html','第二个测试任务_2018-11-08 19_58_5387.log',3,1,'2018-11-08 11:59:28.000000',1),(81,'Test_TestBaidu1539222138766.CollectProjects_2018-11-09_09-30-11.html','第二个测试任务_2018-11-09 09_30_0921.log',3,1,'2018-11-09 01:30:54.000000',1),(82,'Test_TestBaidu1539222138766.CollectProjects_2018-11-09_09-47-04.html','第二个测试任务_2018-11-09 09_47_0232.log',3,1,'2018-11-09 01:47:41.000000',1),(83,'Test_TestBaidu1539222138766.CollectProjects_2018-11-09_10-04-28.html','第二个测试任务_2018-11-09 10_04_2514.log',3,1,'2018-11-09 02:05:03.000000',1),(84,'Test_TestBaidu1539222138766.CollectProjects_2018-11-09_10-08-27.html','第二个测试任务_2018-11-09 10_08_2522.log',3,1,'2018-11-09 02:09:03.000000',1),(85,'Test_TestBaidu1539222138766.CollectProjects_2018-11-09_10-09-59.html','第二个测试任务_2018-11-09 10_09_5721.log',3,1,'2018-11-09 02:10:35.000000',1),(86,'Test_TestBaidu1539222138766.CollectProjects_2018-11-09_10-11-35.html','测试任务1，添加于11_1_2018-11-09 10_11_339.log',2,1,'2018-11-09 02:12:10.000000',1),(87,'Test_TestBaidu1539222138766.CollectProjects_2018-11-09_10-13-45.html','第二个测试任务_2018-11-09 10_13_4379.log',3,1,'2018-11-09 02:14:20.000000',1),(88,'Test_TestBaidu1539222138766.CollectProjects_2018-11-09_10-15-20.html','第二个测试任务_2018-11-09 10_15_1825.log',3,1,'2018-11-09 02:15:56.000000',1),(89,'Test_TestBaidu1539222138766.CollectProjects_2018-11-09_10-23-34.html','第二个测试任务_2018-11-09 10_23_3263.log',3,1,'2018-11-09 02:24:09.000000',1),(90,'Test_TestBaidu1539222138766.CollectProjects_2018-11-09_10-25-52.html','第二个测试任务_2018-11-09 10_25_4968.log',3,1,'2018-11-09 02:26:27.000000',1),(91,'Test_TestBaidu1539222138766.CollectProjects_2018-11-09_10-41-34.html','第二个测试任务_2018-11-09 10_41_1876.log',3,1,'2018-11-09 02:42:09.000000',1),(92,'Test_TestBaidu1539222138766.CollectProjects_2018-11-09_11-01-51.html','第二个测试任务_2018-11-09 11_01_4916.log',3,1,'2018-11-09 03:02:29.000000',1),(93,'Test_TestBaidu1539222138766.CollectProjects_2018-11-09_11-03-33.html','第二个测试任务_2018-11-09 11_03_3124.log',3,1,'2018-11-09 03:04:08.000000',1),(94,'Test_TestBaidu1539222138766.CollectProjects_2018-11-09_11-07-00.html','第二个测试任务_2018-11-09 11_06_5871.log',3,1,'2018-11-09 03:07:35.000000',1),(95,'Test_TestBaidu1539222138766.CollectProjects_2018-11-09_11-14-24.html','第二个测试任务_2018-11-09 11_14_2296.log',3,1,'2018-11-09 03:15:00.000000',1),(96,'Test_TestBaidu1539222138766.CollectProjects_2018-11-09_13-33-56.html','第二个测试任务_2018-11-09 13_33_5440.log',3,1,'2018-11-09 05:34:31.000000',1),(97,'Test_TestBaidu1539222138766.CollectProjects_2018-11-09_13-47-17.html','第二个测试任务_2018-11-09 13_47_1726.log',3,1,'2018-11-09 05:47:53.000000',1);
/*!40000 ALTER TABLE `task_result` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `task_taskstatus`
--

DROP TABLE IF EXISTS `task_taskstatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `task_taskstatus` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `desc` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `task_taskstatus`
--

LOCK TABLES `task_taskstatus` WRITE;
/*!40000 ALTER TABLE `task_taskstatus` DISABLE KEYS */;
INSERT INTO `task_taskstatus` VALUES (1,'正常','该任务为正常可使用状态'),(2,'需要修改','该任务需要修改'),(3,'无效','该任务无效');
/*!40000 ALTER TABLE `task_taskstatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `task_tasksuitemapping`
--

DROP TABLE IF EXISTS `task_tasksuitemapping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `task_tasksuitemapping` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `task` int(11) NOT NULL,
  `suite` int(11) NOT NULL,
  PRIMARY KEY (`id`)
)
  ENGINE = InnoDB
  AUTO_INCREMENT = 10
  DEFAULT CHARSET = utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `task_tasksuitemapping`
--

LOCK TABLES `task_tasksuitemapping` WRITE;
/*!40000 ALTER TABLE `task_tasksuitemapping` DISABLE KEYS */;
INSERT INTO `task_tasksuitemapping`
VALUES (1, 2, 5), (2, 3, 5), (3, 4, 5), (4, 5, 5), (5, 6, 5), (6, 7, 5), (7, 8, 4), (8, 9, 5), (9, 9, 4);
/*!40000 ALTER TABLE `task_tasksuitemapping` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `task_testresulttype`
--

DROP TABLE IF EXISTS `task_testresulttype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `task_testresulttype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(20) NOT NULL,
  `desc` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `task_testresulttype`
--

LOCK TABLES `task_testresulttype` WRITE;
/*!40000 ALTER TABLE `task_testresulttype` DISABLE KEYS */;
INSERT INTO `task_testresulttype` VALUES (1,'成功','全部成功'),(2,'部分成功','部分测试用例执行失败'),(3,'全部失败','全部测试用例失败'),(4,'无效','该次测试为无效测试');
/*!40000 ALTER TABLE `task_testresulttype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `task_testtask`
--

DROP TABLE IF EXISTS `task_testtask`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `task_testtask` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `status` int(11) NOT NULL,
  `product` int(11) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `create_user` int(11) NOT NULL,
  `desc` varchar(100) NOT NULL,
  `last_run_time` datetime(6) DEFAULT NULL,
  `runtime` int(11) NOT NULL,
  PRIMARY KEY (`id`)
)
  ENGINE = InnoDB
  AUTO_INCREMENT = 10
  DEFAULT CHARSET = utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `task_testtask`
--

LOCK TABLES `task_testtask` WRITE;
/*!40000 ALTER TABLE `task_testtask` DISABLE KEYS */;
INSERT INTO `task_testtask` VALUES (2,'测试任务1，添加于11/1',1,1,'2018-11-01 07:00:14.690552',1,'','2018-11-09 02:11:36.000000',28),(3,'第二个测试任务',1,2,'2018-11-01 07:05:59.778680',1,'','2018-11-09 05:47:17.000000',42),(4,'第三个测试任务',1,1,'2018-11-01 07:31:25.007934',1,'','2018-11-07 02:49:15.000000',2);
/*!40000 ALTER TABLE `task_testtask` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `testcase_casemodule`
--

DROP TABLE IF EXISTS `testcase_casemodule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `testcase_casemodule` (
  `id`            int(11) NOT NULL AUTO_INCREMENT,
  `name`          varchar(255) NOT NULL,
  `child_module`  INT(11)          DEFAULT NULL,
  `parent_module` INT(11)          DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `testcase_casemodule`
--

LOCK TABLES `testcase_casemodule` WRITE;
/*!40000 ALTER TABLE `testcase_casemodule` DISABLE KEYS */;
INSERT INTO `testcase_casemodule`
VALUES (1, '默认', NULL, NULL), (2, '登录', NULL, NULL), (3, '项目管理', NULL, NULL), (4, '用户管理', NULL, NULL);
/*!40000 ALTER TABLE `testcase_casemodule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `testcase_suitcasemapping`
--

DROP TABLE IF EXISTS `testcase_suitcasemapping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `testcase_suitcasemapping` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `suit` int(11) NOT NULL,
  `case` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `testcase_suitcasemapping`
--

LOCK TABLES `testcase_suitcasemapping` WRITE;
/*!40000 ALTER TABLE `testcase_suitcasemapping` DISABLE KEYS */;
INSERT INTO `testcase_suitcasemapping` VALUES (2,4,7),(3,5,7);
/*!40000 ALTER TABLE `testcase_suitcasemapping` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `testcase_testcase`
--

DROP TABLE IF EXISTS `testcase_testcase`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `testcase_testcase` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `precondition` longtext,
  `steps` longtext NOT NULL,
  `expect` longtext NOT NULL,
  `create_user` int(11) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `last_edit_user` int(11) NOT NULL,
  `last_edit_time` datetime(6) NOT NULL,
  `case_module` int(11) NOT NULL,
  `editable` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `testcase_testcase`
--

LOCK TABLES `testcase_testcase` WRITE;
/*!40000 ALTER TABLE `testcase_testcase` DISABLE KEYS */;
INSERT INTO `testcase_testcase` VALUES (2,'账号登录：输入框的输入限制验证','账号：Admin 密码：Admin 浏览器：Chrome','不输入账号，仅输入密码后，点击登录按钮\r\n输入正确的账号，不输入密码后，点击登录按钮\r\n保持账号和密码的输入框为空，点击登录按钮\r\n在账号输入框中输入一串空格后，输入正确的密码，点击登录按钮\r\n在密码输入框中输入一串空格后，输入正确的密码，点击登录按钮','登录失败，无请求发送，页面提示信息正确合理\r\n登录失败，无请求发送，页面提示信息正确合理\r\n登录失败，无请求发送，页面提示信息正确合理\r\n登录失败，无请求发送，页面提示信息正确合理\r\n登录失败，无请求发送，页面提示信息正确合理',3,'2018-09-18 07:39:24.173068',2,'2018-09-14 02:50:16.000000',2,1),(3,'用户登录：用户信息获取正确','无','在账号和密码输入栏中输入正确的账号密码后，点击登录按钮','跳转页面正确，页面显示的已登录用户正确',3,'2018-09-18 06:16:48.699344',1,'2018-09-14 02:51:34.000000',2,1),(4,'项目管理：新建产品的入口验证1','用户已登录\r\n用户拥有产品相关的权限','点击页面上方的产品TAB，进入到产品主页\r\n点击产品主页左侧的所有产品\r\n点击添加产品','产品主页显示无异常\r\n产品主页下拉菜单中的最后一项显示为添加产品\r\n页面跳转到添加产品页',2,'2018-09-14 06:48:08.146182',2,'2018-09-14 03:00:04.000000',3,1),(5,'项目管理：新建产品的入口验证2','用户已登录\r\n用户拥有产品相关的权限','点击页面上方的产品TAB，进入到产品主页\r\n点击产品主页左侧的所有产品\r\n点击添加产品','产品主页显示无异常\r\n产品主页下拉菜单中的最后一项显示为添加产品\r\n页面跳转到添加产品页',3,'2018-09-14 06:48:13.910743',3,'2018-09-14 02:45:36.000000',3,1),(6,'项目管理：新建产品的入口验证3','用户已登录\r\n用户拥有产品相关的权限','点击页面上方的产品TAB，进入到产品主页\r\n点击产品主页左侧的所有产品\r\n点击添加产品','产品主页显示无异常\r\n产品主页下拉菜单中的最后一项显示为添加产品\r\n页面跳转到添加产品页',4,'2018-09-14 06:48:18.458493',4,'2018-09-14 03:03:38.000000',3,1),(7,'用户管理:用户列表显示4','用户已登录','点击上方的用户TAB，查看页面跳转\r\n查看页面的数据是否和数据库保持一致','页面跳转到用户列表页面\r\n页面的数据和数据库保持一致，无重复项',3,'2018-09-14 06:48:27.343899',2,'2018-09-14 03:06:16.000000',4,1),(8,'用户管理:用户列表显示5','用户已登录\r\n用户已登录\r\n用户已登录\r\n用户已登录','点击上方的用户TAB，查看页面跳转\r\n查看页面的数据是否和数据库保持一致\r\n点击上方的用户TAB，查看页面跳转\r\n查看页面的数据是否和数据库保持一致\r\n点击上方的用户TAB，查看页面跳转\r\n查看页面的数据是否和数据库保持一致\r\n点击上方的用户TAB，查看页面跳转\r\n查看页面的数据是否和数据库保持一致','页面跳转到用户列表页面\r\n页面的数据和数据库保持一致，无重复项\r\n页面跳转到用户列表页面\r\n页面的数据和数据库保持一致，无重复项\r\n页面跳转到用户列表页面\r\n页面的数据和数据库保持一致，无重复项\r\n页面跳转到用户列表页面\r\n页面的数据和数据库保持一致，无重复项',3,'2018-09-14 06:48:32.861227',3,'2018-09-14 03:06:56.000000',4,1),(9,'用户管理:用户列表显示6','用户已登录\r\n用户已登录\r\n用户已登录\r\n用户已登录','点击上方的用户TAB，查看页面跳转\r\n查看页面的数据是否和数据库保持一致\r\n点击上方的用户TAB，查看页面跳转\r\n查看页面的数据是否和数据库保持一致\r\n点击上方的用户TAB，查看页面跳转\r\n查看页面的数据是否和数据库保持一致\r\n点击上方的用户TAB，查看页面跳转\r\n查看页面的数据是否和数据库保持一致','页面跳转到用户列表页面\r\n页面的数据和数据库保持一致，无重复项\r\n页面跳转到用户列表页面\r\n页面的数据和数据库保持一致，无重复项\r\n页面跳转到用户列表页面\r\n页面的数据和数据库保持一致，无重复项\r\n页面跳转到用户列表页面\r\n页面的数据和数据库保持一致，无重复项',4,'2018-09-14 06:48:37.532870',4,'2018-09-14 03:07:24.000000',4,1),(10,'用户管理:用户列表显示10','用户已登录\r\n用户已登录\r\n用户已登录\r\n用户已登录','点击上方的用户TAB，查看页面跳转\r\n查看页面的数据是否和数据库保持一致\r\n点击上方的用户TAB，查看页面跳转\r\n查看页面的数据是否和数据库保持一致\r\n点击上方的用户TAB，查看页面跳转\r\n查看页面的数据是否和数据库保持一致\r\n点击上方的用户TAB，查看页面跳转\r\n查看页面的数据是否和数据库保持一致','页面跳转到用户列表页面\r\n页面的数据和数据库保持一致，无重复项\r\n页面跳转到用户列表页面\r\n页面的数据和数据库保持一致，无重复项\r\n页面跳转到用户列表页面\r\n页面的数据和数据库保持一致，无重复项\r\n页面跳转到用户列表页面\r\n页面的数据和数据库保持一致，无重复项',4,'2018-09-14 06:48:42.730035',4,'2018-09-14 03:07:44.000000',4,1),(11,'登录页面可以正常打开','无','打开网站http://100.64.15.43/zentao/my/','可以正常打开',4,'2018-10-09 11:38:27.791080',4,'2018-10-09 11:38:27.791080',3,1),(12,'信息化：登录功能验证','账号：zhugc\r\n密码：X123465','进入到http://100.64.15.43/zentao/my/后，输入账号和密码后，点击登录','登录成功',4,'2018-10-09 11:39:40.188407',4,'2018-10-09 11:39:40.188407',3,1);
/*!40000 ALTER TABLE `testcase_testcase` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `testcase_testsuite`
--

DROP TABLE IF EXISTS `testcase_testsuite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `testcase_testsuite` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `create_user` int(11) NOT NULL,
  `desc` varchar(100) DEFAULT NULL,
  `setup` int(11) DEFAULT NULL,
  `teardown` int(11) DEFAULT NULL,
  `last_edit_time` datetime(6) NOT NULL,
  `last_editer` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `testcase_testsuite`
--

LOCK TABLES `testcase_testsuite` WRITE;
/*!40000 ALTER TABLE `testcase_testsuite` DISABLE KEYS */;
INSERT INTO `testcase_testsuite` VALUES (4,'一个简单的测试套件','2018-10-11 01:50:27.507247',1,'测试套件描述',NULL,NULL,'2018-10-11 01:50:27.507247',1),(5,'正确的测试套件','2018-10-11 01:51:30.865050',1,'测试套件',NULL,NULL,'2018-10-11 01:51:30.865050',1);
/*!40000 ALTER TABLE `testcase_testsuite` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_privilege`
--

DROP TABLE IF EXISTS `user_privilege`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_privilege` (
  `id` int(10) unsigned NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_privilege`
--

LOCK TABLES `user_privilege` WRITE;
/*!40000 ALTER TABLE `user_privilege` DISABLE KEYS */;
INSERT INTO `user_privilege` VALUES (1,'Admin'),(2,'Senior Tester'),(3,'Tester'),(4,'Guest');
/*!40000 ALTER TABLE `user_privilege` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_user`
--

DROP TABLE IF EXISTS `user_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_user` (
  `name` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `last_login_time` datetime(6) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `privilege` int(11) NOT NULL,
  `email` varchar(254) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `real_name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_user_email_1c6f3d1a_uniq` (`email`),
  UNIQUE KEY `user_user_name_254b66a7_uniq` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_user`
--

LOCK TABLES `user_user` WRITE;
/*!40000 ALTER TABLE `user_user` DISABLE KEYS */;
INSERT INTO `user_user` VALUES ('admin','admin','2018-09-05 15:34:41.000000','2018-09-05 15:34:45.000000',1,'admin@admin.com',1,'admin'),('renzy','1234','2018-09-11 06:17:44.000000','2018-09-11 06:17:45.000000',1,'renzy@mail.jj.cn',2,'任宗毅'),('yinp','1234','2018-09-11 06:18:06.000000','2018-09-11 06:18:07.000000',1,'yinp@mail.jj.cn',3,'尹鹏'),('pengyy','1234','2018-09-11 06:18:27.000000','2018-09-11 06:18:28.000000',1,'pengyy@mail.jj.cn',4,'彭榆耀');
/*!40000 ALTER TABLE `user_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'testdb'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-15 18:21:33
