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
    public partial class Listar: Form
    {
        public Listar()
        {
            InitializeComponent();
            this.StartPosition = FormStartPosition.CenterScreen; // Centrar ventana en la pantalla
        }

        private void dataGridView2_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private async void btnListar_Click(object sender, EventArgs e)
        {
            ApiService apiService = new ApiService();
            List<Residencial> residenciales =  await apiService.GetResidencialesAsync();

            // Filtrar según los botones seleccionados
            List<Residencial> filtrados = new List<Residencial>(residenciales);

            if (btnActivos.Checked)
            {
                filtrados = residenciales.Where(red => red.EstadoCuenta.Equals("AC", StringComparison.OrdinalIgnoreCase)).ToList();
            }
            else if (btnInactivos.Checked)
            {
                filtrados = residenciales.Where(red => red.EstadoCuenta.Equals("INAC", StringComparison.OrdinalIgnoreCase)).ToList();
            }

            if (btnEstratoBajo.Checked)
            {
                filtrados = residenciales.Where(red => red.Estrato >= 1 && red.Estrato <= 3).ToList();
            }
            else if (btnEstrtatoAlto.Checked)
            {
                filtrados = residenciales.Where(red => red.Estrato >= 4 && red.Estrato <= 6).ToList();
            }

            // Asignar la lista filtrada al DataGridView
            dataGridView2.DataSource = filtrados;

    
        }
    }
}
