use Google;
go
CREATE PROCEDURE agregarTexto @Texto varchar(50)
AS
BEGIN
	INSERT INTO dbo.Rese�as(Texto)
	VALUES(@Texto)
END
go