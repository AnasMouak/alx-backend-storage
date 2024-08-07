-- Drop the procedure if it already exists
DROP PROCEDURE IF EXISTS AddBonus;

-- Create the stored procedure
DELIMITER //

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    DECLARE project_id INT;

    -- Try to find the project ID, or insert a new project if it doesn't exist
    SELECT id INTO project_id
    FROM projects
    WHERE name = project_name
    LIMIT 1;

    IF project_id IS NULL THEN
        -- Insert new project and get the new project ID
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;

    -- Insert the correction
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, project_id, score);
END //

DELIMITER ;
