namespace Cliente
{
    partial class Listar
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.dataGridView2 = new System.Windows.Forms.DataGridView();
            this.btnListar = new System.Windows.Forms.Button();
            this.btnActivos = new System.Windows.Forms.RadioButton();
            this.btnInactivos = new System.Windows.Forms.RadioButton();
            this.btnEstratoBajo = new System.Windows.Forms.RadioButton();
            this.btnEstrtatoAlto = new System.Windows.Forms.RadioButton();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView2)).BeginInit();
            this.SuspendLayout();
            // 
            // dataGridView2
            // 
            this.dataGridView2.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridView2.Location = new System.Drawing.Point(12, 12);
            this.dataGridView2.Name = "dataGridView2";
            this.dataGridView2.Size = new System.Drawing.Size(587, 232);
            this.dataGridView2.TabIndex = 0;
            this.dataGridView2.CellContentClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.dataGridView2_CellContentClick);
            // 
            // btnListar
            // 
            this.btnListar.Location = new System.Drawing.Point(524, 274);
            this.btnListar.Name = "btnListar";
            this.btnListar.Size = new System.Drawing.Size(75, 23);
            this.btnListar.TabIndex = 3;
            this.btnListar.Text = "Listar";
            this.btnListar.UseVisualStyleBackColor = true;
            this.btnListar.Click += new System.EventHandler(this.btnListar_Click);
            // 
            // btnActivos
            // 
            this.btnActivos.AutoSize = true;
            this.btnActivos.Location = new System.Drawing.Point(13, 279);
            this.btnActivos.Name = "btnActivos";
            this.btnActivos.Size = new System.Drawing.Size(58, 17);
            this.btnActivos.TabIndex = 4;
            this.btnActivos.TabStop = true;
            this.btnActivos.Text = "Activar";
            this.btnActivos.UseVisualStyleBackColor = true;
            // 
            // btnInactivos
            // 
            this.btnInactivos.AutoSize = true;
            this.btnInactivos.Location = new System.Drawing.Point(92, 279);
            this.btnInactivos.Name = "btnInactivos";
            this.btnInactivos.Size = new System.Drawing.Size(68, 17);
            this.btnInactivos.TabIndex = 5;
            this.btnInactivos.TabStop = true;
            this.btnInactivos.Text = "Inactivos";
            this.btnInactivos.UseVisualStyleBackColor = true;
            // 
            // btnEstratoBajo
            // 
            this.btnEstratoBajo.AutoSize = true;
            this.btnEstratoBajo.Location = new System.Drawing.Point(185, 279);
            this.btnEstratoBajo.Name = "btnEstratoBajo";
            this.btnEstratoBajo.Size = new System.Drawing.Size(85, 17);
            this.btnEstratoBajo.TabIndex = 6;
            this.btnEstratoBajo.TabStop = true;
            this.btnEstratoBajo.Text = "Estrato 1,2,3";
            this.btnEstratoBajo.UseVisualStyleBackColor = true;
            // 
            // btnEstrtatoAlto
            // 
            this.btnEstrtatoAlto.AutoSize = true;
            this.btnEstrtatoAlto.Location = new System.Drawing.Point(288, 279);
            this.btnEstrtatoAlto.Name = "btnEstrtatoAlto";
            this.btnEstrtatoAlto.Size = new System.Drawing.Size(85, 17);
            this.btnEstrtatoAlto.TabIndex = 7;
            this.btnEstrtatoAlto.TabStop = true;
            this.btnEstrtatoAlto.Text = "Estrato 4,5,6";
            this.btnEstrtatoAlto.UseVisualStyleBackColor = true;
            // 
            // Listar
            // 
            this.ClientSize = new System.Drawing.Size(611, 335);
            this.Controls.Add(this.btnEstrtatoAlto);
            this.Controls.Add(this.btnEstratoBajo);
            this.Controls.Add(this.btnInactivos);
            this.Controls.Add(this.btnActivos);
            this.Controls.Add(this.btnListar);
            this.Controls.Add(this.dataGridView2);
            this.Name = "Listar";
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView2)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.DataGridView dataGridView1;
        private System.Windows.Forms.DataGridViewTextBoxColumn Id;
        private System.Windows.Forms.DataGridViewTextBoxColumn propietario;
        private System.Windows.Forms.DataGridViewTextBoxColumn direccion;
        private System.Windows.Forms.DataGridViewTextBoxColumn fechaCreacion;
        private System.Windows.Forms.DataGridViewTextBoxColumn estadoCuenta;
        private System.Windows.Forms.DataGridViewTextBoxColumn estrato;
        private System.Windows.Forms.DataGridViewTextBoxColumn consumo;
        private System.Windows.Forms.DataGridViewTextBoxColumn subsidio;
        private System.Windows.Forms.DataGridViewTextBoxColumn tipoVivienda;
        private System.Windows.Forms.DataGridViewTextBoxColumn valorFactura;
        private System.Windows.Forms.DataGridView dataGridView2;
        private System.Windows.Forms.Button btnListar;
        private System.Windows.Forms.RadioButton btnActivos;
        private System.Windows.Forms.RadioButton btnInactivos;
        private System.Windows.Forms.RadioButton btnEstratoBajo;
        private System.Windows.Forms.RadioButton btnEstrtatoAlto;
    }
}