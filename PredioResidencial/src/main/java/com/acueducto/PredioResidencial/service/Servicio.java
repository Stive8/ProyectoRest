package com.acueducto.PredioResidencial.service;

import com.acueducto.PredioResidencial.model.Comercial;
import com.acueducto.PredioResidencial.model.LicenciaComercial;
import com.acueducto.PredioResidencial.persistence.Data;
import lombok.AllArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@AllArgsConstructor
@Service
public class Servicio implements IServicio {

    @Autowired
    private final Data data;

    private static int countId = 1;

    @Override
    public int incrementarId() {
        return countId++;
    }

    @Override
    public List<LicenciaComercial> getLicenciasComerciales() {
        return data.getLicencias() != null ? new ArrayList<>(data.getLicencias()) : new ArrayList<>();
    }

    @Override
    public void actualizarLicenciaComercial(String codigo, String representanteLegal, LocalDate fechaVencimiento) {
        if (data.getLicencias() == null) {
            return;
        }

        for (LicenciaComercial licencia : data.getLicencias()) {
            if (licencia.getCodigo().equalsIgnoreCase(codigo)) {
                licencia.setRepresentanteLegal(representanteLegal);
                licencia.setFechaVencimiento(fechaVencimiento);
                break;
            }
        }
    }

    @Override
    public Comercial crearPredioComercial(String propietario, String direccion, LocalDateTime fechaRegistro,
                                          int estrato, double consumo, String tipoComercio) {

        // Validaciones defensivas
        if (propietario == null || propietario.isEmpty()) {
            throw new IllegalArgumentException("El nombre del propietario no puede estar vacío.");
        }
        if (direccion == null || direccion.isEmpty()) {
            throw new IllegalArgumentException("La dirección no puede estar vacía.");
        }
        if (fechaRegistro == null) {
            throw new IllegalArgumentException("La fecha de registro no puede ser nula.");
        }
        if (estrato < 0) {
            throw new IllegalArgumentException("El estrato no puede ser negativo.");
        }
        if (consumo < 0) {
            throw new IllegalArgumentException("El consumo no puede ser negativo.");
        }
        if (tipoComercio == null || tipoComercio.isEmpty()) {
            throw new IllegalArgumentException("El tipo de Comercio no puede estar vacío.");
        }

        // Crear objeto comercial y calcular factura
        Comercial comercial = new Comercial(incrementarId(), propietario, direccion, fechaRegistro, estrato, consumo, 0, tipoComercio, "");

        double valorFactura = comercial.calcularPago();
        comercial.setValorFactura(valorFactura);

        return comercial;
    }

    @Override
    public LicenciaComercial crearLicenciaComercial(String representate, String codigo, LocalDate fechaVencimiento, int idPredio) {
        LicenciaComercial licenciaComercial = new LicenciaComercial(representate, codigo, fechaVencimiento);
        buscarPredioComercialPorId(idPredio).get().setCodigoLicenciaComercial(licenciaComercial.getCodigo());
        return licenciaComercial;
    }

    @Override
    public void agregarComercial(Comercial comercial) {
        data.getComerciales().add(comercial);
    }

    @Override
    public void agregarLicencia(LicenciaComercial licenciaComercial) {
        data.getLicencias().add(licenciaComercial);

    }


    @Override
    public Comercial actualizarPredioComercial(int id, String propietario, String direccion, int estrato, double consumo, String tipoComercio, String codigoLicencia) {
        // Validaciones defensivas
        if (propietario == null || propietario.isEmpty()) {
            throw new IllegalArgumentException("El nombre del propietario no puede estar vacío.");
        }
        if (direccion == null || direccion.isEmpty()) {
            throw new IllegalArgumentException("La dirección no puede estar vacía.");
        }
        if (estrato < 1 || estrato > 6) {
            throw new IllegalArgumentException("El estrato debe estar entre 1 y 6.");
        }
        if (consumo < 0) {
            throw new IllegalArgumentException("El consumo no puede ser negativo.");
        }
        if (tipoComercio == null || tipoComercio.isEmpty()) {
            throw new IllegalArgumentException("El tipo de comercio no puede estar vacío.");
        }


        // Buscar el predio comercial por ID



        Optional<Comercial> comercialOpt = buscarPredioComercialPorId(id);
        if (!comercialOpt.isPresent()) {
            throw new IllegalArgumentException("No se encontró un predio comercial con el ID proporcionado.");
        }

        Comercial comercial = comercialOpt.get();
        comercial.setPropietario(propietario);
        comercial.setDireccion(direccion);
        comercial.setEstrato(estrato);
        comercial.setConsumo(consumo);
        comercial.setTipoComercio(tipoComercio);
        comercial.setCodigoLicenciaComercial(codigoLicencia);

        // Recalcular la factura
        double valorFactura = comercial.calcularPago();
        comercial.setValorFactura(valorFactura);

        return comercial;
    }


    @Override
    public void eliminarPredioComercial(int id) {
        List<Comercial> comerciales = data.getComerciales();
        for (int i = 0; i < comerciales.size(); i++) {
            if (comerciales.get(i).getId() == id) {
                comerciales.remove(i);
                return;
            }
        }
        throw new IllegalArgumentException("No se encontró un predio comercial con el ID: " + id);
    }

    @Override
    public void eliminarLicencia(String codigo) {
        // Verificar si existe un Comercial con esa licencia
        buscarComercialPorLicencia(codigo).ifPresent(comercial ->
                comercial.setCodigoLicenciaComercial("")
        );

        // Verificar si las licencias existen y eliminar la licencia
        if (data.getLicencias() != null) {
            data.getLicencias().removeIf(licencia -> licencia.getCodigo().equalsIgnoreCase(codigo));
        }
    }

    @Override
    public Optional<Comercial> buscarPredioComercialPorId(int id) {
        for (Comercial red : data.getComerciales()) {
            if (red.getId() == id) {
                return Optional.of(red);
            }
        }
        return Optional.empty();
    }

    @Override
    public Optional<LicenciaComercial> buscarLicenciaPorId(String codigo) {
        for (LicenciaComercial licenciaComercial : data.getLicencias()) {
            if (licenciaComercial.getCodigo().equalsIgnoreCase(codigo)) {
                return Optional.of(licenciaComercial);
            }
        }
        return Optional.empty();
    }


    @Override
    public List<Comercial> getPrediosComerciales() {
        return data.getComerciales();
    }


    public void imprimirComerciales() {
        for (Comercial red : data.getComerciales()) {
            System.out.println(red);
        }
    }

    public Optional<Comercial> buscarComercialPorLicencia(String codigo) {
        if (data.getComerciales() == null || codigo == null) {
            return Optional.empty();
        }

        for (Comercial comercial : data.getComerciales()) {
            if (comercial.getCodigoLicenciaComercial() != null &&
                    comercial.getCodigoLicenciaComercial().equalsIgnoreCase(codigo)) {
                return Optional.of(comercial);
            }
        }
        return Optional.empty();
    }


}
