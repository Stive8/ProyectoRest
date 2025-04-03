namespace Cliente
{
    internal class Request
    {
        public int Id { get; set; }
        public string Propietario { get; set; }
        public string Direccion { get; set; }
        public string EstadoCuenta { get; set; }
        public int Estrato { get; set; }
        public double Consumo { get; set; }
        public double Subsidio { get; set; }
        public string TipoVivienda { get; set; }
    }
}