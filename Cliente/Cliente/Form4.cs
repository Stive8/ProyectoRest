using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Newtonsoft.Json;
using RestSharp;

namespace Cliente
{
    public partial class Eliminar : Form
    {
        public Eliminar()
        {
            InitializeComponent();
            this.StartPosition = FormStartPosition.CenterScreen; // Centrar ventana en la pantalla
        }

        private void btnEliminar_Click(object sender, EventArgs e)
        {

            try
            {
                // Obtener el ID desde el campo de texto
                if (!int.TryParse(txtId.Text.Trim(), out int id))
                {
                    MessageBox.Show("Error: El ID debe ser un número entero.");
                    return;
                }

                // Confirmar eliminación (opcional, pero recomendado)
                DialogResult result = MessageBox.Show($"¿Estás seguro de eliminar el predio con ID {id}?",
                                                      "Confirmar eliminación",
                                                      MessageBoxButtons.YesNo,
                                                      MessageBoxIcon.Warning);
                if (result == DialogResult.No)
                {
                    return;
                }

                // Crear el cliente REST
                var options = new RestClientOptions("http://localhost:8081");
                var client = new RestClient(options);

                // Crear la solicitud DELETE
                var request = new RestRequest($"/predio/eliminar/{id}", Method.Delete);

                // Enviar la solicitud
                var response = client.Execute(request);

                if (response.StatusCode == System.Net.HttpStatusCode.NoContent) // Cambia OK por NoContent
                {
                    MessageBox.Show("Predio eliminado exitosamente.");
                    LimpiarCampos();
                }
                else
                {
                    MessageBox.Show("Error al eliminar predio: " + response.StatusCode + "\nContenido: " + response.Content);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error inesperado: " + ex.Message);
            }

        }
        private void LimpiarCampos()
        {
            txtId.Text = "";
            txtPropietario.Text = "";
            txtDireccion.Text = "";
            txtFecha.Text = "";
            txtEstado.Text = "";
            txtEstrato.Text = "";
            txtConsumo.Text = "";
            txtSubsidio.Text = "";
            txtVivienda.Text = "";
        }

        private void btnConsultar_Click(object sender, EventArgs e)
        {

            try
            {
                if (!int.TryParse(txtId.Text.Trim(), out int id))
                {
                    MessageBox.Show("Error: El ID debe ser un número entero.");
                    return;
                }

                var options = new RestClientOptions("http://localhost:8081");
                var client = new RestClient(options);

                var request = new RestRequest($"/predio/buscar/{id}", Method.Get);

                var response = client.Execute(request);

                if (response.StatusCode == System.Net.HttpStatusCode.OK)
                {
                    var predio = JsonConvert.DeserializeObject<Residencial>(response.Content);
                    txtPropietario.Text = predio.Propietario;
                    txtDireccion.Text = predio.Direccion;
                    txtFecha.Text = predio.FechaRegistro.ToString("yyyy-MM-ddTHH:mm:ss");
                    txtEstado.Text = predio.EstadoCuenta;
                    txtEstrato.Text = predio.Estrato.ToString();
                    txtConsumo.Text = predio.Consumo.ToString();
                    txtSubsidio.Text = predio.Subsidio.ToString();
                    txtVivienda.Text = predio.TipoVivienda;
                }
                else
                {
                    MessageBox.Show("Error al consultar predio: " + response.StatusCode + "\nContenido: " + response.Content);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error inesperado: " + ex.Message);
            }

        }
    }
}
