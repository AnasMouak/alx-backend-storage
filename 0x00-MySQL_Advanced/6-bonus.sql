-- Drop the procedure if it already exists
DROP PROCEDURE IF EXISTS AddBonus;

-- Create the stored procedure
DELIMITER //

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    -- Insert the project if it doesn't exist and get the project id
    INSERT INTO projects (name) 
    VALUES (project_name) 
    ON DUPLICATE KEY UPDATE id = LAST_INSERT_ID(id);
    
    -- Insert the correction
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, LAST_INSERT_ID(), score);
END //

DELIMITER ;
