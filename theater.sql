DROP SCHEMA IF EXISTS theater;
CREATE SCHEMA theater;

CREATE TABLE SeatRow
(	seatrow VARCHAR(2) NOT NULL,
	PRIMARY KEY (seatrow),
    CONSTRAINT seatrow_chk CHECK((seatrow >= "A" AND seatrow <= "R" 
    AND seatrow != "I") OR seatrow = "AA" OR seatrow = "BB"
    OR seatrow = "CC" OR seatrow = "DD" OR seatrow = "EE"
    OR seatrow = "FF" OR seatrow = "GG" OR seatrow = "HH")
	);

CREATE TABLE SeatNum
(	num VARCHAR(3) NOT NULL,
	PRIMARY KEY (num),
    CONSTRAINT seatnum_chk CHECK((num >= 1 AND num <= 15) 
    OR (num >= 101 AND num <= 126))
	);

CREATE TABLE Seat
(	SeatRow VARCHAR(2) NOT NULL,
	SeatNumber VARCHAR(3) NOT NULL,
    Section TEXT(10) NOT NULL,
    Side TEXT(6) NOT NULL,
    PricingTier TEXT(13) NOT NULL,
    Wheelchair BOOLEAN NOT NULL,
    PRIMARY KEY (SeatRow, SeatNumber),
    FOREIGN KEY (SeatRow) REFERENCES SeatRow(seatrow),
    FOREIGN KEY (SeatNumber) REFERENCES SeatNum(num)
    );

CREATE TABLE Customer
(	CustomerID INT NOT NULL,
	FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    PaymentMethod TEXT NOT NULL,
    PRIMARY KEY (CustomerID),
    CONSTRAINT payment_chk CHECK(PaymentMethod = "cash" OR PaymentMethod = "credit card")
    );

CREATE TABLE Ticket
(	TicketNumber INT AUTO_INCREMENT NOT NULL,
	CustomerID INT NOT NULL,
    SeatRow VARCHAR(2) NOT NULL,
    SeatNumber VARCHAR(3) NOT NULL,
    ShowTime VARCHAR(255) NOT NULL,
    PRIMARY KEY (TicketNumber),
    FOREIGN KEY (CustomerID) References Customer(CustomerID),
    CONSTRAINT tickets UNIQUE (SeatRow, SeatNumber, ShowTime)
	);

INSERT Customer
VALUES ("1234", "John", "Johnson", "Cash");

INSERT Ticket(CustomerID, SeatRow, SeatNumber, ShowTime)
VALUES ('1234', 'A', '6', 'April 15 2021 at 2:00pm');

INSERT Ticket(CustomerID, SeatRow, SeatNumber, ShowTime)
VALUES ('1234', 'A', '8', 'April 15 2021 at 2:00pm');

INSERT Ticket(CustomerID, SeatRow, SeatNumber, ShowTime)
VALUES ('1234', 'A', '10', 'April 15 2021 at 2:00pm');

INSERT Ticket(CustomerID, SeatRow, SeatNumber, ShowTime)
VALUES ('1234', 'A', '9', 'April 15 2021 at 2:00pm');
