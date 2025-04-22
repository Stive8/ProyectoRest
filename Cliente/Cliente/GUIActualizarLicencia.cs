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
    public partial class GUIActualizarLicencia : Form
    {
        public GUIActualizarLicencia()
        {
            InitializeComponent();
        }

        private void btnConsultar_Click(object sender, EventArgs e)
        {

            try
            {
                string codigo = txtCodigo.Text.Trim();
                if (string.IsNullOrEmpty(codigo))
                {
                    MessageBox.Show("Error: El código de licencia es obligatorio.", "Error",
                        MessageBoxButtons.OK, MessageBoxIcon.Error);
                    return;
                }

                var options = new RestClientOptions("http://localhost:8081");
                var client = new RestClient(options);

                var request = new RestRequest($"/licencia/buscar/{codigo}", Method.Get);
                var response = client.Execute(request);

                if (response.StatusCode == System.Net.HttpStatusCode.OK)
                {
                    var licencia = JsonConvert.DeserializeObject<dynamic>(response.Content);
                    txtRepresentante.Text = licencia.representanteLegal?.ToString() ?? "";
                    txtFechaVencimiento.Text = licencia.fechaVencimiento?.ToString() ?? "";

                    // Habilitar campos para edición y botón Actualizar
                    txtRepresentante.Enabled = true;
                    txtFechaVencimiento.Enabled = true;
                    btnActualizar.Enabled = true;
                    txtCodigo.Enabled = false; // Bloquear código tras consulta
                }
                else if (response.StatusCode == System.Net.HttpStatusCode.NotFound)
                {
                    MessageBox.Show($"No se encontró una licencia con el código {codigo}.", "No encontrado",
                        MessageBoxButtons.OK, MessageBoxIcon.Information);
                    LimpiarCampos();
                }
                else
                {
                    MessageBox.Show($"Error al consultar licencia: {response.StatusCode}\nContenido: {response.Content}",
                        "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    LimpiarCampos();
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Error inesperado: {ex.Message}", "Error",
                    MessageBoxButtons.OK, MessageBoxIcon.Error);
                LimpiarCampos();
            }
        }

        private void btnActualizar_Click(object sender, EventArgs e)
        {

            try
            {
                // Validar campos
                string codigo = txtCodigo.Text.Trim();
                string representante = txtRepresentante.Text.Trim();
                string fechaVencimiento = txtFechaVencimiento.Text.Trim();
            
                if (string.IsNullOrEmpty(codigo) || string.IsNullOrEmpty(representante) ||
                    string.IsNullOrEmpty(fechaVencimiento) )
                {
                    MessageBox.Show("Error: Todos los campos son obligatorios.", "Error",
                        MessageBoxButtons.OK, MessageBoxIcon.Error);
                    return;
                }

                // Validar que representante no sea solo números
                if (representante.All(char.IsDigit))
                {
                    MessageBox.Show("Error: El representante legal no puede ser solo números.", "Error",
                        MessageBoxButtons.OK, MessageBoxIcon.Error);
                    return;
                }


                // Crear el objeto para la solicitud
                var data = new
                {
                    codigo,
                    representanteLegal = representante,
                    fechaVencimiento
                };

                // Crear el cliente REST
                var options = new RestClientOptions("http://localhost:8081");
                var client = new RestClient(options);

                // Crear la solicitud PUT
                var request = new RestRequest("/licencia/actualizar", Method.Put);
                request.AddJsonBody(data);

                // Enviar la solicitud
                var response = client.Execute(request);

                if (response.StatusCode == System.Net.HttpStatusCode.OK)
                {
                    MessageBox.Show("Licencia actualizada exitosamente.", "Éxito",
                        MessageBoxButtons.OK, MessageBoxIcon.Information);
                    LimpiarCampos();
                }
                else if (response.StatusCode == System.Net.HttpStatusCode.NotFound)
                {
                    MessageBox.Show("Error: La licencia o el predio especificado no existe.", "No encontrado",
                        MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
                else if (response.StatusCode == System.Net.HttpStatusCode.BadRequest)
                {
                    MessageBox.Show($"Error en los datos: {response.Content}", "Error",
                        MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
                else
                {
                    MessageBox.Show($"Error al actualizar licencia: {response.StatusCode}\nContenido: {response.Content}",
                        "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Error inesperado: {ex.Message}", "Error",
                    MessageBoxButtons.OK, MessageBoxIcon.Error);
            }


        }

        private void LimpiarCampos()
        {
            txtCodigo.Text = "";
            txtRepresentante.Text = "";
            txtFechaVencimiento.Text = "";
            txtRepresentante.Enabled = false;
            txtFechaVencimiento.Enabled = false;
            btnActualizar.Enabled = false;
            txtCodigo.Enabled = true;
        }
    }
}
