CREATE DATABASE demoDB
USE demoDB

-- CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'Welcome@12345$';
-- OPEN MASTER KEY DECRYPTION BY PASSWORD = 'Welcome@12345$';

CREATE DATABASE SCOPED CREDENTIAL demoCreadentials
with IDENTITY='SHARED ACCESS SIGNATURE',
SECRET = 'sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupiytfx&se=2024-09-25T18:45:24Z&st=2024-09-25T10:45:24Z&spr=https&sig=tAKdGYj7Y6UNd9%2FcSzpdvA5KfBLAPVPg7oNtomZcd2U%3D';
GO

CREATE EXTERNAL DATA SOURCE ExternalDataSource WITH (
    LOCATION='https://xyzretailstorage741.blob.core.windows.net/'
    CREDENTIAL=demoCredentials

)

CREATE EXTERNAL TABLE synapseCSV (
    [Invoice ID] VARCHAR(50),	
    [Branch] VARCHAR(50),
    [City] VARCHAR(50),
    [Customer type] VARCHAR(50),	
    [Gender] VARCHAR(50),	
    [Product line] VARCHAR(50),	
    [Unit price] FLOAT,	
    [Quantity] INT,	
    [Tax 5%] FLOAT,
    [Total] FLOAT,	
    [Date] DATE,
    [Time] VARCHAR(50),
    [Payment] VARCHAR(50),	
    [cogs] FLOAT,
    [gross margin] FLOAT,
     [percentage] FLOAT,
    [gross income] FLOAT,
    [Rating] FLOAT
)
WITH (
    LOCATION = 'https://source-data@xyzretailstorage741.dfs.core.windows.net/',
    DATA_SOURCE = BlobStorage,
    FILE_FORMAT = CsvFormat
);