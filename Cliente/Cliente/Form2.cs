using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Net.Http;
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
            this.StartPosition = FormStartPosition.CenterScreen; // Centrar ventana en la pantalla
            txtFecha.Text = DateTime.Now.ToString("yyyy-MM-ddTHH:mm:ss");
        }

        private void btnSet_Click(object sender, EventArgs e)
        {
            // Aquí puedes agregar lógica si deseas usar este botón
        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                // Validación previa de campos obligatorios
                if (string.IsNullOrWhiteSpace(txtPropietario.Text) ||
                    string.IsNullOrWhiteSpace(txtDireccion.Text) ||
                //    string.IsNullOrWhiteSpace(txtEstado.Text) ||
                    string.IsNullOrWhiteSpace(txtEstrato.Text) ||
                    string.IsNullOrWhiteSpace(txtConsumo.Text) ||
                //    string.IsNullOrWhiteSpace(txtSubsidio.Text) ||
                    string.IsNullOrWhiteSpace(txtComercio.Text))
                {
                    MessageBox.Show("Por favor complete todos los campos antes de continuar.", "Campos incompletos", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                    return;
                }

                string propietario = txtPropietario.Text.Trim();
                string direccion = txtDireccion.Text.Trim();
                string fechaRegistro = txtFecha.Text;
                //string estadoCuenta = txtEstado.Text.Trim();
                string tipoComercio = txtComercio.Text.Trim();

                // Validación propietario (ya es string por definición)
                if (!propietario.All(char.IsLetter))
                {
                    MessageBox.Show("El campo 'Propietario' solo debe contener letras.", "Error de formato", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    return;
                }

                // Validación estadoCuenta ("AC" o "INAC")
                //if (estadoCuenta != "AC" && estadoCuenta != "INAC")
                //{
                //    MessageBox.Show("El campo 'Estado de Cuenta' debe ser 'AC' o 'INAC'.", "Error de formato", MessageBoxButtons.OK, MessageBoxIcon.Error);
                //    return;
                //}

                // Validación tipoVivienda (ya es string si no está vacío)

                // Validación y conversión segura de números
                if (!int.TryParse(txtEstrato.Text.Trim(), out int estrato))
                {
                    MessageBox.Show("El campo 'Estrato' debe ser un número entero válido.", "Error de formato", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    return;
                }

                if (estrato < 1 || estrato > 6)
                {
                    MessageBox.Show("El campo 'Estrato' debe estar entre 1 y 6.", "Error de valor", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    return;
                }

                if (!double.TryParse(txtConsumo.Text.Trim(), out double consumo))
                {
                    MessageBox.Show("El campo 'Consumo' debe ser un número decimal válido.", "Error de formato", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    return;
                }

                //if (!int.TryParse(txtSubsidio.Text.Trim(), out int subsidio))
                //{
                //    MessageBox.Show("El campo 'Subsidio' debe ser un número entero válido.", "Error de formato", MessageBoxButtons.OK, MessageBoxIcon.Error);
                //    return;
                //}

                // Crear el cliente REST
                var options = new RestClientOptions("http://localhost:8081");
                var client = new RestClient(options);
                var request = new RestRequest("/predio/crear", Method.Post);
                request.RequestFormat = DataFormat.Json;

                // Agregar los datos al cuerpo de la solicitud
                request.AddBody(new
                {
                    propietario = propietario,
                    direccion = direccion,
                    fechaRegistro = fechaRegistro,
                    //estadoCuenta = estadoCuenta,
                    estrato = estrato,
                    consumo = consumo,
                    //subsidio = subsidio,
                    tipoComercio = tipoComercio
                });

                // Enviar la solicitud
                var response = client.Post(request);

                // Verificar el estado de la respuesta
                if (response.IsSuccessful)
                {
                    MessageBox.Show("Registro creado exitosamente. Código de respuesta: " + (int)response.StatusCode, "Éxito", MessageBoxButtons.OK, MessageBoxIcon.Information);
                }
                else
                {
                    MessageBox.Show("Error al crear el registro. Código: " + (int)response.StatusCode + "\nDetalle: " + response.Content, "Error en respuesta", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
            catch (HttpRequestException ex)
            {
                MessageBox.Show("Error de conexión al servidor: " + ex.Message, "Error de red", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            catch (FormatException ex)
            {
                MessageBox.Show("Error de formato: " + ex.Message, "Error de datos", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error inesperado: " + ex.Message, "Error general", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void label10_Click(object sender, EventArgs e)
        {
            // Acción si deseas que al hacer click en label10 pase algo
        }

        private void label1_Click(object sender, EventArgs e)
        {
            // Acción si deseas que al hacer click en label1 pase algo
        }
    }
}
