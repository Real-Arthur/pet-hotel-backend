CREATE TABLE "owners" (
	"id" SERIAL PRIMARY KEY,
	"first_name" VARCHAR(100), 
	"last_name" VARCHAR(100)
	);
CREATE TABLE "pets" (
	"id" SERIAL PRIMARY KEY,
	"owner_id" INT REFERENCES "owners",
	"name" VARCHAR(100), 
	"breed" VARCHAR(100), 
	"color" VARCHAR(100), 
	"is_checked_in" BOOLEAN
	);
	
CREATE TABLE "junction" (
	"id" SERIAL PRIMARY KEY,
	"pet_id" INT REFERENCES "pets",
	"owner_id" INT REFERENCES "owners"
);

INSERT INTO "owners" ("first_name", "last_name")
VALUES ('Arthur', 'Carson');

INSERT INTO "pets" ("owner_id", "name", "breed", "color", "is_checked_in")
VALUES (1, 'Charlie', 'Shih-tzu', 'Black', True);
