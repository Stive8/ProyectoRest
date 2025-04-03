package com.acueducto.PredioResidencial.model;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

import java.time.LocalDateTime;

@AllArgsConstructor
@Getter
@Setter
@ToString
public class Request {

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


}
