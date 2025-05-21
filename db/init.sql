CREATE TABLE IF NOT EXISTS weather (
    country VARCHAR(100) PRIMARY KEY,
    temperature INTEGER,
    humidity INTEGER
);

INSERT INTO weather (country, temperature, humidity) VALUES
('Deutschland', 20, 60),
('USA', 25, 55),
('Spanien', 28, 50),
('Frankreich', 22, 65),
('Italien', 26, 55),
('Kanada', 18, 70),
('Brasilien', 30, 75),
('Japan', 24, 60)
ON CONFLICT (country) DO NOTHING;
