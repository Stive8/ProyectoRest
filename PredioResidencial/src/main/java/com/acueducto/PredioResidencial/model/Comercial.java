package com.acueducto.PredioResidencial.model;

import lombok.*;

import java.time.LocalDateTime;


@AllArgsConstructor
@Getter
@Setter
@ToString

public class Comercial {

    private int id;
    private String propietario;
    private String direccion;
    private LocalDateTime fechaRegistro;
    private int estrato;
    private double consumo;
    private double valorFactura;
    private String tipoComercio;
    private String codigoLicenciaComercial;

    public double definirTarifa() {

        int estrato = this.estrato;
        double tarifa;

        switch (estrato) {
            case 1:

                tarifa = 1000;

                break;

            case 2:
                tarifa = 2000;
                break;

            case 3:
                tarifa = 3000;
                break;

            case 4:
                tarifa = 4000;
                break;

            case 5:
                tarifa = 5000;
                break;

            case 6:
                tarifa = 6000;
                break;
            default:
                tarifa = 0;

        }

        return tarifa;

    }


    public double calcularPago() {
        return definirTarifa() * getConsumo();
    }


}
