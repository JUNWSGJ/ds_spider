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
  `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
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
  `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
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
-- Table `pluto`.`ds_match_event_jiaoqiu`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pluto`.`ds_match_event_jiaoqiu`;

CREATE TABLE IF NOT EXISTS `pluto`.`ds_match_event_jiaoqiu`(
  `id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `match_id` BIGINT(20) UNSIGNED NOT NULL,
  `home_away` VARCHAR(8) NULL COMMENT '主队(home)/客队(away)',
  `team_id` BIGINT(20) UNSIGNED NULL,
  `team_name` VARCHAR(45) NOT NULL COMMENT '球队名称',
  `time_stamp` SMALLINT(5) UNSIGNED NOT NULL COMMENT '比赛时间戳（单位分钟）',
  `v` INT(5) NOT NULL COMMENT '值',
  `info` VARCHAR(45) NULL COMMENT '待求证字段',
  `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `ds_match_event_jiaoqiu_id` (`id` ASC),
  INDEX `ds_match_event_jiaoqiu_idx_u` (`match_id` ASC, `team_name` ASC , `time_stamp` ASC , `info` ASC),
  INDEX `ds_match_event_jiaoqiu_idx` (`match_id` ASC, `team_name` ASC , `time_stamp` ASC),
  INDEX `ds_match_event_match_id` (`match_id` ASC)
  )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

-- -----------------------------------------------------
-- Table `pluto`.`ds_match_event_shezheng`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pluto`.`ds_match_event_shezheng`;

CREATE TABLE IF NOT EXISTS `pluto`.`ds_match_event_shezheng`(
  `id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `match_id` BIGINT(20) UNSIGNED NOT NULL,
  `home_away` VARCHAR(8) NULL COMMENT '主队(home)/客队(away)',
  `team_id` BIGINT(20) UNSIGNED NULL,
  `team_name` VARCHAR(45) NOT NULL COMMENT '球队名称',
  `time_stamp` SMALLINT(5) UNSIGNED NOT NULL COMMENT '比赛时间戳（单位分钟）',
  `v` INT(5) NOT NULL COMMENT '值',
  `info` VARCHAR(45) NULL COMMENT '待求证字段',
  `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `ds_match_event_shezheng_id` (`id` ASC),
  INDEX `ds_match_event_shezheng_idx_u` (`match_id` ASC, `team_name` ASC , `time_stamp` ASC , `info` ASC),
  INDEX `ds_match_event_shezheng_idx` (`match_id` ASC, `team_name` ASC , `time_stamp` ASC),
  INDEX `ds_match_event_match_id` (`match_id` ASC)
  )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

-- -----------------------------------------------------
-- Table `pluto`.`ds_match_event_shepian`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pluto`.`ds_match_event_shepian`;

CREATE TABLE IF NOT EXISTS `pluto`.`ds_match_event_shepian`(
  `id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `match_id` BIGINT(20) UNSIGNED NOT NULL,
  `home_away` VARCHAR(8) NULL COMMENT '主队(home)/客队(away)',
  `team_id` BIGINT(20) UNSIGNED NULL,
  `team_name` VARCHAR(45) NOT NULL COMMENT '球队名称',
  `time_stamp` SMALLINT(5) UNSIGNED NOT NULL COMMENT '比赛时间戳（单位分钟）',
  `v` INT(5) NOT NULL COMMENT '值',
  `info` VARCHAR(45) NULL COMMENT '待求证字段',
  `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `ds_match_event_shepian_id` (`id` ASC),
  INDEX `ds_match_event_shepian_idx_u` (`match_id` ASC, `team_name` ASC , `time_stamp` ASC , `info` ASC),
  INDEX `ds_match_event_shepian_idx` (`match_id` ASC, `team_name` ASC , `time_stamp` ASC),
  INDEX `ds_match_event_match_id` (`match_id` ASC)
  )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

-- -----------------------------------------------------
-- Table `pluto`.`ds_match_event_weixian`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pluto`.`ds_match_event_weixian`;

