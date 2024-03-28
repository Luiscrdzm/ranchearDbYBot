DELIMITER $$

CREATE OR REPLACE FUNCTION estrella(IN idP INT,IN calidad ENUM('plata','oro','iridio')) RETURNS INT
BEGIN
    RETURN (SELECT precioVenta*(CASE calidad WHEN 1 THEN 1.25 WHEN 2 THEN 1.5 WHEN 3 THEN 2 END) FROM plantas WHERE plantas.idP=idP);
END $$

CREATE OR REPLACE FUNCTION menorPrecio(IN id INT) RETURNS INT
BEGIN
    RETURN (SELECT MIN(precioCompra)
    FROM plantas NATURAL JOIN compraSemillas
    WHERE plantas.idP = id);
END $$

DELIMITER ;