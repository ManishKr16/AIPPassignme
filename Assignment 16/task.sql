CREATE TABLE Members (
    member_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    join_date DATE
);

CREATE TABLE Books (
    book_id INT PRIMARY KEY,
    title VARCHAR(200),
    author VARCHAR(100),
    available BOOLEAN
);

CREATE TABLE Loans (
    loan_id INT PRIMARY KEY,
    member_id INT,
    book_id INT,
    loan_date DATE,
    return_date DATE,
    FOREIGN KEY (member_id) REFERENCES Members(member_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);
INSERT INTO Members (member_id, name, email, join_date) VALUES
(1, 'Rahul Sharma', 'rahul@gmail.com', '2023-01-10'),
(2, 'Priya Verma', 'priya@gmail.com', '2023-03-22'),
(3, 'Amit Singh', 'amit@gmail.com', '2023-05-15');


INSERT INTO Books (book_id, title, author, available) VALUES
(1, 'The Great Gatsby', 'F. Scott Fitzgerald', TRUE),
(2, '1984', 'George Orwell', TRUE),
(3, 'To Kill a Mockingbird', 'Harper Lee', TRUE);


INSERT INTO Loans (loan_id, member_id, book_id, loan_date, return_date) VALUES
(1, 1, 2, '2023-06-01', NULL),
(2, 2, 1, '2023-06-05', '2023-06-15');

SELECT 
    Members.name AS member_name,
    Books.title AS book_title,
    Books.author,
    Loans.loan_date,
    Loans.return_date
FROM Loans
JOIN Members ON Loans.member_id = Members.member_id
JOIN Books ON Loans.book_id = Books.book_id
WHERE Members.member_id = 1;

UPDATE Books
SET available = FALSE
WHERE book_id = 101;

DELETE FROM Loans
WHERE loan_id = 2;

