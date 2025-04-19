package com.acueducto.PredioResidencial.model;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;

import java.time.LocalDate;


@Getter
@Setter
@AllArgsConstructor
public class LicenciaComercial {

    private String representanteLegal;
    private String codigo;
    private LocalDate fechaVencimiento;


}
