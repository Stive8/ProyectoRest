package com.acueducto.PredioResidencial.model;


import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

@AllArgsConstructor
@Getter
@Setter
@ToString
public class ActualizarComercialRequest {
    private int index;
    private String propietario;
    private String direccion;
    private int estrato;
    private double consumo;
    private String tipoComercio;
    private String numeroLicenciaComercial;
}