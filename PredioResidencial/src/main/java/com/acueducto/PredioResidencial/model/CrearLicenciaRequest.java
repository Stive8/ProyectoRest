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

public class CrearLicenciaRequest {

    private String representanteLegal;
    private String codigo;
    private LocalDate fechaVencimiento;
    private int idPredio;
}
