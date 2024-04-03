CREATE TABLE vendedores(
    idV INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE plantas(
    idP INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    precioVenta INT NOT NULL, -- Precio de venta por cada una de las unidades cosechadas
    diasMaduracion INT NOT NULL, 
    experiencia INT NOT NULL,
    temporada SET('primavera', 'verano', 'otoño', 'invierno') NOT NULL,
    recosecha bool NOT NULL,
    diasRecosecha INT NULL,
    produccion INT NOT NULL,
    chanceExtra INT NULL
);

CREATE TABLE notas(
    idN INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion text NOT NULL
);

CREATE TABLE plantasNotas(
    idP INT,
    idN INT,
    PRIMARY KEY (idP, idN)
);
ALTER TABLE plantasNotas
    ADD CONSTRAINT fk_pn_planta FOREIGN KEY (idP) REFERENCES plantas(idP),
    ADD CONSTRAINT fk_pn_nota FOREIGN KEY (idN) REFERENCES notas(idN);

CREATE TABLE compraSemillas(
    idV INT,
    idP INT,
    precioCompra INT NOT NULL,
    PRIMARY KEY (idV, idP)
);
ALTER TABLE compraSemillas
    ADD CONSTRAINT fk_cs_vendedor FOREIGN KEY (idV) REFERENCES vendedores(idV),
    ADD CONSTRAINT fk_cs_planta FOREIGN KEY (idP) REFERENCES plantas(idP);