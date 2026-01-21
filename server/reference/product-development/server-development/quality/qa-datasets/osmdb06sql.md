---
description: >-
  Information on the standardized datasets and database dumps used for
  OpenStreetMap.
---

# osmdb06.sql

Below is the schema described in the [OpenStreetMap Dataset Use](openstreetmap-dataset.md) article. To use, copy everything in the box below into a file called '`osmdb06.sql`', then continue with the instructions.

```
-- phpMyAdmin SQL Dump
-- version 2.11.9.3
-- http://www.phpmyadmin.net
--
-- Хост: mysql.leonenko.info
-- Час стварэньня: 16 Сак 2009, 15:12
-- Вэрсія сэрвэра: 5.0.67
-- Вэрсія PHP: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- База дадзеных: `osmapper_belarus`
--

-- --------------------------------------------------------

--
-- Структура табліцы `changesets`
--

DROP TABLE IF EXISTS `changesets`;
CREATE TABLE IF NOT EXISTS `changesets` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `user_id` BIGINT(20) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `min_lat` INT(11) DEFAULT NULL,
  `max_lat` INT(11) DEFAULT NULL,
  `min_lon` INT(11) DEFAULT NULL,
  `max_lon` INT(11) DEFAULT NULL,
  `closed_at` DATETIME NOT NULL,
  `num_changes` INT(11) NOT NULL DEFAULT '0',
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=20103 ;

-- --------------------------------------------------------

--
-- Структура табліцы `changeset_tags`
--

DROP TABLE IF EXISTS `changeset_tags`;
CREATE TABLE IF NOT EXISTS `changeset_tags` (
  `id` BIGINT(64) NOT NULL,
  `k` VARCHAR(255) NOT NULL DEFAULT '',
  `v` VARCHAR(255) NOT NULL DEFAULT '',
  KEY `changeset_tags_id_idx` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура табліцы `current_nodes`
--

DROP TABLE IF EXISTS `current_nodes`;
CREATE TABLE IF NOT EXISTS `current_nodes` (
  `id` BIGINT(64) NOT NULL AUTO_INCREMENT,
  `latitude` INT(11) NOT NULL,
  `longitude` INT(11) NOT NULL,
  `changeset_id` BIGINT(20) NOT NULL,
  `visible` TINYINT(1) NOT NULL,
  `timestamp` DATETIME NOT NULL,
  `tile` INT(10) UNSIGNED NOT NULL,
  `version` BIGINT(20) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `current_nodes_timestamp_idx` (`timestamp`),
  KEY `current_nodes_tile_idx` (`tile`),
  KEY `changeset_id` (`changeset_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=348816842 ;

-- --------------------------------------------------------

--
-- Структура табліцы `current_node_tags`
--

