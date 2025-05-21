CREATE TABLE IF NOT EXISTS weather (
    code VARCHAR(2) PRIMARY KEY,
    country VARCHAR(100),    -- German name
    country_en VARCHAR(100), -- English name
    temperature INTEGER,
    humidity INTEGER,
    info TEXT
);

INSERT INTO weather (code, country, country_en, temperature, humidity, info) VALUES
('DE', 'Deutschland', 'Germany', 20, 60, 'Information über Deutschland'),
('US', 'USA', 'United States', 25, 55, 'Information about the United States'),
('ES', 'Spanien', 'Spain', 28, 50, 'Information über Spanien'),
('FR', 'Frankreich', 'France', 22, 65, 'Information sur la France'),
('IT', 'Italien', 'Italy', 26, 55, 'Informazioni sull\'Italia'),
('CA', 'Kanada', 'Canada', 18, 70, 'Information about Canada'),
('BR', 'Brasilien', 'Brazil', 30, 75, 'Informações sobre o Brasil'),
('JP', 'Japan', 'Japan', 24, 60, 'Japan ni kansuru jōhō'),
('GB', 'Großbritannien', 'United Kingdom', 21, 65, 'Information about the UK'),
('AU', 'Australien', 'Australia', 23, 55, 'Information about Australia'),
('IN', 'Indien', 'India', 27, 70, 'Information about India'),
('CN', 'China', 'China', 29, 60, 'Information about China'),
('RU', 'Russland', 'Russia', 19, 55, 'Information about Russia'),
('MX', 'Mexiko', 'Mexico', 31, 65, 'Información sobre México'),
('ZA', 'Südafrika', 'South Africa', 22, 50, 'Information about South Africa'),
('AR', 'Argentinien', 'Argentina', 24, 55, 'Información sobre Argentina'),
('NL', 'Niederlande', 'Netherlands', 20, 60, 'Informatie over Nederland'),
('SE', 'Schweden', 'Sweden', 18, 65, 'Information om Sverige'),
('CH', 'Schweiz', 'Switzerland', 19, 60, 'Informationen zur Schweiz'),
('AT', 'Österreich', 'Austria', 21, 55, 'Informationen zu Österreich'),
('PT', 'Portugal', 'Portugal', 26, 55, 'Informações sobre Portugal'),
('PL', 'Polen', 'Poland', 20, 65, 'Informacje o Polsce'),
('BE', 'Belgien', 'Belgium', 19, 60, 'Informations sur la Belgique'),
('NO', 'Norwegen', 'Norway', 17, 70, 'Informasjon om Norge'),
('DK', 'Dänemark', 'Denmark', 16, 65, 'Information om Danmark')
ON CONFLICT (code) DO NOTHING;
