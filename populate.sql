-- phpMyAdmin SQL Dump
-- version 4.2.12deb2
-- http://www.phpmyadmin.net
--
-- Client :  localhost
-- Généré le :  Mer 23 Septembre 2015 à 16:05
-- Version du serveur :  5.5.44-0+deb8u1
-- Version de PHP :  5.6.13-0+deb8u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données :  `centech`
--

-- --------------------------------------------------------

--
-- Structure de la table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
`id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Contenu de la table `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(2, 'Centech'),
(3, 'Executive');

-- --------------------------------------------------------

--
-- Structure de la table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
`id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
`id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=88 DEFAULT CHARSET=latin1;

--
-- Contenu de la table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add permission', 2, 'add_permission'),
(5, 'Can change permission', 2, 'change_permission'),
(6, 'Can delete permission', 2, 'delete_permission'),
(7, 'Can add group', 3, 'add_group'),
(8, 'Can change group', 3, 'change_group'),
(9, 'Can delete group', 3, 'delete_group'),
(10, 'Can add user', 4, 'add_user'),
(11, 'Can change user', 4, 'change_user'),
(12, 'Can delete user', 4, 'delete_user'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add site', 7, 'add_site'),
(20, 'Can change site', 7, 'change_site'),
(21, 'Can delete site', 7, 'delete_site'),
(22, 'Can add education', 8, 'add_education'),
(23, 'Can change education', 8, 'change_education'),
(24, 'Can delete education', 8, 'delete_education'),
(25, 'Can add expertise', 9, 'add_expertise'),
(26, 'Can change expertise', 9, 'change_expertise'),
(27, 'Can delete expertise', 9, 'delete_expertise'),
(28, 'Can add user profile', 10, 'add_userprofile'),
(29, 'Can change user profile', 10, 'change_userprofile'),
(30, 'Can delete user profile', 10, 'delete_userprofile'),
(31, 'Can add floor plan', 11, 'add_floorplan'),
(32, 'Can change floor plan', 11, 'change_floorplan'),
(33, 'Can delete floor plan', 11, 'delete_floorplan'),
(34, 'Can add company status', 12, 'add_companystatus'),
(35, 'Can change company status', 12, 'change_companystatus'),
(36, 'Can delete company status', 12, 'delete_companystatus'),
(37, 'Can add company', 13, 'add_company'),
(38, 'Can change company', 13, 'change_company'),
(39, 'Can delete company', 13, 'delete_company'),
(40, 'Can add presence', 14, 'add_presence'),
(41, 'Can change presence', 14, 'change_presence'),
(42, 'Can delete presence', 14, 'delete_presence'),
(43, 'Can add founder', 15, 'add_founder'),
(44, 'Can change founder', 15, 'change_founder'),
(45, 'Can delete founder', 15, 'delete_founder'),
(46, 'Can add mentor', 16, 'add_mentor'),
(47, 'Can change mentor', 16, 'change_mentor'),
(48, 'Can delete mentor', 16, 'delete_mentor'),
(49, 'Can add kpi', 17, 'add_kpi'),
(50, 'Can change kpi', 17, 'change_kpi'),
(51, 'Can delete kpi', 17, 'delete_kpi'),
(52, 'Can add customer experiment', 18, 'add_customerexperiment'),
(53, 'Can change customer experiment', 18, 'change_customerexperiment'),
(54, 'Can delete customer experiment', 18, 'delete_customerexperiment'),
(55, 'Can add Business canvas element', 19, 'add_businesscanvaselement'),
(56, 'Can change Business canvas element', 19, 'change_businesscanvaselement'),
(57, 'Can delete Business canvas element', 19, 'delete_businesscanvaselement'),
(58, 'Can add Archive', 20, 'add_archive'),
(59, 'Can change Archive', 20, 'change_archive'),
(60, 'Can delete Archive', 20, 'delete_archive'),
(61, 'Can add bourse', 21, 'add_bourse'),
(62, 'Can change bourse', 21, 'change_bourse'),
(63, 'Can delete bourse', 21, 'delete_bourse'),
(64, 'Can add subvention', 22, 'add_subvention'),
(65, 'Can change subvention', 22, 'change_subvention'),
(66, 'Can delete subvention', 22, 'delete_subvention'),
(67, 'Can add investissement', 23, 'add_investissement'),
(68, 'Can change investissement', 23, 'change_investissement'),
(69, 'Can delete investissement', 23, 'delete_investissement'),
(70, 'Can add pret', 24, 'add_pret'),
(71, 'Can change pret', 24, 'change_pret'),
(72, 'Can delete pret', 24, 'delete_pret'),
(73, 'Can add vente', 25, 'add_vente'),
(74, 'Can change vente', 25, 'change_vente'),
(75, 'Can delete vente', 25, 'delete_vente'),
(76, 'Can add Value proposition canvas type', 26, 'add_valuepropositioncanvastype'),
(77, 'Can change Value proposition canvas type', 26, 'change_valuepropositioncanvastype'),
(78, 'Can delete Value proposition canvas type', 26, 'delete_valuepropositioncanvastype'),
(79, 'Can add Value proposition canvas element', 27, 'add_valuepropositioncanvaselement'),
(80, 'Can change Value proposition canvas element', 27, 'change_valuepropositioncanvaselement'),
(81, 'Can delete Value proposition canvas element', 27, 'delete_valuepropositioncanvaselement'),
(82, 'Can add card', 28, 'add_card'),
(83, 'Can change card', 28, 'change_card'),
(84, 'Can delete card', 28, 'delete_card'),
(85, 'Can add comment', 29, 'add_comment'),
(86, 'Can change comment', 29, 'change_comment'),
(87, 'Can delete comment', 29, 'delete_comment');

-- --------------------------------------------------------

--
-- Structure de la table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
`id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) DEFAULT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Contenu de la table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$20000$mam9DkEE8vNU$ipZiplbEkZZSRz/b7NWp0GAi9UnXnEKt4Etda/pwwHI=', '2015-09-23 20:02:29', 1, 'root', '', '', 'rignon.noel@openmailbox.org', 1, 1, '2015-09-18 15:32:12'),
(2, 'pbkdf2_sha256$20000$fUI2vCETUAW0$bTWfbVMZ5/NqDZubaKRssP0YzQ7KEHUMqf+5bK+vZ8A=', '2015-09-20 20:06:02', 0, 'exec', '', '', '', 0, 1, '2015-09-20 20:04:37');

-- --------------------------------------------------------

--
-- Structure de la table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
`id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Contenu de la table `auth_user_groups`
--

INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES
(1, 1, 2),
(2, 2, 3);

-- --------------------------------------------------------

--
-- Structure de la table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
`id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `businessCanvas_archive`
--

CREATE TABLE IF NOT EXISTS `businessCanvas_archive` (
`id` int(11) NOT NULL,
  `date` datetime DEFAULT NULL,
  `company_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `businessCanvas_archive_elements`
--

CREATE TABLE IF NOT EXISTS `businessCanvas_archive_elements` (
`id` int(11) NOT NULL,
  `archive_id` int(11) NOT NULL,
  `businesscanvaselement_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `businessCanvas_businesscanvaselement`
--

CREATE TABLE IF NOT EXISTS `businessCanvas_businesscanvaselement` (
`id` int(11) NOT NULL,
  `title` varchar(200) NOT NULL,
  `comment` longtext NOT NULL,
  `date` datetime NOT NULL,
  `disactivated` tinyint(1) NOT NULL,
  `company_id` int(11) NOT NULL,
  `type` varchar(20) DEFAULT NULL,
  `updated` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `company_company`
--

CREATE TABLE IF NOT EXISTS `company_company` (
`id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `logo` varchar(100) NOT NULL,
  `url` varchar(200) NOT NULL,
  `video` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `created` datetime NOT NULL,
  `updated` datetime NOT NULL,
  `companyStatus_id` int(11) NOT NULL,
  `incubated_on` date,
  `facebook` varchar(200),
  `googlePlus` varchar(200),
  `linkedIn` varchar(200),
  `twitter` varchar(200),
  `endOfIncubation` date
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `company_companystatus`
--

CREATE TABLE IF NOT EXISTS `company_companystatus` (
`id` int(11) NOT NULL,
  `status` varchar(50) NOT NULL,
  `comment` longtext NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `company_company_founders`
--

CREATE TABLE IF NOT EXISTS `company_company_founders` (
`id` int(11) NOT NULL,
  `company_id` int(11) NOT NULL,
  `founder_id` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `company_company_mentors`
--

CREATE TABLE IF NOT EXISTS `company_company_mentors` (
`id` int(11) NOT NULL,
  `company_id` int(11) NOT NULL,
  `mentor_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `company_presence`
--

CREATE TABLE IF NOT EXISTS `company_presence` (
`id` int(11) NOT NULL,
  `date` datetime NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

--
-- Contenu de la table `company_presence`
--

INSERT INTO `company_presence` (`id`, `date`) VALUES
(1, '2015-09-15 00:00:00'),
(2, '2015-09-08 00:00:00'),
(3, '2015-09-08 00:00:00'),
(4, '2015-09-11 00:00:00'),
(5, '2015-09-16 00:00:00'),
(6, '2015-09-23 00:00:00'),
(7, '2015-09-28 00:00:00'),
(8, '2015-09-28 00:00:00'),
(9, '2015-09-01 00:00:00'),
(10, '2015-09-08 00:00:00');

-- --------------------------------------------------------

--
-- Structure de la table `company_presence_company`
--

CREATE TABLE IF NOT EXISTS `company_presence_company` (
`id` int(11) NOT NULL,
  `presence_id` int(11) NOT NULL,
  `company_id` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
`id` int(11) NOT NULL,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

--
-- Contenu de la table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2015-09-18 16:56:15', '1', 'root', 2, 'Modifié groups et date_joined.', 4, 1),
(2, '2015-09-20 20:04:37', '2', 'exec', 1, '', 4, 1),
(3, '2015-09-20 20:04:39', '2', 'exec', 1, '', 10, 1),
(4, '2015-09-20 20:05:50', '2', 'exec', 2, 'Modifié groups et date_joined.', 4, 1),
(5, '2015-09-21 23:06:05', '4', 'Fondateur2', 2, 'Modifié password.', 4, 1),
(6, '2015-09-21 23:08:26', '3', 'Fondateur', 2, 'Modifié password.', 4, 1),
(7, '2015-09-23 19:50:30', '3', 'Fondateur', 3, '', 4, 1),
(8, '2015-09-23 19:50:30', '4', 'Fondateur2', 3, '', 4, 1),
(9, '2015-09-23 19:50:40', '1', 'Compagnie  de Toto', 3, '', 13, 1);

-- --------------------------------------------------------

--
-- Structure de la table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
`id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=latin1;

--
-- Contenu de la table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(20, 'businessCanvas', 'archive'),
(19, 'businessCanvas', 'businesscanvaselement'),
(13, 'company', 'company'),
(12, 'company', 'companystatus'),
(14, 'company', 'presence'),
(5, 'contenttypes', 'contenttype'),
(18, 'experiment', 'customerexperiment'),
(21, 'finance', 'bourse'),
(23, 'finance', 'investissement'),
(24, 'finance', 'pret'),
(22, 'finance', 'subvention'),
(25, 'finance', 'vente'),
(15, 'founder', 'founder'),
(8, 'home', 'education'),
(9, 'home', 'expertise'),
(11, 'home', 'floorplan'),
(10, 'home', 'userprofile'),
(28, 'kanboard', 'card'),
(29, 'kanboard', 'comment'),
(17, 'kpi', 'kpi'),
(16, 'mentor', 'mentor'),
(6, 'sessions', 'session'),
(7, 'sites', 'site'),
(27, 'valuePropositionCanvas', 'valuepropositioncanvaselement'),
(26, 'valuePropositionCanvas', 'valuepropositioncanvastype');

-- --------------------------------------------------------

--
-- Structure de la table `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
`id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=70 DEFAULT CHARSET=latin1;

--
-- Contenu de la table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2015-09-18 15:25:09'),
(2, 'auth', '0001_initial', '2015-09-18 15:25:12'),
(3, 'admin', '0001_initial', '2015-09-18 15:25:12'),
(4, 'contenttypes', '0002_remove_content_type_name', '2015-09-18 15:25:13'),
(5, 'auth', '0002_alter_permission_name_max_length', '2015-09-18 15:25:13'),
(6, 'auth', '0003_alter_user_email_max_length', '2015-09-18 15:25:14'),
(7, 'auth', '0004_alter_user_username_opts', '2015-09-18 15:25:14'),
(8, 'auth', '0005_alter_user_last_login_null', '2015-09-18 15:25:14'),
(9, 'auth', '0006_require_contenttypes_0002', '2015-09-18 15:25:14'),
(10, 'home', '0001_initial', '2015-09-18 15:25:15'),
(11, 'mentor', '0001_initial', '2015-09-18 15:25:16'),
(12, 'founder', '0001_initial', '2015-09-18 15:25:17'),
(13, 'company', '0001_initial', '2015-09-18 15:25:21'),
(14, 'businessCanvas', '0001_initial', '2015-09-18 15:25:23'),
(15, 'businessCanvas', '0002_businesscanvaselement_newtype', '2015-09-18 15:25:24'),
(16, 'businessCanvas', '0003_auto_20150604_1253', '2015-09-18 15:25:24'),
(17, 'businessCanvas', '0004_auto_20150604_1257', '2015-09-18 15:25:24'),
(18, 'businessCanvas', '0005_auto_20150604_1304', '2015-09-18 15:25:25'),
(19, 'businessCanvas', '0006_auto_20150604_1305', '2015-09-18 15:25:25'),
(20, 'businessCanvas', '0007_auto_20150610_1512', '2015-09-18 15:25:29'),
(21, 'businessCanvas', '0008_auto_20150610_1527', '2015-09-18 15:25:29'),
(22, 'businessCanvas', '0009_delete_businesscanvastype', '2015-09-18 15:25:29'),
(23, 'company', '0002_auto_20150610_1511', '2015-09-18 15:25:35'),
(24, 'company', '0003_auto_20150623_1059', '2015-09-18 15:25:38'),
(25, 'company', '0004_company_incubated_on', '2015-09-18 15:25:38'),
(26, 'company', '0005_auto_20150706_1309', '2015-09-18 15:25:39'),
(27, 'company', '0006_company_endofincubation', '2015-09-18 15:25:40'),
(28, 'company', '0007_companystatus_comment', '2015-09-18 15:25:40'),
(29, 'experiment', '0001_initial', '2015-09-18 15:25:41'),
(30, 'experiment', '0002_auto_20150708_1549', '2015-09-18 15:25:42'),
(31, 'experiment', '0003_auto_20150708_1558', '2015-09-18 15:25:43'),
(32, 'experiment', '0004_auto_20150727_1405', '2015-09-18 15:25:44'),
(33, 'finance', '0001_initial', '2015-09-18 15:25:46'),
(34, 'finance', '0002_auto_20150610_1511', '2015-09-18 15:25:52'),
(35, 'finance', '0003_auto_20150626_1328', '2015-09-18 15:25:56'),
(36, 'founder', '0002_auto_20150610_1511', '2015-09-18 15:25:56'),
(37, 'home', '0002_auto_20150610_1511', '2015-09-18 15:25:57'),
(38, 'home', '0003_auto_20150623_1059', '2015-09-18 15:25:57'),
(39, 'home', '0004_auto_20150706_1310', '2015-09-18 15:25:59'),
(40, 'home', '0005_floorplan', '2015-09-18 15:25:59'),
(41, 'kanboard', '0001_initial', '2015-09-18 15:26:00'),
(42, 'kanboard', '0002_auto_20150713_1359', '2015-09-18 15:26:02'),
(43, 'kanboard', '0003_comment', '2015-09-18 15:26:02'),
(44, 'kanboard', '0004_auto_20150729_0951', '2015-09-18 15:26:03'),
(45, 'kpi', '0001_initial', '2015-09-18 15:26:05'),
(46, 'kpi', '0002_auto_20150604_1022', '2015-09-18 15:26:05'),
(47, 'kpi', '0003_auto_20150610_1511', '2015-09-18 15:26:07'),
(48, 'kpi', '0004_kpi_newtype', '2015-09-18 15:26:08'),
(49, 'kpi', '0005_auto_20150630_1051', '2015-09-18 15:26:08'),
(50, 'kpi', '0006_auto_20150630_1112', '2015-09-18 15:26:09'),
(51, 'kpi', '0007_auto_20150630_1113', '2015-09-18 15:26:10'),
(52, 'kpi', '0008_auto_20150630_1114', '2015-09-18 15:26:10'),
(53, 'kpi', '0009_delete_kpitype', '2015-09-18 15:26:10'),
(54, 'kpi', '0010_remove_kpi_phase', '2015-09-18 15:26:11'),
(55, 'kpi', '0011_auto_20150708_1334', '2015-09-18 15:26:12'),
(56, 'kpi', '0012_auto_20150708_1343', '2015-09-18 15:26:12'),
(57, 'kpi', '0013_auto_20150727_1405', '2015-09-18 15:26:13'),
(58, 'mentor', '0002_auto_20150610_1511', '2015-09-18 15:26:14'),
(59, 'mentor', '0003_mentor_type', '2015-09-18 15:26:14'),
(60, 'mentor', '0004_auto_20150706_1102', '2015-09-18 15:26:14'),
(61, 'mentor', '0005_mentor_url', '2015-09-18 15:26:15'),
(62, 'mentor', '0006_auto_20150727_1405', '2015-09-18 15:26:15'),
(63, 'sessions', '0001_initial', '2015-09-18 15:26:16'),
(64, 'sites', '0001_initial', '2015-09-18 15:26:16'),
(65, 'valuePropositionCanvas', '0001_initial', '2015-09-18 15:26:17'),
(66, 'company', '0008_auto_20150918_1739', '2015-09-18 17:39:58'),
(67, 'company', '0009_auto_20150918_1741', '2015-09-18 17:41:56'),
(68, 'company', '0008_auto_20150918_1745', '2015-09-18 17:45:34'),
(69, 'company', '0008_auto_20150918_1750', '2015-09-18 17:51:04');

-- --------------------------------------------------------

--
-- Structure de la table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('z0nbbtecrdubuebi63ksv2egde5x5lnk', 'MDk3MGZmNWMxNzU5MTQxNGY4OTMyOWQ1NzY5NTIyMjNmNzk4ZTY4MDp7Il9hdXRoX3VzZXJfaGFzaCI6IjY5MjEzMzNkZDc2MDkyZTc5NjM4MjhiMzdiMTYyNzMzMzA0N2Y2YjYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiY29tcGFueVNlbGVjdGVkIjoxfQ==', '2015-10-07 20:02:29');

-- --------------------------------------------------------

--
-- Structure de la table `django_site`
--

CREATE TABLE IF NOT EXISTS `django_site` (
`id` int(11) NOT NULL,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Contenu de la table `django_site`
--

INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
(1, 'example.com', 'example.com');

-- --------------------------------------------------------

--
-- Structure de la table `experiment_customerexperiment`
--

CREATE TABLE IF NOT EXISTS `experiment_customerexperiment` (
`id` int(11) NOT NULL,
  `dateStart` datetime DEFAULT NULL,
  `dateFinish` datetime DEFAULT NULL,
  `hypothesis` longtext NOT NULL,
  `validated` tinyint(1) DEFAULT NULL,
  `experiment_description` longtext NOT NULL,
  `test_subject_count` int(10) unsigned NOT NULL,
  `test_subject_description` longtext NOT NULL,
  `conclusions` longtext NOT NULL,
  `company_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `finance_bourse`
--

CREATE TABLE IF NOT EXISTS `finance_bourse` (
`id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `dateSoumission` date NOT NULL,
  `sommeSoumission` int(10) unsigned NOT NULL,
  `dateReception` date DEFAULT NULL,
  `sommeReception` int(10) unsigned DEFAULT NULL,
  `description` varchar(512) NOT NULL,
  `company_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `finance_investissement`
--

CREATE TABLE IF NOT EXISTS `finance_investissement` (
`id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `dateSoumission` date NOT NULL,
  `sommeSoumission` int(10) unsigned NOT NULL,
  `dateReception` date DEFAULT NULL,
  `sommeReception` int(10) unsigned DEFAULT NULL,
  `description` varchar(512) NOT NULL,
  `company_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `finance_pret`
--

CREATE TABLE IF NOT EXISTS `finance_pret` (
`id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `dateSoumission` date NOT NULL,
  `sommeSoumission` int(10) unsigned NOT NULL,
  `dateReception` date DEFAULT NULL,
  `sommeReception` int(10) unsigned DEFAULT NULL,
  `description` varchar(512) NOT NULL,
  `company_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `finance_subvention`
--

CREATE TABLE IF NOT EXISTS `finance_subvention` (
`id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `dateSoumission` date NOT NULL,
  `sommeSoumission` int(10) unsigned NOT NULL,
  `dateReception` date DEFAULT NULL,
  `sommeReception` int(10) unsigned DEFAULT NULL,
  `description` varchar(512) NOT NULL,
  `company_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `finance_vente`
--

CREATE TABLE IF NOT EXISTS `finance_vente` (
`id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `dateSoumission` date NOT NULL,
  `sommeSoumission` int(10) unsigned NOT NULL,
  `dateReception` date DEFAULT NULL,
  `sommeReception` int(10) unsigned DEFAULT NULL,
  `description` varchar(512) NOT NULL,
  `company_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `founder_founder`
--

CREATE TABLE IF NOT EXISTS `founder_founder` (
  `userprofile_ptr_id` int(11) NOT NULL,
  `equity` double NOT NULL,
  `about` varchar(2000) NOT NULL,
  `education_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `founder_founder_expertise`
--

CREATE TABLE IF NOT EXISTS `founder_founder_expertise` (
`id` int(11) NOT NULL,
  `founder_id` int(11) NOT NULL,
  `expertise_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `home_education`
--

CREATE TABLE IF NOT EXISTS `home_education` (
`id` int(11) NOT NULL,
  `education` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `home_expertise`
--

CREATE TABLE IF NOT EXISTS `home_expertise` (
`id` int(11) NOT NULL,
  `expertise` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `home_floorplan`
--

CREATE TABLE IF NOT EXISTS `home_floorplan` (
`id` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `home_userprofile`
--

CREATE TABLE IF NOT EXISTS `home_userprofile` (
`userProfile_id` int(11) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `website` varchar(200) NOT NULL,
  `picture` varchar(100) NOT NULL,
  `user_id` int(11) NOT NULL,
  `facebook` varchar(200),
  `googlePlus` varchar(200),
  `linkedIn` varchar(200),
  `twitter` varchar(200)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Contenu de la table `home_userprofile`
--

INSERT INTO `home_userprofile` (`userProfile_id`, `phone`, `website`, `picture`, `user_id`, `facebook`, `googlePlus`, `linkedIn`, `twitter`) VALUES
(1, '', '', '', 1, NULL, NULL, NULL, NULL),
(2, '', '', '', 2, '', '', '', '');

-- --------------------------------------------------------

--
-- Structure de la table `kanboard_card`
--

CREATE TABLE IF NOT EXISTS `kanboard_card` (
`id` int(11) NOT NULL,
  `title` varchar(80) NOT NULL,
  `comment` longtext NOT NULL,
  `deadline` date DEFAULT NULL,
  `phase` varchar(50) NOT NULL,
  `order` smallint(6) NOT NULL,
  `created` datetime NOT NULL,
  `updated` datetime NOT NULL,
  `assigned_id` int(11) DEFAULT NULL,
  `company_id` int(11) NOT NULL,
  `creator_id` int(11) DEFAULT NULL,
  `state` tinyint(1) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `kanboard_comment`
--

CREATE TABLE IF NOT EXISTS `kanboard_comment` (
`id` int(11) NOT NULL,
  `comment` longtext NOT NULL,
  `created` datetime NOT NULL,
  `updated` datetime NOT NULL,
  `card_id` int(11) NOT NULL,
  `creator_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `kpi_kpi`
--

CREATE TABLE IF NOT EXISTS `kpi_kpi` (
`id` int(11) NOT NULL,
  `level` int(11) NOT NULL,
  `period_start` datetime DEFAULT NULL,
  `comment` longtext NOT NULL,
  `company_id` int(11) NOT NULL,
  `type` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `mentor_mentor`
--

CREATE TABLE IF NOT EXISTS `mentor_mentor` (
  `userprofile_ptr_id` int(11) NOT NULL,
  `about` varchar(2000) NOT NULL,
  `type` varchar(20),
  `url` varchar(200)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `mentor_mentor_expertise`
--

CREATE TABLE IF NOT EXISTS `mentor_mentor_expertise` (
`id` int(11) NOT NULL,
  `mentor_id` int(11) NOT NULL,
  `expertise_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `valuePropositionCanvas_valuepropositioncanvaselement`
--

CREATE TABLE IF NOT EXISTS `valuePropositionCanvas_valuepropositioncanvaselement` (
`id` int(11) NOT NULL,
  `title` varchar(200) NOT NULL,
  `comment` longtext NOT NULL,
  `date` datetime NOT NULL,
  `company_id` int(11) NOT NULL,
  `type_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `valuePropositionCanvas_valuepropositioncanvastype`
--

CREATE TABLE IF NOT EXISTS `valuePropositionCanvas_valuepropositioncanvastype` (
`id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Index pour les tables exportées
--

--
-- Index pour la table `auth_group`
--
ALTER TABLE `auth_group`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `name` (`name`);

--
-- Index pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `group_id` (`group_id`,`permission_id`), ADD KEY `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` (`permission_id`);

--
-- Index pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `content_type_id` (`content_type_id`,`codename`);

--
-- Index pour la table `auth_user`
--
ALTER TABLE `auth_user`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `username` (`username`);

--
-- Index pour la table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `user_id` (`user_id`,`group_id`), ADD KEY `auth_user_groups_group_id_30a071c9_fk_auth_group_id` (`group_id`);

--
-- Index pour la table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `user_id` (`user_id`,`permission_id`), ADD KEY `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` (`permission_id`);

--
-- Index pour la table `businessCanvas_archive`
--
ALTER TABLE `businessCanvas_archive`
 ADD PRIMARY KEY (`id`), ADD KEY `businessCanvas_archive_company_id_5b60770d_fk_company_company_id` (`company_id`);

--
-- Index pour la table `businessCanvas_archive_elements`
--
ALTER TABLE `businessCanvas_archive_elements`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `archive_id` (`archive_id`,`businesscanvaselement_id`), ADD KEY `D695caad242210a282ce659e581f55f4` (`businesscanvaselement_id`);

--
-- Index pour la table `businessCanvas_businesscanvaselement`
--
ALTER TABLE `businessCanvas_businesscanvaselement`
 ADD PRIMARY KEY (`id`), ADD KEY `businessCanvas_busines_company_id_37e33d43_fk_company_company_id` (`company_id`);

--
-- Index pour la table `company_company`
--
ALTER TABLE `company_company`
 ADD PRIMARY KEY (`id`), ADD KEY `company_company_bc2a574f` (`companyStatus_id`);

--
-- Index pour la table `company_companystatus`
--
ALTER TABLE `company_companystatus`
 ADD PRIMARY KEY (`id`);

--
-- Index pour la table `company_company_founders`
--
ALTER TABLE `company_company_founders`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `company_id` (`company_id`,`founder_id`), ADD KEY `compan_founder_id_538a7b60_fk_founder_founder_userprofile_ptr_id` (`founder_id`);

--
-- Index pour la table `company_company_mentors`
--
ALTER TABLE `company_company_mentors`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `company_id` (`company_id`,`mentor_id`), ADD KEY `company_c_mentor_id_79758e62_fk_mentor_mentor_userprofile_ptr_id` (`mentor_id`);

--
-- Index pour la table `company_presence`
--
ALTER TABLE `company_presence`
 ADD PRIMARY KEY (`id`);

--
-- Index pour la table `company_presence_company`
--
ALTER TABLE `company_presence_company`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `presence_id` (`presence_id`,`company_id`), ADD KEY `company_presence_compa_company_id_69e57fad_fk_company_company_id` (`company_id`);

--
-- Index pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
 ADD PRIMARY KEY (`id`), ADD KEY `django_admin__content_type_id_5151027a_fk_django_content_type_id` (`content_type_id`), ADD KEY `django_admin_log_user_id_1c5f563_fk_auth_user_id` (`user_id`);

--
-- Index pour la table `django_content_type`
--
ALTER TABLE `django_content_type`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `django_content_type_app_label_3ec8c61c_uniq` (`app_label`,`model`);

--
-- Index pour la table `django_migrations`
--
ALTER TABLE `django_migrations`
 ADD PRIMARY KEY (`id`);

--
-- Index pour la table `django_session`
--
ALTER TABLE `django_session`
 ADD PRIMARY KEY (`session_key`), ADD KEY `django_session_de54fa62` (`expire_date`);

--
-- Index pour la table `django_site`
--
ALTER TABLE `django_site`
 ADD PRIMARY KEY (`id`);

--
-- Index pour la table `experiment_customerexperiment`
--
ALTER TABLE `experiment_customerexperiment`
 ADD PRIMARY KEY (`id`), ADD KEY `experiment_customerexp_company_id_2798546c_fk_company_company_id` (`company_id`);

--
-- Index pour la table `finance_bourse`
--
ALTER TABLE `finance_bourse`
 ADD PRIMARY KEY (`id`), ADD KEY `finance_bourse_company_id_7cad3d97_fk_company_company_id` (`company_id`);

--
-- Index pour la table `finance_investissement`
--
ALTER TABLE `finance_investissement`
 ADD PRIMARY KEY (`id`), ADD KEY `finance_investissement_company_id_589bd4e0_fk_company_company_id` (`company_id`);

--
-- Index pour la table `finance_pret`
--
ALTER TABLE `finance_pret`
 ADD PRIMARY KEY (`id`), ADD KEY `finance_pret_company_id_7cecf0f8_fk_company_company_id` (`company_id`);

--
-- Index pour la table `finance_subvention`
--
ALTER TABLE `finance_subvention`
 ADD PRIMARY KEY (`id`), ADD KEY `finance_subvention_company_id_6f9e4ebc_fk_company_company_id` (`company_id`);

--
-- Index pour la table `finance_vente`
--
ALTER TABLE `finance_vente`
 ADD PRIMARY KEY (`id`), ADD KEY `finance_vente_company_id_78db5858_fk_company_company_id` (`company_id`);

--
-- Index pour la table `founder_founder`
--
ALTER TABLE `founder_founder`
 ADD PRIMARY KEY (`userprofile_ptr_id`), ADD KEY `founder_founder_education_id_4eafa1d3_fk_home_education_id` (`education_id`);

--
-- Index pour la table `founder_founder_expertise`
--
ALTER TABLE `founder_founder_expertise`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `founder_id` (`founder_id`,`expertise_id`), ADD KEY `founder_founder_exper_expertise_id_6816930e_fk_home_expertise_id` (`expertise_id`);

--
-- Index pour la table `home_education`
--
ALTER TABLE `home_education`
 ADD PRIMARY KEY (`id`);

--
-- Index pour la table `home_expertise`
--
ALTER TABLE `home_expertise`
 ADD PRIMARY KEY (`id`);

--
-- Index pour la table `home_floorplan`
--
ALTER TABLE `home_floorplan`
 ADD PRIMARY KEY (`id`);

--
-- Index pour la table `home_userprofile`
--
ALTER TABLE `home_userprofile`
 ADD PRIMARY KEY (`userProfile_id`), ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Index pour la table `kanboard_card`
--
ALTER TABLE `kanboard_card`
 ADD PRIMARY KEY (`id`), ADD KEY `kanboard_card_company_id_6c088822_fk_company_company_id` (`company_id`), ADD KEY `kanbo_assigned_id_221423d0_fk_founder_founder_userprofile_ptr_id` (`assigned_id`), ADD KEY `kanboard_card_creator_id_44ca5de5_fk_auth_user_id` (`creator_id`);

--
-- Index pour la table `kanboard_comment`
--
ALTER TABLE `kanboard_comment`
 ADD PRIMARY KEY (`id`), ADD KEY `kanboard_comment_card_id_6fd9ccac_fk_kanboard_card_id` (`card_id`), ADD KEY `kanboard_comment_creator_id_4d4dc29b_fk_auth_user_id` (`creator_id`);

--
-- Index pour la table `kpi_kpi`
--
ALTER TABLE `kpi_kpi`
 ADD PRIMARY KEY (`id`), ADD KEY `kpi_kpi_company_id_1cc137f6_fk_company_company_id` (`company_id`);

--
-- Index pour la table `mentor_mentor`
--
ALTER TABLE `mentor_mentor`
 ADD PRIMARY KEY (`userprofile_ptr_id`);

--
-- Index pour la table `mentor_mentor_expertise`
--
ALTER TABLE `mentor_mentor_expertise`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `mentor_id` (`mentor_id`,`expertise_id`), ADD KEY `mentor_mentor_experti_expertise_id_21d0c124_fk_home_expertise_id` (`expertise_id`);

--
-- Index pour la table `valuePropositionCanvas_valuepropositioncanvaselement`
--
ALTER TABLE `valuePropositionCanvas_valuepropositioncanvaselement`
 ADD PRIMARY KEY (`id`), ADD KEY `valuePropositionCanvas_company_id_493250dd_fk_company_company_id` (`company_id`), ADD KEY `valuePropositionCanvas_valuepropositioncanvaselement_94757cae` (`type_id`);

--
-- Index pour la table `valuePropositionCanvas_valuepropositioncanvastype`
--
ALTER TABLE `valuePropositionCanvas_valuepropositioncanvastype`
 ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables exportées
--

--
-- AUTO_INCREMENT pour la table `auth_group`
--
ALTER TABLE `auth_group`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=88;
--
-- AUTO_INCREMENT pour la table `auth_user`
--
ALTER TABLE `auth_user`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT pour la table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT pour la table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `businessCanvas_archive`
--
ALTER TABLE `businessCanvas_archive`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `businessCanvas_archive_elements`
--
ALTER TABLE `businessCanvas_archive_elements`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `businessCanvas_businesscanvaselement`
--
ALTER TABLE `businessCanvas_businesscanvaselement`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `company_company`
--
ALTER TABLE `company_company`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT pour la table `company_companystatus`
--
ALTER TABLE `company_companystatus`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT pour la table `company_company_founders`
--
ALTER TABLE `company_company_founders`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT pour la table `company_company_mentors`
--
ALTER TABLE `company_company_mentors`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `company_presence`
--
ALTER TABLE `company_presence`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT pour la table `company_presence_company`
--
ALTER TABLE `company_presence_company`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=10;
--
-- AUTO_INCREMENT pour la table `django_content_type`
--
ALTER TABLE `django_content_type`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=30;
--
-- AUTO_INCREMENT pour la table `django_migrations`
--
ALTER TABLE `django_migrations`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=70;
--
-- AUTO_INCREMENT pour la table `django_site`
--
ALTER TABLE `django_site`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT pour la table `experiment_customerexperiment`
--
ALTER TABLE `experiment_customerexperiment`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `finance_bourse`
--
ALTER TABLE `finance_bourse`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `finance_investissement`
--
ALTER TABLE `finance_investissement`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `finance_pret`
--
ALTER TABLE `finance_pret`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `finance_subvention`
--
ALTER TABLE `finance_subvention`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `finance_vente`
--
ALTER TABLE `finance_vente`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `founder_founder_expertise`
--
ALTER TABLE `founder_founder_expertise`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `home_education`
--
ALTER TABLE `home_education`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `home_expertise`
--
ALTER TABLE `home_expertise`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `home_floorplan`
--
ALTER TABLE `home_floorplan`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `home_userprofile`
--
ALTER TABLE `home_userprofile`
MODIFY `userProfile_id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT pour la table `kanboard_card`
--
ALTER TABLE `kanboard_card`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT pour la table `kanboard_comment`
--
ALTER TABLE `kanboard_comment`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `kpi_kpi`
--
ALTER TABLE `kpi_kpi`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `mentor_mentor_expertise`
--
ALTER TABLE `mentor_mentor_expertise`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `valuePropositionCanvas_valuepropositioncanvaselement`
--
ALTER TABLE `valuePropositionCanvas_valuepropositioncanvaselement`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `valuePropositionCanvas_valuepropositioncanvastype`
--
ALTER TABLE `valuePropositionCanvas_valuepropositioncanvastype`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- Contraintes pour les tables exportées
--

--
-- Contraintes pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
ADD CONSTRAINT `auth_group_permissions_group_id_58c48ba9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
ADD CONSTRAINT `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Contraintes pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
ADD CONSTRAINT `auth_permissi_content_type_id_51277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Contraintes pour la table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
ADD CONSTRAINT `auth_user_groups_group_id_30a071c9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
ADD CONSTRAINT `auth_user_groups_user_id_24702650_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
ADD CONSTRAINT `auth_user_user_permissions_user_id_7cd7acb6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
ADD CONSTRAINT `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Contraintes pour la table `businessCanvas_archive`
--
ALTER TABLE `businessCanvas_archive`
ADD CONSTRAINT `businessCanvas_archive_company_id_5b60770d_fk_company_company_id` FOREIGN KEY (`company_id`) REFERENCES `company_company` (`id`);

--
-- Contraintes pour la table `businessCanvas_archive_elements`
--
ALTER TABLE `businessCanvas_archive_elements`
ADD CONSTRAINT `businessCanvas__archive_id_715e01eb_fk_businessCanvas_archive_id` FOREIGN KEY (`archive_id`) REFERENCES `businessCanvas_archive` (`id`),
ADD CONSTRAINT `D695caad242210a282ce659e581f55f4` FOREIGN KEY (`businesscanvaselement_id`) REFERENCES `businessCanvas_businesscanvaselement` (`id`);

--
-- Contraintes pour la table `businessCanvas_businesscanvaselement`
--
ALTER TABLE `businessCanvas_businesscanvaselement`
ADD CONSTRAINT `businessCanvas_busines_company_id_37e33d43_fk_company_company_id` FOREIGN KEY (`company_id`) REFERENCES `company_company` (`id`);

--
-- Contraintes pour la table `company_company`
--
ALTER TABLE `company_company`
ADD CONSTRAINT `company_co_companyStatus_id_508e7666_fk_company_companystatus_id` FOREIGN KEY (`companyStatus_id`) REFERENCES `company_companystatus` (`id`);

--
-- Contraintes pour la table `company_company_founders`
--
ALTER TABLE `company_company_founders`
ADD CONSTRAINT `company_company_founde_company_id_11856284_fk_company_company_id` FOREIGN KEY (`company_id`) REFERENCES `company_company` (`id`),
ADD CONSTRAINT `compan_founder_id_538a7b60_fk_founder_founder_userprofile_ptr_id` FOREIGN KEY (`founder_id`) REFERENCES `founder_founder` (`userprofile_ptr_id`);

--
-- Contraintes pour la table `company_company_mentors`
--
ALTER TABLE `company_company_mentors`
ADD CONSTRAINT `company_company_mentor_company_id_120492eb_fk_company_company_id` FOREIGN KEY (`company_id`) REFERENCES `company_company` (`id`),
ADD CONSTRAINT `company_c_mentor_id_79758e62_fk_mentor_mentor_userprofile_ptr_id` FOREIGN KEY (`mentor_id`) REFERENCES `mentor_mentor` (`userprofile_ptr_id`);

--
-- Contraintes pour la table `company_presence_company`
--
ALTER TABLE `company_presence_company`
ADD CONSTRAINT `company_presence_compa_company_id_69e57fad_fk_company_company_id` FOREIGN KEY (`company_id`) REFERENCES `company_company` (`id`),
ADD CONSTRAINT `company_presence_com_presence_id_171b0006_fk_company_presence_id` FOREIGN KEY (`presence_id`) REFERENCES `company_presence` (`id`);

--
-- Contraintes pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
ADD CONSTRAINT `django_admin_log_user_id_1c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
ADD CONSTRAINT `django_admin__content_type_id_5151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Contraintes pour la table `experiment_customerexperiment`
--
ALTER TABLE `experiment_customerexperiment`
ADD CONSTRAINT `experiment_customerexp_company_id_2798546c_fk_company_company_id` FOREIGN KEY (`company_id`) REFERENCES `company_company` (`id`);

--
-- Contraintes pour la table `finance_bourse`
--
ALTER TABLE `finance_bourse`
ADD CONSTRAINT `finance_bourse_company_id_7cad3d97_fk_company_company_id` FOREIGN KEY (`company_id`) REFERENCES `company_company` (`id`);

--
-- Contraintes pour la table `finance_investissement`
--
ALTER TABLE `finance_investissement`
ADD CONSTRAINT `finance_investissement_company_id_589bd4e0_fk_company_company_id` FOREIGN KEY (`company_id`) REFERENCES `company_company` (`id`);

--
-- Contraintes pour la table `finance_pret`
--
ALTER TABLE `finance_pret`
ADD CONSTRAINT `finance_pret_company_id_7cecf0f8_fk_company_company_id` FOREIGN KEY (`company_id`) REFERENCES `company_company` (`id`);

--
-- Contraintes pour la table `finance_subvention`
--
ALTER TABLE `finance_subvention`
ADD CONSTRAINT `finance_subvention_company_id_6f9e4ebc_fk_company_company_id` FOREIGN KEY (`company_id`) REFERENCES `company_company` (`id`);

--
-- Contraintes pour la table `finance_vente`
--
ALTER TABLE `finance_vente`
ADD CONSTRAINT `finance_vente_company_id_78db5858_fk_company_company_id` FOREIGN KEY (`company_id`) REFERENCES `company_company` (`id`);

--
-- Contraintes pour la table `founder_founder`
--
ALTER TABLE `founder_founder`
ADD CONSTRAINT `founder_founder_education_id_4eafa1d3_fk_home_education_id` FOREIGN KEY (`education_id`) REFERENCES `home_education` (`id`),
ADD CONSTRAINT `f_userprofile_ptr_id_65d8306c_fk_home_userprofile_userProfile_id` FOREIGN KEY (`userprofile_ptr_id`) REFERENCES `home_userprofile` (`userProfile_id`);

--
-- Contraintes pour la table `founder_founder_expertise`
--
ALTER TABLE `founder_founder_expertise`
ADD CONSTRAINT `founder_founder_exper_expertise_id_6816930e_fk_home_expertise_id` FOREIGN KEY (`expertise_id`) REFERENCES `home_expertise` (`id`),
ADD CONSTRAINT `founde_founder_id_3e3ea94c_fk_founder_founder_userprofile_ptr_id` FOREIGN KEY (`founder_id`) REFERENCES `founder_founder` (`userprofile_ptr_id`);

--
-- Contraintes pour la table `home_userprofile`
--
ALTER TABLE `home_userprofile`
ADD CONSTRAINT `home_userprofile_user_id_7bb7d5ad_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `kanboard_card`
--
ALTER TABLE `kanboard_card`
ADD CONSTRAINT `kanboard_card_company_id_6c088822_fk_company_company_id` FOREIGN KEY (`company_id`) REFERENCES `company_company` (`id`),
ADD CONSTRAINT `kanboard_card_creator_id_44ca5de5_fk_auth_user_id` FOREIGN KEY (`creator_id`) REFERENCES `auth_user` (`id`),
ADD CONSTRAINT `kanbo_assigned_id_221423d0_fk_founder_founder_userprofile_ptr_id` FOREIGN KEY (`assigned_id`) REFERENCES `founder_founder` (`userprofile_ptr_id`);

--
-- Contraintes pour la table `kanboard_comment`
--
ALTER TABLE `kanboard_comment`
ADD CONSTRAINT `kanboard_comment_card_id_6fd9ccac_fk_kanboard_card_id` FOREIGN KEY (`card_id`) REFERENCES `kanboard_card` (`id`),
ADD CONSTRAINT `kanboard_comment_creator_id_4d4dc29b_fk_auth_user_id` FOREIGN KEY (`creator_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `kpi_kpi`
--
ALTER TABLE `kpi_kpi`
ADD CONSTRAINT `kpi_kpi_company_id_1cc137f6_fk_company_company_id` FOREIGN KEY (`company_id`) REFERENCES `company_company` (`id`);

--
-- Contraintes pour la table `mentor_mentor`
--
ALTER TABLE `mentor_mentor`
ADD CONSTRAINT `m_userprofile_ptr_id_3d77364a_fk_home_userprofile_userProfile_id` FOREIGN KEY (`userprofile_ptr_id`) REFERENCES `home_userprofile` (`userProfile_id`);

--
-- Contraintes pour la table `mentor_mentor_expertise`
--
ALTER TABLE `mentor_mentor_expertise`
ADD CONSTRAINT `mentor_mentor_experti_expertise_id_21d0c124_fk_home_expertise_id` FOREIGN KEY (`expertise_id`) REFERENCES `home_expertise` (`id`),
ADD CONSTRAINT `mentor_men_mentor_id_992f8d3_fk_mentor_mentor_userprofile_ptr_id` FOREIGN KEY (`mentor_id`) REFERENCES `mentor_mentor` (`userprofile_ptr_id`);

--
-- Contraintes pour la table `valuePropositionCanvas_valuepropositioncanvaselement`
--
ALTER TABLE `valuePropositionCanvas_valuepropositioncanvaselement`
ADD CONSTRAINT `c9014259bcb5492064e66ea91ecb7a0b` FOREIGN KEY (`type_id`) REFERENCES `valuePropositionCanvas_valuepropositioncanvastype` (`id`),
ADD CONSTRAINT `valuePropositionCanvas_company_id_493250dd_fk_company_company_id` FOREIGN KEY (`company_id`) REFERENCES `company_company` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
