using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Cliente
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void toolStripMenuItem4_Click(object sender, EventArgs e)
        {

            // Crear una instancia del formulario Form2
            Crear form2 = new Crear();

            // Mostrar el formulario
            form2.Show();

        }

        private void toolStripMenuItem6_Click(object sender, EventArgs e)
        {

            // Crear una instancia del formulario Form2
            Consultar form3 = new Consultar();

            // Mostrar el formulario
            form3.Show();

        }

        private void toolStripMenuItem5_Click(object sender, EventArgs e)
        {

            // Crear una instancia del formulario Form2
            Eliminar form4 = new Eliminar();

            // Mostrar el formulario
            form4.Show();

        }
    }
}
