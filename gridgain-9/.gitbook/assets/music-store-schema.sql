-- Music Store Sample Database Schema for Apache Ignite 3
-- Distribution zones, tables, and indexes
--
-- Two zones: MusicStore (2 replicas, partitioned) and MusicStoreReplicated (3 replicas, reference data)
-- Colocation chains: Artist->Album->Track, Customer->Invoice->InvoiceLine, Playlist->PlaylistTrack

-- Distribution Zones

CREATE ZONE IF NOT EXISTS MusicStore WITH REPLICAS=2, PARTITIONS=25, STORAGE_PROFILES='default';
CREATE ZONE IF NOT EXISTS MusicStoreReplicated WITH REPLICAS=3, PARTITIONS=25, STORAGE_PROFILES='default';

-- Reference Data Tables (MusicStoreReplicated zone, 3 replicas on every node)

CREATE TABLE IF NOT EXISTS Genre (
    GenreId INT NOT NULL,
    Name VARCHAR(120),
    PRIMARY KEY (GenreId)
) ZONE MusicStoreReplicated;

CREATE TABLE IF NOT EXISTS MediaType (
    MediaTypeId INT NOT NULL,
    Name VARCHAR(120),
    PRIMARY KEY (MediaTypeId)
) ZONE MusicStoreReplicated;

-- Music Entity Tables (MusicStore zone, 2 replicas, colocated)

CREATE TABLE IF NOT EXISTS Artist (
    ArtistId INT NOT NULL,
    Name VARCHAR(120) NOT NULL,
    PRIMARY KEY (ArtistId)
) ZONE MusicStore;

CREATE TABLE IF NOT EXISTS Album (
    AlbumId INT NOT NULL,
    ArtistId INT NOT NULL,
    Title VARCHAR(160) NOT NULL,
    PRIMARY KEY (AlbumId, ArtistId)
) COLOCATE BY (ArtistId) ZONE MusicStore;

CREATE INDEX IF NOT EXISTS IFK_AlbumArtistId ON Album (ArtistId);

CREATE TABLE IF NOT EXISTS Track (
    TrackId INT NOT NULL,
    AlbumId INT,
    Name VARCHAR(200) NOT NULL,
    MediaTypeId INT NOT NULL,
    GenreId INT,
    Composer VARCHAR(220),
    Milliseconds INT NOT NULL,
    Bytes INT,
    UnitPrice DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (TrackId, AlbumId)
) COLOCATE BY (AlbumId) ZONE MusicStore;

CREATE INDEX IF NOT EXISTS IFK_TrackAlbumId ON Track (AlbumId);
CREATE INDEX IF NOT EXISTS IFK_TrackGenreId ON Track (GenreId);
CREATE INDEX IF NOT EXISTS IFK_TrackMediaTypeId ON Track (MediaTypeId);

-- Business Entity Tables (MusicStore zone, 2 replicas, colocated)

CREATE TABLE IF NOT EXISTS Customer (
    CustomerId INT NOT NULL,
    FirstName VARCHAR(40) NOT NULL,
    LastName VARCHAR(20) NOT NULL,
    Company VARCHAR(80),
    Address VARCHAR(70),
    City VARCHAR(40),
    State VARCHAR(40),
    Country VARCHAR(40),
    PostalCode VARCHAR(10),
    Phone VARCHAR(24),
    Fax VARCHAR(24),
    Email VARCHAR(60) NOT NULL,
    SupportRepId INT,
    PRIMARY KEY (CustomerId)
) ZONE MusicStore;

CREATE INDEX IF NOT EXISTS IFK_CustomerSupportRepId ON Customer (SupportRepId);

CREATE TABLE IF NOT EXISTS Employee (
    EmployeeId INT NOT NULL,
    LastName VARCHAR(20) NOT NULL,
    FirstName VARCHAR(20) NOT NULL,
    Title VARCHAR(30),
    ReportsTo INT,
    BirthDate DATE,
    HireDate DATE,
    Address VARCHAR(70),
    City VARCHAR(40),
    State VARCHAR(40),
    Country VARCHAR(40),
    PostalCode VARCHAR(10),
    Phone VARCHAR(24),
    Fax VARCHAR(24),
    Email VARCHAR(60),
    PRIMARY KEY (EmployeeId)
) ZONE MusicStore;

CREATE INDEX IF NOT EXISTS IFK_EmployeeReportsTo ON Employee (ReportsTo);

CREATE TABLE IF NOT EXISTS Invoice (
    InvoiceId INT NOT NULL,
    CustomerId INT NOT NULL,
    InvoiceDate DATE NOT NULL,
    BillingAddress VARCHAR(70),
    BillingCity VARCHAR(40),
    BillingState VARCHAR(40),
    BillingCountry VARCHAR(40),
    BillingPostalCode VARCHAR(10),
    Total DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (InvoiceId, CustomerId)
) COLOCATE BY (CustomerId) ZONE MusicStore;

CREATE INDEX IF NOT EXISTS IFK_InvoiceCustomerId ON Invoice (CustomerId);

CREATE TABLE IF NOT EXISTS InvoiceLine (
    InvoiceLineId INT NOT NULL,
    InvoiceId INT NOT NULL,
    TrackId INT NOT NULL,
    UnitPrice DECIMAL(10,2) NOT NULL,
    Quantity INT NOT NULL,
    PRIMARY KEY (InvoiceLineId, InvoiceId)
) COLOCATE BY (InvoiceId) ZONE MusicStore;

CREATE INDEX IF NOT EXISTS IFK_InvoiceLineInvoiceId ON InvoiceLine (InvoiceId);
CREATE INDEX IF NOT EXISTS IFK_InvoiceLineTrackId ON InvoiceLine (TrackId);

-- Playlist Tables (MusicStore zone, 2 replicas, colocated)

CREATE TABLE IF NOT EXISTS Playlist (
    PlaylistId INT NOT NULL,
    Name VARCHAR(120),
    PRIMARY KEY (PlaylistId)
) ZONE MusicStore;

CREATE TABLE IF NOT EXISTS PlaylistTrack (
    PlaylistId INT NOT NULL,
    TrackId INT NOT NULL,
    PRIMARY KEY (PlaylistId, TrackId)
) COLOCATE BY (PlaylistId) ZONE MusicStore;

CREATE INDEX IF NOT EXISTS IFK_PlaylistTrackPlaylistId ON PlaylistTrack (PlaylistId);
CREATE INDEX IF NOT EXISTS IFK_PlaylistTrackTrackId ON PlaylistTrack (TrackId);
