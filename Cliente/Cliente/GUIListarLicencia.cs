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
    public partial class GUIListarLicencia : Form
    {
        public GUIListarLicencia()
        {
            InitializeComponent();
        }

        private void btnListar_Click(object sender, EventArgs e)
        {

            try
            {
                // Crear el cliente REST
                var options = new RestClientOptions("http://localhost:8081");
                var client = new RestClient(options);

                // Crear la solicitud GET
                var request = new RestRequest("/licencia/listar", Method.Get);
                var response = client.Execute(request);

                if (response.StatusCode == System.Net.HttpStatusCode.OK)
                {
                    // Deserializar la lista de licencias
                    var licencias = JsonConvert.DeserializeObject<List<dynamic>>(response.Content);

                    // Crear lista para los datos
                    var licenciasMostradas = new List<object>();
                    foreach (var licencia in licencias)
                    {
                        licenciasMostradas.Add(new
                        {
                            Codigo = licencia.codigo?.ToString() ?? "",
                            RepresentanteLegal = licencia.representanteLegal?.ToString() ?? "",
                            FechaVencimiento = licencia.fechaVencimiento?.ToString() ?? "",
                        });
                    }

                    // Asignar la lista al DataGridView
                    dataGridViewLicencias.DataSource = null; // Limpiar fuente de datos
                    dataGridViewLicencias.DataSource = licenciasMostradas;
                }
                else
                {
                    MessageBox.Show($"Error al listar licencias: {response.StatusCode}\nContenido: {response.Content}",
                        "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Error inesperado: {ex.Message}", "Error",
                    MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }
    }
    
}
