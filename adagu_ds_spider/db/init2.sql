USE `pluto`;

-- -----------------------------------------------------
-- Table `pluto`.`ds_league`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pluto`.`ds_league`;

CREATE TABLE IF NOT EXISTS `pluto`.`ds_league`(
  `id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL COMMENT '联赛名称',
  `name_short` VARCHAR(45) NULL COMMENT '联赛名称',
  `url` VARCHAR(400) NULL COMMENT '联赛url',
  `created_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `ds_league_id` (`id` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
  ;

-- -----------------------------------------------------
-- Table `pluto`.`ds_team`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pluto`.`ds_team`;

CREATE TABLE IF NOT EXISTS `pluto`.`ds_team`(
  `id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL COMMENT '球队名称',
  `name_short` VARCHAR(45) NULL COMMENT '球队名称',
  `url` VARCHAR(400) NULL COMMENT '球队url',
  `created_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `ds_team_id` (`id` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

-- -----------------------------------------------------
-- Table `pluto`.`ds_match`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pluto`.`ds_match` ;

CREATE TABLE IF NOT EXISTS `pluto`.`ds_match`(
  `id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `league_id` BIGINT(20) UNSIGNED NOT NULL,
  `start_time` DATETIME NOT NULL COMMENT '开赛时间',
  `home_id` BIGINT(20) UNSIGNED NOT NULL COMMENT '主队id',
  `away_id` BIGINT(20) UNSIGNED NOT NULL COMMENT '客队id',
  `home_score` SMALLINT(5) NULL COMMENT '主队进球数',
  `away_score` SMALLINT(5) NULL COMMENT '客队进球数',
  `url` VARCHAR(400) NULL COMMENT '比赛url',
  `created_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `ds_match_id` (`id` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

-- -----------------------------------------------------
-- Table `pluto`.`ds_match_event`
-- 现场数据
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pluto`.`ds_match_event`;

CREATE TABLE IF NOT EXISTS `pluto`.`ds_match_event`(
  `id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `match_id` BIGINT(20) UNSIGNED NOT NULL,
  `type` char(1) NOT NULL COMMENT '事件类型:o-射正,f-射偏,g-进球,d-危险进攻,a-进攻,c-角球',
  `home_away` char(8) NULL COMMENT '主队(H)/客队(A)',
  `team_id` BIGINT(20) UNSIGNED NULL,
  `team_name` VARCHAR(45) NOT NULL COMMENT '球队名称',
  `timestamp` SMALLINT(5) UNSIGNED NOT NULL COMMENT '比赛时间戳（单位分钟）',
  `v` INT(5) NOT NULL COMMENT '值',
  `info` VARCHAR(45) NULL COMMENT '待求证字段',
  `created_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `ds_match_event_id` (`id` ASC),
  INDEX `ds_match_event_idx_u` (`match_id` ASC, `team_name` ASC , `timestamp` ASC , `info` ASC),
  INDEX `ds_match_event_idx` (`match_id` ASC, `team_name` ASC , `timestamp` ASC),
  INDEX `ds_match_event_match_id` (`match_id` ASC)
  )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

-- -----------------------------------------------------
-- Table `pluto`.`ds_match_event_text`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pluto`.`ds_match_event_text`;

CREATE TABLE IF NOT EXISTS `pluto`.`ds_match_event_text`(
  `id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `match_id` BIGINT(20) UNSIGNED NOT NULL,
  `home_away` CHAR(1) NULL COMMENT '主队(H)/客队(A)',
  `team_id` BIGINT(20) UNSIGNED NULL,
  `team_name` VARCHAR(45) NULL COMMENT '球队名称',
  `timestamp` SMALLINT(5) UNSIGNED NULL COMMENT '比赛时间戳（单位分钟）',
  `txt` VARCHAR(400) NOT NULL COMMENT '事件内容',
  `info` VARCHAR(45) NULL COMMENT '待求证字段',
  `created_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `ds_match_event_text_id` (`id` ASC),
  INDEX `ds_match_event_text_idx_u` (`match_id` ASC, `team_name` ASC , `timestamp` ASC , `info` ASC),
  INDEX `ds_match_event_text_idx` (`match_id` ASC, `team_name` ASC , `timestamp` ASC),
  INDEX `ds_match_event_text_match_id` (`match_id` ASC)
  )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;
