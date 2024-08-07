-- Drop the function if it already exists
DROP FUNCTION IF EXISTS SafeDiv;

-- Create the function SafeDiv
DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END //

DELIMITER ;
