CREATE DATABASE equipment_failures;

USE equipment_failures;

CREATE TABLE Problem (
  id INT PRIMARY KEY AUTO_INCREMENT,
  problem VARCHAR(255)
);

CREATE TABLE Cause (
  id INT PRIMARY KEY AUTO_INCREMENT,
  cause VARCHAR(255),
  problem_id INT,
  FOREIGN KEY (problem_id) REFERENCES Problem(id)
);

CREATE TABLE Action (
  id INT PRIMARY KEY AUTO_INCREMENT,
  action VARCHAR(255),
  cause_id INT,
  FOREIGN KEY (cause_id) REFERENCES Cause(id)
);

CREATE TABLE Troubleshooting (
  id INT PRIMARY KEY AUTO_INCREMENT,
  type VARCHAR(20),
  equipment VARCHAR(50),
  problem_id INT,
  FOREIGN KEY (problem_id) REFERENCES Problem(id)
);
