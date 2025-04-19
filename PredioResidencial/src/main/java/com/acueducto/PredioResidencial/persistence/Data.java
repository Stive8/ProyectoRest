package com.acueducto.PredioResidencial.persistence;

import com.acueducto.PredioResidencial.model.Comercial;
import com.acueducto.PredioResidencial.model.LicenciaComercial;
import lombok.Getter;
import org.springframework.stereotype.Component;

import java.util.ArrayList;
import java.util.List;

@Getter
@Component
public class Data {

    private final List<Comercial> comerciales = new ArrayList<>();

    public List<LicenciaComercial> licencias = new ArrayList<>();


}