DROP TABLE IF EXISTS `current_node_tags`;
CREATE TABLE IF NOT EXISTS `current_node_tags` (
  `id` BIGINT(64) NOT NULL,
  `k` VARCHAR(255) NOT NULL DEFAULT '',
  `v` VARCHAR(255) NOT NULL DEFAULT '',
  PRIMARY KEY  (`id`,`k`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура табліцы `current_relations`
--

DROP TABLE IF EXISTS `current_relations`;
CREATE TABLE IF NOT EXISTS `current_relations` (
  `id` BIGINT(64) NOT NULL AUTO_INCREMENT,
  `changeset_id` BIGINT(20) NOT NULL,
  `timestamp` DATETIME NOT NULL,
  `visible` TINYINT(1) NOT NULL,
  `version` BIGINT(20) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `current_relations_timestamp_idx` (`timestamp`),
  KEY `changeset_id` (`changeset_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=80283 ;

-- --------------------------------------------------------

--
-- Структура табліцы `current_relation_members`
--

DROP TABLE IF EXISTS `current_relation_members`;
CREATE TABLE IF NOT EXISTS `current_relation_members` (
  `id` BIGINT(64) NOT NULL,
  `member_type` ENUM('node','way','relation') NOT NULL DEFAULT 'node',
  `member_id` BIGINT(11) NOT NULL,
  `member_role` VARCHAR(255) NOT NULL DEFAULT '',
  `sequence_id` INT(11) NOT NULL DEFAULT '0',
  PRIMARY KEY  (`id`,`member_type`,`member_id`,`member_role`,`sequence_id`),
  KEY `current_relation_members_member_idx` (`member_type`,`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура табліцы `current_relation_tags`
--

DROP TABLE IF EXISTS `current_relation_tags`;
CREATE TABLE IF NOT EXISTS `current_relation_tags` (
  `id` BIGINT(64) NOT NULL,
  `k` VARCHAR(255) NOT NULL DEFAULT '',
  `v` VARCHAR(255) NOT NULL DEFAULT '',
  PRIMARY KEY  (`id`,`k`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура табліцы `current_ways`
--

DROP TABLE IF EXISTS `current_ways`;
CREATE TABLE IF NOT EXISTS `current_ways` (
  `id` BIGINT(64) NOT NULL AUTO_INCREMENT,
  `changeset_id` BIGINT(20) NOT NULL,
  `timestamp` DATETIME NOT NULL,
  `visible` TINYINT(1) NOT NULL,
  `version` BIGINT(20) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `current_ways_timestamp_idx` (`timestamp`),
  KEY `changeset_id` (`changeset_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=31336923 ;

-- --------------------------------------------------------

--
-- Структура табліцы `current_way_nodes`
--

DROP TABLE IF EXISTS `current_way_nodes`;
CREATE TABLE IF NOT EXISTS `current_way_nodes` (
  `id` BIGINT(64) NOT NULL,
  `node_id` BIGINT(64) NOT NULL,
  `sequence_id` BIGINT(11) NOT NULL,
  PRIMARY KEY  (`id`,`sequence_id`),
  KEY `current_way_nodes_node_idx` (`node_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура табліцы `current_way_tags`
--

DROP TABLE IF EXISTS `current_way_tags`;
CREATE TABLE IF NOT EXISTS `current_way_tags` (
  `id` BIGINT(64) NOT NULL,
  `k` VARCHAR(255) NOT NULL DEFAULT '',
  `v` VARCHAR(255) NOT NULL DEFAULT '',
  PRIMARY KEY  (`id`,`k`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура табліцы `diary_comments`
--

DROP TABLE IF EXISTS `diary_comments`;
CREATE TABLE IF NOT EXISTS `diary_comments` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `diary_entry_id` BIGINT(20) NOT NULL,
  `user_id` BIGINT(20) NOT NULL,
  `body` text NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `diary_comments_entry_id_idx` (`diary_entry_id`,`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура табліцы `diary_entries`
--

DROP TABLE IF EXISTS `diary_entries`;
CREATE TABLE IF NOT EXISTS `diary_entries` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `user_id` BIGINT(20) NOT NULL,
  `title` VARCHAR(255) NOT NULL,
  `body` text NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  `latitude` DOUBLE DEFAULT NULL,
  `longitude` DOUBLE DEFAULT NULL,
  `language` VARCHAR(3) DEFAULT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура табліцы `friends`
--

DROP TABLE IF EXISTS `friends`;
CREATE TABLE IF NOT EXISTS `friends` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `user_id` BIGINT(20) NOT NULL,
  `friend_user_id` BIGINT(20) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `user_id_idx` (`friend_user_id`),
  KEY `friends_user_id_idx` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура табліцы `gps_points`
--

DROP TABLE IF EXISTS `gps_points`;
CREATE TABLE IF NOT EXISTS `gps_points` (
  `altitude` FLOAT DEFAULT NULL,
  `trackid` INT(11) NOT NULL,
  `latitude` INT(11) NOT NULL,
  `longitude` INT(11) NOT NULL,
  `gpx_id` BIGINT(64) NOT NULL,
  `timestamp` DATETIME DEFAULT NULL,
  `tile` INT(10) UNSIGNED NOT NULL,
  KEY `points_gpxid_idx` (`gpx_id`),
  KEY `points_tile_idx` (`tile`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура табліцы `gpx_files`
--

DROP TABLE IF EXISTS `gpx_files`;
CREATE TABLE IF NOT EXISTS `gpx_files` (
  `id` BIGINT(64) NOT NULL AUTO_INCREMENT,
  `user_id` BIGINT(20) NOT NULL,
  `visible` TINYINT(1) NOT NULL DEFAULT '1',
  `name` VARCHAR(255) NOT NULL DEFAULT '',
  `size` BIGINT(20) DEFAULT NULL,
  `latitude` DOUBLE DEFAULT NULL,
  `longitude` DOUBLE DEFAULT NULL,
  `timestamp` DATETIME NOT NULL,
  `public` TINYINT(1) NOT NULL DEFAULT '1',
  `description` VARCHAR(255) NOT NULL DEFAULT '',
  `inserted` TINYINT(1) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `gpx_files_timestamp_idx` (`timestamp`),
  KEY `gpx_files_visible_public_idx` (`visible`,`public`),
  KEY `gpx_files_user_id_idx` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура табліцы `gpx_file_tags`
--

DROP TABLE IF EXISTS `gpx_file_tags`;
CREATE TABLE IF NOT EXISTS `gpx_file_tags` (
  `gpx_id` BIGINT(64) NOT NULL DEFAULT '0',
  `tag` VARCHAR(255) NOT NULL,
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY  (`id`),
  KEY `gpx_file_tags_gpxid_idx` (`gpx_id`),
  KEY `gpx_file_tags_tag_idx` (`tag`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура табліцы `messages`
--

DROP TABLE IF EXISTS `messages`;
CREATE TABLE IF NOT EXISTS `messages` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `from_user_id` BIGINT(20) NOT NULL,
  `title` VARCHAR(255) NOT NULL,
  `body` text NOT NULL,
  `sent_on` DATETIME NOT NULL,
  `message_read` TINYINT(1) NOT NULL DEFAULT '0',
  `to_user_id` BIGINT(20) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `messages_to_user_id_idx` (`to_user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура табліцы `nodes`
--

DROP TABLE IF EXISTS `nodes`;
CREATE TABLE IF NOT EXISTS `nodes` (
  `id` BIGINT(64) NOT NULL,
  `latitude` INT(11) NOT NULL,
  `longitude` INT(11) NOT NULL,
  `changeset_id` BIGINT(20) NOT NULL,
  `visible` TINYINT(1) NOT NULL,
  `timestamp` DATETIME NOT NULL,
  `tile` INT(10) UNSIGNED NOT NULL,
  `version` BIGINT(20) NOT NULL,
  PRIMARY KEY  (`id`,`version`),
  KEY `nodes_timestamp_idx` (`timestamp`),
  KEY `nodes_tile_idx` (`tile`),
  KEY `changeset_id` (`changeset_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура табліцы `node_tags`
--

DROP TABLE IF EXISTS `node_tags`;
CREATE TABLE IF NOT EXISTS `node_tags` (
  `id` BIGINT(64) NOT NULL,
  `version` BIGINT(20) NOT NULL,
  `k` VARCHAR(255) NOT NULL DEFAULT '',
  `v` VARCHAR(255) NOT NULL DEFAULT '',
  PRIMARY KEY  (`id`,`version`,`k`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура табліцы `relations`
--

DROP TABLE IF EXISTS `relations`;
CREATE TABLE IF NOT EXISTS `relations` (
  `id` BIGINT(64) NOT NULL DEFAULT '0',
  `changeset_id` BIGINT(20) NOT NULL,
  `timestamp` DATETIME NOT NULL,
  `version` BIGINT(20) NOT NULL,
  `visible` TINYINT(1) NOT NULL DEFAULT '1',
  PRIMARY KEY  (`id`,`version`),
  KEY `relations_timestamp_idx` (`timestamp`),
  KEY `changeset_id` (`changeset_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура табліцы `relation_members`
--

DROP TABLE IF EXISTS `relation_members`;
CREATE TABLE IF NOT EXISTS `relation_members` (
  `id` BIGINT(64) NOT NULL DEFAULT '0',
  `member_type` ENUM('node','way','relation') NOT NULL DEFAULT 'node',
  `member_id` BIGINT(11) NOT NULL,
  `member_role` VARCHAR(255) NOT NULL DEFAULT '',
  `version` BIGINT(20) NOT NULL DEFAULT '0',
  `sequence_id` INT(11) NOT NULL DEFAULT '0',
  PRIMARY KEY  (`id`,`version`,`member_type`,`member_id`,`member_role`,`sequence_id`),
  KEY `relation_members_member_idx` (`member_type`,`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура табліцы `relation_tags`
--

DROP TABLE IF EXISTS `relation_tags`;
CREATE TABLE IF NOT EXISTS `relation_tags` (
  `id` BIGINT(64) NOT NULL DEFAULT '0',
  `k` VARCHAR(255) NOT NULL DEFAULT '',
  `v` VARCHAR(255) NOT NULL DEFAULT '',
  `version` BIGINT(20) NOT NULL,
  PRIMARY KEY  (`id`,`version`,`k`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура табліцы `schema_migrations`
--

DROP TABLE IF EXISTS `schema_migrations`;
CREATE TABLE IF NOT EXISTS `schema_migrations` (
  `version` VARCHAR(255) NOT NULL,
  UNIQUE KEY `unique_schema_migrations` (`version`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура табліцы `sessions`
--

DROP TABLE IF EXISTS `sessions`;
CREATE TABLE IF NOT EXISTS `sessions` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `session_id` VARCHAR(255) DEFAULT NULL,
  `data` text,
  `created_at` DATETIME DEFAULT NULL,
  `updated_at` DATETIME DEFAULT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `sessions_session_id_idx` (`session_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

-- --------------------------------------------------------

--
-- Структура табліцы `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `email` VARCHAR(255) NOT NULL,
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `active` INT(11) NOT NULL DEFAULT '0',
  `pass_crypt` VARCHAR(255) NOT NULL,
  `creation_time` DATETIME NOT NULL,
  `display_name` VARCHAR(255) NOT NULL DEFAULT '',
  `data_public` TINYINT(1) NOT NULL DEFAULT '0',
  `description` text NOT NULL,
  `home_lat` DOUBLE DEFAULT NULL,
  `home_lon` DOUBLE DEFAULT NULL,
  `home_zoom` SMALLINT(6) DEFAULT '3',
  `nearby` INT(11) DEFAULT '50',
  `pass_salt` VARCHAR(255) DEFAULT NULL,
  `image` text,
  `administrator` TINYINT(1) NOT NULL DEFAULT '0',
  `email_valid` TINYINT(1) NOT NULL DEFAULT '0',
  `new_email` VARCHAR(255) DEFAULT NULL,
  `visible` TINYINT(1) NOT NULL DEFAULT '1',
  `creation_ip` VARCHAR(255) DEFAULT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `users_email_idx` (`email`),
  UNIQUE KEY `users_display_name_idx` (`display_name`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=101442 ;

-- --------------------------------------------------------

--
-- Структура табліцы `user_preferences`
--

DROP TABLE IF EXISTS `user_preferences`;
CREATE TABLE IF NOT EXISTS `user_preferences` (
  `user_id` BIGINT(20) NOT NULL,
  `k` VARCHAR(255) NOT NULL,
  `v` VARCHAR(255) NOT NULL,
  PRIMARY KEY  (`user_id`,`k`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура табліцы `user_tokens`
--

DROP TABLE IF EXISTS `user_tokens`;
CREATE TABLE IF NOT EXISTS `user_tokens` (
  `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `user_id` BIGINT(20) NOT NULL,
  `token` VARCHAR(255) NOT NULL,
  `expiry` DATETIME NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `user_tokens_token_idx` (`token`),
  KEY `user_tokens_user_id_idx` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура табліцы `ways`
--

DROP TABLE IF EXISTS `ways`;
CREATE TABLE IF NOT EXISTS `ways` (
  `id` BIGINT(64) NOT NULL DEFAULT '0',
  `changeset_id` BIGINT(20) NOT NULL,
  `timestamp` DATETIME NOT NULL,
  `version` BIGINT(20) NOT NULL,
  `visible` TINYINT(1) NOT NULL DEFAULT '1',
  PRIMARY KEY  (`id`,`version`),
  KEY `ways_timestamp_idx` (`timestamp`),
  KEY `changeset_id` (`changeset_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура табліцы `way_nodes`
--

DROP TABLE IF EXISTS `way_nodes`;
CREATE TABLE IF NOT EXISTS `way_nodes` (
  `id` BIGINT(64) NOT NULL,
  `node_id` BIGINT(64) NOT NULL,
  `version` BIGINT(20) NOT NULL,
  `sequence_id` BIGINT(11) NOT NULL,
  PRIMARY KEY  (`id`,`version`,`sequence_id`),
  KEY `way_nodes_node_idx` (`node_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура табліцы `way_tags`
--

DROP TABLE IF EXISTS `way_tags`;
CREATE TABLE IF NOT EXISTS `way_tags` (
  `id` BIGINT(64) NOT NULL DEFAULT '0',
  `k` VARCHAR(255) NOT NULL,
  `v` VARCHAR(255) NOT NULL,
  `version` BIGINT(20) NOT NULL,
  PRIMARY KEY  (`id`,`version`,`k`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Абмежаваньні для экспартаваных табліц
--

--
-- Абмежаваньні для табліцы `current_nodes`
--
ALTER TABLE `current_nodes`
  ADD CONSTRAINT `current_nodes_ibfk_1` FOREIGN KEY (`changeset_id`) REFERENCES `changesets` (`id`);

--
-- Абмежаваньні для табліцы `current_node_tags`
--
ALTER TABLE `current_node_tags`
  ADD CONSTRAINT `current_node_tags_ibfk_1` FOREIGN KEY (`id`) REFERENCES `current_nodes` (`id`);

--
-- Абмежаваньні для табліцы `current_relations`
--
ALTER TABLE `current_relations`
  ADD CONSTRAINT `current_relations_ibfk_1` FOREIGN KEY (`changeset_id`) REFERENCES `changesets` (`id`);

--
-- Абмежаваньні для табліцы `current_relation_members`
--
ALTER TABLE `current_relation_members`
  ADD CONSTRAINT `current_relation_members_ibfk_1` FOREIGN KEY (`id`) REFERENCES `current_relations` (`id`);

--
-- Абмежаваньні для табліцы `current_relation_tags`
--
ALTER TABLE `current_relation_tags`
  ADD CONSTRAINT `current_relation_tags_ibfk_1` FOREIGN KEY (`id`) REFERENCES `current_relations` (`id`);

--
-- Абмежаваньні для табліцы `current_ways`
--
ALTER TABLE `current_ways`
  ADD CONSTRAINT `current_ways_ibfk_1` FOREIGN KEY (`changeset_id`) REFERENCES `changesets` (`id`);

--
-- Абмежаваньні для табліцы `current_way_nodes`
--
ALTER TABLE `current_way_nodes`
  ADD CONSTRAINT `current_way_nodes_ibfk_2` FOREIGN KEY (`node_id`) REFERENCES `current_nodes` (`id`),
  ADD CONSTRAINT `current_way_nodes_ibfk_1` FOREIGN KEY (`id`) REFERENCES `current_ways` (`id`);

--
-- Абмежаваньні для табліцы `current_way_tags`
--
ALTER TABLE `current_way_tags`
  ADD CONSTRAINT `current_way_tags_ibfk_1` FOREIGN KEY (`id`) REFERENCES `current_ways` (`id`);

--
-- Абмежаваньні для табліцы `nodes`
--
ALTER TABLE `nodes`
  ADD CONSTRAINT `nodes_ibfk_1` FOREIGN KEY (`changeset_id`) REFERENCES `changesets` (`id`);

--
-- Абмежаваньні для табліцы `node_tags`
--
ALTER TABLE `node_tags`
  ADD CONSTRAINT `node_tags_ibfk_1` FOREIGN KEY (`id`, `version`) REFERENCES `nodes` (`id`, `version`);

--
-- Абмежаваньні для табліцы `relations`
--
ALTER TABLE `relations`
  ADD CONSTRAINT `relations_ibfk_1` FOREIGN KEY (`changeset_id`) REFERENCES `changesets` (`id`);

--
-- Абмежаваньні для табліцы `relation_members`
--
ALTER TABLE `relation_members`
  ADD CONSTRAINT `relation_members_ibfk_1` FOREIGN KEY (`id`, `version`) REFERENCES `relations` (`id`, `version`);

--
-- Абмежаваньні для табліцы `relation_tags`
--
ALTER TABLE `relation_tags`
  ADD CONSTRAINT `relation_tags_ibfk_1` FOREIGN KEY (`id`, `version`) REFERENCES `relations` (`id`, `version`);

--
-- Абмежаваньні для табліцы `ways`
--
ALTER TABLE `ways`
  ADD CONSTRAINT `ways_ibfk_1` FOREIGN KEY (`changeset_id`) REFERENCES `changesets` (`id`);

--
-- Абмежаваньні для табліцы `way_nodes`
--
ALTER TABLE `way_nodes`
  ADD CONSTRAINT `way_nodes_ibfk_1` FOREIGN KEY (`id`, `version`) REFERENCES `ways` (`id`, `version`);

--
-- Абмежаваньні для табліцы `way_tags`
--
ALTER TABLE `way_tags`
  ADD CONSTRAINT `way_tags_ibfk_1` FOREIGN KEY (`id`, `version`) REFERENCES `ways` (`id`, `version`);
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
