CREATE TABLE DimLaptop (
    LaptopID SERIAL PRIMARY KEY,
    Company VARCHAR(255) NOT NULL,
    Product VARCHAR(255) NOT NULL,
    TypeName VARCHAR(255) NOT NULL,
    Inches DECIMAL(3,1) NOT NULL,
    Screen VARCHAR(255) NOT NULL,
    Touchscreen BOOLEAN NOT NULL,
    IPSpanel BOOLEAN NOT NULL,
    RetinaDisplay BOOLEAN NOT NULL
);

CREATE TABLE DimSpesifikasi (
    SpesifikasiID SERIAL PRIMARY KEY,
    CPU_company VARCHAR(255) NOT NULL,
    CPU_freq DECIMAL(3,1) NOT NULL,
    CPU_model VARCHAR(255) NOT NULL,
    Ram INT NOT NULL,
    PrimaryStorage INT NOT NULL,
    PrimaryStorageType VARCHAR(255) NOT NULL,
    SecondaryStorage INT NOT NULL,
    SecondaryStorageType VARCHAR(255) NOT NULL,
    GPU_company VARCHAR(255) NOT NULL,
    GPU_model VARCHAR(255) NOT NULL
);

CREATE TABLE DimWaktu (
    WaktuID SERIAL PRIMARY KEY,
    Tahun INT NOT NULL,
    Kuartal INT CHECK (Kuartal BETWEEN 1 AND 4),
    Bulan INT CHECK (Bulan BETWEEN 1 AND 12),
    Tanggal DATE UNIQUE NOT NULL
);

CREATE TABLE FactHarga (
    HargaID SERIAL PRIMARY KEY,
    LaptopID INT REFERENCES DimLaptop(LaptopID),
    SpesifikasiID INT REFERENCES DimSpesifikasi(SpesifikasiID),
    WaktuID INT REFERENCES DimWaktu(WaktuID),
    Price_euros DECIMAL(10,2) NOT NULL
);