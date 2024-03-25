DELIMITER $$

CREATE PROCEDURE estrellas(IN idP INT)
BEGIN
    SELECT
        precioVenta*1.25 as Plata,
        precioVenta*1.5 as Oro,
        precioVenta*2 as Iridio
    FROM plantas
    WHERE idP = plantas.idP;
END $$

CREATE PROCEDURE plantasTemporada(IN temporada VARCHAR(50))
BEGIN
    SELECT
        *
    FROM plantas
    WHERE FIND_IN_SET(temporada, plantas.temporada);
END $$

DELIMITER ;