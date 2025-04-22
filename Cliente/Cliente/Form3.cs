using System;
using System.Windows.Forms;
using Newtonsoft.Json;
using RestSharp;

namespace Cliente
{
    public partial class Consultar : Form
    {
        public Consultar()
        {
            InitializeComponent();
            this.StartPosition = FormStartPosition.CenterScreen; // Centrar ventana en la pantalla
        }

        private void btnConsultar_Click(object sender, EventArgs e)
        {
            try
            {
                // Obtener el ID desde el JTextField
                if (!int.TryParse(txtId.Text.Trim(), out int id))
                {
                    MessageBox.Show("Error: El ID debe ser un número entero.");
                    return;
                }

                // Crear el cliente REST
                var options = new RestClientOptions("http://localhost:8081");
                var client = new RestClient(options);

                var request = new RestRequest($"/predio/buscar/{id}", Method.Get);

                // Enviar la solicitud
                var response = client.Execute(request);

                // Verificar si la respuesta es exitosa
                if (response.StatusCode == System.Net.HttpStatusCode.OK)
                {
                    // Convertir la respuesta JSON a un objeto
                    var predio = JsonConvert.DeserializeObject<Residencial>(response.Content);

                    // Mostrar los datos en los campos de texto
                    txtPropietario.Text = predio.Propietario;
                    txtDireccion.Text = predio.Direccion;
                    txtFecha.Text = predio.FechaRegistro.ToString("yyyy-MM-ddTHH:mm:ss");
                    //txtEstado.Text = predio.EstadoCuenta;
                    txtEstrato.Text = predio.Estrato.ToString();
                    txtConsumo.Text = predio.Consumo.ToString();
                    //txtSubsidio.Text = predio.Subsidio.ToString();
                    txtComercio.Text = predio.TipoComercio;
                }
                else
                {
                    MessageBox.Show("Error al consultar predio: " + response.StatusCode);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error inesperado: " + ex.Message);
            }
        }

    }


}
