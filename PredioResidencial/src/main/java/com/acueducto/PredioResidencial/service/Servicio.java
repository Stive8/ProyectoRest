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
    public Residencial crearPredioResidencial(String propietario, String direccion, LocalDateTime fechaRegistro, String estadoCuenta, int estrato, double consumo , int subsidio, String tipoVivienda) {

        Residencial residencial = new Residencial(incrementarId(),propietario,direccion,fechaRegistro,estadoCuenta,estrato,consumo,0, subsidio, tipoVivienda);
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
        Residencial pre = (Residencial) data.getResidenciales().get(index-1);
        pre.setConsumo(consumo);
        pre.setDireccion(direccion);
        pre.setEstadoCuenta(estadoCuenta);
        pre.setEstrato(estrato);
        pre.setPropietario(propietario);
        pre.setSubsidio(subsidio);
        pre.setTipoVivienda(tipoVivienda);

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
