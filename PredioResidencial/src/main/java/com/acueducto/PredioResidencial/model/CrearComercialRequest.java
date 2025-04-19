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
public class CrearComercialRequest {

    private String propietario;
    private String direccion;
    private LocalDateTime fechaRegistro;
    private int estrato;
    private double consumo;
    private String tipoComercio;


}
