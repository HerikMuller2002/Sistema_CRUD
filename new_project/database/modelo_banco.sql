CREATE DATABASE equipment_failures;

USE equipment_failures;

CREATE TABLE Problem (
  id INT PRIMARY KEY AUTO_INCREMENT,
  problem VARCHAR(255)
);

CREATE TABLE Cause (
  id INT PRIMARY KEY AUTO_INCREMENT,
  cause VARCHAR(255)
);

CREATE TABLE Action (
  id INT PRIMARY KEY AUTO_INCREMENT,
  action VARCHAR(255)
);

CREATE TABLE Equipment (
  id INT PRIMARY KEY AUTO_INCREMENT,
  equipment VARCHAR(50)
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
