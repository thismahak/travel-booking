CREATE DATABASE travel_db;

USE travel_db;  -- Replace with actual DB name

INSERT INTO core_traveloption (type, source, destination, date_time, price, available_seats)
VALUES 
('Flight', 'Delhi', 'Mumbai', '2025-07-20 08:00:00', 3500.00, 60),
('Train', 'Mumbai', 'Pune', '2025-07-21 14:00:00', 600.00, 100),
('Bus', 'Jaipur', 'Delhi', '2025-07-22 19:00:00', 800.00, 35),
('Flight', 'Chennai', 'Bangalore', '2025-07-23 09:30:00', 2200.00, 50),
('Train', 'Delhi', 'Lucknow', '2025-07-24 06:15:00', 450.00, 120),
('Bus', 'Kolkata', 'Bhubaneswar', '2025-07-25 17:45:00', 700.00, 40);
