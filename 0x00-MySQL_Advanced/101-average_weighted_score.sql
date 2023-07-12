-- Create the stored procedure
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE user_id INT;
    DECLARE total_score FLOAT DEFAULT 0;
    DECLARE total_weight FLOAT DEFAULT 0;
    DECLARE avg_score FLOAT DEFAULT 0;
    
    -- Cursor to iterate over user IDs
    DECLARE cur CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET @done = TRUE;
    
    -- Open the cursor
    OPEN cur;
    
    -- Loop through each user
    user_loop: LOOP
        -- Fetch the next user ID
        FETCH cur INTO user_id;
        
        -- Exit the loop if no more users
        IF @done THEN
            LEAVE user_loop;
        END IF;
        
        -- Calculate the total weighted score and total weight for the user
        SELECT SUM(corrections.score * projects.weight), SUM(projects.weight)
        INTO total_score, total_weight
        FROM corrections
        JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;
        
        -- Calculate the average weighted score
        IF total_weight > 0 THEN
            SET avg_score = total_score / total_weight;
        END IF;
        
        -- Update the user's average score
        UPDATE users SET average_score = avg_score WHERE id = user_id;
    END LOOP user_loop;
    
    -- Close the cursor
    CLOSE cur;
END //
DELIMITER ;
