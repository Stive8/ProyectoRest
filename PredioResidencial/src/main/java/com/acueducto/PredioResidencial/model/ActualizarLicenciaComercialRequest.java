package com.acueducto.PredioResidencial.model;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

import java.time.LocalDate;

@AllArgsConstructor
@Getter
@Setter
@ToString
public class ActualizarLicenciaComercialRequest {

    private String codigo;
    private String representanteLegal;
    private LocalDate fechaVencimiento;

}