-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema dwfa
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `dwfa` ;

-- -----------------------------------------------------
-- Schema dwfa
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dwfa` DEFAULT CHARACTER SET latin1 ;
USE `dwfa` ;

-- -----------------------------------------------------
-- Table `dwfa`.`countries`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dwfa`.`countries` ;

CREATE TABLE IF NOT EXISTS `dwfa`.`countries` (
  `country_name` VARCHAR(60) NOT NULL,
  `region` VARCHAR(25) NULL,
  PRIMARY KEY (`country_name`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dwfa`.`fao_data`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dwfa`.`fao_data` ;

CREATE TABLE IF NOT EXISTS `dwfa`.`fao_data` (
  `fao_country_name` VARCHAR(60) NOT NULL,
  `fao_year` YEAR NOT NULL,
  `female_population` INT NULL DEFAULT NULL,
  `male_population` INT NULL DEFAULT NULL,
  `rural_population` INT NULL DEFAULT NULL,
  `urban_population` INT NULL DEFAULT NULL,
  `political_stability` FLOAT NULL DEFAULT NULL,
  `water_rural_basic` INT NULL DEFAULT NULL,
  `water_urban_basic` INT NULL DEFAULT NULL,
  `water_total_safe` INT NULL DEFAULT NULL,
  PRIMARY KEY (`fao_country_name`, `fao_year`),
  CONSTRAINT `pop_country_name`
    FOREIGN KEY (`fao_country_name`)
    REFERENCES `dwfa`.`countries` (`country_name`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dwfa`.`wash_mortality_2016`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dwfa`.`wash_mortality_2016` ;

CREATE TABLE IF NOT EXISTS `dwfa`.`wash_mortality_2016` (
  `wm_country_name` VARCHAR(60) NOT NULL,
  `female_deaths` INT NULL,
  `male_deaths` INT NULL,
  PRIMARY KEY (`wm_country_name`),
  CONSTRAINT `wm_country_name`
    FOREIGN KEY (`wm_country_name`)
    REFERENCES `dwfa`.`countries` (`country_name`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
