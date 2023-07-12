-- Create the stored procedure
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score FLOAT DEFAULT 0;
    DECLARE total_weight FLOAT DEFAULT 0;
    DECLARE avg_score FLOAT DEFAULT 0;
    
    -- Calculate the total weighted score and total weight
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
END //
DELIMITER ;
