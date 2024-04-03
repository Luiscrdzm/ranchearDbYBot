DELIMITER $$

CREATE OR REPLACE FUNCTION menorPrecio(IN id INT) RETURNS INT
BEGIN
    RETURN (SELECT MIN(precioCompra)
    FROM plantas NATURAL JOIN compraSemillas
    WHERE plantas.idP = id);
END $$

DELIMITER ;