-- cash_flow.account_detail definition

CREATE TABLE `account_detail` (
  `id_account` int(11) NOT NULL,
  `balance` float DEFAULT NULL,
  `last_modified` date NOT NULL DEFAULT curdate(),
  UNIQUE KEY `account_detail_un` (`id_account`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


-- cash_flow.account_list definition

CREATE TABLE `account_list` (
  `id_account` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `password` varchar(35) NOT NULL,
  `name` varchar(75) NOT NULL,
  `status` int(11) NOT NULL,
  `role` int(11) DEFAULT NULL,
  `created_date` date DEFAULT NULL,
  `last_modified` date DEFAULT curdate(),
  PRIMARY KEY (`id_account`),
  UNIQUE KEY `account_list_un` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- cash_flow.account_role definition

CREATE TABLE `account_role` (
  `role` int(11) NOT NULL AUTO_INCREMENT,
  `desc_role` varchar(50) NOT NULL,
  PRIMARY KEY (`role`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- cash_flow.cash_flow definition

CREATE TABLE `cash_flow` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` datetime NOT NULL DEFAULT current_timestamp(),
  `type` varchar(10) NOT NULL,
  `destination` varchar(30) DEFAULT NULL,
  `debit` float DEFAULT NULL,
  `credit` float DEFAULT NULL,
  `id_account` int(11) NOT NULL,
  `notes` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- cash_flow.type_transaction definition

CREATE TABLE `type_transaction` (
  `id_type` int(11) NOT NULL AUTO_INCREMENT,
  `desc_type` varchar(50) NOT NULL,
  PRIMARY KEY (`id_type`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;