CREATE TABLE IF NOT EXISTS `pluto`.`ds_match_event_weixian`(
  `id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `match_id` BIGINT(20) UNSIGNED NOT NULL,
  `home_away` VARCHAR(8) NULL COMMENT '主队(home)/客队(away)',
  `team_id` BIGINT(20) UNSIGNED NULL,
  `team_name` VARCHAR(45) NOT NULL COMMENT '球队名称',
  `time_stamp` SMALLINT(5) UNSIGNED NOT NULL COMMENT '比赛时间戳（单位分钟）',
  `v` INT(5) NOT NULL COMMENT '值',
  `info` VARCHAR(45) NULL COMMENT '待求证字段',
  `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `ds_match_event_weixian_id` (`id` ASC),
  INDEX `ds_match_event_weixian_idx_u` (`match_id` ASC, `team_name` ASC , `time_stamp` ASC , `info` ASC),
  INDEX `ds_match_event_weixian_idx` (`match_id` ASC, `team_name` ASC , `time_stamp` ASC),
  INDEX `ds_match_event_match_id` (`match_id` ASC)
  )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

-- -----------------------------------------------------
-- Table `pluto`.`ds_match_event_jingong`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pluto`.`ds_match_event_jingong`;

CREATE TABLE IF NOT EXISTS `pluto`.`ds_match_event_jingong`(
  `id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `match_id` BIGINT(20) UNSIGNED NOT NULL,
  `home_away` VARCHAR(8) NULL COMMENT '主队(home)/客队(away)',
  `team_id` BIGINT(20) UNSIGNED NULL,
  `team_name` VARCHAR(45) NOT NULL COMMENT '球队名称',
  `time_stamp` SMALLINT(5) UNSIGNED NOT NULL COMMENT '比赛时间戳（单位分钟）',
  `v` INT(5) NOT NULL COMMENT '值',
  `info` VARCHAR(45) NULL COMMENT '待求证字段',
  `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `ds_match_event_jingong_id` (`id` ASC),
  INDEX `ds_match_event_jingong_idx_u` (`match_id` ASC, `team_name` ASC , `time_stamp` ASC , `info` ASC),
  INDEX `ds_match_event_jingong_idx` (`match_id` ASC, `team_name` ASC , `time_stamp` ASC),
  INDEX `ds_match_event_match_id` (`match_id` ASC)
  )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

-- -----------------------------------------------------
-- Table `pluto`.`ds_match_event_jinqiu`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pluto`.`ds_match_event_jinqiu`;

CREATE TABLE IF NOT EXISTS `pluto`.`ds_match_event_jinqiu`(
  `id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `match_id` BIGINT(20) UNSIGNED NOT NULL,
  `home_away` VARCHAR(8) NULL COMMENT '主队(home)/客队(away)',
  `team_id` BIGINT(20) UNSIGNED NULL,
  `team_name` VARCHAR(45) NOT NULL COMMENT '球队名称',
  `time_stamp` SMALLINT(5) UNSIGNED NOT NULL COMMENT '比赛时间戳（单位分钟）',
  `v` INT(5) NOT NULL COMMENT '值',
  `info` VARCHAR(45) NULL COMMENT '待求证字段',
  `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `ds_match_event_jinqiu_id` (`id` ASC),
  INDEX `ds_match_event_jinqiu_idx_u` (`match_id` ASC, `team_name` ASC , `time_stamp` ASC , `info` ASC),
  INDEX `ds_match_event_jinqiu_idx` (`match_id` ASC, `team_name` ASC , `time_stamp` ASC),
  INDEX `ds_match_event_match_id` (`match_id` ASC)
  )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

-- -----------------------------------------------------
-- Table `pluto`.`ds_match_event`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pluto`.`ds_match_event`;

CREATE TABLE IF NOT EXISTS `pluto`.`ds_match_event`(
  `id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `match_id` BIGINT(20) UNSIGNED NOT NULL,
  `home_away` VARCHAR(8) NULL COMMENT '主队(home)/客队(away)',
  `team_id` BIGINT(20) UNSIGNED NULL,
  `team_name` VARCHAR(45) NULL COMMENT '球队名称',
  `time_stamp` SMALLINT(5) UNSIGNED NULL COMMENT '比赛时间戳（单位分钟）',
  `txt` VARCHAR(400) NOT NULL COMMENT '事件内容',
  `info` VARCHAR(45) NULL COMMENT '待求证字段',
  `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `ds_match_event_id` (`id` ASC),
  INDEX `ds_match_event_idx_u` (`match_id` ASC, `team_name` ASC , `time_stamp` ASC , `info` ASC),
  INDEX `ds_match_event_idx` (`match_id` ASC, `team_name` ASC , `time_stamp` ASC),
  INDEX `ds_match_event_match_id` (`match_id` ASC)
  )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;
