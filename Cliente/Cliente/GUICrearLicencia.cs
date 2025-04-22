using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using RestSharp;

namespace Cliente
{
    public partial class GUICrearLicencia : Form
    {
        public GUICrearLicencia()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                // Validar campos
                string codigo = txtCodigo.Text.Trim();
                string representante = txtRepresentante.Text.Trim();
                string fechaVencimiento = txtFechaVencimiento.Text.Trim();
                string idPredioText = txtIdPredio.Text.Trim();

                if (string.IsNullOrEmpty(codigo) || string.IsNullOrEmpty(representante) ||
                    string.IsNullOrEmpty(fechaVencimiento) || string.IsNullOrEmpty(idPredioText))
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

                // Validar que idPredio sea un número entero
                if (!int.TryParse(idPredioText, out int idPredio))
                {
                    MessageBox.Show("Error: El ID del predio debe ser un número entero.", "Error",
                        MessageBoxButtons.OK, MessageBoxIcon.Error);
                    return;
                }

                // Crear el objeto para la solicitud
                var data = new
                {
                    codigo,
                    representanteLegal = representante,
                    fechaVencimiento,
                    idPredio
                };

                // Crear el cliente REST
                var options = new RestClientOptions("http://localhost:8081");
                var client = new RestClient(options);

                // Crear la solicitud POST
                var request = new RestRequest("/licencia/crear", Method.Post);
                request.AddJsonBody(data);

                // Enviar la solicitud
                var response = client.Execute(request);

                if (response.StatusCode == System.Net.HttpStatusCode.OK)
                {
                    MessageBox.Show("Licencia creada exitosamente.", "Éxito",
                        MessageBoxButtons.OK, MessageBoxIcon.Information);
                    LimpiarCampos();
                }
                else if (response.StatusCode == System.Net.HttpStatusCode.NotFound)
                {
                    MessageBox.Show("Error: El predio con el ID especificado no existe.", "No encontrado",
                        MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
                else if (response.StatusCode == System.Net.HttpStatusCode.BadRequest)
                {
                    MessageBox.Show($"Error en los datos: {response.Content}", "Error",
                        MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
                else
                {
                    MessageBox.Show($"Error al crear licencia: {response.StatusCode}\nContenido: {response.Content}",
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
            txtIdPredio.Text = "";
        }

        private void label4_Click(object sender, EventArgs e)
        {

        }
    }

}
