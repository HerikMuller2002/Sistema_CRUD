CREATE DATABASE SupportTroubleshootDB;

USE SupportTroubleshootDB;

CREATE TABLE Subject (
  id INT PRIMARY KEY AUTO_INCREMENT,
  equipment_pt VARCHAR(50)
  equipment_en VARCHAR(50)
);

CREATE TABLE Problem (
  id INT PRIMARY KEY AUTO_INCREMENT,
  problem_pt VARCHAR(255)
  problem_en VARCHAR(255)
);

CREATE TABLE Cause (
  id INT PRIMARY KEY AUTO_INCREMENT,
  cause_pt VARCHAR(255)
  cause_en VARCHAR(255)
);

CREATE TABLE Action (
  id INT PRIMARY KEY AUTO_INCREMENT,
  action_pt VARCHAR(255)
  action_en VARCHAR(255)
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
