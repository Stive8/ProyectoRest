package com.acueducto.PredioResidencial.service;

import com.acueducto.PredioResidencial.model.Comercial;
import com.acueducto.PredioResidencial.model.LicenciaComercial;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

public interface IServicio {

    Comercial crearPredioComercial(String propietario, String direccion, LocalDateTime fechaRegistro,
                                   int estrato, double consumo, String tipoComercio);

    LicenciaComercial crearLicenciaComercial(String representate, String codigo,
                                             LocalDate fechaVencimiento, int idPredio);

    void agregarComercial(Comercial comercial);

    void agregarLicencia(LicenciaComercial licenciaComercial);

    Comercial actualizarPredioComercial(int index, String propietario, String direccion,
                                        int estrato, double consumo, String tipoComercio, String codigoLicencia);

    void eliminarPredioComercial(int id);

    void eliminarLicencia(String codigo);

    Optional<Comercial> buscarPredioComercialPorId(int id);

    Optional<LicenciaComercial> buscarLicenciaPorId(String codigo);

    List<Comercial> getPrediosComerciales();

    int incrementarId();

    List<LicenciaComercial> getLicenciasComerciales();

    void actualizarLicenciaComercial(String codigo, String representanteLegal, LocalDate fechaVencimiento);


}
