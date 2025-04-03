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
    public partial class Crear : Form
    {
        public Crear()
        {
            InitializeComponent();
            txtFecha.Text = DateTime.Now.ToString("yyyy-MM-ddTHH:mm:ss");
        }

        private void btnSet_Click(object sender, EventArgs e)
        {



        }

       /* private void btnGet_Click(object sender, EventArgs e)
        {

            var options = new RestClientOptions("http://localhost:8081");
            var client = new RestClient(options);
            var request = new RestRequest("/employees/test");

            var response = client.Get(request);
            txtValue.Text = response.Content;

        }*/

        private void button1_Click(object sender, EventArgs e)
        {


            try
            {
                // Obtener valores de los JTextField en el formulario
                string propietario = txtPropietario.Text.Trim();
                string direccion = txtDireccion.Text.Trim();
                string fechaRegistro = txtFecha.Text;
                string estadoCuenta = txtEstado.Text.Trim();
                int estrato = int.Parse(txtEstrato.Text.Trim());
                double consumo = double.Parse(txtConsumo.Text.Trim());
                int subsidio = int.Parse(txtSubsidio.Text.Trim());
                string tipoVivienda = txtVivienda.Text.Trim();

                // Crear el cliente REST
                var options = new RestClientOptions("http://localhost:8081");
                var client = new RestClient(options);
                var request = new RestRequest("/predio/crear", Method.Post);
                request.RequestFormat = DataFormat.Json;

                // Agregar el JSON con los valores ingresados
                request.AddBody(new
                {
                    propietario = propietario,
                    direccion = direccion,
                    fechaRegistro = fechaRegistro,
                    estadoCuenta = estadoCuenta,
                    estrato = estrato,
                    consumo = consumo,
                    subsidio = subsidio,
                    tipoVivienda = tipoVivienda
                });

                // Enviar la solicitud
                var response = client.Post(request);

                // Mostrar respuesta en MessageBox
                MessageBox.Show("Código de respuesta: " + response.StatusCode);
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error: " + ex.Message);
            }

        }

        private void label10_Click(object sender, EventArgs e)
        {

        }
    }
}
