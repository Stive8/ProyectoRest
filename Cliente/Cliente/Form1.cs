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
            this.StartPosition = FormStartPosition.CenterScreen; // Centrar ventana en la pantalla
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

        private void toolStripMenuItem7_Click(object sender, EventArgs e)
        {
            // Crear una instancia del formulario Form2
            Listar form5 = new Listar();

            // Mostrar el formulario
            form5.Show();
        }

        private void actualizarToolStripMenuItem_Click(object sender, EventArgs e)
        {

            GUIActualizar guiActualizar = new GUIActualizar();

            // Mostrar el formulario
            guiActualizar.Show();

        }

        private void acercaDeToolStripMenuItem_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Integrantes:\n Stiven Alvarez \n Brayhan Ortegon \n Juanita Rodriguez", "Acerca de", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        private void toolStripMenuItem8_Click(object sender, EventArgs e)
        {
            GUICrearLicencia gUICrearLicencia = new GUICrearLicencia();
            gUICrearLicencia.Show();

        }

        private void toolStripMenuItem9_Click(object sender, EventArgs e)
        {
            GUIEliminarLicencia gUIEliminarLicencia = new GUIEliminarLicencia();
            gUIEliminarLicencia.Show();
        }

        private void toolStripMenuItem10_Click(object sender, EventArgs e)
        {
            GUIConsultarLicencia gUIConsultarLicencia = new GUIConsultarLicencia();
            gUIConsultarLicencia.Show();
        }

        private void actualizarToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            GUIActualizarLicencia gUIActualizarLicencia = new GUIActualizarLicencia();
            gUIActualizarLicencia.Show();
        }

        private void toolStripMenuItem11_Click(object sender, EventArgs e)
        {
            GUIListarLicencia gUIListarLicencia = new GUIListarLicencia();
            gUIListarLicencia.Show();
        }
    }
}
