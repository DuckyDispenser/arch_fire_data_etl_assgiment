-- Not used

-- CREATE TABLE testing-art.work_space.incident_desc(
--     `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     `incident_borough` TEXT NOT NULL,
--     `policeprecinct` BIGINT NULL,
--     `zipcode` INT NULL,
--     `incident_classification` TEXT NULL,
--     `incident_classification_group` TEXT NULL,
--     `incident_close_datetime` DATETIME NOT NULL,
--     `incident_datetime` DATETIME NOT NULL,
--     `valid_incident_rspns_time_indc` BIGINT NULL,
--     `incident_response_seconds_qy` INT NULL,
--     `incident_travel_tm_seconds_qy` INT NULL,
--     `citycouncildistrict` INT NULL,
--     `communityschooldistrict` INT NULL,
--     `congressionaldistrict` INT NULL,
--     `valid_dispatch_rspns_time_indc` TEXT NULL,
--     `valid_incident_rspns_time_indc` TEXT NULL,
--     `engines_assigned_quantity` INT NULL,
--     `ladders_assigned_quantity` INT NULL,
--     `other_units_assigned_quantity` INT NULL
-- );
-- CREATE TABLE testing-art.work_space.alarm_boxs(
--     `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     `incident_id` BIGINT NOT NULL,
--     `alarm_box_location` TEXT NULL,
--     `alarm_box_borough` TEXT NULL,
--     `alarm_source_description_tx` TEXT NULL,
--     `highest_alarm_level` TEXT NULL
-- );
-- CREATE TABLE testing-art.work_space.incident(
--     `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     `provider_starfire_incident_id` BIGINT NULL,
--     `incident_datetime` TIMESTAMP NULL,
--     `alarm_box_number` BIGINT NULL
-- );
-- ALTER TABLE
--     `incident` ADD CONSTRAINT `incident_provider_starfire_incident_id_foreign` FOREIGN KEY(`provider_starfire_incident_id`) REFERENCES `alarm_boxs`(`incident_id`);
-- ALTER TABLE
--     `incident` ADD CONSTRAINT `incident_alarm_box_number_foreign` FOREIGN KEY(`alarm_box_number`) REFERENCES `alarm_boxs`(`id`);
-- ALTER TABLE
--     `incident` ADD CONSTRAINT `incident_provider_starfire_incident_id_foreign` FOREIGN KEY(`provider_starfire_incident_id`) REFERENCES `incident_desc`(`id`);