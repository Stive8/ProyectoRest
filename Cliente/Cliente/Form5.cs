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
        }

        private void dataGridView2_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private async void btnListar_Click(object sender, EventArgs e)
        {
            ApiService apiService = new ApiService();
            List<Residencial> residenciales =  await apiService.GetResidencialesAsync();

            // Filtrar según los botones seleccionados
            List<Residencial> filtrados;

            if (btnActivos.Checked)
            {
                filtrados = residenciales.Where(red => red.EstadoCuenta.Equals("AC", StringComparison.OrdinalIgnoreCase)).ToList();
            }
            else if (btnInactivos.Checked)
            {
                filtrados = residenciales.Where(red => red.EstadoCuenta.Equals("INAC", StringComparison.OrdinalIgnoreCase)).ToList();
            }
            else
            {
                filtrados = residenciales; // Si no hay filtro, mostrar todos
            }

            // Asignar la lista filtrada al DataGridView
            dataGridView2.DataSource = filtrados;

    
        }
    }
}
