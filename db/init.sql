CREATE TABLE IF NOT EXISTS weather (
    country VARCHAR(100) PRIMARY KEY,
    temperature INTEGER,
    humidity INTEGER
);

INSERT INTO weather (country, temperature, humidity) VALUES
('Deutschland', 20, 60),
('USA', 25, 55),
('Spanien', 28, 50)
ON CONFLICT (country) DO NOTHING;
