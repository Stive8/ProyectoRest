package com.acueducto.PredioResidencial.controller;


import com.acueducto.PredioResidencial.model.ActualizarLicenciaComercialRequest;
import com.acueducto.PredioResidencial.model.Comercial;
import com.acueducto.PredioResidencial.model.CrearLicenciaRequest;
import com.acueducto.PredioResidencial.model.LicenciaComercial;
import com.acueducto.PredioResidencial.service.IServicio;
import lombok.AllArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@AllArgsConstructor
@RestController
@RequestMapping(value = "licencia")
public class LicenciaController {

    private final IServicio servicio;

    @PostMapping("crear")
    public ResponseEntity<String> crearLicencia(@RequestBody CrearLicenciaRequest request) {

        System.out.println("Petición POST recibida");

        Optional<Comercial> existenteOpt = servicio.buscarPredioComercialPorId(request.getIdPredio());

        if (existenteOpt.isEmpty()) {
            return ResponseEntity.status(HttpStatus.NOT_FOUND)
                    .body("El predio con ID " + request.getIdPredio() + " no existe.");
        }

        try {
            LicenciaComercial licenciaComercial = servicio.crearLicenciaComercial(
                    request.getRepresentanteLegal(),
                    request.getCodigo(),
                    request.getFechaVencimiento(),
                    request.getIdPredio());

            servicio.agregarLicencia(licenciaComercial);
            existenteOpt.get().setCodigoLicenciaComercial(request.getCodigo());
            return new ResponseEntity<>("Licencia Creada Exitosamente", HttpStatus.OK);


        } catch (NumberFormatException e) {
            return new ResponseEntity<>("Error de formato en los valores numéricos: " + e.getMessage(), HttpStatus.BAD_REQUEST);
        } catch (IllegalArgumentException e) {
            return new ResponseEntity<>("Error en los datos: " + e.getMessage(), HttpStatus.BAD_REQUEST);
        } catch (Exception e) {
            e.printStackTrace();
            return new ResponseEntity<>("Error interno en el servidor: " + e.getMessage(), HttpStatus.INTERNAL_SERVER_ERROR);
        }


    }

    @GetMapping("buscar/{value}")
    public ResponseEntity<?> consultarLicencia(@PathVariable("value") String codigo) {
        try {
            System.out.println("Petición GET");

            var licencia = servicio.buscarLicenciaPorId(codigo);

            if (licencia.isEmpty()) {
                return ResponseEntity.status(HttpStatus.NOT_FOUND)
                        .body("La licencia con Código " + codigo + " no existe.");
            }

            return ResponseEntity.ok(licencia.get());
        } catch (Exception e) {
            e.printStackTrace();
            System.out.println("Petición GET con error");
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                    .body("Error inesperado: " + e.getMessage());
        }
    }

    @DeleteMapping("eliminar/{value}")
    public ResponseEntity<?> eliminarLicencia(@PathVariable("value") String value) {
        try {
            var licencia = servicio.buscarLicenciaPorId(value);

            if (licencia.isEmpty()) {
                return ResponseEntity.status(HttpStatus.NOT_FOUND).body("La licencia con codigo " + value + " no existe.");
            }

            servicio.eliminarLicencia(value);
            return ResponseEntity.ok("Licencia eliminada correctamente");
        } catch (Exception e) {
            e.printStackTrace();
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("Error al eliminar la licencia: " + e.getMessage());
        }
    }
    @PutMapping("actualizar")
    public ResponseEntity<?> actualizarLicencia(@RequestBody ActualizarLicenciaComercialRequest request) {
        try {
            Optional<LicenciaComercial> existenteOpt = servicio.buscarLicenciaPorId(request.getCodigo());

            if (existenteOpt.isEmpty()) {
                return ResponseEntity.status(HttpStatus.NOT_FOUND)
                        .body("La licencia con código " + request.getCodigo() + " no existe.");
            }

            servicio.actualizarLicenciaComercial(
                    request.getCodigo(),
                    request.getRepresentanteLegal(),
                    request.getFechaVencimiento()
            );

            return ResponseEntity.ok("Licencia actualizada correctamente");

        } catch (Exception e) {
            e.printStackTrace();
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                    .body("Error al actualizar la licencia: " + e.getMessage());
        }
    }

    @GetMapping("listar")
    public ResponseEntity<List<LicenciaComercial>> listarLicencias() {
        try {
            List<LicenciaComercial> licencias = servicio.getLicenciasComerciales();
            return ResponseEntity.ok(licencias);
        } catch (Exception e) {
            e.printStackTrace();
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
        }
    }

}
