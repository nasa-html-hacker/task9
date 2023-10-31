SELECT * FROM Mobile;
INSERT INTO Mobile (ID_phone, Brand, Model) VALUES (1, 'Samsung', 'Galaxy S21');
UPDATE Mobile SET Brand = 'Apple' WHERE ID_phone = 1;
DELETE FROM Mobile WHERE ID_phone = 1;
