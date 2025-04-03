package com.acueducto.PredioResidencial.service;

import com.acueducto.PredioResidencial.model.Residencial;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

public interface IServicio {

    public Residencial crearPredioResidencial(String propietario, String direccion, LocalDateTime fechaRegistro, String estadoCuenta, int estrato, double consumo, int subsidio, String tipoVivienda);

    public Residencial actualizarPredioResidencial(int index, int subsidio, String tipoVivienda, String propietario, String direccion, String estadoCuenta, int estrato, double consumo);

    public void eliminarPredioResidencial(int id);

    public Optional<Residencial> buscarPredioResidencialPorId(int id);

    public List<Residencial> getPrediosResidenciales();

    public int incrementarId();

    public void agregarResidencial(Residencial residencial);




}
