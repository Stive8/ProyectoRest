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
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
        }

        private void btnSet_Click(object sender, EventArgs e)
        {


            var value = txtValue.Text.Trim();
            var options = new RestClientOptions("http://localhost:8081");
            var client = new RestClient(options);
            var request = new RestRequest("/employees/set");

            request.RequestFormat = DataFormat.Json;

            request.AddBody(new
            {
                cedula = 222,
                nombre = "Pepito Grillo"
            });

            var response = client.Post(request);
            MessageBox.Show("Response: " + response.StatusCode);

        }

        private void btnGet_Click(object sender, EventArgs e)
        {

            var options = new RestClientOptions("http://localhost:8081");
            var client = new RestClient(options);
            var request = new RestRequest("/employees/test");

            var response = client.Get(request);
            txtValue.Text = response.Content;

        }
    }
}
