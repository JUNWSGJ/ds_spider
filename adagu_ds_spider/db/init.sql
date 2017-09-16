USE `adagu`;

-- -----------------------------------------------------
-- Table `adagu`.`ds_league`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `adagu`.`ds_league`;

CREATE TABLE IF NOT EXISTS `adagu`.`ds_league`(
  `id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL COMMENT '联赛名称',
  `name_short` VARCHAR(45) NULL COMMENT '联赛名称',
  `url` VARCHAR(400) NULL COMMENT '联赛url',
  `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `ds_league_id` (`id` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
  ;

-- -----------------------------------------------------
-- Table `adagu`.`ds_team`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `adagu`.`ds_team`;

CREATE TABLE IF NOT EXISTS `adagu`.`ds_team`(
  `id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL COMMENT '球队名称',
  `name_short` VARCHAR(45) NULL COMMENT '球队名称',
  `url` VARCHAR(400) NULL COMMENT '球队url',
  `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `ds_team_id` (`id` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

-- -----------------------------------------------------
-- Table `adagu`.`ds_match`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `adagu`.`ds_match` ;

CREATE TABLE IF NOT EXISTS `adagu`.`ds_match`(
  `id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `league_id` BIGINT(20) UNSIGNED NOT NULL,
  `start_time` DATETIME NOT NULL COMMENT '开赛时间',
  `home_id` BIGINT(20) UNSIGNED NOT NULL COMMENT '主队id',
  `away_id` BIGINT(20) UNSIGNED NOT NULL COMMENT '客队id',
  `home_goal` SMALLINT(5) NULL COMMENT '主队进球数',
  `away_goal` SMALLINT(5) NULL COMMENT '客队进球数',
  `url` VARCHAR(400) NULL COMMENT '比赛url',
  `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `ds_match_id` (`id` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

-- -----------------------------------------------------
-- Table `adagu`.`ds_match_event`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `adagu`.`ds_match_event`;

CREATE TABLE IF NOT EXISTS `adagu`.`ds_match_event`(
  `id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `match_id` BIGINT(20) UNSIGNED NOT NULL,
  `home_away` VARCHAR(8) NULL COMMENT '主队(home)/客队(away)',
  `team_name` VARCHAR(45) NOT NULL COMMENT '球队名称',
  `time_stamp` SMALLINT(5) UNSIGNED NOT NULL COMMENT '比赛时间戳（单位分钟）',
  `type` SMALLINT(2) NOT NULL COMMENT '事件类型(0-角球;1-射正球门;2-射偏球门;3-危险进攻;4-进攻)',
  `v` INT(5) NOT NULL COMMENT '值',
  `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `ds_match_id` (`id` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;
