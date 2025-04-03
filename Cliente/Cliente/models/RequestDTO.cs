


public class RequestDTO
{
	public string Propietario { get; set; }
	public string Direccion { get; set; }
	public string FechaRegistro { get; set; }
	public string EstadoCuenta { get; set; }
	public int Estrato { get; set; }
	public double Consumo { get; set; }
	public double ValorFactura { get; set; }
	public int Subsidio { get; set; }
	public string TipoVivienda { get; set; }

	// Constructor vacío (opcional pero recomendado)
	public RequestDTO() { }
}
