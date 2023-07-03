CREATE DATABASE IndustrialTroubleshootDB;

USE IndustrialTroubleshootDB;

CREATE TABLE equipment (
  id INT PRIMARY KEY AUTO_INCREMENT,
  equipment_name_pt VARCHAR(50)
  equipment_name_en VARCHAR(50)
);

CREATE TABLE issue (
  id INT PRIMARY KEY AUTO_INCREMENT,
  issue_description_pt VARCHAR(255)
  issue_description_en VARCHAR(255)
);

CREATE TABLE root_cause (
  id INT PRIMARY KEY AUTO_INCREMENT,
  cause_pt VARCHAR(255)
  cause_en VARCHAR(255)
);

CREATE TABLE resolution (
  id INT PRIMARY KEY AUTO_INCREMENT,
  resolution_action_pt VARCHAR(255)
  resolution_action_en VARCHAR(255)
);


CREATE TABLE Troubleshooting (
  id INT PRIMARY KEY AUTO_INCREMENT,
  type VARCHAR(20),
  equipment_id INT,
  FOREIGN KEY (equipment_id) REFERENCES Equipment(id),
  problem_id INT,
  FOREIGN KEY (problem_id) REFERENCES Problem(id),
  cause_id INT,
  FOREIGN KEY (cause_id) REFERENCES Cause(id),
  action_id INT,
  FOREIGN KEY (action_id) REFERENCES Action(id)
);
