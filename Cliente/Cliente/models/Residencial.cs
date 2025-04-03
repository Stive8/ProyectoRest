namespace Cliente.models
{

    public class Residencial
    {
        public int Id { get; set; }
        public string Propietario { get; set; }
        public string Direccion { get; set; }
        public DateTime FechaRegistro { get; set; }
        public string EstadoCuenta { get; set; }
        public int Estrato { get; set; }
        public double Consumo { get; set; }
        public double ValorFactura { get; set; }
        public int Subsidio { get; set; }
        public string TipoVivienda { get; set; }
    }



}


