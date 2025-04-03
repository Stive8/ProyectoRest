package com.acueducto.PredioResidencial.persistence;

import com.acueducto.PredioResidencial.model.Residencial;
import org.springframework.stereotype.Component;

import java.util.ArrayList;
import java.util.List;

@Component
public class Data {

    private final List<Residencial> residenciales = new ArrayList<>();

    public List<Residencial> getResidenciales() {
        return residenciales;
    }


}
