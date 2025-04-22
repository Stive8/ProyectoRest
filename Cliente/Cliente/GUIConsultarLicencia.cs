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
    public partial class GUIConsultarLicencia : Form
    {
        public GUIConsultarLicencia()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
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

        private void LimpiarCampos()
        {
            txtRepresentante.Text = "";
            txtFechaVencimiento.Text = "";
        }
    }
}
