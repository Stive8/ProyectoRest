package com.acueducto.PredioResidencial.model;

import lombok.*;

import java.time.LocalDateTime;


@AllArgsConstructor
@Getter
@Setter
@ToString

public class Residencial {

    private int id;
    private String propietario;
    private String direccion;
    private LocalDateTime fechaRegistro;
    private String estadoCuenta;
    private int estrato;
    private double consumo;
    private double valorFactura;
    private int subsidio;
    private String tipoVivienda;


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

    public double calcularSubsidio() {
        switch (getSubsidio()) {
            case 1:
                return 0.02;
            case 2:
                return 0.05;
            case 3:
                return 0.08;
            default:
                return 0;
        }
    }

    public double calcularPago() {
        double tarifaFinal = definirTarifa() * getConsumo();
        return tarifaFinal * (1 - calcularSubsidio());
    }



}
