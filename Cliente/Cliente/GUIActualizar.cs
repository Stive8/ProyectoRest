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
    public partial class GUIActualizar : Form
    {
        public GUIActualizar()
        {
            InitializeComponent();
            this.StartPosition = FormStartPosition.CenterScreen; // Centrar ventana en la pantalla
            txtFecha.ReadOnly = true;
        }

        private void btnActualizar_Click(object sender, EventArgs e)
        {

            try
            {
                // Obtener el ID desde el campo de texto
                if (!int.TryParse(txtId.Text.Trim(), out int id))
                {
                    MessageBox.Show("Error: El ID debe ser un número entero.");
                    return;
                }

                // Validar los campos editables
                if (string.IsNullOrWhiteSpace(txtPropietario.Text) ||
                    string.IsNullOrWhiteSpace(txtDireccion.Text) ||
                    string.IsNullOrWhiteSpace(txtEstado.Text) ||
                    string.IsNullOrWhiteSpace(txtVivienda.Text))
                {
                    MessageBox.Show("Error: Los campos Propietario, Dirección, Estado y Tipo de Vivienda no pueden estar vacíos.");
                    return;
                }

                if (!int.TryParse(txtEstrato.Text.Trim(), out int estrato))
                {
                    MessageBox.Show("Error: El estrato debe ser un número entero.");
                    return;
                }

                if (!double.TryParse(txtConsumo.Text.Trim(), out double consumo))
                {
                    MessageBox.Show("Error: El consumo debe ser un número decimal.");
                    return;
                }

                if (!double.TryParse(txtSubsidio.Text.Trim(), out double subsidio))
                {
                    MessageBox.Show("Error: El subsidio debe ser un número decimal.");
                    return;
                }

                // Crear el objeto Request con los datos a actualizar
                var requestData = new Request
                {
                    Id = id,
                    Propietario = txtPropietario.Text.Trim(),
                    Direccion = txtDireccion.Text.Trim(),
                    EstadoCuenta = txtEstado.Text.Trim(),
                    Estrato = estrato,
                    Consumo = consumo,
                    Subsidio = subsidio,
                    TipoVivienda = txtVivienda.Text.Trim()
                };

                // Crear el cliente REST
                var options = new RestClientOptions("http://localhost:8081");
                var client = new RestClient(options);

                // Crear la solicitud PUT
                var request = new RestRequest($"/predio/actualizar/{id}", Method.Put);
                request.AddJsonBody(requestData); // Agregar el cuerpo JSON

                // Enviar la solicitud
                var response = client.Execute(request);

                // Verificar la respuesta
                if (response.StatusCode == System.Net.HttpStatusCode.OK)
                {
                    MessageBox.Show("Predio actualizado exitosamente.");
                }
                else
                {
                    MessageBox.Show("Error al actualizar predio: " + response.StatusCode + "\nContenido: " + response.Content);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error inesperado: " + ex.Message);
            }

        }

        
        private void btnConsultar_Click_1(object sender, EventArgs e)
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

        private void txtDireccion_TextChanged(object sender, EventArgs e)
        {

        }
    }
}