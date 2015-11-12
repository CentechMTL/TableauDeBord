-- phpMyAdmin SQL Dump
-- version 4.2.12deb2
-- http://www.phpmyadmin.net
--
-- Client :  localhost
-- Généré le :  Jeu 05 Novembre 2015 à 15:20
-- Version du serveur :  5.5.44-0+deb8u1
-- Version de PHP :  5.6.13-0+deb8u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données :  `TableauDeBord`
--

--
-- Contenu de la table `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(2, 'Centech'),
(3, 'Executive');

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

--
-- Contenu de la table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$20000$mam9DkEE8vNU$ipZiplbEkZZSRz/b7NWp0GAi9UnXnEKt4Etda/pwwHI=', '2015-09-23 20:02:29', 1, 'root', '', '', 'rignon.noel@openmailbox.org', 1, 1, '2015-09-18 15:32:12'),
(2, 'pbkdf2_sha256$20000$fUI2vCETUAW0$bTWfbVMZ5/NqDZubaKRssP0YzQ7KEHUMqf+5bK+vZ8A=', '2015-09-20 20:06:02', 0, 'exec', '', '', '', 0, 1, '2015-09-20 20:04:37');

--
-- Contenu de la table `auth_user_groups`
--

INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES
(1, 1, 2),
(2, 2, 3);

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

--
-- Contenu de la table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('z0nbbtecrdubuebi63ksv2egde5x5lnk', 'MDk3MGZmNWMxNzU5MTQxNGY4OTMyOWQ1NzY5NTIyMjNmNzk4ZTY4MDp7Il9hdXRoX3VzZXJfaGFzaCI6IjY5MjEzMzNkZDc2MDkyZTc5NjM4MjhiMzdiMTYyNzMzMzA0N2Y2YjYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiY29tcGFueVNlbGVjdGVkIjoxfQ==', '2015-10-07 20:02:29');

--
-- Contenu de la table `django_site`
--

INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
(1, 'example.com', 'example.com');

--
-- Contenu de la table `home_userprofile`
--

INSERT INTO `home_userprofile` (`userProfile_id`, `phone`, `website`, `picture`, `user_id`, `facebook`, `googlePlus`, `linkedIn`, `twitter`) VALUES
(1, '', '', '', 1, NULL, NULL, NULL, NULL),
(2, '', '', '', 2, '', '', '', '');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
