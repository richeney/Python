# SQL Revision

## Topics

[SQL](https://isaaccomputerscience.org/topics/sql?examBoard=aqa&stage=gcse)

## Database: SportsClub

> Key: bold fields are primary keys, italic fields refer to another table for consistency

### Member

| Field | Type |
|---|---|
| **MemberId** | CHAR(6) |
| FirstName | VARCHAR(30) |
| LastName | VARCHAR (30) |
| Phone | VARCHAR(15) |

### Course

| Field | Type |
|---|---|
| **CourseCode** | CHAR(6) |
| Description | VARCHAR(100) |
| Fee | DECIMAL (13,2) |

### Instructor

| Field | Type |
|---|---|
| **InstructorId** | INT |
| FirstName | VARCHAR(30) |
| LastName | VARCHAR (30) |
| Email | VARCHAR (30) |

### Certificate

| Field | Type |
|---|---|
| ***MemberID*** | CHAR(6) |
| ***CourseCode*** | CHAR(6) |
| AssessmentDate | DATE |
| *InstructorID* | INT |

## Practice

1. List the instructors, showing first and last name, and email address
1. Repeat, but sort by surname
1. List the course code, name and price where price is more than £20. Sort by most expensive to least.
1. Add a new course: Squash, £25, with a code CR0010
1. List the course names and price where the course code starts with CR.
1. Emily and Jack Marr were assessed on 11/05/2023 by squash instructor, Greta. Add the records in.
1. Output the member's first and last name, course description, assessment date.
1. Abdel Patel's number has changed to 01632 912345.
1. Do a quick check by showing the whole Member table.
1. Joe Donald has left the club.
1. Rerun the command to output the members, course name and assessments, but also add the assessor's firstname and sort it by date, most recent first.

## Picture

Here is a nice picture of Fluffy, who's guarding the answers...

![Fluffy](https://images.saymedia-content.com/.image/c_limit%2Ccs_srgb%2Cq_auto:eco%2Cw_520/MTc2Mjk0MjYxMjIxMjM3OTMz/harry-potter-fluffy.webp)

## Answers

We're checking, not cheating, right?

1. List the instructors, showing first and last name, and email address

    ```sql
    SELECT FirstName, LastName, Email
    FROM Instructor;
    ```

1. Repeat, but sort by surname

    ```sql
    SELECT FirstName, LastName, Email
    FROM Instructor
    ORDER BY LastName;
    ```

1. List the course code, name and price where price is more than £20. Sort by most expensive to least.

    ```sql
    SELECT CourseCode, Description, Fee
    FROM Course
    WHERE Fee > 20
    ORDER BY Fee DESC;
    ```

1. Add a new course: Squash, £25, with a code CR0010

    ```sql
    INSERT INTO Course (CourseCode, Description, Fee)
    VALUES ('CR0010', 'Squash', 25);
    ```

1. List the course names and price where the course code starts with CR.

    ```sql
    SELECT Description, Fee
    FROM Course
    WHERE CourseCode LIKE "CR%";
    ```

1. Emily and Jack Marr were assessed on 11/05/2023 by squash instructor, Greta. Add the records in.

    ```sql
    SELECT MemberID
    FROM Member
    WHERE LastName = "Marr";

    SELECT InstructorId
    FROM Instructor
    WHERE FirstName = "Greta";

    INSERT INTO Certificate(MemberID, CourseCode, AssessmentDate, InstructorID)
    VALUES
    ('012010','CR0010','2023-05-11',2),
    ('148765','CR0010','2023-05-11',2);
    ```

1. Output the member's first and last name, course description, assessment date.

    ```sql
    SELECT Member.FirstName, Member.LastName, Course.Description, Certificate.AssessmentDate
    FROM Member, Course, Certificate
    WHERE Certificate.MemberId = Member.MemberId AND Certificate.CourseCode = Course.CourseCode;
    ```

1. Abdel Patel's number has changed to 01632 912345.

    ```sql
    UPDATE Member
    SET Phone = "01632 912345"
    WHERE FirstName = "Abdel" AND LastName = "Patel";
    ```

1. Do a quick check by showing the whole Member table.

    ```sql
    SELECT * FROM Member;
    ```

1. Joe Donald has left the club.

    ```sql
    SELECT *
    FROM Member
    WHERE FirstName = "Joe" AND LastName = "Donald";

    DELETE
    FROM Member
    WHERE FirstName = "Joe" AND LastName = "Donald";
    ```

1. Rerun the command to output the members, course name and assessments, but also add the assessor's firstname and sort it by date, most recent first.

    ```sql
    SELECT Member.FirstName, Member.LastName, Course.Description, Certificate.AssessmentDate, Instructor.FirstName
    FROM Member, Course, Certificate, Instructor
    WHERE Certificate.MemberId = Member.MemberId AND Certificate.CourseCode = Course.CourseCode AND Certificate.InstructorId = Instructor.InstructorId
    ORDER BY Certificate.AssessmentDate DESC;
    ```

Easy peasy!
