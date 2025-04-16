package com.acueducto.PredioResidencial.service;

import com.acueducto.PredioResidencial.model.Residencial;
import com.acueducto.PredioResidencial.persistence.Data;
import lombok.AllArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

@AllArgsConstructor
@Service
public class Servicio implements IServicio{

    @Autowired
    private final Data data;

    private static int countId = 1;

    @Override
    public int incrementarId() {
        return countId++;
    }

    @Override
    public Residencial crearPredioResidencial(String propietario, String direccion, LocalDateTime fechaRegistro,
                                              String estadoCuenta, int estrato, double consumo, int subsidio, String tipoVivienda) {

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
        if (estadoCuenta == null || estadoCuenta.isEmpty()) {
            throw new IllegalArgumentException("El estado de cuenta no puede estar vacío.");
        }
        if (estrato < 0) {
            throw new IllegalArgumentException("El estrato no puede ser negativo.");
        }
        if (consumo < 0) {
            throw new IllegalArgumentException("El consumo no puede ser negativo.");
        }
        if (subsidio < 0) {
            throw new IllegalArgumentException("El subsidio no puede ser negativo.");
        }
        if (tipoVivienda == null || tipoVivienda.isEmpty()) {
            throw new IllegalArgumentException("El tipo de vivienda no puede estar vacío.");
        }

        // Crear objeto residencial y calcular factura
        Residencial residencial = new Residencial(incrementarId(), propietario, direccion, fechaRegistro,
                estadoCuenta, estrato, consumo, 0, subsidio, tipoVivienda);

        double valorFactura = residencial.calcularPago();
        residencial.setValorFactura(valorFactura);

        return residencial;
    }

    @Override
    public void agregarResidencial(Residencial residencial) {

        data.getResidenciales().add(residencial);


    }

    @Override
    public Residencial actualizarPredioResidencial(int index, int subsidio, String tipoVivienda, String propietario, String direccion, String estadoCuenta, int estrato, double consumo) {
        // Validaciones defensivas
        if (index <= 0 || index > data.getResidenciales().size()) {
            throw new IllegalArgumentException("El índice del predio es inválido.");
        }
        if (propietario == null || propietario.isEmpty()) {
            throw new IllegalArgumentException("El nombre del propietario no puede estar vacío.");
        }
        if (direccion == null || direccion.isEmpty()) {
            throw new IllegalArgumentException("La dirección no puede estar vacía.");
        }
        if (estadoCuenta == null || estadoCuenta.isEmpty()) {
            throw new IllegalArgumentException("El estado de cuenta no puede estar vacío.");
        }
        if (!estadoCuenta.equals("AC") && !estadoCuenta.equals("INAC")) {
            throw new IllegalArgumentException("El estado de cuenta debe ser 'AC' o 'INAC'.");
        }
        if (estrato < 1 || estrato > 6) {
            throw new IllegalArgumentException("El estrato debe estar entre 1 y 6.");
        }
        if (consumo < 0) {
            throw new IllegalArgumentException("El consumo no puede ser negativo.");
        }
        if (subsidio < 0) {
            throw new IllegalArgumentException("El subsidio no puede ser negativo.");
        }
        if (tipoVivienda == null || tipoVivienda.isEmpty()) {
            throw new IllegalArgumentException("El tipo de vivienda no puede estar vacío.");
        }

        // Actualizar valores
        Residencial pre = (Residencial) data.getResidenciales().get(index - 1);
        pre.setConsumo(consumo);
        pre.setDireccion(direccion);
        pre.setEstadoCuenta(estadoCuenta);
        pre.setEstrato(estrato);
        pre.setPropietario(propietario);
        pre.setSubsidio(subsidio);
        pre.setTipoVivienda(tipoVivienda);

        // Recalcular factura
        double valorFactura = pre.calcularPago();
        pre.setValorFactura(valorFactura);

        return pre;
    }

    @Override
    public void eliminarPredioResidencial(int id) {

        data.getResidenciales().remove(id-1);

    }

    @Override
    public Optional<Residencial> buscarPredioResidencialPorId(int id) {

        System.out.println(data.getResidenciales().toString());
        for (Residencial red : data.getResidenciales()) {
            if (red.getId() == id) {
                return Optional.of(red);
            }
        }
        return null;
    }

    @Override
    public List<Residencial> getPrediosResidenciales() {
        return data.getResidenciales();
    }


    public void imprimirResidencial(){
        for (Residencial red: data.getResidenciales()){
            System.out.println(red);
        }
    }

}
