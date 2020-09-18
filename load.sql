DROP TABLE IF EXISTS sketch.yeyuan2;

CREATE TABLE sketch.yeyuan2 (
	total_population DECIMAL NOT NULL, 
	white DECIMAL NOT NULL, 
	"black_or_African" DECIMAL NOT NULL, 
	indian_and_alaska_native DECIMAL NOT NULL, 
	asian DECIMAL NOT NULL, 
	native_hawaiian_and_other_pacific_islander DECIMAL NOT NULL, 
	total_in_living_units DECIMAL NOT NULL, 
	total_in_households DECIMAL NOT NULL, 
	in_family_households DECIMAL NOT NULL, 
	median_household_income DECIMAL, 
	median_age DECIMAL NOT NULL, 
	"State" DECIMAL NOT NULL, 
	"County" DECIMAL NOT NULL, 
	"Tract" DECIMAL NOT NULL, 
	"BlockGroup" DECIMAL NOT NULL
);

\COPY sketch.yeyuan2 from 'acs_data_yeyuan2.csv' WITH CSV HEADER;
