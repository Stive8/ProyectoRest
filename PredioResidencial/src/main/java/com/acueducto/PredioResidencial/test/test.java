package com.acueducto.PredioResidencial.test;

import com.acueducto.PredioResidencial.model.Residencial;
import com.acueducto.PredioResidencial.persistence.Data;
import com.acueducto.PredioResidencial.service.Servicio;

import java.time.LocalDateTime;

public class test {

    public static void main(String[] args) {

        Servicio servicio = new Servicio(new Data());

        Residencial red = servicio.crearPredioResidencial("aaa", "aaa", LocalDateTime.now(), "AC", 2, 12,12,"Casa");
        servicio.agregarResidencial(red);

        red = servicio.crearPredioResidencial("bbb", "bbb", LocalDateTime.now(), "ASD", 3, 1,1,"Apto");
        servicio.agregarResidencial(red);


        servicio.imprimirResidencial();

        //servicio.actualizarPredioResidencial(1,2,"APTO","GG", "IBAGUE", LocalDateTime.now(), "INACTIVO", 2, 12);

        System.out.println("//////////////////////////////////");
        servicio.imprimirResidencial();










    }
}
