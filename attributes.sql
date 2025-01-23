CREATE TABLE attributes (
    id SERIAL PRIMARY KEY,
    attribute_name varchar(50) NOT NULL,
    attribute_description varchar(255),
    attribute_value varchar(50),
    person_id int,
    CONSTRAINT fk_person
        FOREIGN KEY(person_id)
            REFERENCES person(id)
);

INSERT INTO attributes (attribute_name, attribute_description, attribute_value, person_id) VALUES 
('eye_color', 'The color of persons eyes', 'blue', 2),
('hair_color', 'The color of persons hair', 'brown', 3),
('fav_color', 'Persons favorite color', 'green', 5),
('city', 'The city person lives in', 'New York', 8),
('house', 'What kind of house the person lives in', 'Apartment', 10),
('pet', 'What kind of pet the person has', 'Dog', 11),
('height', 'Is the person short or tall', 'short', 9);

SELECT * from attributes;